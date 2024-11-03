import random
from src.config import NUM_CITIES, INITIAL_TEMP, COOLING_RATE
from src.tsp import TSP


def main():
    # Generate random cities
    cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(NUM_CITIES)]

    # Create a TSP solver instance with the specified configurations
    tsp_solver = TSP(cities, initial_temp=INITIAL_TEMP, cooling_rate=COOLING_RATE)

    # Solve the TSP problem
    best_route, best_distance = tsp_solver.simulated_annealing()

    # Display results
    print("Best route found:", best_route)
    print("Total distance of the best route:", best_distance)


if __name__ == "__main__":
    main()
