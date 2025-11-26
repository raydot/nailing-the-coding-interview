# Dynamic Programming and Greedy Algorithms

When I was a child my father used to read to me from Aesop’s Fables. I was really drawn to a few of them, but one that stands out in my mind is the fable of "The Ants and the Grasshopper." I think the reason it particularly stands out is because there was a Disney cartoon called "The Grasshopper and the Ants" based on this very same fable that seemed to be on our television and awful lot.

In the cartoon a violin-playing, tobacco-spitting, dandified, anthropomorphized grasshopper eats, fiddles and dances his days away while the ants are busy preparing for harder times ahead. Failing to heed the warning of the Ant Queen herself, the grasshopper is surprised to find himself in a blustery winter in the magic forest. As it begins to snow the ant becomes increasingly desperate until with his last ounce of strength he comes across the ants who live in a happy cavern inside a tree. The ants save the grasshopper’s life by pulling him inside and warming him up, and he plays the fiddle for them and…​well I can’t say he seems to learn his lesson, but I’m sure you get the point.

I’m going to suggest we use these two characters in discussing dynamic programming and greedy algorithms. Both approaches can be considered "optimization strategies," or a way to find not just a solution to a problem but the best solution to the problem. The similarities end there, however, and while both are very powerful problem solving methods, dynamic programming is more like the ants, and greedy algorithms are more like the grasshopper.

Dynamic programming is the careful, thoughtful strategy that plans ahead, accomplishing tasks in manageable chunks and putting away their results for future use. Greedy algorithms are the brash grasshopper, looking for the quickest solution that works which can often — but not always — lead to the best solution to the problem at hand. I don’t want to overplay this metaphor so I think everyone gets the basic idea, right?   Good. Let’s begin.

## Introduction to Dynamic Programming

So what is this big, bad thing called dynamic programming? It’s got a flashy name, but the concept itself is straightforward. At its core, dynamic programming is a way to solve a complex problem by breaking it down into smaller and simpler subproblems. The algorithm solves each of these subproblems, and then stores their solutions, reusing those solutions to solve larger problems.

This should sound like a few other things that have some up in the book including recursion, the divide-and-conquer strategy discussed in merge sort, and the general, abiding advice given to approaching programming interviews: "break the problem down into smaller pieces." If you understand that concept, you’re a good part of the way to understanding dynamic programming.

Aside from the breaking down, there are two other key ideas that make dynamic programming so, um…​dynamic. The first idea is that the subproblems must overlap, and that’s the more challenging of the two so we’ll come back to it in a moment. The second idea is that the solutions to the subproblems are stored, a process known as "memoization." Pay attention to that word; it’s sounds like "memorization" and it acts like memorization, but it’s not, it’s "memoization." Memoization is the process of storing expensive computations so they can be used again later without being recomputed.

## Memoization

Here is a very simple example of memoization, and one that blew my mind the first time I saw it. Remember the Fibonacci sequence from Chapter 11? Again, it a series of numbers where each one is the sum of the two preceding numbers in the series. The series starts with 0 and 1 and so: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144…​

The code for computing the Fibonacci sequence can be done using recursion, and here again is the code from Chapter 11:

``` python
def fibonacci(n):
    if n <= 0: # There are no negative fibonacci numbers
        return 0
    elif n == 1: # First number in sequence, no recursion needed
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Recursion!

print(fibonacci(10))  # Output: 55
```

You can run this code and it wont take too long, but remember, you’re only looking for the 10th number in the sequence. As pointed out in chapter 11, this recursive solution is not terribly efficient, clocking in at the regrettable O(2^n) time complexity to account for the unwinding of the recursion stack. This algorithm is not efficient because it recalculates the same Fibonacci number over and over again. To find the 10th Fibonacci number, it calculates the 9th and 8th Fibonacci numbers, but to find the 9th Fibonacci number it calculates the 8th and 7th Fibonacci numbers, and so on. When it gets to the 8th Fibonacci number, it calculates the 7th and 6th Fibonacci numbers, but to find the 7th Fibonacci number it calculates the 6th and 5th Fibonacci numbers, etc., etc. This algorithm does not remember these numbers. It comes up with them fresh every single time.

Let’s add some timing to the code so we can see how long it takes to run in Earth time, not just in Big O time. We can run the code with a few different values of n to see how long it takes to compute.

``` python
import time

def fibonacci(n):
    if n <= 0: # There are no negative fibonacci numbers
        return 0
    elif n == 1: # First number in sequence, no recursion needed
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Recursion!

def fibonacci_timer():
    test_values = [10, 20, 30, 35, 40, 45]

    print("Performance times:")
    print ('=' * 40)

    for n in test_values:
      start_time = time.perf_counter()
      result = fibonacci(n)
      end_time = time.perf_counter()

      total_time = end_time - start_time
      print(f"fibonacci({n}) = {result:>10} | Time: {total_time:>7.4f}s")

fibonacci_timer()
```

The results of running this code on the computer I’m using to write this book are:

``` text
Performance times:
========================================
fibonacci(10) =         55 | Time:  0.0000s
fibonacci(20) =       6765 | Time:  0.0024s
fibonacci(30) =     832040 | Time:  0.2657s
fibonacci(35) =    9227465 | Time:  2.9454s
fibonacci(40) =  102334155 | Time: 31.9365s
fibonacci(45) = 1134903170 | Time: 360.0277s
```python

Whoa, growing fast! I stopped at 45 because I didn’t want to miss my next book deadline, but feel free to try it with larger numbers if you’re not into the whole brevity thing.

Fear not, there is a solution at hand here. If instead of computing Fibonacci numbers afresh each time we go down the recursion stack, what if we store them so that when we need them again we can simply return them without computing:

``` python
def fibonacci_memoized(n, memo=None):
    if memo is None:
        memo = {}

    # If we've already got the value use that
    # instead of recomputing it (memoization)
    if n in memo:
        return memo[n]

    # Base cases
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)

    # Store the result before returning
    memo[n] = result
    return result
```

Running this memoized version of the Fibonacci code makes a huge difference! Even the looking for the 500th Fibonacci number takes only a fraction of a second:

``` text
Performance times:
========================================
fibonacci(10) =         55 | Time:  0.0000s
fibonacci(20) =       6765 | Time:  0.0000s
fibonacci(30) =     832040 | Time:  0.0000s
fibonacci(35) =    9227465 | Time:  0.0000s
fibonacci(40) =  102334155 | Time:  0.0000s
fibonacci(45) = 1134903170 | Time:  0.0000s
fibonacci(100) = 354224848179261915075 | Time:  0.0001s
fibonacci(500) = ENORMOUS NUMBER! | Time:  0.0006s
```javascript

My computer was able to calculate `fibonacci(500)` which resulted in a number slightly less than 14 with 103 zeros after it in just 0.0006 seconds. This is a speedup of about 122,725 times over the naive recursive version. Go memoization!

> **Why So Much Fibonacci?**
>
> I’ve always thought the Fibonacci sequence is cool, never more so than the first time I saw it clearly at work in a head of romanesco cauliflower. You should come to my parties!
>
> At the same time, though, so what? I’m not a botanist or a population biologist, so what do I care about Fibonacci numbers?
>
> The reason the Fibonacci sequence is used so often in computer science is because it’s applicable to a wide array of problems. It’s a fantastic example that can be used to illustrate functions, recursion, dynamic programming, chart making, and, yep, memoization.
>
> The intuition of it is easy to lose though.
>
> Why is matters is because it stands for a kind of programming problem that is very common in coding interviews. That’s the problem where you know something has a kind of boundary, but you don’t know what it is.
>
> If you have siblings you may have wrestled them at some point. When you wrestle your siblings, especially your younger siblings, you know that there is a limit to how much you can overpower them. You might knock them down and sit on them, but you aren’t trying to actually hurt them in any serious way, you’re just goofing around. There’s a limit, right? And you know you’ve hit it when you go too far and your sibling starts crying and you know you’re in trouble and the game isn’t fun any more.
>
> Fibonacci is like that. Have a look at the timing example. Things were going just fine until we got to 40, and then it wasn’t fun any more. I’m sure my computer could handle 50 but I just don’t want to know how long it would take. That’s the "boundary" of the Fibonacci sequence. What dynamic programming can help you do is figure out how to get to that boundary without going past it. It can help you figure out how to solve the problem without going too far and getting into trouble.
>
> How high can you drop an egg without it breaking? How many times can you fold a piece of paper in half? How far out can you build a bridge from one side of a river without additional support? How many times can you call a function before it runs out of memory? These are all problems that can be solved using dynamic programming, and the Fibonacci sequence is the generic example that shares one thing in common with all of them: a boundary.

## Overlapping Subproblems

The second key idea in dynamic programming that the subproblems must overlap. This is exactly what using recursion with fibonacci does: it breaks the larger problem into a series of subproblems, solving the fibonacci for each item before the one we’re interested in before finally arriving at the base case.

Here’s a different set of subproblems that will give you a sense of something you might be asked in a programming interview: The ants are getting ready for winter. They’ve got a finite amount of storage (boundary!) in the anthill. They have different types of things to store, each with different nutritional values and size requirements.

We’ll keep the math easy and limit it to these three items:

- Aphids: 9 nutrition units, 5 storage units

- Larvae: 6 nutrition units, 4 storage units

- Fungi: 4 nutrition units, 3 storage units

Beginning with a simple example, let’s say the anthill has one storage chamber with 11 available storage units. How can the most nutrition be packed into this unit?

There are a few combinations of things to be considered:

One idea is to take two aphids, using 10 storage units and yielding 18 nutrition units. Great start! There’s a storage unit empty but the ants are ready for winter. Is it possible to do better?

The ants try packing the anthill another way. this time they choose to pack in two larvae and one fungi, using 11 storage units and yielding 16 nutrition units. That’s not so good though. The storage is full but the nutrition value is lower.

The third idea is to take one aphid and two fungi, filling the storage but not optimizing the nutrition value. The ants are getting upset! What’s the best way to pack the storage units?

While this is fairly simple example that can be worked out with pencil and paper, (or just by looking at it) it illustrates exactly the kind of problem dynamic programming is good at.

Here’s is how dynamic programming can be used to solve this problem. This code is comprised of two parts, a dynamic programming algorithm that uses memoization to store the results of subproblems, and a demonstration function that shows how the algorithm works:

``` python
def ant_food_storage_dp(storage_capacity, foods):
    # storage_capacity = total storage units available
    # foods = list of tuples (nutrition, storage_units, name)
    # Example: foods = [(4, 3, "Aphids"), (3, 2, "Larvae"), (2, 1, "Fungi")]

    memo = {}

    def dp(remaining_storage, food_index):
        # Base case
        if remaining_storage <= 0 or food_index >= len(foods):
            return 0, []

        # Have we already solved this subproblem?
        if (remaining_storage, food_index) in memo:
            return memo[(remaining_storage, food_index)]

        nutrition, storage_units, name = foods[food_index]

        # Option 1: Skip this food type entirely (move to next food type)
        skip_nutrition, skip_items = dp(remaining_storage, food_index + 1)

        # Option 2: Take one of this food type
        take_nutrition = 0
        take_items = []
        if storage_units <= remaining_storage:
            # Take one item, then see what's optimal with remaining space
            remaining_nutrition, remaining_items = dp(remaining_storage - storage_units, food_index)
            take_nutrition = nutrition + remaining_nutrition
            take_items = [name] + remaining_items

        # Choose the option with maximum nutrition
        if take_nutrition > skip_nutrition:
            best_option = (take_nutrition, take_items)
        else:
            best_option = (skip_nutrition, skip_items)

        # Memoize the result and return
        memo[(remaining_storage, food_index)] = best_option
        return best_option

    return dp(storage_capacity, 0)

def demonstrate_ant_storage(capacity=11):
    foods = [
        (9, 5, "Aphids"),   # 9 nutrition, 5 storage units
        (6, 4, "Larvae"),   # 6 nutrition, 4 storage units
        (4, 3, "Fungi")     # 4 nutrition, 3 storage units
    ]

    storage_capacity = capacity

    print("=== Ant Food Storage Problem ===")
    print(f"Storage capacity: {storage_capacity} units")
    print("\nAvailable foods:")
    for nutrition, storage, name in foods:
        ratio = nutrition / storage
        print(f"  {name}: {nutrition} nutrition, {storage} storage (ratio: {ratio:.2f})")

    # Call the dynamic programming function
    max_nutrition, optimal_items = ant_food_storage_dp(storage_capacity, foods)


    print(f"\nOptimal solution: {max_nutrition} nutrition units")
    print("Selected items:")

    # Count and display the items
    from collections import Counter
    item_counts = Counter(optimal_items)

    total_storage_used = 0
    total_nutrition = 0

    for item_name, count in item_counts.items():
        # Find the nutrition and storage for this item
        for nutrition, storage, name in foods:
            if name == item_name:
                item_nutrition = nutrition * count
                item_storage = storage * count
                print(f"  {count} {item_name}: {item_nutrition} nutrition, {item_storage} storage")
                total_storage_used += item_storage
                total_nutrition += item_nutrition
                break

    print(f"\nTotal: {total_nutrition} nutrition, {total_storage_used} storage units used")
    print(f"Storage remaining: {storage_capacity - total_storage_used} units")

# Run the demonstration
demonstrate_ant_storage()
```

It turns out the first solution was the correct one, to pack to aphids. Even though it left a storage unit empty, this was the solution that yielded the most nutrition. Winner winner aphid dinner! Play around with the storage sizes and nutritional values of this example and see if you can’t come up with some interesting ways to pack the anthill.

## A New Wrinkle

This starter dynamic programming problem is easy because it relaxes one crucial assumption: the ants have an unlimited amount of available food to play around with. They can afford to take — and waste — as much of any type of food as they want. In reality, though — and I know this from talking to some ants — things won’t be quite so simple. There may be constraints on the available types of food or limitations on the way the food can be stored.

This brings us to a fairly common dynamic programming interview question known as "The Backpack Problem." In The Backpack Problem you have a backpack (often called a "knapsack") with a limited amount of space, and a set of items with various weights and values. How can you maximize the value of the items that can fit in the backpack while still remaining under the maximum allowable weight?

One way in which this might be presented is with three items. The first item has a value of 60, and a weight of 10. The second item has a value of 100, and a weight of 20. The third item has a value of 120, and a weight of 30. That’s it, there are only these three items. How do you pack your backpack? How do you repack your backpack if you are given another one that’s larger? Or smaller?

This problem is "binary," because there are only two choices for each item, you take it or you don’t. You may see it referred to as the "0/1 Knapsack Problem" for these very reasons.

In order for the solution to scale to various sizes of backpacks and item weights, one way to approach a solution is by filling in a table. The table will have a row for each item and a column for each possible weight limit. The algorithm fills in the table according to each item’s weight and value, and then uses the table to determine the maximum value that can be achieved without exceeding the weight limit of the backpack. The table is built up iteratively, and the solution is found by looking at the last cell in the table, which contains the maximum value that can be achieved with the given items and weight limit Here is the finished table:

| Items ↓ | 10 | 20 | 30 | 40 | 50 |
|----|----|----|----|----|----|
| 0 (no items) | 0 | 0 | 0 | 0 | 0 |
| 1 (value=60, weight=10) | 60 | 60 | 60 | 60 | 60 |
| 2 (value=100, weight=20) | 60 | <span class="highlight">100</span> ③ | 160 | 160 | 160 |
| 3 (value=120, weight=30) | 60 | 100 ② | 180 | <span class="highlight">220</span> ④ | <span class="highlight">**220**</span> ① |

1/0 Knapsack Dynamic Programming Table with Backtracking Path

**Backtracking Steps:** ① Final answer: 220 at \[3,50\] ② Move left by Item 3’s weight (30): \[3,20\] = 100 ③ Item 2 was selected here: \[2,20\] = 100 ④ Item 3 was selected here: \[3,50\] = 220

**Result:** Take Items 2 (value=100, weight=20) + Item 3 (value=120, weight=30) = 220 total value

``` python
def knapsack(capacity, weights, values, n):
    """
    0/1 Knapsack Problem using Dynamic Programming

    Args:
        capacity: Maximum weight the knapsack can hold
        weights: List of item weights
        values: List of item values
        n: Number of items

    Returns:
        Maximum value achievable
    """
    # Create DP table: dp[i][w] = max value using first i items with weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Option 1: Don't include current item
            dp[i][w] = dp[i-1][w]

            # Option 2: Include current item (if it fits)
            if weights[i-1] <= w:
                include_value = values[i-1] + dp[i-1][w - weights[i-1]]
                dp[i][w] = max(dp[i][w], include_value)

    return dp[n][capacity]

def knapsack_with_items(capacity, weights, values, n):
    """
    Returns both maximum value and which items to take
    """
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                include_value = values[i-1] + dp[i-1][w - weights[i-1]]
                dp[i][w] = max(dp[i][w], include_value)

    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)  # Item index
            w -= weights[i-1]

    return dp[n][capacity], selected_items[::-1]

# Test the solution
def test_knapsack():
    capacity = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    n = len(weights)

    print("=== 0/1 Knapsack Problem ===")
    print(f"Capacity: {capacity}")
    print("Items:")
    for i in range(n):
        ratio = values[i] / weights[i]
        print(f"  Item {i}: value={values[i]}, weight={weights[i]} (ratio: {ratio:.2f})")

    max_value, selected = knapsack_with_items(capacity, weights, values, n)

    print(f"\nMaximum value: {max_value}")
    print("Selected items:")
    total_weight = 0
    for idx in selected:
        print(f"  Item {idx}: value={values[idx]}, weight={weights[idx]}")
        total_weight += weights[idx]
    print(f"Total weight: {total_weight}/{capacity}")

test_knapsack()
```

## Why Dynamic Programming Matters

## Building Intuition: Reasoning about Dynamic Programming

## Solving Problems using Dynamic Programming

## Example problems

### The Fox, the Chicken, and the Grain

When I was in college we were sitting around our house living room eating chicken wings and thinking deep thoughts when someone brought up the classic problem of the fox, the chicken, and the grain.

A farmer is walking home with three things he bought in town, a fox, a chicken, and a bag of grain. (Why would a farmer buy a fox? Present for his kid? I don’t know, not the point, just go with it.) He comes to the river he has to cross to get home, but as he begins to load his items into his small boat he realizes he can only fit one other item into the boat with him at a time (boundary!). He further realizes that if he leaves the chicken alone with the grain, the chicken will eat the grain, and if he leaves the fox alone with the chicken, the fox will eat the chicken. (The grain is a peace-loving grain and will eat nothing else.) How can the farmer get all three items across the river without losing any of them?

We must have been eating some really hot wings, because this one blew our mind. Can you figure out how to solve this problem? Can you figure out how to solve this problem using dynamic programming?

### The Climbing Stair problem

### The Knapsack problem

### Longest common substring

### The Coin Change problem

## Greedy Algorithms

## Why Greedy Algorithms Matter

## Building Intuition: Reasoning about Greedy Algorithms

## Solving Problems using Greedy Algorithms

## Greedy Algorithms in Practice

## Counterexamples: Trust, but Verify

## Example problems

### The Activity Selection problem

### The Coin Change problem

### The Fractional Knapsack problem
