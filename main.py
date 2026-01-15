import multiprocessing
import time
import sys
import os

# Import local modules
from sensors.virtual_sensors import start_sensors
from balancer.distributor import balance_and_distribute
import config

if __name__ == "__main__":
    print("==========================================================")
    print("🚀 IOT EDGE: INTRA-NODE BALANCER SIMULATION INITIALIZING")
    print("==========================================================")
    
    # Inter-process communication pipeline (Queue)
    # Sensors will produce data into this queue, Balancer will consume from it.
    data_pipeline = multiprocessing.Queue()

    # Process 1: Start the virtual sensors in an independent process
    sensor_process = multiprocessing.Process(target=start_sensors, args=(data_pipeline,))
    
    # Process 2: Start the Load Balancer in another independent process
    balancer_process = multiprocessing.Process(target=balance_and_distribute, args=(data_pipeline,))

    try:
        # Launch both processes
        sensor_process.start()
        balancer_process.start()

        # Keep the main thread alive until interrupted by the user
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n🛑 [MAIN] User interrupt detected. Shutting down simulation...")
        # Graceful termination of child processes
        sensor_process.terminate()
        balancer_process.terminate()
        print("✅ System successfully terminated.")