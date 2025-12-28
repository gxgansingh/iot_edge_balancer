import os

# ----------------- IOT SENSOR SETTINGS -----------------
NUM_SENSORS = 5                     # Number of virtual sensors to simulate
GENERATION_INTERVAL = 1.0           # Frequency of data generation in seconds

# ----------------- BALANCER SETTINGS -------------------
CPU_THRESHOLD = 75.0                # Threshold percentage to classify a core as 'overloaded'
WORKER_PROCESSES = os.cpu_count()   # Dynamically counts the total CPU cores on the host machine

# ----------------- LOGGING SETTINGS --------------------
LOG_FILE_PATH = "logs/system_metrics.csv" # Path to store performance metrics

print(f"System Configuration Loaded: Utilizing {WORKER_PROCESSES} CPU cores for load balancing.")