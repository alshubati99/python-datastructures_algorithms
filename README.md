# Python Data Structures and Algorithms Course by LinkedIn Learning
# [*Course Certificate*]()

### Stacks
- using class to represent stack 
- learning push and pop
- using list allows others to use inster, remove , etc.
- LIFO (Last In, First Out)
- add item to top of stack: append()
- retrieve item from top of stack: pop()
- pop() removes a value and returns it, whereas peek() only returns a value, without removing it. 

### 2D lists 
- lists of lists. 
- Graph theory and preparing mazes. 
- Nodes and Edges. 
- Undirected and Directed graphs.
- Weighted Graphs. 
- (5,7) => row 5 and column 7.

### Depth-First Search:
- Based on Stack DS
- Applications:
    - Optimization for criteria.
    - Pathfinding.
    - Scheduling algorithms
    - Assessing investment decision trees.
    - Ordering of formula cell evaluation in spreadsheets.
    - Data serialization.
    - Determining the order of compilation tasks for software builds.
    - Resolving symbol dependencies. 
- Algorithm:
    - Pop the stack.
    - Is this the goal?
    - if so, we are done.
    - Otherwise, push undiscovered neighbors onto the stack and add update predecessors/discovered.
    - Repeat this until no more items in the stack. (Repeate until stack is empty)
### Queue:
- CPU scheduling.
- FIFO (First in, First Out)
- enqueue(): add item to the queue.
- dequeue(): remove item from queue. 

### Breadth-First Search:
- Based on Queue DS.
- Uses the shortest path.
- Applications:
    - GPS systems.
    - Flight reservations systems.
    - Finding neighbor nodes in peer-to-peer networks.
    - Social networking sites to find connctions between users.
    - Web crawlers.
    - Many applications in artificial intelligence.
    - Electronics and communication engineering.
    - Scientific modeling. 
- Algorithm: 
    - enqueue.
    - is this the goal?
    - if so, we are done.
    - otherwise, enqueue undiscovered neighbors and update predessors.
    - repeat until queue is empty. 

### Priority Queue:
- Applications: 
    - AI => A* search algorithm.
    - Optimizing algorithms.
    - Operating system process scheduling.
    - Bandwidth management.
    - Statistical analysis.
    - Spam filtering
- Operations:
    - get(): retrieve the item with the heighest priority.
    - put(item): add item to priority queue.
    - is_empty(): determine if the priority queue is empty.

### A* Search:
- Applications:
    - Traffic navigational system (GPS).
    - Social netwrok analysis.
    - Natural language processing.
    - Machine learning.
    - Puzzle solutions and puzzle analogous problems.
    - Algorithmic trading.
    - Robotics.
    - Video games.
- It uses Heuristic to be implemented.
- Manhanten Search.
- G value: best distance from start to current cell.
- H value: heuristic distance from current cell to destination.
- F value: the sum of the G value and H value (representing the probable optimal value or minimum distance based on the heuristic used)
- V and G values are stored in dictionaries. 
- Algorithm:
    - Get heighest priority item from priority queue (min F-value):
    - is it the goal?
    - if so, we are done
    - otherwise: put undiscovered neighbours, calculate f-values, update predecessors
    - repeat until queue is empty. 

> Stick with foundations until u understand the whole idea. 