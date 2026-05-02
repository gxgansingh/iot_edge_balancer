# IoT Edge Balancer

Simulation of an intra-node load balancer for synthetic IoT traffic. The project compares a simple minimum-load distributor with a game-theory-inspired weighted strategy that routes work across CPU cores based on current load.

## Overview

The repository contains two runnable simulations:

- `main.py` starts the sensor generator and the basic balancer in separate processes.
- `main_game_theory.py` starts the sensor generator and the mixed-strategy game-theory balancer.

Both variants use `multiprocessing.Queue` to pass synthetic sensor events from `sensors/virtual_sensors.py` to the balancer logic in `balancer/`.

## Introduction

In high-velocity IoT environments, edge nodes can be hit by many data packets at the same millisecond, creating a thundering herd effect.

Most deterministic load balancers keep choosing the same best-looking core, which can cause core clumping: one CPU core gets overloaded while the others stay underused. This project treats resource allocation as a non-cooperative game so that no single core is overwhelmed.

## Educational Deep Dive

### 1. Bypassing the Python GIL

Standard Python code is restricted by the Global Interpreter Lock, which prevents one process from using multiple cores at the same time. This project uses inter-process communication and `multiprocessing` to create independent worker processes, allowing hardware-level parallelism on a multi-core system.
