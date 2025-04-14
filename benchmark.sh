#!/bin/bash

set -e

overwrite=false
provided_logs=false
generate_only=false
smoke_test=false
skip_omdt=false
model_subset=false

# CHANGE THIS ACCORDING TO YOUR SYSTEM
thread_count=2 # Ideally you should have 16GB of RAM per thread (sometimes OMDT needs more)

while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -o | --overwrite ) overwrite=true; shift ;;
        -p | --provided-logs ) provided_logs=true; shift ;;
        -g | --generate-only ) generate_only=true; shift ;;
        -t | --smoke-test ) smoke_test=true; shift ;;
        -s | --skip-omdt ) skip_omdt=true; shift ;;
        -m | --model-subset) model_subset=true; shift ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
done

benchmarks_dir="./benchmarks"
models_dir="./models"
if [ "$model_subset" = true ]; 
then
    benchmarks_dir="./benchmarks-subset"
    models_dir="./models-subset"
fi

if [ "$smoke_test" = true ]; 
then
    if [ "$model_subset" = true ]; 
    then
        echo "generating dtPAYNT log files"
        python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir ./benchmarks-subset --experiment-name paynt-smoke-test --workers $thread_count --depth-max 1 --generate-csv --smoke-test --restart --timeout 30

        echo "generating OMDT log files"
        if [ -f results/logs/omdt-smoke-test/results.csv ]; then
            rm results/logs/omdt-smoke-test/results.csv
        fi
        cd /opt/OMDT
        python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir ./models-subset --experiment-name omdt-smoke-test --workers $thread_count --depth-max 1 --restart --timeout 30 --maxmem 32 --generate-csv
        cd -

        if [ ! -f ./results/logs/dtcontrol-smoke-test.csv ]; then
            echo "generating dtControl results"
            python3 generate-dtcontrol-results.py --models-dir ./benchmarks-subset --output-dir results/logs/dtcontrol-smoke-test --generate-csv --smoke-test
        fi

        echo "creating csv file with results for OMDT"
        python3 best-time-omdt-parser.py --log-dir ./results/logs/omdt-smoke-test --smoke-test

        echo ""
        echo "testing smoke test results"
        echo ""

        line_count=$(wc -l < ./results/logs/paynt-smoke-test.csv)
        if [ "$line_count" -ne 14 ]; then
            echo "Error: ./results/logs/paynt-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 14 (1 header, 13 models) lines."
            exit 1
        fi

        line_count=$(wc -l < ./results/logs/omdt-smoke-test.csv)
        if [ "$line_count" -ne 14 ]; then
            echo "Error: ./results/logs/omdt-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 14 (1 header, 13 models) lines."
            exit 1
        fi

        line_count=$(wc -l < ./results/logs/dtcontrol-smoke-test.csv)
        if [ "$line_count" -ne 14 ]; then
            echo "Error: ./results/logs/dtcontrol-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 14 (1 header, 13 models) lines."
            exit 1
        fi
        
        echo "Smoke test passed!"
        exit 0
    fi


    echo "generating dtPAYNT log files"
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir ./benchmarks --experiment-name paynt-smoke-test --workers $thread_count --depth-max 1 --generate-csv --smoke-test --restart --timeout 30

    echo "generating OMDT log files"
    if [ -f results/logs/omdt-smoke-test/results.csv ]; then
        rm results/logs/omdt-smoke-test/results.csv
    fi
    cd /opt/OMDT
    python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir ./models --experiment-name omdt-smoke-test --workers $thread_count --depth-max 1 --restart --timeout 30 --maxmem 32 --generate-csv
    cd -

    if [ ! -f ./results/logs/dtcontrol-smoke-test.csv ]; then
        echo "generating dtControl results"
        python3 generate-dtcontrol-results.py --models-dir ./benchmarks --output-dir dtcontrol-smoke-test --generate-csv --smoke-test
    fi

    echo "creating csv file with results for OMDT"
    python3 best-time-omdt-parser.py --log-dir ./results/logs/omdt-smoke-test --smoke-test

    echo ""
    echo "testing smoke test results"
    echo ""

    line_count=$(wc -l < ./results/logs/paynt-smoke-test.csv)
    if [ "$line_count" -ne 22 ]; then
        echo "Error: ./results/logs/paynt-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 22 (1 header, 21 models) lines."
        exit 1
    fi

    line_count=$(wc -l < ./results/logs/omdt-smoke-test.csv)
    if [ "$line_count" -ne 22 ]; then
        echo "Error: ./results/logs/omdt-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 22 (1 header, 21 models) lines."
        exit 1
    fi

    line_count=$(wc -l < ./results/logs/dtcontrol-smoke-test.csv)
    if [ "$line_count" -ne 22 ]; then
        echo "Error: ./results/logs/dtcontrol-smoke-test.csv does not contain a row for each model in the smoke test. It contains $line_count lines and it should contain 22 (1 header, 21 models) lines."
        exit 1
    fi
    
    echo "Smoke test passed!"
    exit 0
fi

if [ "$provided_logs" = true ]; 
then
    echo "Using provided log files..."
    python3 generate-tables-and-figures.py --file-path original-logs/final-merge.csv --add-dtcontrol-depths
    echo "Generated results using the original log files to 'results/generated-results'"
    exit 0
fi

if [ "$generate_only" = true ]; 
then
    echo "generating dtPAYNT csv"
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir ./benchmarks --experiment-name paynt-cav-final --generate-csv --workers $thread_count --show-only

    echo "generating OMDT csv"
    python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir ./models --experiment-name omdt-cav-final --workers $thread_count --maxmem 32 --generate-csv --show-only

    if [ ! -f ./results/logs/dtcontrol-final.csv ]; then
        echo "generating dtControl results"
        python3 generate-dtcontrol-results.py --models-dir ./benchmarks --output-dir dtcontrol-cav-final --generate-csv
    fi

    echo "creating csv file with results for OMDT"
    python3 best-time-omdt-parser.py --log-dir ./results/logs/omdt-cav-final

    echo "merging csv files"
    python3 merge-csv-files.py

    echo "generating tables and figures"
    python3 generate-tables-and-figures.py
    echo "Generated results to 'results/generated-results'"
    exit 0
fi

if [ "$overwrite" = true ]; 
then
    echo "Overwriting existing log files..."

    echo "generating dtPAYNT log files"
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir $benchmarks_dir --experiment-name paynt-cav-final --generate-csv --workers $thread_count --restart

    if [ "$skip_omdt" = false ]; then
    
        echo "generating OMDT log files"
        if [ -f results/logs/omdt-cav-final/results.csv ]; then
            rm results/logs/omdt-cav-final/results.csv
        fi
        cd /opt/OMDT
        python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir $models_dir --experiment-name omdt-cav-final --workers $thread_count --restart --maxmem 32 --generate-csv
        cd -
    else
        echo "skipping OMDT"
    fi

    echo "generating dtControl results"
    python3 generate-dtcontrol-results.py --models-dir $benchmarks_dir --output-dir ./results/logs/dtcontrol-cav-final --generate-csv
else
    echo "generating dtPAYNT log files"
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir $benchmarks_dir --experiment-name paynt-cav-final --generate-csv --workers $thread_count

    if [ "$skip_omdt" = false ]; then
        echo "generating OMDT log files"
        cd /opt/OMDT
        python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir $models_dir --experiment-name omdt-cav-final --workers $thread_count --maxmem 32 --generate-csv
        cd -
    else
        echo "skipping OMDT"
    fi

    if [ ! -f ./results/logs/dtcontrol-final.csv ]; then
        echo "generating dtControl results"
        python3 generate-dtcontrol-results.py --models-dir $benchmarks_dir --output-dir ./results/logs/dtcontrol-cav-final --generate-csv
    fi
fi


echo "creating csv file with results for OMDT"
python3 best-time-omdt-parser.py --log-dir ./results/logs/omdt-cav-final

echo "merging csv files"
python3 merge-csv-files.py

echo "generating tables and figures"
python3 generate-tables-and-figures.py

echo "Generated results to 'results/generated-results'"
