# Benchmarks for decision tree synthesis (CAV'25 submission)

Contents of this repository:

- results.csv: complete experimental results
- benchmarks: directory with three types of benchmarks, each with its own set of associated files as detailed below

- benchmarks/qcomp/\*/ and benchmarks/maze/\*/
    + model.prism: original PRISM model
    + model-random.drn: model.prism with don't-care action and all actions enabled

- benchmarks/omdt/\*/
    + model-random.drn: model.prism with don't-care action and all actions enabled

- benchmarks/\*/\*/
    + state-valuations.json: state valuations for model-random.drn
    + discounted.props: discount-factor specification
    + scheduler-final.storm.json: scheduler for model-random.drn
