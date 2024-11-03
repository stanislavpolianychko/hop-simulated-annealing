import random
import time
from src.tsp import TSP


def main(testing_case):
    # Common settings for cities
    default_number_of_cities = 10
    default_grid_size = 100

    cities = [(random.randint(0, default_grid_size), random.randint(0, default_grid_size)) for _ in range(default_number_of_cities)]

    # Define configurations based on testing case
    if testing_case == 1:
        initial_temp = 10000
        cooling_rate = 0.99
        print("\nRunning Configuration 1: Baseline Setup")

    elif testing_case == 2:
        initial_temp = 10000
        cooling_rate = 0.95
        print("\nRunning Configuration 2: Faster Cooling Rate")

    elif testing_case == 3:
        initial_temp = 20000
        cooling_rate = 0.995
        print("\nRunning Configuration 3: Higher Initial Temperature and Slower Cooling")

    else:
        raise ValueError("Invalid testing case. Please choose 1, 2, or 3.")

    # Create a TSP solver instance with the specified configurations
    tsp_solver = TSP(cities, initial_temp=initial_temp, cooling_rate=cooling_rate)

    # Measure the time taken to solve the TSP problem
    start_time = time.time()
    best_route, best_distance, iterations = tsp_solver.simulated_annealing()
    end_time = time.time()

    # Calculate performance metrics
    execution_time = end_time - start_time

    # Display results and metrics
    print("Best route found:", best_route)
    print("Total distance of the best route:", best_distance)
    print("Iterations:", iterations)
    print("Execution time (seconds):", execution_time)


if __name__ == "__main__":
    # Run each test case to gather experimental data
    print("TESTING CASE 1:")
    main(testing_case=1)
    print("TESTING CASE 2:")
    main(testing_case=2)
    print("TESTING CASE 4:")
    main(testing_case=3)
