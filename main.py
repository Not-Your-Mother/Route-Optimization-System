# Author: Kimberly DeSear, Student ID: 012281223
# main.py
# Purpose: Contains the Main file for WGUPS project.

from datetime import time, timedelta, datetime
from data import package_address_truck_list, all_packages, adjacency_dict
from tracking import Tracking
from status import Status
from route import Route
from truck import Truck
from hash_table import HashTable


def main():
    AVERAGE_SPEED = 18  # variable for pre-set average speed

    #instantiates Hash Table and injects package data to create package objects
    hash_table = HashTable()
    hash_table.insert_packages(all_packages)

    #creates lists to hold packages assigned to each truck
    truck_package_list_1 = []
    truck_package_list_2 = []
    truck_package_list_3 = []

    #sets each trucks departure time
    truck_1_departure_time = time(8, 00)
    truck_2_departure_time = time(8, 00)
    truck_3_departure_time = time(9, 10)

    #reads master package list and assigns packages to each truck by index filter
    for truck in package_address_truck_list:
        if truck[2] == 1:
            truck_package_list_1.append(truck)
        if truck[2] == 2:
            truck_package_list_2.append(truck)
        if truck[2] == 3:
            truck_package_list_3.append(truck)

    # creates 3 truck objects, passing the truck number, it's package list, and departure time
    truck1 = Truck(1, truck_package_list_1, truck_1_departure_time)
    truck2 = Truck(2, truck_package_list_2, truck_2_departure_time)
    truck3 = Truck(3, truck_package_list_3, truck_3_departure_time)

    # creates 3 route objects, passing one truck list and the adjacency dictionary to calculate each truck's route
    route1 = Route(truck_package_list_1, adjacency_dict)
    route2 = Route(truck_package_list_2, adjacency_dict)
    route3 = Route(truck_package_list_3, adjacency_dict)

    # prompts the creation of the filtered adjacency list for each truck's route,
    # so that only necessary adjacencies are used
    route1.filter_adjacency_list()
    route2.filter_adjacency_list()
    route3.filter_adjacency_list()

    # starts the nearest_neighbor() function in each route, assigning the resultant route to the truck object
    truck1.route = route1.nearest_neighbor()
    truck2.route = route2.nearest_neighbor()
    truck3.route = route3.nearest_neighbor()

    # calculates the final distance of each truck by taking the final node in the route and pulling its
    # accumulated distance
    truck1_distance = truck1.route[-1][2]
    truck2_distance = truck2.route[-1][2]
    truck3_distance = truck3.route[-1][2]

    # total distance of entire route as function of distance of each truck
    total_distance = truck1_distance + truck2_distance + truck3_distance

    # Calculate delivery times
    # takes all route nodes and loops through them by package_id, calculates delivery time by taking
    # each node's accumulated distance, dividing by an average speed constant (18 mph), using the result to calculate
    # the duration of time to the node, and then using the departure_time assigned to the package, calculating the actual
    # delivery time.
    all_nodes = [truck1.route, truck2.route, truck3.route]
    for route in all_nodes:
        for node in route:
            package = hash_table.get_package(node[0])
            if package is not None:
                accumulated_distance = node[2]
                decimal_hours = accumulated_distance / AVERAGE_SPEED
                hours = int(decimal_hours)
                minutes = round((decimal_hours - hours) * 60)
                package.delivery_time = (datetime.combine(datetime.today(), package.departure_time) +
                                         timedelta(hours=hours, minutes=minutes)).time()

    # instantiate Status class
    status = Status()

    # instantiate Tracking class
    tracking = Tracking()

    while True:
        # start user_interface and assign to variables being returned for query, pass distance variables for display
        query_package_id, query_time = tracking.user_interface(truck1_distance, truck2_distance, truck3_distance,
                                                               total_distance)
        if query_package_id is None or query_time is None:
            return
        package_query_list = []
        if query_package_id == "all":
            for i in range(1, 41):
                package_query_list.append(hash_table.get_package(i))

        else:
            package_query_list.append(hash_table.get_package(int(query_package_id)))

        # calls status_clear to ensure clean list before status update is called
        status.status_clear()
        status_list = status.status_update(query_time, package_query_list)

        # using data passed from user_interface, starts look_up function
        tracking.look_up(package_query_list, status_list)

        # calls display_results to display user-requested information
        tracking.display_results()


if __name__ == '__main__':
    main()
