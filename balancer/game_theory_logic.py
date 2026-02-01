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

def heavy_computation(load_factor, assigned_core):
    """Background task simulation"""
    dummy = 0
    for i in range(load_factor * 2000000): 
        dummy += i

def balance_and_distribute(data_queue):
    print("✅ [BALANCER] Load Balancer Active. Monitoring CPU Cores...")
    
    while True:
        if not data_queue.empty():
            sensor_data = data_queue.get()
            
            # 1. Check CPU Load
            core_loads = psutil.cpu_percent(interval=None, percpu=True)
            
            # 2. ALGORITHM UPDATE: Randomized Selection among Free Cores
            min_load = min(core_loads)
            candidates = [i for i, load in enumerate(core_loads) if load == min_load]
            best_core = random.choice(candidates)
            
            # 3. Log & Execute
            print(f"🔄 Routing {sensor_data['sensor_id']} -> CPU Core {best_core} (Load: {min_load}%)")
            log_metrics(core_loads, best_core, sensor_data['sensor_id'])
            
            task_thread = threading.Thread(
                target=heavy_computation, 
                args=(sensor_data["processing_load"], best_core)
            )
            task_thread.start()
            
        else:
            time.sleep(0.01)