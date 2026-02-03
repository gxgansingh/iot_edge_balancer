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

def game_theory_balance(data_queue):
    print("[GAME THEORY] Balancer Active using Mixed Strategy Nash Equilibrium...")
    
    while True:
        if not data_queue.empty():
            sensor_data = data_queue.get()
            
            # 1. Get Current State (Load of all cores)
            core_loads = psutil.cpu_percent(interval=None, percpu=True)
            total_cores = len(core_loads)
            
            # 2. GAME THEORY ALGORITHM: Calculate Probabilities (Utility Function)
            # Logic: More Free Space = Higher Probability of Selection
            # Formula: Utility_i = (100 - Load_i)
            
            utilities = [(100 - load) for load in core_loads]
            total_utility = sum(utilities)
            
            if total_utility == 0:
                # If all cores are fully loaded, use uniform distribution
                probabilities = [1/total_cores] * total_cores
            else:
                # Normalize values to get Probability Distribution (0.0 to 1.0)
                probabilities = [u / total_utility for u in utilities]
            
            # 3. Decision Making based on Weighted Randomness (Mixed Strategy)
            # Instead of picking the absolute min, we pick based on probability weights
            best_core = random.choices(range(total_cores), weights=probabilities, k=1)[0]
            