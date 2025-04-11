
thread_count=2 # Ideally you should have 16GB of RAM per thread

echo "generating dtPAYNT log files for Q3"
python3 experiments-dts-cav.py --paynt-dir ./ --models-dir ./models-q3 --experiment-name cav-q3 --generate-csv --workers $thread_count