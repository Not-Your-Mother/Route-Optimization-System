# status.py
# Author: Kimberly DeSear
# Purpose: Contains the Status class for WGUPS project.

#Status class takes query_time and calculates appropriate status based on time and returns for display
from datetime import time

class Status:
    def __init__(self):
        self.query_time = None
        self.package_query_list = []
        self.status_list = []
        self.status_clear()

    #ensures a clear status_list so results do not accumulate from multiple queries
    def status_clear(self):
        self.query_time = None
        self.package_query_list = []
        self.status_list = []

    #uses delay_marker in package objects to assign correct status logic
    def status_update(self, query_time, package_query_list):
        self.query_time = query_time
        self.package_query_list = package_query_list

        for package in self.package_query_list:
            departure_time = package.departure_time
            delivery_time = package.delivery_time
            delay_marker = package.delay_marker
            address = package.address
            zip_code = package.zip_code

            # display_marker 0 = no delay, uses standard logic
            if delay_marker == 0:
                # sets status "At Hub" if the query time entered is before pacakge departure time
                if query_time < departure_time:
                    status = "At Hub"
                    status_time = query_time

                # sets status "En Route" if query time entered is after departure time but before delivery time
                elif departure_time <= query_time < delivery_time:
                    status = "En Route"
                    status_time = query_time

                # sets status as delivered if neither of the previous conditions are true (i.e., query time is
                # delivery time or later)
                else:
                    status = "Delivered"
                    status_time = delivery_time

                self.status_list.append((package.package_id, status, status_time))


            #delay_marker 1 = delayed in transit, displays custom delay message
            if delay_marker == 1:
                # sets custom message for package prior to departure, indicating that package was delayed in transit
                if query_time < departure_time:
                    status = "Delayed: In Transit"
                    status_time = query_time

                elif departure_time <= query_time < delivery_time:
                    status = "En Route"
                    status_time = query_time

                else:
                    status = "Delivered"
                    status_time = package.delivery_time

                self.status_list.append((package.package_id, status, status_time))

            # delay marker 2 = incorrect address, only for package 9, ensures that correct address is returned
            #   at appropriate time, returns custom status messages
            if delay_marker == 2:
                # prior to the time for address correction, package 9 indicates delay due to incorrect address
                delay_time_9 = time(10, 20)
                if query_time < delay_time_9:
                    status = "Delayed: Incorrect Address"
                    status_time = query_time
                    self.status_list.append((package.package_id, status, status_time))

                # after address correction, but prior to delivery,
                # corrected address and custom en route message displayed for package 9
                elif delay_time_9 <= query_time < delivery_time:
                    status = "En Route: Address corrected"
                    address = "410 S. State St."
                    zip_code = "84111"
                    status_time = query_time
                    self.status_list.append((package.package_id, status, status_time, address, zip_code))

                # if neither previous condition is met, the package will indicate delivered with the corrected address
                else:
                    status = "Delivered: Address corrected"
                    address = "410 S. State St."
                    zip_code = "84111"
                    status_time = delivery_time
                    self.status_list.append((package.package_id, status, status_time, address, zip_code))

        #list of appropriate status information returned to main for display
        return self.status_list


















