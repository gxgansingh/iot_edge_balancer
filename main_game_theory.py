import multiprocessing
import time
import sys
import os

# Import modules
from sensors.virtual_sensors import start_sensors

# Notice: importing the new logic
from balancer.game_theory_logic import game_theory_balance 
import config

if __name__ == "__main__":
    print("==========================================================")
    print("🧠 IOT EDGE: GAME THEORY LOAD BALANCING SIMULATION")
    print("   Algorithm: Non-Cooperative Mixed Strategy")
    print("==========================================================")
    
    data_pipeline = multiprocessing.Queue()

    # Process 1: Sensors (Same as before)
    sensor_process = multiprocessing.Process(target=start_sensors, args=(data_pipeline,))
    
    # Process 2: Game Theory Balancer (New Logic)
    balancer_process = multiprocessing.Process(target=game_theory_balance, args=(data_pipeline,))

    try:
        sensor_process.start()
        balancer_process.start()

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n🛑 [MAIN] Shutting down Game Theory Simulation...")
        sensor_process.terminate()
        balancer_process.terminate()
        print("✅ System successfully terminated.")