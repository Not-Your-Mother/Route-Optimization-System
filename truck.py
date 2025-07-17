# truck.py
# Author: Kimberly DeSear
# Purpose: Contains the Truck class for WGUPS project.

# Create Truck class container to hold all truck-specific information
class Truck:
    def __init__(self, truck_id, package_list, departure_time, route=None):
        self.truck_id = truck_id
        self.package_list = package_list
        self.departure_time = departure_time
        self.route = route




