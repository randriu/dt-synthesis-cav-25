
thread_count=1 # Ideally you should have 32GB of RAM per thread

echo "generating dtPAYNT log files for Q3"
python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir ./benchmarks-q3 --experiment-name paynt-cav-q3 --generate-csv --workers $thread_count --q3 --depth-max 4 --restart --timeout 1200 --maxmem 32