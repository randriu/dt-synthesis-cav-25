
mkdir results/logs/paynt-cav-q4

python3 /opt/paynt/paynt.py benchmarks-q4/qcomp/consensus-4-2 --sketch model.prism --props model.props --add-dont-care-action --dt-reduction > results/logs/paynt-cav-q4/consensus.log
python3 /opt/paynt/paynt.py benchmarks-q4/qcomp/csma-3-4 --sketch model.prism --props model.props --add-dont-care-action --dt-reduction > results/logs/paynt-cav-q4/csma.log