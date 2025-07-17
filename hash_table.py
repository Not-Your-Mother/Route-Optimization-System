# hash_table.py
# Author: Kimberly DeSear
# Purpose: Contains the hash table for WGUPS project.

from package import Package

# create custom hash table structure
class HashTable:
    def __init__(self):
        self.size = 41
        self.table = [None] * self.size

    # pass data from package tuples from main, extracting key and creating package objects
    def insert_packages (self, all_packages):
        for row in all_packages:
            key = row[0]
            package = Package(*row)
            self.table[key] = package

    # create getter method to allow package object data to be passed to other parts of the program
    def get_package(self, key):
        package = self.table[key]
        if package is None:
            return None
        return package



