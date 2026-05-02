# IoT Edge Balancer

Simulation of an intra-node load balancer for synthetic IoT traffic. The project compares a simple minimum-load distributor with a game-theory-inspired weighted strategy that routes work across CPU cores based on current load.

## Overview

The repository contains two runnable simulations:

- `main.py` starts the sensor generator and the basic balancer in separate processes.
- `main_game_theory.py` starts the sensor generator and the mixed-strategy game-theory balancer.

Both variants use `multiprocessing.Queue` to pass synthetic sensor events from `sensors/virtual_sensors.py` to the balancer logic in `balancer/`.
