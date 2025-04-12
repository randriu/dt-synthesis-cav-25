#!/bin/bash

overwrite=false
provided_logs=false
generate_only=false
thread_count=2 # Ideally you should have 16GB of RAM per thread

while getopts opg flag
do
    case "${flag}" in
        o)
            overwrite=true
            ;;
        p)
            provided_logs=true
            ;;
        g)
            generate_only=true
            ;;
    esac
done

if [ "$provided_logs" = true ]; 
then
    echo "Using provided log files..."
    python3 generate-tables-and-figures.py --file-path original-logs/final-merge.csv --add-dtcontrol-depths
    echo "Generated results using the original log files to 'generated-results'"
    exit 0
fi

if [ "$generate_only" = true ]; 
then
    echo "Generating the results"
    python3 generate-tables-and-figures.py
    exit 0
fi

if [ "$overwrite" = true ]; 
then
    echo "Overwriting existing log files..."

    echo "generating dtPAYNT log files"
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir ./benchmarks --experiment-name paynt-cav-final --generate-csv --workers $thread_count --restart

    echo "generating OMDT log files"
    cd /opt/OMDT
    python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir ./models --experiment-name omdt-cav-final --workers $thread_count --restart
    cd -

    echo "generating dtControl results"
    python3 generate-dtcontrol-results.py --models-dir ./benchmarks --generate-csv
else
    echo "generating dtPAYNT log files"
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir ./benchmarks --experiment-name paynt-cav-final --generate-csv --workers $thread_count

    echo "generating OMDT log files"
    cd /opt/OMDT
    python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir ./models --experiment-name omdt-cav-final --workers $thread_count
    cd -

    if [ -f ./dtcontrol-final.csv ]; then
        echo "generating dtControl results"
        python3 generate-dtcontrol-results.py --models-dir ./benchmarks --generate-csv
    fi
fi


echo "creating csv file with results for OMDT"
python3 best-time-omdt-parser.py --log-dir ./logs/omdt-cav-final

echo "merging csv files"
python3 merge-csv-files.py

echo "generating tables and figures"
python3 generate-tables-and-figures.py

echo "Generated results to 'generated-results'"