import psutil
import time
import csv
import os
import sys
import threading
import random

# Root folder path setup
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def log_metrics(core_loads, assigned_core, sensor_id):
    """Logs the decision for visualization."""
    # Log file path
    log_file = "logs/game_theory_metrics.csv"
    
    file_exists = os.path.isfile(log_file)
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            headers = ["Timestamp", "Sensor_ID", "Assigned_Core"] + [f"Core_{i}_Load" for i in range(len(core_loads))]
            writer.writerow(headers)
        row = [time.strftime("%H:%M:%S"), sensor_id, assigned_core] + core_loads
        writer.writerow(row)