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
<ul>
  <li><b>Randomness:</b> They use randomness to explore different solutions, helping avoid getting stuck in local optima.</li>
  <li><b>Objective Function:</b> This function measures the "cost" or "fitness" of a solution, guiding the algorithm toward optimal solutions.</li>
  <li><b>Acceptance Probability:</b> Allows worse solutions to be accepted based on probability (controlled by a parameter like "temperature"), enabling broader exploration.</li>
  <li><b>Cooling Schedule:</b> Defines how a parameter like "temperature" gradually decreases, shifting the algorithm from exploration to fine-tuning.</li>
  <li><b>Termination Condition:</b> A stopping point, often set by a low temperature, a maximum number of iterations, or a minimal improvement threshold.</li>
</ul>

<h2>Used Sources and Real World Problems Solved with SA (TSP)</h2>
<h3>Used Sources</h3>
<ul>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S1877050919303667">ScienceDirect - Simulated Annealing Algorithm: A Review</a></li>
</ul>

<h3>Real World Problems Solved with SA</h3>

<ol>
  <li>Where it's used?</li>
  <li>How and what is applied here?</li>
</ol>

<ul>
  <li><b>Airline Crew Scheduling:</b> Airlines like American Airlines and Delta use SA to schedule flight crew rotations. It helps balance crew availability, minimize costs, and meet regulations on working hours, which is complex due to thousands of flights and staff.
    <ul>
      <li><b>Adaptive Simulated Annealing:</b> Dynamically adjusts parameters based on constraints like crew availability, legal requirements, and working hours, enabling flexible scheduling across thousands of variables.</li>
    </ul>
  </li>
  
  <li><b>Data Center Optimization:</b> Companies with large data centers, such as Google and Facebook, use SA to optimize server allocation and resource management, reducing power consumption and improving server efficiency.
    <ul>
      <li><b>Energy-Aware Simulated Annealing:</b> This variation includes an energy cost function to minimize power consumption, addressing both resource efficiency and thermal management needs.</li>
    </ul>
  </li>
  
  <li><b>Telecommunications Network Design:</b> Telecom companies like AT&T use SA to design network layouts, optimizing cable and router placement to minimize costs and maximize performance.
    <ul>
      <li><b>Multi-Objective Simulated Annealing (MOSA):</b> Optimizes multiple goals (e.g., cable length, latency, cost) simultaneously, balancing trade-offs in network structure to maintain performance and scalability.</li>
    </ul>
  </li>
  
  <li><b>Circuit Design in Electronics:</b> Companies like Intel and AMD use SA in chip design to lay out circuits efficiently, reducing connection length and manufacturing costs.
    <ul>
      <li><b>Parallel Simulated Annealing:</b> Runs multiple SA processes in parallel, managing the complex component layout and reducing the time needed to achieve minimal wiring length across microchips.</li>
    </ul>
  </li>
  
  <li><b>Delivery Route Optimization:</b> Logistics companies like FedEx and UPS apply SA to optimize delivery routes, especially for last-mile delivery, to reduce travel distance and fuel consumption.
    <ul>
      <li><b>Hybrid Simulated Annealing with Genetic Algorithms (SA-GA):</b> Combines SA’s local optimization with genetic algorithms’ diversity in search, useful for last-mile delivery by creating efficient, fuel-saving routes.</li>
    </ul>
  </li>
  
  <li><b>Portfolio Optimization in Finance:</b> Financial institutions like JP Morgan and Goldman Sachs use SA to balance and diversify investment portfolios, exploring different asset allocations to maximize returns and minimize risk.
    <ul>
      <li><b>Stochastic Simulated Annealing:</b> Models market uncertainties and adapts investment strategies, introducing random variations to assess diverse asset allocations, balancing risk and reward in changing markets.</li>
    </ul>
  </li>
  
  <li><b>Scheduling in Manufacturing:</b> Companies like Toyota and Ford use SA to optimize manufacturing schedules, balancing machine usage, minimizing downtime, and meeting production targets.
    <ul>
      <li><b>Discrete Simulated Annealing:</b> Optimizes manufacturing schedules where time slots and resources are discrete, helping allocate machinery and minimize downtime for continuous production.</li>
    </ul>
  </li>
  
  <li><b>Air Traffic Management:</b> NASA explores using SA to manage and optimize air traffic flow, simulating flight paths and schedules to reduce congestion and improve safety in busy airspaces.
    <ul>
      <li><b>Dynamic Simulated Annealing:</b> Adjusts in real time to changing flight patterns, modeling shifting parameters to minimize congestion and optimize safety.</li>
    </ul>
  </li>
  
  <li><b>Protein Folding in Biotechnology:</b> Pharmaceutical companies like Pfizer and Merck use SA to model protein folding, crucial in drug discovery, to simulate protein structures and understand drug interactions.
    <ul>
      <li><b>Temperature-Adjusted Simulated Annealing:</b> Mimics temperature-sensitive protein folding, exploring multiple patterns to predict stable structures efficiently.</li>
    </ul>
  </li>
  
  <li><b>Urban Planning and Land Use:</b> Cities and government agencies, such as in Singapore and the Netherlands, use SA for urban planning, optimizing land use and infrastructure placement to balance residential, commercial, and industrial spaces.
    <ul>
      <li><b>Spatial Simulated Annealing:</b> Considers spatial constraints and neighborhood effects to allocate land use effectively, balancing accessibility and environmental factors.</li>
    </ul>
  </li>
</ul>

<h2>Exact SA algorithms and problems that can be solved by them</h2>

<h3>Traveling Salesman Problem (TSP)</h3>
<ul>
  <li>In TSP, the goal is to find the shortest possible route for a salesperson to visit each city once and return to the starting point. Since there are numerous possible routes (which grow exponentially with each new city), finding the best route by brute force would be incredibly slow.</li>
  <li>Simulated Annealing can explore a variety of routes, gradually refining choices to find the shortest path without getting trapped in poor local routes.</li>
</ul>
<pre><code>
Initialize a random route through all cities
Set initial temperature

While temperature > 1:
    Generate a new route by swapping two cities in the current route
    Calculate the distance (cost) of the new route
    If new route is shorter, accept it
    If longer, accept it with a probability based on temperature
    Reduce temperature
Return best route found
</code></pre>

<h3>Job Scheduling</h3>
<ul>
  <li>In scheduling problems, tasks need to be assigned to resources (like machines or time slots) while minimizing total costs or time. It’s common in manufacturing, cloud computing, and project management.</li>
  <li>SA explores different schedules and chooses arrangements that reduce downtime or maximize efficiency, adjusting the schedule as it cools down for an optimized allocation.</li>
</ul>
<pre><code>
Initialize a random job schedule
Set initial temperature

While temperature > 1:
    Generate a new schedule by swapping tasks or resources
    Calculate the new schedule’s efficiency or cost
    If new schedule is better, accept it
    If worse, accept it based on probability using temperature
    Lower temperature
Return optimized schedule
</code></pre>

<h3>Resource Allocation</h3>
<ul>
  <li>Resource allocation problems involve distributing limited resources (like bandwidth, money, or materials) across competing needs to optimize results.</li>
  <li>Using SA, you can explore different ways to allocate resources without being constrained by local optima, finding better configurations and potentially saving costs or increasing productivity.</li>
</ul>
<pre><code>
Start with an initial allocation of resources
Set initial temperature

While temperature > 1:
    Make a small change in the resource allocation
    Calculate the new allocation’s cost or performance
    If the allocation is better, accept it
    If worse, accept it with a probability based on temperature
    Reduce temperature gradually
Return best resource allocation
</code></pre>

<h3>Machine Learning Model Tuning</h3>
<ul>
  <li>Training machine learning models often involves tuning parameters (like learning rate, number of layers, or dropout rate) to improve accuracy and performance. With many parameters, this can become a complex optimization problem.</li>
  <li>SA allows for broad exploration of parameter combinations, gradually converging on a set that best improves model performance, even in highly non-linear search spaces.</li>
</ul>
<pre><code>
Initialize model parameters randomly
Set initial temperature

While temperature > 1:
    Modify a parameter (e.g., learning rate, layer size)
    Measure model performance on validation set
    If performance improves, accept the new parameters
    If worse, accept based on probability with temperature
    Lower temperature
Return optimized model parameters
</code></pre>

<h3>Circuit Design and Layout</h3>
<ul>
  <li>In circuit design, components need to be arranged efficiently to minimize wire length and avoid overcrowding, improving performance and reducing manufacturing costs.</li>
  <li>SA helps find an optimal layout by exploring component placements and iterating toward designs with minimal wire crossings and optimal component arrangement.</li>
</ul>
<pre><code>
Start with an initial layout of components
Set initial temperature

While temperature > 1:
    Change component positions slightly
    Calculate layout’s wiring cost and component spacing
    If layout is improved, accept it
    If worse, accept with a probability based on temperature
    Decrease temperature
Return optimized circuit layout
</code></pre>

<h2>Description of Example Research Problem and Model</h2>

<h3>Traveling Salesman Problem (TSP)</h3>
<ul>
  <li><b>Problem:</b> Imagine a traveling salesperson who needs to visit several cities and return to the starting point. The goal is to find the shortest route that visits each city exactly once. With a large number of cities, the number of possible routes is enormous, making it challenging to calculate the best route using traditional methods.</li>
  <li><b>Model:</b> We model the problem as a graph, where cities are nodes and the roads between them are edges with distances (travel costs).</li>
  <li><b>Steps for problem solving:</b>
    <ol>
      <li>Start with a random route that includes all cities.</li>
      <li>The algorithm gradually changes the route with small adjustments, such as swapping two cities, and calculates the new route’s length.</li>
      <li>If the new route is shorter, it accepts it. If it's longer, it may still accept it with a certain probability (based on temperature) to avoid getting stuck in local minimum.</li>
      <li>By slowly cooling the temperature, the algorithm focuses on increasingly better solutions until it finds an optimal route.</li>
    </ol>
  </li>
</ul>

<h3>Example Code for Traveling Salesman Problem (TSP) in Python</h3>
<p>It's just a sample code example - you can explore the real used implementation in 'src' folder</p>
<pre><code class="language-python">
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
</code></pre>

<h2>Research & Problems & Experiments Results</h2>
<p>During the implementation testing, which you can find in the 'src' folder of this repository, we used three different configuration setups to explore the impact of various algorithm settings on performance.</p>

<div style="display: flex; flex-direction: column; gap: 20px;">

<div>
<h3>Testing Case 1: Baseline Setup</h3>
  <ul>
    <li><b>Provided Configurations</b>: 10 cities, 10000 initial temperature, 0.99 cooling rate</li>
    <li><b>Results</b>:</li>
    <ul>
      <li><b>Best Route Found</b>: [(34, 46), (25, 3), (33, 12), (38, 55), (56, 69), (70, 76), (77, 75), (93, 98), (56, 87), (37, 57)]</li>
      <li><b>Total Distance of Best Route</b>: 258.32</li>
      <li><b>Iterations</b>: 917</li>
      <li><b>Execution Time</b>: 0.0126 seconds</li>
    </ul>
    <p>In this setup, with a moderate initial temperature and cooling rate, the algorithm found a relatively short route. The algorithm took 917 iterations to converge, balancing exploration and convergence. This resulted in a good-quality solution (short distance) within a reasonable execution time. This baseline provides a point of comparison for other configurations, showing how moderate settings impact both solution quality and speed.</p>
</div>

<div>
<h3>Testing Case 2: Faster Cooling Rate</h3>
  <ul>
    <li><b>Provided Configurations</b>: 10 cities, 10000 initial temperature, 0.95 cooling rate</li>
    <li><b>Results</b>:</li>
    <ul>
      <li><b>Best Route Found</b>: [(84, 88), (92, 81), (100, 78), (86, 37), (63, 8), (58, 45), (38, 12), (31, 29), (11, 91), (55, 74)]</li>
      <li><b>Total Distance of Best Route</b>: 338.34</li>
      <li><b>Iterations</b>: 180</li>
      <li><b>Execution Time</b>: 0.0024 seconds</li>
    </ul>
    <p>With a faster cooling rate, the algorithm reduced its temperature quickly, leading it to converge in only 180 iterations. This caused it to find a longer route (higher distance) compared to the baseline, indicating that it likely settled for a less optimal solution because it didn’t explore as many options. However, the faster cooling did make the execution time shorter (almost five times faster than the baseline), which could be beneficial when speed is prioritized over finding the absolute best solution.</p>
</div>

<div>
<h3>Testing Case 3: Higher Initial Temperature and Slower Cooling</h3>
  <ul>
    <li><b>Provided Configurations</b>: 10 cities, 20000 initial temperature, 0.995 cooling rate</li>
    <li><b>Results</b>:</li>
    <ul>
      <li><b>Best Route Found</b>: [(100, 15), (94, 36), (78, 35), (70, 82), (42, 94), (27, 58), (17, 49), (20, 5), (57, 38), (75, 25)]</li>
      <li><b>Total Distance of Best Route</b>: 311.27</li>
      <li><b>Iterations</b>: 1976</li>
      <li><b>Execution Time</b>: 0.0259 seconds</li>
    </ul>
    <p>With a higher initial temperature and slower cooling rate, the algorithm explored many more route options, taking 1976 iterations to find a solution. This resulted in a solution with a slightly shorter distance than Testing Case 2, but not as short as the baseline solution. The execution time was longer, as expected, due to the extended number of iterations. This configuration shows that increasing exploration time can improve the solution quality, but the results may not be as efficient as a balanced setup (like the baseline).</p>
</div>

</div>

<h3>Summary of Findings</h3>
<ul>
  <li><b>Quality vs. Speed Trade-off</b>: Testing Case 2 was the fastest but resulted in a poorer solution due to the quick convergence. Testing Case 3, with a slower cooling rate, took the longest but didn’t produce the best route distance, suggesting that more iterations don’t always guarantee the best solution.</li>
  <li><b>Balanced Configuration</b>: The baseline (Testing Case 1) struck a good balance between quality and speed, offering a short route distance without excessive computation time.</li>
  <li><b>Temperature and Cooling Rate Impact</b>: Higher initial temperatures and slower cooling rates increase exploration but also require more iterations and time. Lower cooling rates speed up convergence, but they risk finding suboptimal solutions.</li>
</ul>

<p>These results show how adjusting the initial temperature and cooling rate can affect both the <b>quality of the route found</b> and the <b>speed of the algorithm</b>. For real-world applications, this balance between solution quality and runtime could be adjusted depending on the importance of speed versus accuracy.</p>
