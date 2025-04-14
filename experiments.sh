#!/bin/bash

set -e

overwrite=false
provided_logs=false
generate_only=false
smoke_test=false
skip_omdt=false
model_subset=false

# CHANGE THIS ACCORDING TO YOUR SYSTEM
no_threads=2 # Ideally, you should have 16GB of RAM per thread (sometimes OMDT needs more)

while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -o | --overwrite ) overwrite=true; shift ;;
        -p | --provided-logs ) provided_logs=true; shift ;;
        -g | --generate-only ) generate_only=true; shift ;;
        -t | --smoke-test ) smoke_test=true; shift ;;
        -s | --skip-omdt ) skip_omdt=true; shift ;;
        -m | --model-subset) model_subset=true; shift ;;
        --no-threads) no_threads="$2"; shift 2 ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
done

benchmarks_dir="./benchmarks/all"
models_dir="./models/all"
if [ "$model_subset" = true ];
then
    benchmarks_dir="./benchmarks/subset"
    models_dir="./models/subset"
fi
if [ "$smoke_test" = true ];
then
    benchmarks_dir="./benchmarks/smoketest"
    models_dir="./models/smoketest"
fi

log_dir="./results/logs"

function run_dtcontrol {
    echo "generating dtControl log files..."
    python3 generate-dtcontrol-results.py --models-dir $benchmarks_dir --generate-csv "$@"
}

function run_dtpaynt {
    echo "generating dtPAYNT log files..."
    python3 experiments-dts-cav.py --paynt-dir /opt/paynt --models-dir $benchmarks_dir --experiment-name paynt-cav-final --generate-csv --workers $no_threads "$@"
}

function run_omdt {
    echo "generating OMDT log files..."
    cd /opt/OMDT
    python3 experiments-dts-cav-omdt.py --omdt-dir ./ --models-dir $models_dir --workers $no_threads --generate-csv --maxmem 32 "$@"
    cd -
}

function test_line_count {
    line_count=$(wc -l < "$1")
    if [ "$line_count" -ne $2 ]; then
        echo "Error: $1 does not contain a row for each model in the smoke test. Expected $line_count lines (including header)"
        exit 1
    fi
}

if [ "$provided_logs" = true ];
then
    echo "using provided log files..."
    python3 generate-tables-and-figures.py --file-path original-logs/final-merge.csv --add-dtcontrol-depths
    echo "Generated results using the original log files to 'results/generated-results'"
    exit 0
fi

if [ "$smoke_test" = true ];
then
    run_dtpaynt --experiment-name paynt-smoke-test --depth-max 1 --smoke-test --restart --timeout 30

    if [ -f ${log_dir}/omdt-smoke-test/results.csv ]; then
        rm ${log_dir}/omdt-smoke-test/results.csv
    fi
    run_omdt --experiment-name omdt-smoke-test --depth-max 1 --restart --timeout 30

    if [ -f ${log_dir}/dtcontrol-smoke-test.csv ]; then
        rm ${log_dir}/dtcontrol-smoke-test.csv
    fi
    run_dtcontrol --output-dir ${log_dir}/dtcontrol-smoke-test --smoke-test

    echo "creating csv file with results for OMDT"
    python3 best-time-omdt-parser.py --log-dir ${log_dir}/omdt-smoke-test --smoke-test

    echo ""
    echo "testing smoke test results"
    echo ""

    test_line_count "${log_dir}/paynt-smoke-test.csv" 7
    test_line_count "${log_dir}/omdt-smoke-test.csv" 7
    test_line_count "${log_dir}/dtcontrol-smoke-test.csv" 7

    echo "Smoke test passed!"
    exit 0
fi


if [ "$generate_only" = true ]; 
then
    run_dtpaynt --experiment-name paynt-cav-final --show-only

    echo "generating OMDT csv"
    run_omdt --experiment-name omdt-cav-final --show-only

    if [ ! -f ${log_dir}/dtcontrol-final.csv ]; then
        run_dtcontrol --output-dir ${log_dir}/dtcontrol-cav-final
    fi

    echo "creating csv file with results for OMDT"
    python3 best-time-omdt-parser.py --log-dir ${log_dir}/omdt-cav-final

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

    run_dtpaynt --experiment-name paynt-cav-final --restart

    if [ "$skip_omdt" = false ]; then
        echo "generating OMDT log files"
        if [ -f ${log_dir}/omdt-cav-final/results.csv ]; then
            rm ${log_dir}/omdt-cav-final/results.csv
        fi
        run_omdt --experiment-name omdt-cav-final --restart
    else
        echo "skipping OMDT"
    fi

    run_dtcontrol --output-dir ${log_dir}/dtcontrol-cav-final
else
    run_dtpaynt --experiment-name paynt-cav-final

    if [ "$skip_omdt" = false ]; then
        echo "generating OMDT log files"
        run_omdt --experiment-name omdt-cav-final
    else
        echo "skipping OMDT"
    fi

    if [ ! -f ${log_dir}/dtcontrol-final.csv ]; then
        run_dtcontrol --output-dir ${log_dir}/dtcontrol-cav-final
    fi
fi


echo "creating csv file with results for OMDT"
python3 best-time-omdt-parser.py --log-dir ${log_dir}/omdt-cav-final

echo "merging csv files"
python3 merge-csv-files.py

echo "generating tables and figures"
python3 generate-tables-and-figures.py
echo "Generated results to 'results/generated-results'"
