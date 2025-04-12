
mkdir logs/paynt-cav-q4

python3 paynt.py models-q4/consensus-4-2 --sketch model.prism --props model.props --add-dont-care-action --dt-reduction > logs/paynt-cav-q4/consensus.log
python3 paynt.py models-q4/csma-3-4 --sketch model.prism --props model.props --add-dont-care-action --dt-reduction > logs/paynt-cav-q4/csma.log