<h1>Simulated Annealing</h1>
<h3>Heuristic Optimalisation Problems Solving using Simulated Annealing</h3>

<h3>Research was done by FEI TUKE Intelligent Systems students:</h2>
<ul>
  <li>Stanislav Polianychko</li>
  <li>Vladyslav Rudion</li>
  <li>Oleksiy Orlyk</li>
</ul>


<h2>Properties and Inspirations of Simulated Annealing</h2>
<h3>What is the inspiration of algorithm?</h3>
<p>Simulated Annealing (SA) is inspired by the process of heating and cooling metals. When metal is very hot, its atoms move around a lot, which helps it take different shapes. As it cools down slowly, the atoms settle into a more stable, strong structure. SA copies this idea by starting with a lot of "freedom" to make big moves and gradually "settling" as it narrows down to the best solution.</p>

<h3>How it's can be useful for coding problems solving?</h3>
<p>Simulated Annealing (SA) is an optimization method that starts with a random solution and a high "temperature," which allows it to explore different options. As the temperature slowly decreases, SA becomes more selective, sticking to better solutions as it "cools" down. It sometimes accepts worse solutions early on to avoid getting stuck, but as temperature lowers, it increasingly focuses on better ones until it finds the optimal solution.</p>

```plaintext
Initialize solution and temperature
While temperature is high:
    Generate new solution by slightly changing current one
    If new solution is better, accept it
    If worse, accept it with a probability based on temperature
    Decrease temperature
Return best solution found
```
* <b>Temperature</b>: A control value that starts high and gradually lowers, influencing the algorithm’s willingness to explore worse solutions early on. As it cools, it narrows the search.
* <b>Cools/Heats</b>: Cooling means gradually reducing the temperature, which makes the algorithm more selective over time. Heating is rarely used but would involve increasing temperature to allow more exploration.

<h3>What are the main properties of Simulated Annealing?</h3>
1. <b>Randomness:</b> They use randomness to explore different solutions, helping avoid getting stuck in local optima.
2. <b>Objective Function:</b> This function measures the "cost" or "fitness" of a solution, guiding the algorithm toward optimal solutions.
3. <b>Acceptance Probability:</b> Allows worse solutions to be accepted based on probability (controlled by a parameter like "temperature"), enabling broader exploration.
4. <b>Cooling Schedule:</b> Defines how a parameter like "temperature" gradually decreases, shifting the algorithm from exploration to fine-tuning.
5. <b>Termination Condition:</b> A stopping point, often set by a low temperature, a maximum number of iterations, or a minimal improvement threshold.

<h2>Used Sources and Real World Problems Solved with SA (TSP)</h2>
<h3>Used Sources</h3>
* <a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a>
* <a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a>
* <a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a>
* <a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a>
* <a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a>
* <a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a>
* <a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a>

<h3>Real World Problems Solved with SA</h3>
1) Where it's used?
2) How and what is applied here?

* <b>Airline Crew Scheduling:</b> Airlines like American Airlines and Delta have used SA to schedule flight crew rotations. It helps balance crew availability, minimize costs, and meet regulations on working hours, which is a complex optimization problem given thousands of flights and staff.
  <br/><b>Adaptive Simulated Annealing:</b> Used to dynamically adjust parameters based on constraints like crew availability, legal requirements, and working hours, allowing for flexible scheduling across thousands of variables.
* <b>Data Center Optimization:</b> Companies with large data centers, such as Google and Facebook, use SA to optimize server allocation and resource management. SA helps reduce power consumption and improve server efficiency by finding optimal configurations for server placements and cooling.
  <br/><b>Energy-Aware Simulated Annealing:</b> This variation incorporates an energy cost function to minimize power consumption in data center layouts, taking into account both resource efficiency and thermal management needs.
* <b>Telecommunications Network Design:</b> Telecom companies like AT&T have used SA to design network layouts, optimizing the placement of cables and routers to minimize costs and maximize performance across large networks.
  <br/><b>Multi-Objective Simulated Annealing (MOSA):</b> Optimizes multiple goals (e.g., cable length, latency, cost) simultaneously, balancing trade-offs in network structure while maintaining performance and scalability.
* <b>Circuit Design in Electronics:</b> Companies like Intel and AMD use SA in chip design to lay out circuits efficiently. SA helps reduce the total length of connections on a chip, improving performance and lowering manufacturing costs by minimizing material usage and optimizing placement.
  <br/><b>Parallel Simulated Annealing:</b> Runs multiple SA processes in parallel to handle the high complexity of component layout, reducing time required to achieve a minimal wiring length across microchips.
* <b>Delivery Route Optimization:</b> Logistics companies like FedEx and UPS apply SA to optimize delivery routes, especially for last-mile delivery. By finding shorter, more efficient routes, SA reduces travel distance and fuel consumption, leading to faster deliveries and lower costs.
  <br/><b>Hybrid Simulated Annealing with Genetic Algorithms (SA-GA):</b> Combines SA’s local optimization with genetic algorithms’ ability to diversify search, especially useful for last-mile delivery by generating efficient, fuel-saving routes.
* <b>Portfolio Optimization in Finance:</b> Financial institutions such as JP Morgan and Goldman Sachs use SA to balance and diversify investment portfolios. SA helps maximize returns by exploring different asset allocations, reducing risk, and optimizing the combination of stocks, bonds, and other assets.
  <br/><b>Stochastic Simulated Annealing:</b> Used to model market uncertainties and adapt investment strategies. It introduces random variations to assess diverse asset allocations, balancing risk and reward under changing market conditions.
* <b>Scheduling in Manufacturing:</b> Companies like Toyota and Ford use SA to optimize manufacturing schedules, balancing machine usage, minimizing downtime, and ensuring that production targets are met. This approach helps streamline operations and reduce costs.
  <br/><b>Discrete Simulated Annealing:</b> Optimizes manufacturing schedules where time slots and resources are discrete variables, helping allocate machinery and minimize downtime for continuous production.
* <b>Air Traffic Management:</b> NASA has explored using SA to manage and optimize air traffic flow. By simulating different flight paths and departure schedules, SA helps reduce congestion and delays, improving safety and efficiency in busy airspaces.
  <br/><b>Dynamic Simulated Annealing:</b> Adjusts in real time to changing flight patterns and schedules. This approach helps model continuously shifting parameters, minimizing congestion and optimizing safety in busy airspaces.
* <b>Protein Folding in Biotechnology:</b> Pharmaceutical companies such as Pfizer and Merck use SA to model protein folding, which is crucial in drug discovery. SA helps simulate the 3D structure of proteins, allowing researchers to understand how drugs interact with their targets.
  <br/><b>Temperature-Adjusted Simulated Annealing:</b> Specifically tailored to mimic the temperature-sensitive nature of protein folding, allowing it to explore multiple folding patterns and predict stable structures efficiently.
* <b>Urban Planning and Land Use:</b> Some cities and government agencies, such as in Singapore and the Netherlands, use SA for urban planning, optimizing land use and infrastructure placement. SA can help balance various land uses—residential, commercial, and industrial—while optimizing accessibility and minimizing environmental impact.
  <br/><b>Spatial Simulated Annealing:</b> Optimizes land use while considering spatial constraints and neighborhood effects. This type helps allocate land for residential, commercial, and industrial use, balancing accessibility and environmental factors.

<h2>Exact SA algorithms and problems what can be solved by them</h2>
<h3>Traveling Salesman Problem (TSP)</h3>
* In TSP, the goal is to find the shortest possible route for a salesperson to visit each city once and return to the starting point. Since there are numerous possible routes (which grow exponentially with each new city), finding the best route by brute force would be incredibly slow.
* Simulated Annealing can explore a variety of routes, gradually refining choices to find the shortest path without getting trapped in poor local routes.
```plaintext
Initialize a random route through all cities
Set initial temperature

While temperature > 1:
    Generate a new route by swapping two cities in the current route
    Calculate the distance (cost) of the new route
    If new route is shorter, accept it
    If longer, accept it with a probability based on temperature
    Reduce temperature
Return best route found
```
<h3>Job Scheduling</h3>
* In scheduling problems, tasks need to be assigned to resources (like machines or time slots) while minimizing total costs or time. It’s common in manufacturing, cloud computing, and project management.
* SA explores different schedules and chooses arrangements that reduce downtime or maximize efficiency, adjusting the schedule as it cools down for an optimized allocation.

```plaintext
Initialize a random job schedule
Set initial temperature

While temperature > 1:
    Generate a new schedule by swapping tasks or resources
    Calculate the new schedule’s efficiency or cost
    If new schedule is better, accept it
    If worse, accept it based on probability using temperature
    Lower temperature
Return optimized schedule
```

<h3>Resource Allocation</h3>
* Resource allocation problems involve distributing limited resources (like bandwidth, money, or materials) across competing needs to optimize results.
* Using SA, you can explore different ways to allocate resources without being constrained by local optima, finding better configurations and potentially saving costs or increasing productivity.
```plaintext
Start with an initial allocation of resources
Set initial temperature

While temperature > 1:
    Make a small change in the resource allocation
    Calculate the new allocation’s cost or performance
    If the allocation is better, accept it
    If worse, accept it with a probability based on temperature
    Reduce temperature gradually
Return best resource allocation
```

<h3>Machine Learning Model Tuning</h3>
* Training machine learning models often involves tuning parameters (like learning rate, number of layers, or dropout rate) to improve accuracy and performance. With many parameters, this can become a complex optimization problem. 
* SA allows for broad exploration of parameter combinations, gradually converging on a set that best improves model performance, even in highly non-linear search spaces.

```plaintext
Initialize model parameters randomly
Set initial temperature

While temperature > 1:
    Modify a parameter (e.g., learning rate, layer size)
    Measure model performance on validation set
    If performance improves, accept the new parameters
    If worse, accept based on probability with temperature
    Lower temperature
Return optimized model parameters
```

<h3>Circuit Design and Layout</h3>
* In circuit design, components need to be arranged efficiently to minimize wire length and avoid overcrowding, improving performance and reducing manufacturing costs. 
* SA helps find an optimal layout by exploring component placements and iterating toward designs with minimal wire crossings and optimal component arrangement.
```plaintext
Start with an initial layout of components
Set initial temperature

While temperature > 1:
    Change component positions slightly
    Calculate layout’s wiring cost and component spacing
    If layout is improved, accept it
    If worse, accept with a probability based on temperature
    Decrease temperature
Return optimized circuit layout
```

<h2>Description of Example Research Problem and Model</h2>

<h3>Traveling Salesman Problem (TSP)</h3>
* <b>Problem:</b> Imagine a traveling salesperson who needs to visit several cities and return to the starting point. The goal is to find the shortest route that visits each city exactly once. With a large number of cities, the number of possible routes is enormous, making it challenging to calculate the best route using traditional methods.
* <b>Model:</b> We model the problem as a graph, where cities are nodes and the roads between them are edges with distances (travel costs).
* <b>Steps for problem solving:</b>
    1. Start with a random route that includes all cities.
    2. The algorithm gradually changes the route with small adjustments, such as swapping two cities, and calculates the new route’s length.
    3. If the new route is shorter, it accepts it. If it's longer, it may still accept it with a certain probability (based on temperature) to avoid getting stuck in local minimum.
    4. By slowly cooling the temperature, the algorithm focuses on increasingly better solutions until it finds an optimal route.

<h3>Example Code for Traveling Salesman Problem (TSP) in Python</h3>
```python
import math
import random

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Calculate the total distance of a given route
def route_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    total_distance += distance(route[-1], route[0])  # Return to the starting city
    return total_distance

# Simulated Annealing function to find the shortest route
def simulated_annealing(cities, initial_temp, cooling_rate):
    # Start with a random initial route
    current_route = cities[:]
    random.shuffle(current_route)
    current_temp = initial_temp
    best_route = current_route
    best_distance = route_distance(best_route)

    while current_temp > 1:
        # Create a new route by swapping two cities
        new_route = current_route[:]
        i, j = random.sample(range(len(cities)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]

        # Calculate the distances of the current and new routes
        current_distance = route_distance(current_route)
        new_distance = route_distance(new_route)
        
        # Accept the new route based on Simulated Annealing criteria
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / current_temp):
            current_route = new_route
            current_distance = new_distance
            if new_distance < best_distance:
                best_route = new_route
                best_distance = new_distance

        # Gradually reduce the temperature
        current_temp *= cooling_rate

    return best_route, best_distance

# Define the cities as coordinates (randomly generated for example purposes)
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]

# Run the Simulated Annealing algorithm
best_route, best_distance = simulated_annealing(cities, initial_temp=10000, cooling_rate=0.99)

print("Best route found:", best_route)
print("Total distance of the best route:", best_distance)
```

// research & problems & results