
import os
import shutil
import subprocess
import json
import click

def contains_sketch(directory):
    if not os.path.isdir(directory):
        return False
    # files = [ os.path.basename(f.path) for f in os.scandir(directory) if f.is_file() ]
    # return b'sketch.templ' in files and b'sketch.props' in files
    subdirectories = [ f.path for f in os.scandir(directory) if f.is_dir() ]
    for x in subdirectories:
        if "decision_trees" in x.__str__():
            subdirectories = []
        if ".benchmark_suite" in x.__str__():
            subdirectories = []
    return len(subdirectories) == 0

def collect_sketches(directory):
    if ".benchmark_suite" in directory.__str__() or "decision_trees" in directory.__str__():
        return []
    if not isinstance(directory, bytes):
        directory = os.fsencode(directory)
    sketches = []
    if contains_sketch(directory):
        sketches.append(directory.decode("utf-8"))
    subdirectories = [ f.path for f in os.scandir(directory) if f.is_dir() ]
    for subdirectory in subdirectories:
        sketches += collect_sketches(subdirectory)
    return sketches

def collect_tasks(models_dir):
    sketches = collect_sketches(models_dir)

    skip = []
    # skip += ["maze"]
    # skip += ["omdt"]
    # skip += ["qcomp"]

    sketches = sorted(sketches)
    sketches = [sketch for sketch in sketches if not any([k in str(sketch) for k in skip])]

    tasks = []
    model_count = 1
    for sketch in sketches:
        model_name = os.path.basename(sketch)
        model_group_name = os.path.basename(os.path.dirname(sketch))
        model_name = f"{model_group_name}-{model_name}"
        if "ij-10" in model_name:
            continue
        command = "dtcontrol --input scheduler-final.storm.json -r --use-preset default".split(' ')
        cleanup = "rm -rf .benchmark_suite decision_trees benchmark.html benchmark.json".split(' ')
        model_str = f"{model_count}/{len(sketches)} - {model_name} -"
        tasks.append((model_name, sketch, command, cleanup, model_str))
        model_count += 1
    return tasks


@click.command()
@click.option('--models-dir', type=str, default="/opt/cav25-experiments/benchmarks", show_default=True, help='Path to the models folder.')
@click.option('--generate-csv', is_flag=True, default=False, show_default=True, help='Generate CSV file with results.')
@click.option('--smoke-test', is_flag=True, default=False, show_default=True, help='Turn on smoke test setting.')
@click.option('--output-dir', type=str, default="./logs/dtcontrol-final-cav/", show_default=True, help='Path to the output folder.')
def main(models_dir, generate_csv, smoke_test, output_dir):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    tasks = collect_tasks(models_dir)

    results = []

    for task in tasks:
        model_name, sketch_dir, command, cleanup, models_str = task
        print(f"{models_str} started")
        
        result = subprocess.run(command, cwd=sketch_dir, capture_output=True)

        log_file = os.path.join(output_dir, f"{model_name}.log")
        with open(log_file, 'w') as f:
            f.write(result.stdout.decode())
            f.write(result.stderr.decode())

            if result.returncode != 0:
                print(f"Error running model {model_name} see {log_file} for details")
        
        result_json = json.load(open(os.path.join(sketch_dir, "benchmark.json")))

        results.append(f"{model_name},{result_json['scheduler-final']['classifiers']['default']['stats']['inner nodes']},{result_json['scheduler-final']['classifiers']['default']['time']}")

        subprocess.run(cleanup, cwd=sketch_dir)

    if generate_csv:
        file = "./logs/dtcontrol-smoke-test.csv" if smoke_test else "./logs/dtcontrol-final.csv"
        with open(file, "w") as f:
            f.write("model,dtcontrol nodes,dtcontrol time\n")
            for result in results:
                f.write(result + "\n")
        print("CSV file generated: dtcontrol-final.csv")
    else:
        print("model,dtcontrol nodes,dtcontrol time")

        for result in results:
            print(result)

if __name__ == '__main__':
    main()