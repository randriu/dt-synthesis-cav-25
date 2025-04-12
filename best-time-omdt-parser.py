import os
import pandas as pd
import click

def parse(log_file_path):
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if line.startswith(' Expl Unexpl'):
            start_index = i
        elif line.startswith('Cutting planes:'):
            end_index = i
            break

    best_time = None
    if start_index is not None and end_index is not None:
        for line in lines[start_index:end_index]:
            if line.startswith('H') or line.startswith('*'):
                best_time = line.split()[-1]

        if best_time:
            best_time = best_time[:-1]  # Remove the last character

    if best_time is None:
        for line in lines:
            if line.startswith('Presolve time:'):
                best_time = line.split()[-1]
                best_time = best_time[:-1]  # Remove the last character
                best_time = best_time.split('.')[0]
                break

    return best_time

def add_best_runtime_column(working_directory):
    results_file_path = os.path.join(working_directory, 'results.csv')
    results_df = pd.read_csv(results_file_path)

    best_runtimes = []
    for index, row in results_df.iterrows():
        mdp_value = row['model']
        depth_value = row['max_depth']
        log_file_path = os.path.join(working_directory, f"{mdp_value}/log-depth-{depth_value}.log")
        
        best_runtime = parse(log_file_path)
        best_runtimes.append(best_runtime)

    results_df['omdt time (best)'] = best_runtimes
    new_results_file_path = os.path.join('./logs/omdt-final.csv')
    results_df.to_csv(new_results_file_path, index=False)

@click.command()
@click.option('--log-dir', type=str, default="./OMDT/logs/cav-final", show_default=True, help='Path to the omdt log folder.')
def main(log_dir):
    result_dirs = [log_dir]
    for x in result_dirs:
        working_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), x)
        add_best_runtime_column(working_directory)


if __name__ == '__main__':
    main()