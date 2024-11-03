import math
import random


class TSP:
    def __init__(self, cities, initial_temp, cooling_rate):
        """
        Initialize the TSP solver with cities, initial temperature, and cooling rate.

        Parameters:
        - cities: List of (x, y) coordinates representing cities.
        - initial_temp: Initial temperature for the Simulated Annealing process.
        - cooling_rate: The rate at which the temperature cools down.
        """
        self.cities = cities
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate

    @staticmethod
    def calculate_distance(city1, city2):
        """Calculate the Euclidean distance between two cities."""
        return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

    def route_distance(self, route):
        """Calculate the total distance of a given route (order of cities)."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.calculate_distance(route[i], route[i + 1])
        total_distance += self.calculate_distance(route[-1], route[0])  # Return to the starting city
        return total_distance

    def simulated_annealing(self):
        """Simulated Annealing algorithm to find the shortest route."""
        current_route = self.cities[:]
        random.shuffle(current_route)
        current_temp = self.initial_temp
        best_route = current_route
        best_distance = self.route_distance(best_route)
        iterations = 0

        while current_temp > 1:
            iterations += 1
            # Create a new route by swapping two cities
            new_route = current_route[:]
            i, j = random.sample(range(len(self.cities)), 2)
            new_route[i], new_route[j] = new_route[j], new_route[i]

            # Calculate the distance of the current and new routes
            current_distance = self.route_distance(current_route)
            new_distance = self.route_distance(new_route)

            # Decide to accept the new route based on temperature
            if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / current_temp):
                current_route = new_route
                current_distance = new_distance
                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance

            # Gradually reduce the temperature
            current_temp *= self.cooling_rate

        return best_route, best_distance, iterations
