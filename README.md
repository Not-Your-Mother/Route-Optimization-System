# Route Optimization System for Delivery Logistics

An automated delivery route planner that solves a constrained Traveling Salesman–style problem using real-world delivery rules. This project was developed as part of WGU's C950 Data Structures and Algorithms II course.

## Project Overview

The system determines the most efficient delivery routes for multiple trucks based on package deadlines, delivery groupings, and manually loaded truck assignments. The focus is on route optimization, algorithm design, and runtime efficiency under constraints similar to real-world logistics systems.

## Key Features

- Nearest neighbor–based greedy algorithm for efficient routing
- Custom-built hash table for package storage and fast lookup
- Manual truck loading and address correction support
- Real-time distance calculation and accumulated mileage tracking

## Tools & Technologies

- Python (3.x)
- Object-Oriented Programming (OOP)
- Greedy Algorithms
- Graph Traversal
- Custom Hash Table Implementation

## File Structure

- `main.py` – Entry point; coordinates delivery logic
- `route.py` – Routing class that performs traversal logic and distance tracking
- `truck.py` – Truck container class
- `package.py` – Package data model
- `hashtable.py` – Custom hash table class
- `tracking.py` – Package tracking and lookup logic
- `status.py` – Status lookup engine based on delivery timing
- `enum_values.py` – Enumerations for delay markers and status types

## How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/YourUsername/route-optimization-system.git
   cd route-optimization-system

2. **Ensure Python 3 is installed**

    Check your version with:

    ```bash
    python3 --version
    ```

3. **Run the program**

    Use:

    ```bash
    python3 main.py
    ```

    Or, if your system uses `python` instead of `python3`:

    ```bash
    python main.py
    ```

4. **Use the menu**

    Once the app launches, follow the menu prompts to:
    - View all package statuses at end-of-day
    - Query the status of a single package at a specific time
    - View all package statuses at a specific time
    - Exit the program   
