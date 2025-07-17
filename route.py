# route.py
# Author: Kimberly DeSear
# Purpose: Contains the route class for WGUPS project.

# create route class structure
class Route:
    def __init__(self, package_list, adjacency_dict):
        self.package_list = package_list
        self.adjacency_dict = adjacency_dict
        self.filtered_adjacency_dict = {} #new dict to hold truck route specific addresses
                                          # (address, package_id) : [(address1, distance), (address2, distance)...]

    # for each package sent from truck class, compare address with adjacency_dict, on match add to new dict
    def filter_adjacency_list(self):
        for package in self.package_list:
            for key in self.adjacency_dict:
                if package[1] == key:
                    self.filtered_adjacency_dict[package[1], package[0]] = self.adjacency_dict[key]
                    # swaps key order from (package_id, address) to (address, package_id)

    # graph transversal, starts at hub, extracts adjacencies from filtered dict, finds shortest distance
    # loops over all key addresses from filtered dict while unvisited_nodes is not empty
    def nearest_neighbor(self):
        current_node = (0, 0)
        distance_accumulator = 0 # holds total distance traveled
        adjacency_list = self.adjacency_dict[0] # values of dict key (address, distance)
        visited_nodes = [current_node] # tracks visited nodes, future use / debugging
        unvisited_nodes = list(self.filtered_adjacency_dict.keys())# list of filtered dict keys (address, package_id)
        truck_route_list = [(current_node[1], current_node[0], distance_accumulator)] # (package_id, address, distance to node)


        while unvisited_nodes:
            temp_list = [] #further filters adjacency_list to ensure only unvisited nodes are measured
            for i in adjacency_list:
                for j in unvisited_nodes:
                    if i[0] == j[0]:
                        temp_list.append(i)
                        break
            adjacency_list = temp_list

            min_tracker = adjacency_list[0] # initializes min_tracker to first list element's distance
            for i in adjacency_list:
                if i[1] < min_tracker[1]:
                    min_tracker = i


            visited_nodes.append(current_node)
            if not unvisited_nodes: # ends while loop if unvisited_nodes is empty
                break
            next_address = min_tracker[0] # extracts address from adjacency list to get next filtered dict entry


            for i in unvisited_nodes: # sets current_node to (address, package_id) instead of just address
                if i[0] == next_address:
                    current_node = i
                    unvisited_nodes.remove(current_node)
                    break

            distance_accumulator += min_tracker[1]
            truck_route_list.append((current_node[1], current_node[0], distance_accumulator))
            adjacency_list = self.filtered_adjacency_dict[current_node]

            # handles duplicate addresses to add correct distance and correct delivery timing
            for i in unvisited_nodes[:]:  # create shallow copy of list for iteration
                if i[0] == current_node[0] and i != current_node: # checks for matching addresses
                    truck_route_list.append((i[1], i[0], distance_accumulator))
                    visited_nodes.append(i)
                    unvisited_nodes.remove(i)

        return truck_route_list


