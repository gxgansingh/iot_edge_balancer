import time
import random
import sys
import os

# Appending root directory to path for config import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def generate_data(sensor_id):
    """Generates synthetic telemetry data for a specific sensor ID."""
    return {
        "sensor_id": f"SENSOR_{sensor_id}",
        "timestamp": time.strftime("%H:%M:%S"),
        "temperature": round(random.uniform(25.0, 85.0), 2), # Range: 25°C to 85°C
        "vibration_freq": round(random.uniform(1.0, 10.0), 2), # Range: 1Hz to 10Hz
        "processing_load": random.randint(5, 20) # Simulates the computational weight of the packet
    }

def start_sensors(data_queue):
    """Continuously generates data and pushes it to the multiprocessing queue."""
    print(f"✅ [SENSORS] {config.NUM_SENSORS} Virtual Sensors Initialized and Transmitting...")
    
    try:
        while True:
            for i in range(1, config.NUM_SENSORS + 1):
                # Generate synthetic data
                sensor_data = generate_data(i)
                
                # Push data to the inter-process pipeline (Queue)
                data_queue.put(sensor_data)
                
            # Wait for the specified interval before the next transmission
            time.sleep(config.GENERATION_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n🛑 [SENSORS] Sensor transmission halted.")