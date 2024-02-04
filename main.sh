#!/bin/bash

script_directory="scripts"

log_file="main.log"

files=("VQHA80_table_manager.py" "VQHA98_table_manager.py" "snowdata_view_schema.sql")

function execute_scripts() {
    current_datetime=$(date +"%Y-%m-%d %H:%M:%S")
    echo "===== Running Scripts - $current_datetime =====" >> "$log_file"
    for file in "${files[@]}"; do
        echo "$current_datetime - Executing $file" >> "$log_file"
        python3 "$script_directory/$file" >> "$log_file" 2>&1
        echo "-------------------------" >> "$log_file"
    done
    echo "===== Scripts Completed - $current_datetime =====" >> "$log_file"
}

# Hauptprogramm
while true; do
    execute_scripts
    echo "Warte 5 Minuten für den nächsten Durchlauf..."
    sleep 300
done
