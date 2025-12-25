import psutil
import time
import csv
import os
import sys

# Appending root directory to path for config import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def log_metrics(core_loads, assigned_core, sensor_id):
    """Logs the CPU metrics and routing decisions to a CSV file for visualization."""
    file_exists = os.path.isfile(config.LOG_FILE_PATH)
    
    with open(config.LOG_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write headers if the file is newly created
        if not file_exists:
            headers = ["Timestamp", "Sensor_ID", "Assigned_Core"] + [f"Core_{i}_Load" for i in range(len(core_loads))]
            writer.writerow(headers)
        
        # Append the current state data
        row = [time.strftime("%H:%M:%S"), sensor_id, assigned_core] + core_loads
        writer.writerow(row)

def heavy_computation(load_factor):
    """Simulates a CPU-bound task to represent sensor data processing."""
    dummy = 0
    # The larger the loop, the higher the simulated CPU utilization
    for i in range(load_factor * 500000): 
        dummy += i
    return dummy

def balance_and_distribute(data_queue):
    """MAIN ALGORITHM: Monitors CPU state and routes data to the optimal core."""
    print("✅ [BALANCER] Load Balancer Active. Monitoring CPU Cores...")
    
    # Infinite loop to constantly poll for new sensor data
    while True:
        if not data_queue.empty():
            # 1. Retrieve data packet from the queue
            sensor_data = data_queue.get()
            
            # 2. Retrieve real-time CPU utilization for all individual cores
            core_loads = psutil.cpu_percent(interval=0.1, percpu=True)
            
            # 3. ALGORITHM: Identify the core with the absolute minimum load
            best_core = core_loads.index(min(core_loads))
            
            # Display the routing decision
            print(f"🔄 Routing {sensor_data['sensor_id']} -> CPU Core {best_core} (Current Load: {core_loads[best_core]}%)")
            
            # 4. Log the metrics for analytical evaluation
            log_metrics(core_loads, best_core, sensor_data['sensor_id'])
            
            # 5. Execute the processing task on the assigned core
            heavy_computation(sensor_data["processing_load"])
            
            print(f"✅ Successfully Processed {sensor_data['sensor_id']}")
        else:
            time.sleep(0.1) # Idle sleep to prevent CPU blocking when queue is empty