import math
import random


class TSP:
    def __init__(self, cities, initial_temp=10000, cooling_rate=0.99):
        """
        Initializes the TSP solver with cities, initial temperature, and cooling rate.

        Parameters:
        - cities: List of (x, y) coordinates representing cities.
        - initial_temp: Initial temperature for the Simulated Annealing process.
        - cooling_rate: The rate at which the temperature cools down.
        """
        self.cities = cities
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate

    @staticmethod
    def distance(city1, city2):
        """Calculate the Euclidean distance between two cities."""
        return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

    def route_distance(self, route):
        """Calculate the total distance of a given route."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance(route[i], route[i + 1])
        total_distance += self.distance(route[-1], route[0])
        return total_distance

    def simulated_annealing(self):
        """Simulated Annealing algorithm to find the shortest route."""
        current_route = self.cities[:]
        random.shuffle(current_route)
        current_temp = self.initial_temp
        best_route = current_route
        best_distance = self.route_distance(best_route)

        while current_temp > 1:
            new_route = current_route[:]
            i, j = random.sample(range(len(self.cities)), 2)
            new_route[i], new_route[j] = new_route[j], new_route[i]

            current_distance = self.route_distance(current_route)
            new_distance = self.route_distance(new_route)


            if new_distance < current_distance or random.random() < math.exp(
                    (current_distance - new_distance) / current_temp):
                current_route = new_route
                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance

            # Gradually reduce the temperature
            current_temp *= self.cooling_rate

        return best_route, best_distance
