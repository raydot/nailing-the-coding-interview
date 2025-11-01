# Graphs

The graph is the data structure most single-handedly responsible for the creation of tech billionaires. Graphs lie the core of social networks, search engines, map applications, dating apps, recommendation engines, and even the web itself. Graphs are a simple concept with myriad uses. In fact, when I was a boy, my grandmother embroidered me a pillow that said "Master graphs, and you’ll never want for work." And she didn’t even own a computer!

## Graph Definition

Graphs are used to represent relationships between things. In computer science, a graph is represented by nodes and edges, sometimes also called vertices (singular: vertex) and arcs. Nodes are the points in the graphs, the things that are related. Edges are the connections between the nodes, the thing that brings them together.

The simplest example is that everyone has a mother and a father. But they done become mothers or fathers until they have children. In a human family tree, the nodes are the people and the edges are what unites the people. People can be connected in many ways, some temporary and some permanent.

Outside of immediate family, people can alway be connected as friends, classmates, or co-workers. Some people might have strong connections in this regard, strong enough that they be "married" or even "bffs." Some people might even have negative connections, like an enemy or an ex.

I was born, so I have a mother and a father. (As of the time of this writing, there’s not really any other way to do that.) But I was also adopted at birth. I would not recognize my birth mother if she came to the door and tried to sell me a vacuum cleaner. I do know the mother and father who raised me, and I have a very close connection to them, but not a biological one. In fact, the only biological relative of mine that I have ever met is my son.

Here is what all of that crazy inter-personal complication might look like as a graph:

Notice that some of these relationships two way, and some are one-way. My son is my son, but I’m not also his son. My BFF is my BFF, but I’m not his BFF (how sad!). But my brother is my brother, and I’m his brother. My wife is my spouse, and I’m also her spouse.

Also notice that some connections are stronger than others. My connection to my son is inviolable, but my connection to my BFF is not. My connection to my brother is strong, but not as strong as my connection to my son. My connection to my birth mother is pretty weak.

In a graph, the strength of the connection is called the "weight" of the edge, which is a very important concept to which I shall return.

## Building Intuition: When to use a graph?

At the level for which this book is intended, if you are asked about using a graph during a coding interview, it’s going to be for a very specific reason. You’re either going to be interviewing for a job where graphs are used a lot, or the interviewer is going to be testing the high-end of your knowledge. If it’s the former, you’re likely not learning anything new in this chapter. It it’s the latter, expect that the interviewer is not going to expect a deep dive. I can’t guarantee any of that, of course, but I’d be willing to give you odds I’m right.

One suggestion I have: stick to the general. Unless you’re absolutely confident about your knowledge of graphs, paint the picture with a very broad brushstroke. Start with the definitions and show understanding.

Of course, if there’s a coding problem that comes up and you know the answer is a graph and the code is dancing before your eyes as you respond, hey, go for it!

## Graph data structures

This next section will cover the representation of graphs in code. Most languages do not come with a built-in "graph" keyword or data structure, and so they have to be built using other data structures. Graphs are primarily represented in code in one of two ways, as a matrix, or as an adjacency list. I’m going to start with the matrix first because even though it can present more of a challenge to manipulate, it’s a lot more intuitive to look at.

<div class="sidebar">

<div class="title">

Back to math class

</div>

Matrices are another subject I slept right through in my high-school math classes. I could not, for the life of me, figure out why it mattered at all for me to understand them. A matrix is nothing more than a rectangular array of numbers. A spreadsheet is a matrix. For that matter, so is a tic-tac-toe board. Mathematicians have come up with very clever ways to manipulate matrices, and that’s all the boring stuff I slept through.

Never fear, because now that I’m older and at least a little bit wiser, I can see matrix addition and multiplication for what it is: a series of algorithms that can be used to manipulate matrices.

You might be programming a game that features a cool alien space ship that needs to move around the screen. The graphic representation is a matrix of pixels. You could come up with graphic representations of the ship at every potential angle of representation, but if you know how to move matrices around, you can just rotate the matrix of pixels instead.

For a programmer, just learning some basic matrix math can take you a long way in terms of manipulating matrices, which means manipulating graphics, graphs, data, and all kinds of other things.

Knowing matrix math also brings all kinds of interesting algorithmic treatments into play. If you are trying to figure out whether it’s possible in a graph to move from point A to point B, you can use matrix math to do that. You don’t have to just put a finger down and trace the path.

</div>

Matrices (plural for matrix) are commonly represented as two-dimensional arrays. The should not come as too much of a surprise.

A two-dimensional array is a collection of arrays. all of the values that run across are called "rows" and all of the values that run down are called "columns." For example, consider this matrix:

``` python
mystery_matrix = [
    [    0,     1,    1,    0,    0,    0  ],
    [    0,     0,    1,    0,    0,    0  ],
    [    0,     0,    0,    1,    1,    0  ],
    [    0,     0,    0,    0,    1,    1  ],
    [    0,     0,    0,    0,    0,    0  ],
    [    0,     0,    0,    0,    0,    0  ]
]
```

Think for a moment about wha this matrix might represent. It could be the walls to a maze in a video game. It could be a graphic representation of a bolt of lightning. It could be a social media or recommendation graph.

It’s actually food web, or a diagram of "who eats whom" in an arctic food chain. Here is is again with some comments added:

``` python
# Food Web Matrix (Binary Relationships)
# 1 = Species A (row) is eaten by Species B (column)
# 0 = No direct predation
food_web = [
    #  Algae  Krill  Fish  Seal  Orca  Bear
    [    0,     1,    1,    0,    0,    0  ],  # Algae    - Primary producer
    [    0,     0,    1,    0,    0,    0  ],  # Krill    - Primary consumer
    [    0,     0,    0,    1,    1,    0  ],  # Fish     - Secondary consumer
    [    0,     0,    0,    0,    1,    1  ],  # Seal     - Tertiary consumer
    [    0,     0,    0,    0,    0,    0  ],  # Orca     - Apex predator
    [    0,     0,    0,    0,    0,    0  ]   # Bear     - Competes with orcas for seals
]
```

Rows in a matrix are what goes across, from left to right. The first row in this matrix is also the first array, `[0, 1, 1, 0, 0, 0]`. The row represents algae, or, more specifically, what eats algae.

Columns in a matrix are what go up and down, from top to bottom. The first column in this matrix is the value of the first item in each array in the matrix, `[0, 0, 0, 0, 0, 0]`. This row also represents algae, or, more specifically, what algae eats.

Don’t forget that this is a representation of a matrix in code form. If this was being used in a math class or on a spreadsheet, there would be no "arrays" or comma separation involved. This is what is known as "matrix notation" of a graph, in code form. Yep, it’s a graph and a matrix and a 2d array and a representation of a food web. All of that, all at the same time. Spend a moment pondering that, let it wash over you in waves, enjoy it.

That’s the matrix and more intuitive representation of a graph, but if you’ve ever worked with 2D arrays you know they can quickly become unwieldy. The adjacency list is a more efficient way to represent a graph, and it is the most common way to do so in code. Here is an example of the food web matrix as an adjacency list:

``` python
# Food Web Adjacency List
food_web = {
    'Algae': ['Krill', 'Fish'],
    'Krill': ['Fish'],
    'Fish': ['Seal', 'Orca'],
    'Seal': ['Orca', 'Bear'],
    'Orca': [],
    'Bear': []
}
```

Instead of a 2D array, the adjacency list is a dictionary, or hash table. All of the species are listed as keys, with the values being an array of the species that eat them. This form provides two immediate advantages over the matrix form:

1.  It’s easier to work with, since items can be accessed by keys instead of grid coordinates.

2.  It’s more efficient, since it only stores the relationships that exist. No need for a "0" value — if there is no relationship then it’s simply not on the list.

For the rest of this chapter we will only be dealing with adjacency lists. The matrix form is still important and I will still reference it, but all of the code will be written for adjacency lists.

## Graph Properties

There are a few basic terms that will be used throughout this chapter to describe the properties of graphs. There are more, but these are the most common and the most important.

### Graph Directedness

Graphs can be described as either "directed" or "undirected." In a directed graph the edges have a direction, and in an undirected graph, they don’t. That’s a distinction with a very big difference, and it’s important to understand.

\<Image of directed vs undirected graph TK\>

The family tree graph is a directed graph. In a family tree graph the edges are directed from older generations to younger, from parents to children, from ancestors to descendants. It’s literally impossible for the graph to flow the other way. The son will never be the father of his father, and the daughter will never be the mother of her mother. It just can’t happen.

An example of an undirected graph is a social network. Frank will be friends with Ben, and Ben will be friends with Frank. There is no "direction" to this friendship, it can go either way. In a social network, therefore, the edges are undirected. (Yes, there are certainly such things as "one-sided" friendships, and we’ll talk about that a little later in the chapter, but for now we’re talking about normal, healthy, bi-directional friendships.)

### Ordinality

Graph ordinality is a measure of how many edges are connected to a node. While most graphs will have some kind of very high upper limit on the number of edges that can be connected to a single node, in some graphs the limit might be small. It’s unusual, for instance, for a single intersection a city to be connected to more than four roads. It’s unusual (although not impossible) for a child to have more than two parents. Most people have only one spouse, one best friend, and one mother.

\<Diagram of graph with ordinality TK\>

Ordinality might also be called "degree," and it’s an important concept that we will return to later in the chapter.

### Cyclicity

In a graph a "cycle" is a path that starts and ends at the same node. This could be as simple as a node that points back to itself, like an escalator or a revolving door, or it could be a complex path through hundreds or even thousands of nodes, but it always ends up at the same node where it started.

A graph that contains a cycle is called a "cyclic graph," and a graph that does not contain a cycle is called an "acyclic graph." A tree is an example of an acyclic graph, and a family tree is a good example of such a tree. Children do not return back to become their parents, for instance.

(Image of cyclic vs acyclic graph TK)

### Weight

Remember when I mentioned "one-sided" friendships? In a social network, some friendships are stronger than others. I have some people who have been my friends for decades, and I have some friends who I have never even met in person. To indicated the strength of a friendship I might assign a "weight" to the edge that connects the two nodes. The weight of an edge is a measure of the strength of the relationship between the two nodes.

\<Image of weighted graph TK\>

In a family tree, the weight of the edge might indicate whether a connection is by blood or by marriage. Or maybe how close one relative is to another by blood. In a city map, the weight of an edge might be used to indicate traffic conditions, the number of lanes or speed limits on a road, or even the number of traffic lights. In a social network the weight of an edge might indicate the strength of a friendship. You might be friends with a celebrity, and maybe you’ve seen all of their movies and have their poster on your wall, but that doesn’t make you their friend in real life. The weight of the edge between you and the celebrity might be very high, but the weight of the edge between the celebrity and you will almost certainly be low.

## Searching graphs

Now that we’ve nailed down some graph basics, let’s talk about some ways in which we can make the information that can be stored in a graph format useful

### Graph Traversal

"Traversal" is the process of visiting each node in a graph one at a time in some order. If you think back to the chapter on trees and pre-order, post-order, amd in-order traversal, hey, yeah, it’s the same kinda thing. There are two main ways to traverse ("walk") a graph: depth-first and breadth-first.

### Depth First Traversal

In a depth-first traversal, the graph is explored a node at a time, starting at the root node and going as deep as possible down each branch before backtracking to explore other branches.

Most coders are gamers (am I wrong?), so I’m going to use the analogy of a First Person Shooter (FPS) game here. Imagine you start the game in a room with six doors. Behind each door lies three quests. In a depth-first traversal you would choose a door, enter it, and then complete all three quests before returning to the main room and choosing a different door.

\<Image of depth first Traversal TK\>

### Breadth First Traversal

In a breadth-first traversal, the graph is explored one level at a time, starting at the root node and then exploring all of the nodes that are the same distance from the root before moving on to the next level.

Returning to the FPS analogy, when you’re in the room with six doors, you would open each door first and have a look around. When you’ve explored what’s behind all six doors, then you go and complete the first quest behind each door. When you’ve completed the first quest you go back to each room and complete the second quest, and then you return to the main room and complete all of the third quests.

\<Image of breadth first Traversal TK\>

### Weighted Graph

In traversing a weighted graph, you might start with a breadth- or depth-first traversal, but the weights of each edge might determine the order in which you visit the nodes. You’ve dealt with this if you’ve ever played an FPS where one of the quests absolutely must be completed before another one can be completed. You can do most of the first one, and most of the second, but you can’t complete the second until you’ve finished the first.

### Ok, but so what?

There can be many different reasons for traversing a graph. You might want to find the shortest path between two nodes, or you might want to find the longest. You might need to visit every single node in the graph, or you might be able to stop searching as soon as you find the one that contains the treasure.

If you’ve ever used a GPS app you’re familiar with not wanting to visit every node. The GPS might even give three ways to get where you’re going, with additional options that might say "10 minutes faster" or "2 minutes slower." But hey, maybe the 10 minutes faster route contains tolls. Maybe the 2 minutes slower route comes with a beautiful view of the ocean. Whichever way you want to go, you only want to go just that one way. Unless you’re one of those people who drives those weird mapping cars, you absolutely don’t want (or need) to go back to the beginning and try every possible route to figure out which one is truly the best.

## Graph Algorithms

That’s a lot of theory! It’s important stuff though. A lot of stuff has been written about graphs, and I really encourage you to go beyond the basics I present in this book.

But not yet! First let’s talk about some of the basics of working with graphs. Here is some Python code that create a very simple social network graph.

``` python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        # Add a new vertex if it doesn't exist already
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add an undirected edge between vertex1 and vertex2
        # Make sure both vertices exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Make sure the graph runs in both directions
        # (undirected graph)
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)

    def display(self):
        # Display the graph structure
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, neighbors))}")


# Create the graph
g = Graph()

# Add edges (connections between people)
g.add_edge('Amir', 'Beth')
g.add_edge('Amir', 'Chen')
g.add_edge('Amir', 'Diego')
g.add_edge('Beth', 'Emma')
g.add_edge('Beth', 'Farid')
g.add_edge('Chen', 'Gina')
g.add_edge('Diego', 'Hiroshi')
g.add_edge('Emma', 'Ian')
g.add_edge('Farid', 'Jamal')
g.add_edge('Gina', 'Kyle')

# Display the graph structure
print("Social Connections:")
g.display()
```

If you run the code above you will see the following output:

``` console
Social Network Connections:
Amir -> Beth, Chen, Diego
Beth -> Amir, Emma, Farid
Chen -> Amir, Gina
Diego -> Amir, Hiroshi
Emma -> Beth, Ian
Farid -> Beth, Jamal
Gina -> Chen, Kyle
Hiroshi -> Diego
Ian -> Emma
Jamal -> Farid
Kyle -> Gina
```

As you can see from the output, we have a simple, undirected graph representing a social network. Don’t be fooled by the arrows (`→`) in the output, that’s just a way to show the connections between the nodes. What it means to say the graph is "undirected" is that the connections go both ways. If Emma is connected to Ian, then Ian is also connected to Emma.

### Building Intuition: Reasoning about Graphs

Before we proceed, this is a great place to stop and reason a bit about what’s presented here. Don’t look at my drawing just yet, cover it with a Post-It, and try doing the following. Draw this graph on a piece of paper or using a graphing program. In this representation, what is a vertex and what is an edge? Who is connected to whom? What does the ordinality of each vertex represent? How will this graph be traversed depth-first? How will this graph be traversed breadth-first? Is there a cycle in this graph? What might be changed to make this graph more useful than it is now?

Like trees, one of the easiest ways I’ve found to build intuition about graphs is to draw them out and reason from there. In fact one of the greatest tools a programmer can have is a pencil and a piece of paper. Or a whiteboard, or a drawing program, or whatever you like to use, but turning code into pictures can really be a big help.

Now that you’ve done that, here’s my version of the graph:

\<Image of social network graph TK\>

Back to the two forms of traversal: depth-first and breadth-first. Here is an algorithm that will traverse the graph in a depth-first manner, starting with Amir and running down all of his connections one at a time, in order.

``` python
def depth_first_traversal(self, start, visited=None):
    if visited is None:
    visited = set()

    visited.add(start)
    print(start)

    for neighbor in self.graph[start]:
    if neighbor not in visited:
        self.depth_first_traversal(neighbor, visited)

# Example usage
g.depth_first_traversal('Amir')
```

When you run this code you see the following output:

``` console
Social Connections:
Amir -> Beth, Chen, Diego
Beth -> Amir, Emma, Farid
Chen -> Amir, Gina
Diego -> Amir, Hiroshi
Emma -> Beth, Ian
Farid -> Beth, Jamal
Gina -> Chen, Kyle
Hiroshi -> Diego
Ian -> Emma
Jamal -> Farid
Kyle -> Gina
```

Was it what you expected? As you can see, Amir knows everybody. Or, well, if he doesn’t know somebody, then he knows someone who knows them, or he knows someone who knows someone who knows them. Right?

<div class="formalpara">

<div class="title">

Six Degrees of Separation / Kevin Bacon

</div>

    When Friendster / MySpace / Facebook first arrived in the web world, people were absolutely blown away.
    How absolutely amazing it was that the "web" part of the "World Wide Web" was finally being both realized and made visible.
    Suddenly, everybody knew everybody, and for a shining moment in time we were indeed a global village.

    Our frame of reference at the time was the "Six Degrees of Separation" theory, made popular by the movie starring Will Smith of the same name that was an adaptation from the play by John Guare of the same name that was modelled on the existential premise posited by Frigyes Karinthyof the same name.

    The theory states that any two people on Earth are connected by no more than six degrees of separation, or six friends of friends, and here it was happening right in front of our very internet-connected eyes.
    What most people didn't realize is the social networks were just graphs!

    Prior to Facebook (or MySpace, or Friendster, depending on where you decided to dive in to social networking) there were a few other popular graph-based internet applications.
    One was "Firefly," which was a really cool music recommendation engine where you entered the bands you liked to listen to and it would recommend other bands you might also like based on the recommendations of other users.

    There was also Plumb Design's "Visual Thesaurus," where a user could enter a word and explore the way in which that word was connected to other words, including synonyms and antonyms, in a memorizing visual format.

    On the lighter side of things was the Facebook game "Six Degrees of Kevin Bacon."
    Enter the name of any actor or movie and a list would return of how that actor or movie was connected to Kevin Bacon, who has been in so many movies that, well, there's a whole game based on it.

    While the thrill of the earliest social networks has faded somewhat, graphs have become a vital part of connecting ideas, interests, and people online.

</div>

Go back to your graph drawing (or mine) and trace out the depth-first traversal. Can you see how it’s working? Notice that each visited node is marked as "visited," which is how the algorithm tracks where it needs to go next.

Let’s add a breadth-first traversal and see what happens there.

``` python
def breadth_first_traversal(self, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(neighbor for neighbor in self.graph[vertex] if neighbor not in visited)
# Example usage
g.breadth_first_traversal('Amir')
```

Adding this function to our graph class and running it provides this output:

``` console
Breadth-First Traversal starting from 'Amir':
Amir
Beth
Chen
Diego
Emma
Farid
Gina
Hiroshi
Ian
Jamal
Kyle
```

The breadth-first traversal starts at Amir and then, instead of running each connection all the way down to the end, visits each of Amir’s friends first, then their friends, then friends of friends, and so on. You will also notice it returns in a different order than the depth-first traversal, and that order just so happens to be alphabetical. Additionally, breadth-first traversal does not require nodes to be marked as "visited."

Again, as suggested for the depth-first traversal, go back to your graph drawing and trace out the breadth-first traversal. Can you see how it’s working? So reasoning from there, can you think of an instance in which depth-first traversal would be better than breadth-first traversal? Or vice versa?

## Dijkstra’s algorithm

I have to open this section by pointing out that Dijkstra’s algorithm was not invented by Lenny Dykstra. He may have batted .355 for the Phillies in 1990 but he was certainly no Moe Berg. (I included that joke for the ten people who will get it and I will stand by it for as long as I draw breath.)

Lenny Dykstra also spelled his last name different than Edgar Dijkstra, the Dutch computer scientist who actually did invent Dijkstra’s algorithm. Dijkstra’s algorithm touches on a number of different subjects covered in this book, but as it specifically relates to graphs, it is a way to find the shortest path between two nodes in a weighted graph. It’s used in a lot of different ways, but probably the most well known is GPS.

While all of the nooks and crannies of Dijkstra’s algorithm are beyond the scope of this book, let’s take a look using a drawing:

\<Image of Dijkstra’s algorithm TK\>

In the drawing you can see that all of the edges contain a number. The number represents the "weight" of the edge, and the "weight" is an indication of the distance between the two nodes. (It’s always important to remember that just because two nodes may be visually close to one another, it doesn’t necessarily mean that they’re close in terms of the distance or travel time between them. Next time you’re in a major city try laying of it it’s transportation maps over a geographical map and you’ll see how transportation are modified to show the way in which the public transportation system works, and not the way the city is laid out geographically.)

Dijkstra’s algorithm is a "greedy" algorithm, which will be discussed again in chapter 13. It works by starting at the first node and then looking at all of the edges connected to it, searching for the one with the lowest weight. It then moves to that node, and repeats the process until it reaches the destination node. By selecting nodes in this "greedy" fashion it might not always find the shortest path, but interestingly enough it will usually find a path that is pretty close to optimal, and in a very short amount of time.

## Map Coloring Problem

Another interesting use of graphs is what is known as the "map coloring problem." Given a map of a country broken down into regions, or a continent broken down into countries, how many colors are needed to color the map in a way that no two adjacent regions are the same color? If you happen to still have an atlas or globe lying around, go ahead and look at the maps contained therein. You’ll see that they’re colored in just the way I describe. The map coloring problem is a classic example of a graph problem, and it can be solved using a variety of algorithms, including greedy algorithms and "backtracking," a method of going back and trying different options until a solution is found.

The map coloring problem actually has a lot of applications in the field of computer science. It can be used to rapidly assign and reassign radio frequences as mobile phone users move between cell towers. It can be used in office software to schedule meeting times in a way that accommodates not only the people in the meetings but the rooms in which they’re held. It’s used in pattern recognition, network design, and all kinds of other things.

A very useful real-world example that might solve a real world problem would be using a map coloring algorithm to assign congressional districts in the United States. This would ideally lead to an end of the process known as "gerrymandering," where a political party in power redraws congressional districts in a way that gives then an edge in winning elections. Take that power out of the hands of the politicians and give it to computers! They’ll be the masters of us soon enough, why not start now?

## Example Questions

### The Königsberg Bridge / Traveling Sales Representative Problems

While these are unlikely to come up in a coding interview, The Königsberg Bridge and Traveling Sales Representatives problems are graph theory classics, and can be used to explain a lot of graph theory concepts.

The Königsberg Bridge problem was of particular interest to Leonhard Euler (rhymes with "boiler," and not "ruler"), a Swiss mathematician who lived in the 18th century. Euler was one of these mathematicians who was so brilliant that he was able to solve problems that no one else could even understand, and in some cases many people still can’t understand.

\<Image of the Königsberg Bridge problem TK\>

It’s a simple problem, really. Given this map of the city of Königsberg, can you find a path across all seven of Köenigsberg’s bridges without crossing any of them more than once?

You can’t, but explaining exactly why, mathematically, is a little more difficult.

The traveling sales representative problem is similar, but focuses on a different metric. Given a list of cities and the distances between them, how can you send the sales representative to visit each city exactly once and return to the starting point in the shortest distance possible?

Again, you won’t be asked directly about either of these problems, but they are great examples of how to think about graph theory. There are a lot of great web sites and YouTube videos that will explain these problems in a lot more detail than I can get into in this book.

### Shortest path, longest path, and fastest path

Many graph problems will be about optimization, and the most common optimization problems are about finding the shortest path, the longest path, or the fastest path between two nodes in a graph. It goes without saying that the shortest path is not always the fastest, and the longest path is not always the slowest. I’ve shown you Dijkstra’s algorithm, which is a way to find the shortest path between two nodes in a weighted graph, but there are many other algorithms that can be used to find the longest or fastest path. Again, these are not likely to come up in a coding interview, but they are great examples of how to think about graph theory.

### Knight walk

The Knight Walk problem is a classic example of a graph traversal problem. Given a chessboard and a knight, how can you move the knight from one square to another in the fewest moves possible? If you’re not familiar with chess, the knight moves in an "L" shape, which means it can move two squares in one direction and then one square in a perpendicular direction, or one square in one direction and then two squares in a perpendicular direction.

\<diagram of knight walk TK\>

The Knight Walk problem can be solved using a breadth-first traversal of the graph, where each square on the chessboard is a node and each possible move of the knight is an edge. Using a breadth-first traversal ensures that the shortest path is found, since it explores all possible moves at each level before moving on to the next level.

Here is a simple implementation of the Knight Walk problem in Python:

``` python
def knight_walk(start, end):
    # Define the possible moves of a knight
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    # Initialize the queue and visited set
    queue = [(start, 0)]  # (position, distance)
    visited = set()

    while queue:
        position, distance = queue.pop(0)

        # If we reached the end position
        if position == end:
            return distance

        # Mark the position as visited
        if position not in visited:
            visited.add(position)

            # Explore all possible moves
            for move in moves:
                new_position = (position[0] + move[0], position[1] + move[1])
                if new_position not in visited and 0 <= new_position[0] < 8 and 0 <= new_position[1] < 8:
                    queue.append((new_position, distance + 1))

    return -1  # If no path found

# Example usage
start = (0, 0)  # Starting position (row, column)
end = (7, 7)    # Ending position (row, column)
print("Minimum moves from", start, "to", end, ":", knight_walk(start, end))
```

What optimizations can you think of to make this code more efficient? What kinds of problems do think this algorithm can be used to solve?

### Flood fill

Another common use of graphs is the "fill" algorithm. Given the boundary of a two-dimensional shape, how can you fill the shape inside the lines with a single color? This has been available to paint and image processing programs for decades, and the fill tool has been represented by a bucket pretty much that entire time.

The fill algorithm is a graph traversal problem. Visit every pixel within a given space that isn’t filled, and fill it. As discussed in this chapter, this can be done with a depth-first or breadth-first traversal. Here is one simple way in which this might be implemented:

``` python
def flood_fill(image, x, y, new_color):
    old_color = image[x][y]
    if old_color == new_color:
        return

    def fill(x, y):
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
            return
        if image[x][y] != old_color:
            return

        image[x][y] = new_color

        fill(x + 1, y)
        fill(x - 1, y)
        fill(x, y + 1)
        fill(x, y - 1)

    fill(x, y)

# Example usage
image = [
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1]
]
flood_fill(image, 1, 1, 2)
```

In this example, the recursive calls to `fill` create a kind of last-in, first-out stack, which is a common way to implement depth-first traversal. Because of this arrangement the fill space is traversed in a depth-first manner, filling in all of the pixels in a given area before moving on to the next.

### Displaying a graph

In our social network example we just dumped the graph to the console line by line, but that didn’t do much to really display the connections between the people using the network. Using a simple drawing library, can you come up with an algorithm that will display the graph in a more visual way?
