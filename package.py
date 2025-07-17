# package.py
# Author: Kimberly DeSear
# Purpose: Contains the Package class for WGUPS project.

#package class creates package objects, holds all package data
from datetime import time

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, truck_id=0, departure_time=time(23, 59), delay_marker=0,
                 special_notes=None, delivery_status= "Delivered", delivery_time=time(23,59)):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.truck_id = truck_id
        self.departure_time = departure_time
        self.delay_marker = delay_marker # 0 = on time, 1 = delayed: in transit, 2 = delayed: wrong address
        self.delivery_status = delivery_status # defaults to Delivered
        self.delivery_time = delivery_time
        self.special_notes = special_notes

        #package_id 0, address 1, city 2, state 3, zip_code 4, deadline 5, weight 6,
        # truck_id 7, departure_time 8, delay_marker 9, delivery_status 10, delivery_time 11, special_notes 12
