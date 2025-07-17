# tracking.py
# Author: Kimberly DeSear
# Purpose: Contains the Tracking class for WGUPS project.
from datetime import time, datetime

# Tracking class contains all logic for the look-up function, user interface, and return display
class Tracking:
    def __init__(self):
        self.display_list = []
        self.query_package_id = None
        self.query_time=None

    # look-up function takes package_query_list and status_list as inputs and creates a display_list of results to send to the display function
    def look_up(self, package_query_list, status_list):
        self.display_list = []
        for package in package_query_list:
            for status in status_list:
                if package.package_id == status[0]:
                    #filtering logic for package 9 handling
                    if package.package_id == 9 and (status[1] == "En Route: Address corrected" or status[1] == "Delivered: Address corrected"):
                        self.display_list.append((package.package_id, status[3], package.city, package.state, package.zip_code, package.deadline,
                        package.weight, status[1], status[2], package.truck_id, package.special_notes))

                    #all other package handling
                    else:
                        self.display_list.append((package.package_id, package.address, package.city, package.state, package.zip_code, package.deadline,
                        package.weight, status[1], status[2], package.truck_id, package.special_notes))

    #user_interface takes in distances to display when requested in user_interface
    #creates menu system for user navigation and input handling to send to main to gather required information for look_up function
    def user_interface(self, truck1_distance, truck2_distance, truck3_distance, total_distance):
        truck1_distance = truck1_distance
        truck2_distance = truck2_distance
        truck3_distance = truck3_distance
        total_distance = total_distance

        #navigation menu logic with input validation and error handling
        while True:
            self.query_time = None
            self.query_package_id = None

            print("*****************************\n* Welcome to WGUPS Tracking *\n*****************************\n")
            print("Please select an option:")
            user_input = input("1. Look up a package by ID\n2. Look up all packages\n3. Total Delivery Miles \n4. Exit\nEnter your choice: ")

            match user_input:
                case "1":
                    self.query_package_id = input("Enter package ID (1-40): ")
                    try:
                        if (int(self.query_package_id)) not in range(1,41):
                            print("\nPlease enter a valid package ID.\n")
                            continue
                        else:
                            pass
                    except ValueError:
                        print("\nPlease enter a valid package ID.\n")
                        continue

                    while True:
                        sub_choice_1 = input("\n1. Enter query time\n2. Request delivery time\n3. Exit\nEnter your choice: ")
                        match sub_choice_1:
                            case "1":
                                self.query_time = input("\nEnter query time (HH:MM AM/PM): \n")
                                try:
                                    self.query_time = datetime.strptime(self.query_time.strip(), "%I:%M %p").time()
                                    break
                                except ValueError:
                                    print("\nPlease enter a valid time\n")

                            case "2":
                                self.query_time = time(17, 00)
                                break
                            case "3":
                                break
                            case _:
                                print("\nInvalid input. Please try again.\n")
                                continue
                    break

                case "2":
                    self.query_package_id = "all"
                    while True:
                        sub_choice_2 = input("\n1. Enter query time\n2. All delivery times\n3. Exit\nEnter your choice: ")
                        match sub_choice_2:
                            case "1":
                                self.query_time = input("\nEnter query time (HH:MM AM/PM): \n")
                                try:
                                    self.query_time = datetime.strptime(self.query_time.strip(), "%I:%M %p").time()
                                    break
                                except ValueError:
                                    print("\nPlease enter a valid time\n")

                            case "2":
                                self.query_time = time(17, 00)
                                break
                            case "3":
                                break
                            case _:
                                print("\nInvalid input. Please try again.\n")
                                continue
                    break

                case "3":
                    print(f"\nTruck 1 Mileage: {truck1_distance:.2f}\nTruck 2 Mileage: {truck2_distance:.2f}\nTruck 3 Mileage: {truck3_distance:.2f}"
                          f"\nTotal Mileage: {total_distance:.2f}\n")
                    self.query_package_id = "all"
                    self.query_time = time(17, 00)
                    break


                case "4":
                    break
                case _:
                    print("\nInvalid input. Please try again.\n")

        return self.query_package_id, self.query_time

    #display logic to take display_list tuples from look_up function and display for readability
    def display_results(self):
        headers = ["Package ID", "Address","City", "State", "Zip Code", "Deadline", "Weight", "Status", "Status-Time", "Truck ID", "Notes" "\n"]

        # creates headers for display
        for header in headers:
            print(header.ljust(25), end="")
        print(("*" * (15 * len(headers))))

        #unpacks tuples and displays information under headers
        for row in self.display_list:
            for item in row:
                print(str(item).ljust(25), end="")
            print()



