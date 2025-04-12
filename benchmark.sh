#!/bin/bash

set -e

overwrite=false
provided_logs=false
generate_only=false
smoke_test=false

# CHANGE THIS ACCORDING TO YOUR SYSTEM
thread_count=2 # Ideally you should have 16GB of RAM per thread

while getopts opgt flag
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
        t)
            smoke_test=true
            ;;
    esac
done

if [ "$smoke_test" = true ]; 
then
    echo "generating dtPAYNT log files"
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir ./benchmarks --experiment-name paynt-smoke-test --workers $thread_count --depth-max 1 --generate-csv --smoke-test --restart --timeout 30

    echo "generating OMDT log files"
    if [ -f logs/omdt-smoke-test/results.csv ]; then
        rm logs/omdt-smoke-test/results.csv
    fi
    cd /opt/OMDT
    python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir ./models --experiment-name omdt-smoke-test --workers $thread_count --depth-max 1 --restart --timeout 30
    cd -

    if [ ! -f ./logs/dtcontrol-smoke-test.csv ]; then
        echo "generating dtControl results"
        python3 generate-dtcontrol-results.py --models-dir ./benchmarks --output-dir dtcontrol-smoke-test --generate-csv --smoke-test
    fi

    echo "creating csv file with results for OMDT"
    python3 best-time-omdt-parser.py --log-dir ./logs/omdt-smoke-test --smoke-test

    echo ""
    echo "testing smoke test results"
    echo ""

    line_count=$(wc -l < ./logs/paynt-smoke-test.csv)
    if [ "$line_count" -ne 22 ]; then
        echo "Error: ./logs/paynt-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 22 (1 header, 21 models) lines."
        exit 1
    fi

    line_count=$(wc -l < ./logs/omdt-smoke-test.csv)
    if [ "$line_count" -ne 22 ]; then
        echo "Error: ./logs/omdt-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 22 (1 header, 21 models) lines."
        exit 1
    fi

    line_count=$(wc -l < ./logs/dtcontrol-smoke-test.csv)
    if [ "$line_count" -ne 22 ]; then
        echo "Error: ./logs/dtcontrol-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 22 (1 header, 21 models) lines."
        exit 1
    fi
    
    echo "Smoke test passed!"
    exit 0
fi

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
    if [ -f logs/omdt-cav-final/results.csv ]; then
        rm logs/omdt-cav-final/results.csv
    fi
    cd /opt/OMDT
    python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir ./models --experiment-name omdt-cav-final --workers $thread_count --restart
    cd -

    echo "generating dtControl results"
    python3 generate-dtcontrol-results.py --models-dir ./benchmarks --output-dir dtcontrol-cav-final --generate-csv
else
    echo "generating dtPAYNT log files"
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir ./benchmarks --experiment-name paynt-cav-final --generate-csv --workers $thread_count

    echo "generating OMDT log files"
    cd /opt/OMDT
    python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir ./models --experiment-name omdt-cav-final --workers $thread_count
    cd -

    if [ ! -f ./logs/dtcontrol-final.csv ]; then
        echo "generating dtControl results"
        python3 generate-dtcontrol-results.py --models-dir ./benchmarks --output-dir dtcontrol-cav-final --generate-csv
    fi
fi


echo "creating csv file with results for OMDT"
python3 best-time-omdt-parser.py --log-dir ./logs/omdt-cav-final

echo "merging csv files"
python3 merge-csv-files.py

echo "generating tables and figures"
python3 generate-tables-and-figures.py

echo "Generated results to 'generated-results'"
