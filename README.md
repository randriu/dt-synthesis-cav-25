# Small Decision Trees for MDPs with Deductive Synthesis

This artifact supplements CAV'25 paper *Small Decision Trees for MDPs with Deductive Synthesis*.


Contents of the artifact:
- dtpaynt.tar: the Docker image containing the tools and benchmarks discussed in the paper, as well as scripts for their automated evaluation
- paper-submission.pdf: the initial version of the paper submitted to CAV'25
- LICENSE: the license file
- README.md: this readme

The first part of this readme describes how to use the artifact to replicate results presented in the paper. The latter part presents the tools, their installation and their usage, the benchmarks and their evaluation outside the scope of this artifact.

---

## Reproducing the experiments

### Using the Docker and quick start

Load the image `dtpaynt.tar` into your Docker environment using:
```
docker load -i dtpaynt.tar
```

If you get a permission error, make sure to precede docker commands with `sudo` to acquire root privileges. Upon loading the image, you can run the container with:
```
docker run -it randriu/dts-cav25
```

TODO add info about gurobi

this will create a docker container. Executing the command above will place you in `/opt/cav25-experiments` folder, from which exeriments can be run using
```
./benchmark.sh 
```

The evaluating script has additional options which will be explained below. 

### Smoke test

As a quick start, try option `-t` to run a , it should take about 20-30 minutes:
```
./benchmark.sh -t
```
This will run dtPAYNT, OMDT for max depth 1 with 30 second timeouts and dtControl with default settings (as it is fast). The smoke test should generate 3 csv files to the `logs` folder.

If you get message "Smoke test passed!" you are all set. If you get the following message "Error: ./logs/omdt-smoke-test.csv does not contain a row for each model in the smoke test." you might still be fine, however, for some models the OMDT takes very long to produce the result after the timeout is reaches and sometimes uses a lot of memory. On some systems this is not a problem but if you are running the experiments on a slower machine sadly we cannot really TODO

You can exit the container via `exit` or `^D`. Upon finishing your review, you can remove the image from the Docker environment using:
```
docker rmi randriu/dts-cav25
```

The Dockerfile used to create the image can be found in TODO

### What can be replicated

The evaluating script `./benchmark.sh` allows to replicate all of the figures in the paper (including appendix) and the model info table from the appendix. For experiments sections Q3 and Q4 we provide scripts `./benchmark-q3.sh` and `./benchmark-q4.sh` which will only produce log files for the corresponding experiments. The reviewers are welcome to explore these log files, we will explain what to look for in these log files below. Therefore every result from the experimental section and the appendix can be replicated via this artifact.

### Executing the evaluating script

Running the benchmark script `./benchmark.sh` will generate all of the log files for dtPAYNT, OMDT and dtControl for all of the 21 models in our benchmark set, and then generate all of the figures from the paper. The runtime of the whole experiments depends on the number of threads you can use which can be adjusted in the file `./benchmark.sh` by changing the value of `thread_count` (default 2). Note that you ideally need at least 16GB of RAM per thread. The whole benchmark will take 21 (models) * 8 (depths) * 20 (minutes) * 2 (tools: OMDT + dtPAYNT) + few minutes for dtControl = ~80-100 hours on a single thread.

To help with this potentially very long runtime we introduce the following options:

- TODO - run only subset of models
- `s` - will skip OMDT evaluation, you can copy the OMDT logs from `original-logs` folder using `cp -r ./original-logs/omdt-cav-final ./logs/`. If you use this option please mind the possible discrepency in the values and runtimes since the comparison will be on runs from different machines

When executing the script repeatedly, it detects whether the log files already exist, so you can *can abort without loss of progress*. To re-run the experiments completely, simply delete the corresponding log files or use option `-o` to force the overwrite.

The generated log files are stored in `logs` folder and the final figures and tables are generated in `genereated-results` folder.

In case the script encounters an error, it generates an error message and proceeds with the evaluation. As a result, the generated figures might be missing some data. You can check the log files to see which experiments failed, remove the corresponding log files and re-run the script if you wish so.

Given the nature of the experiments, their outcome heavily depends on the timing, so the produced tables and figures will be different, although the underlying qualitative comparison of the approaches should be preserved. The original results were obtained on a PC equipped with AMD EPYC 9124 16-Core Processor (each experiment uses single core) and 360GB of RAM. The experiments can be run on much more modestly equiped PCs/laptops, although it might happen that some more demanding experiments will run out of memory or simply lead to worse results.

The original log files that were used when preparing the submission can be found in `original-logs`. If you wish to generate results from these log files use the option `-p`.

---

## Using the tools outside the scope of the artifact

dtPAYNT is implemented inside the tool PAYNT, which is built on top of Storm using the python bindings of StormPy. Below we provide for each tool (including OMDT and dtControl) the links that contain information about how to install them outside of docker.

- PAYNT
    - source: https://github.com/randriu/synthesis
    - used version: https://github.com/randriu/synthesis/tree/dts-cav
    - used Storm version: TODO
    - used StormPy version: TODO
- OMDT
    - source: https://github.com/tudelft-cda-lab/OMDT
    - used version (includes parsing for .drn models): https://github.com/TheGreatfpmK/OMDT
- dtControl
    - source: https://gitlab.com/live-lab/software/dtcontrol
    - used version: https://gitlab.com/live-lab/software/dtcontrol/-/tree/paynt-colab

We provide a small overview of how to use the tools outside of the benchmark script. For full information, please visit the linked documentation.

### PAYNT

PAYNT is a tool written in Python3. To run the small decision tree synthesis use:

```
python3 paynt.py path/to/model/folder --tree-enumeration --tree-depth=X
```

X represents the maximum depth the synthesized DT should have. This command assumes the model folder contains both the model description and a specification. For more information about the settings of PAYNT, visit https://github.com/randriu/synthesis.

### OMDT

OMDT is also written in Python3. It uses the LP solver gurobi. To run OMDT from https://github.com/tudelft-cda-lab/OMDT (original IJCAI'23 code) use:

```
python3 run.py omdt model-name --seed 0 --max_depth X --time_limit Y
```

and to run OMDT from https://github.com/TheGreatfpmK/OMDT which also supports the parsing of drn format models.

```
python3 run-experiment.py omdt model-name --seed 0 --max_depth X --time_limit Y --model-file-name model-name.drn
```

X represents the maximum depth the synthesized DT should have and Y the timeout in seconds.


### dtControl

TODO


## Parts of the source code relevant to the paper

TODO

## Testing the correctness of dtPAYNT

TODO

## Models

TODO
