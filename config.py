import os

# ----------------- IOT SENSOR SETTINGS -----------------
NUM_SENSORS = 5                     
GENERATION_INTERVAL = 0.1           # CHANGE: Fast Data! (Pehle 1.0 tha, ab 0.1 kiya)

# ----------------- BALANCER SETTINGS -------------------
CPU_THRESHOLD = 75.0                
WORKER_PROCESSES = os.cpu_count()   

# ----------------- LOGGING SETTINGS --------------------
LOG_FILE_PATH = "logs/system_metrics.csv" 

print(f"System Configuration Loaded: Utilizing {WORKER_PROCESSES} CPU cores for load balancing.")