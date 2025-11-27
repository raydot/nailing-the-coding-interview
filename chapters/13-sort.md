## Sort

Now that we’ve bit off that large chunk of search we’re ready to move on to sort. We’ll consider sort both on its own and as it relates to search, with the goal, as always, towards building an intuitive understanding that can be used to solve problems in interviews.

### What does “sort” mean?

Sort means putting things in some kind of order, usually either ascending or descending. The order can be determined by many things but usually involves some kind of sequence of information. For instance, a list of sports players can be sorted in a variety of names given a specific sequence. The players could be sorted by name, age, a given statistic, eye color, distance from home to stadium, pet type, number of children, favorite candy, etc. When we talk about sort we’re talking about putting things in order to create a context for comparison.

<div class="example">

<div class="title">

Things Used to Come With Instructions

Not so long ago, computers actually came with instruction manuals. There was a time when not everyone just grew up knowing how to use a mouse. In fact, games like Minesweeper and Solitare were included with Windows for that exact purpose — teaching people how to use a mouse.

The earliest versions of the Java Development Kit (JDK) that came out in the mid 1990’s used to come with an applet called "SortDemo." Running this demo would allow the user to choose between different sorting algorithms, such as bubble sort, insertion sort, and quick sort, and then watch as the applet sorted a list of numbers in real time.

In the days before AI and YouTube, Java was a great way to get started with programming. It was readily accessible and could run pretty much anywhere. Applets are now sadly a thing of the past, but the legacy of the SortDemo lives on. Check out "algs4.jar,"" Princeton University’s library of Java and Python apps aimed at teaching algorithms. It can be found at `https://algs4.cs.princeton.edu/code/`.

### How is sort used?

Sort can be used either simply to put information in order on its own, or in service of another process. Some search algorithms benefit from the information first being sorted, as was discussed in the last section on search.

### Why sort is important to understand

Like search, sort isn’t one specific thing but a range of solutions to various problems. Understanding sort is important because it allows you to choose the right algorithm for the right problem, and to understand the tradeoffs involved in each choice.

### Building Intuition: Reasoning about Sort

The basic truth about sort is a simple one: can a set of data be organized in a way that makes it easier to reason about. If the answer is yes, then it’s time to sort. Like with search, there is a tradeoff between speed and size, as well as a difference between sorting small sets of data and larger ones.

This section will teach the basic concepts, but it’s important to download and play with the code, try it out on different sets of data, run it against a timing algorithm, and really understand the key differences between different approaches.

## Types of Sort Part I, Basic Sorting

During the 1970’s and 1980’s when computer science was preparing for the days ahead when computers could actually do all of the things computer scientists dreamed about, a lot of thought was put into the most effective ways to search. There are a lot of different sorting algorithms out there, some very general and some hyper-specialized.

I’m pretty sure an entire book could be written about sort alone. Since this is of course not that book, I’m going to start with an overview of some of the more commonly used and easy-to-understand versions of sort. Again, and as with search, I invite you to play with these examples, use them with your own data, and gain a real understanding of the differences. Also again and as with search, your job interview coding test might not contain a question that is specifically about search, but the reasoning skill you will gain from understanding search might help you solve the problem.

The algorithms selected in this chapter are meant to cover an array of sorting strategies, culminating in merge sort. Merge sort is really a culmination of many ideas presented elsewhere in this book. If there’s one thing you take away from this chapter, focus on understanding merge sort.

Insertion and bubble sort were covered in Chapter 4 in the context of arrays. But sort is data structure agnostic, to some extent. Whether the data is stored in a flat file, array, object, dictionary or database, these sorting methods can all be applied.

### Insertion sort

In Chapter 4 we covered bubble sort and insertion sort in that order. In this chapter I’m going to reverse the order to make a slightly different point. Let’s start with insertion sort this time because it’s fairly intuitive. The idea behind insertion sort is that you move things around until they’re sorted.

Let’s start with the intuition: say you collect sneakers. You want to come up with a way to organize your sneakers in your closet. You do this but putting your favorite sneaker on the left side of the closet because it "feels" like it goes first. Then, one-by-one, you put each remaining pair of sneakers into the line. If it feels like it goes second, you put it to the right of the first pair. Or maybe you don’t like it so much, and so you put it at the end of the line of sneakers.

Every sneaker that comes in has to fit somewhere in this schema. Nothing will go to the left of your first sneaker, because that’s your favorite. But everything else will go between the pair of sneakers that’s a little bit better, and a little bit worse. By the time you get to the bottom of the pile your sneakers are now sorted in a line from best to worst. (You also could have done this with any other criterion including color, price, drip, height, etc.)

Going back to our fruit example, let’s look at how insertion sort can be used to sort all of the fruits alphabetically:

    def insertion_sort_catalog(fruits):
        """Sort fruits alphabetically"""
        for i in range(1, len(fruits)):
            current_fruit = fruits[i]
            j = i - 1
            # Find the right spot and insert
            while j >= 0 and fruits[j]['name'] > current_fruit['name']:
                fruits[j + 1] = fruits[j]
                j -= 1
            fruits[j + 1] = current_fruit

This good, intuitive way to build a search, and probably what most of us would do if we were asked to come up with our own search algorithm. The idea is right down the line and stick each fruit exactly where it belongs. You should notice either from looking at the code or from remembering Chapter 4 that this of course comes with a O(n^2) time complexity, because you have a loop nested inside a loop. If you have just a little bit of data, you could do a lot worse than to use insertion sort. Which brings us to…​

### Bubble sort

Bubble sort definitely looks like an improvement over insertion sort. In bubble sort you go right down the line and compare every item with the item right next to it. If they’re out of order, you swap them. Quite the optimization, eh?

    def bubble_sort_prices(fruits):
        """Sort fruit by price"""
        n = len(fruits)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Compare every adjacent pair
                if fruits[j]['price_per_lb'] > fruits[j + 1]['price_per_lb']:
                    fruits[j], fruits[j + 1] = fruits[j + 1], fruits[j]

Bubble sort is less code (by two lines) and easier to comprehend and remember. Sure it’s O(n^2), but that’s the same as insertion sort, right? You’re probably used to my style by now, so when I ask if something’s right, you’ve probably figured the answer is no, it’s not right. Well this is no exception!

Even though bubble sort is a slightly more "obvious" solution, and even though the time complexity is indeed O(n^2) for both, bubble sort can actually require quite a few more comparisons.

The reason why is that insertion sort goes over each item once, puts it where it belongs, and moves on to the next item. Bubble sort compares everything over and over again — including things that are already sorted before! That might be fine for apples and bananas, which begin with letters near the beginning of the English alphabet, but if you had an employee that checked if everthing was already sorted before filing away the raspberries and soursop you would quickly suggest that one of the two of you was in the wrong line of work.

Again, both algorithms are O(n^2). Asymptotic notation is a great place to start in algorithm comparison, but remember that it usually describes the _limit_ of the algorithm, and sometimes that’s just not the whole story. "Run down to the farthest edge of the property and I’ll give you a dollar," is a far more appealing proposition to the resident of a New York City studio apartment occupant than it is to a Wisconsin farm dweller. In Wisconsin you could be running for miles to get that dollar while in New York you might not even have to get off your couch.

### Selection sort

Selection sort works in a simple fashion. Take the smallest item and put it at the front of the array/queue/stack. Then select the next smallest item and put it next. Continue doing this until all of the items are sorted. It works the same as selection sort with one significant difference. Insteading of doing all of the comparing that’s done with insertion sort, selection sort maintains a part of the array that it already considers to be sorted.

It’s kind of like opening birthday presents. Most people, given a stack of presents, open them in one of two ways: biggest one first, or biggest one last. Either way, once a present is opened, it does not get returned to the candidate pile. It’s been opened, it’s no longer under consideration.

    def selection_sort_fruits(fruits):
        """Sort fruits by name using selection sort"""
        n = len(fruits)
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            min_index = i
            for j in range(i + 1, n):
                if fruits[j]['name'] < fruits[min_index]['name']:
                    min_index = j
            # Swap the found minimum element with the first element
            fruits[i], fruits[min_index] = fruits[min_index], fruits[i]

With selection sort a "min_index" is added. The "min_index" acts as a marker to separate the sorted from the unsorted. If an item from the unsorted side is the smallest item remaining, it gets moved to the front of the unsorted line and the marker increased by one. By the time this algorithm is finished, the items are sorted from smallest to largest. While the runtime of this algorithm is also O(n^2) like bubble sort and insertion sort, depending on the state of the starting list — especially if it’s already mostly sorted — selection sort can run in nearly O(n) time.

## Types of Sort Part II, Advanced Sorting

If you’ve read this far and stopped, you would actually have a pretty good algorithmic basic for searching that would server you pretty well in an interview. But if there’s been a lingering doubt at the back of your mind, "O(n^2) is not good enough! There must be something better," you’re absolutely right.

There are many sorting algorithms that run in better than O(n^2), and they all use the same basic idea: divide and conquer. Let’s pause for a moment to consider what that means.

There are three steps to divide and conquer:

- Divide

Divide the sort space into smaller parts

- Conquer

Sort those smaller parts

- Combine

Combine the smaller parts back into the original sort space

Et voila, you have a sorted list. This is the basic idea behind quick sort and merge sort, which are arguably (and unarguably) the two most widely used sorting algorithms in the computer science world.

### Quick sort

In the examples so far we’ve been choosing very specific use cases to justify the types of sort used. But the fruit stand has grown and we can’t code our feelings any more, we need a more general purpose algorithm that can sort by _more_ criteria. We need to sort fruit by price, calorie value, color, sweetness index, all of it. This is where quick sort comes in.

The way quick sort works is by starting with the "divide" step. Quick sort selects a "pivot" point in the data, and then organizes the data into things that are lower than the pivot, and things and are higher. This pivot can be found anywhere in the data, but since the data isn’t already sorted (right?) it’s just as useful to simply choose the first (or last) item in the list. Quick sort doesn’t get hung up on finding the "perfect" pivot, it just needs somewhere to start. Once the pivot is selected the data is split into the two parts mentioned earlier, lower than the pivot and higher than the pivot.

\<Diagram of pivot splitting TK\>

Now for the "conquer" step: Remember back in the last chapter when we talked about the recursive "base case." Quick sort’s base case is sorted data. If you have an array with exactly one piece of data in it, it must be sorted, right? This is where quick sort finds the base case. More specifically, if quick sort selects the pivot, but doesn’t find anything to split to the left or right of it, then what’s left must be sorted, right? Take a moment to sit with that. It broke my brain a bit the first time I heard it.

\<Diagram of base case TK\>

With all of the pieces broken down into their smallest, sorted bits, quick sort has hit the base case and conquered! Now it unwinds the recursive stack to "combine" the data back together like a reverse-Godzilla, leaving nothing but order in its wake.

    def quick_sort_fruits(fruits, key='name'):
        # Base case
        if len(fruits) <= 1:
            return fruits

        # DIVIDE: Choose pivot and partition
        pivot, less_than, greater_than = partition_fruits(fruits, key)

        # CONQUER: Recursively sort partitions
        sorted_less = quick_sort_fruits(less_than, key)
        sorted_greater = quick_sort_fruits(greater_than, key)

        # COMBINE: Merge results
        return combine_partitions(sorted_less, pivot, sorted_greater)

    def partition_fruits(fruits, key):
        """
        Divide step: partition fruits around a pivot

        Returns:
            tuple: (pivot_fruit, fruits_less_than_pivot, fruits_greater_than_pivot)
        """
        pivot = fruits[0]
        pivot_value = pivot[key]

        less_than = []
        greater_than = []

        for fruit in fruits[1:]:
            if fruit[key] < pivot_value:
                less_than.append(fruit)
            else:
                greater_than.append(fruit)

        return pivot, less_than, greater_than

    def combine_partitions(sorted_less, pivot, sorted_greater):
        """
        Combine step: merge sorted partitions back together
        """
        return sorted_less + [pivot] + sorted_greater

    # Usage example
    def demonstrate_quicksort():
        sample_fruits = [
            {"name": "Mango", "price_per_lb": 3.99, "sweetness": 8},
            {"name": "Apple", "price_per_lb": 2.49, "sweetness": 6},
            {"name": "Banana", "price_per_lb": 1.29, "sweetness": 7},
            {"name": "Cherry", "price_per_lb": 5.99, "sweetness": 5}
        ]

        print("Original fruits:")
        for fruit in sample_fruits:
            print(f"  {fruit['name']}: ${fruit['price_per_lb']}")

        # Sort by price
        sorted_by_price = quick_sort_fruits(sample_fruits, 'price_per_lb')

        print("\nSorted by price:")
        for fruit in sorted_by_price:
            print(f"  {fruit['name']}: ${fruit['price_per_lb']}")


    demonstrate_quicksort()

Run the code and prepare to be amazed! No for loops for one thing. As always I ask you to pause for a moment and look over the code and consider the run time. Quick sort breaks things in half repeatedly. This should remind of a tree, as discussed in Chapter 9. Usually when you’re able to break a problem in half, repeatedly, the run time becomes logarithmic, and indeed quick sort can run as fast as O(n log n). Pretty cool, right?

I mentioned earlier that the first time I saw quick sort it broke my brain, and that wasn’t hyperbole. You might find yourself looking at this algorithm thinking "but what actually happens?" That’s the beauty of the base case. When a recursive algorithm hits the base case it knows it doesn’t have anywhere else to go, nothing else to recurse. It has effectively hit bottom. So then it begins to "unwind" in the same order things were passed to it, like the example of the TV news report in Chapter 11. That’s where the "sort" happens, and that’s the genius of quick sort.

But wait, up there I said quick sort "can" run as fast as O(n log n) and not "does" run at that speed. Let’s review some language from Chapter 2. Even though algorithms are most often discussed in terms of "Big O," keep in mind there are other benchmarks. Big O talks about the "upper bound" of the algorithm, or the worst case. To talk about the "lower bound" or best case, we used Big Omega (Ω). For a "tight bound," which for the purposes of this book can be read as "average case," the notation is Big Theta (Θ).

While quick sort _usually_ runs in O(n log n) time, that’s predicated on the idea that choosing the first item in an array as the pivot is an optimal selection. The problem is, it might not be. If the pivot is usually an average value — as you should expect if the data is fairly random — then everything works out fine. The problem comes in when the pivot is not an average value, and may in fact repeatedly be the worst possible value that can be chosen. This occurs when the data is already mostly sorted. If the item repeatedly chosen for the pivot is always either the smallest or largest element, then the sort becomes linear and quick sort runs much closer to our old friend O(n^2) time, the same as all of the other sort algorithms we’ve considered.

There are ways to updo your quick sort so this doesn’t happen. You can pick three numbers at random and always choose the median as the pivot for example. Of course, the more you have to do to get the right numbers the less quick the algorithm, it’s a balancing act.

The takeaway: while quick sort is indeed O(n^2) it is also Θ(n log n). It will definitely work in n log n time with the right kind of data. But is there an algorithm that can dispense with the maybe and always run at O(n log n)? Read on, dear reader, and find out.

### Merge sort

If you were brave enough to weather that section break you have at last arrived at merge sort, the holy grail, the magic temple at the top of the mountain. Conceptually, anyway. Quick sort might be a bit more widely used and a bit more of a general purpose algorithm, but merge sort adds a few conceptual details that will really help cement an understanding of sort algorithms.

Merge sort is primarily different from quick sort in that while quick sort does the hard work up front in the divide step, merge sort does the hard work in the conquer step. Merge sort does the "divide" step by always splitting a list exactly in half, with no regard to anything other than finding the middle. The "conquer" part is the same as quick sort’s: dividing the lists down until you come to a lone item, which is, by virtue of its very existence, sorted.

\<Image of Merge Sort "divide" TK\>

It’s the "combine" step where the merge sort magic happens. Consider two lists, list A and list B. Your goal is to organize these two lists into a combined list from smallest to largest. Merge sort will start at the first item in each list. It will choose the smaller item between the two lists, and merge it into combined list. Then it will go back to the next item in the list it chose from, and do the comparison again. It will do this item by item until both lists are empty, at which point the combined list will be in sorted order.

\<Image of Merge Sort "combine" TK\>

Here is an example of merge sort in action:

    def merge_sort_fruits(fruits, key='name'):
        """Sort fruits using merge sort algorithm"""
        # Base case
        if len(fruits) <= 1:
            return fruits

        # DIVIDE: Always split exactly in half
        mid = len(fruits) // 2
        left_half = merge_sort_fruits(fruits[:mid], key)
        right_half = merge_sort_fruits(fruits[mid:], key)

        # COMBINE: Merge the sorted halves
        return merge_sorted_halves(left_half, right_half, key)

    def merge_sorted_halves(left, right, key):
        """
        Combine step: merge two sorted fruit lists into one sorted list

        Args:
            left: First sorted list of fruits
            right: Second sorted list of fruits
            key: The attribute to sort by

        Returns:
            Combined sorted list of fruits
        """
        merged_result = []
        i = j = 0

        # Compare first fruits from each sorted list and merge
        while i < len(left) and j < len(right):
            if left[i][key] <= right[j][key]:
                merged_result.append(left[i])
                i += 1
            else:
                merged_result.append(right[j])
                j += 1

        # Add any remaining fruits from left list
        while i < len(left):
            merged_result.append(left[i])
            i += 1

        # Add any remaining fruits from right list
        while j < len(right):
            merged_result.append(right[j])
            j += 1

        return merged_result

    # Usage example
    def demonstrate_mergesort():
        """Demonstrate merge sort with sample fruit data"""
        sample_fruits = [
            {"name": "Mango", "price_per_lb": 3.99, "sweetness": 8},
            {"name": "Apple", "price_per_lb": 2.49, "sweetness": 6},
            {"name": "Banana", "price_per_lb": 1.29, "sweetness": 7},
            {"name": "Cherry", "price_per_lb": 5.99, "sweetness": 5}
        ]

        print("Original fruits:")
        for fruit in sample_fruits:
            print(f"  {fruit['name']}: ${fruit['price_per_lb']}")

        # Sort by price using merge sort
        sorted_by_price = merge_sort_fruits(sample_fruits, 'price_per_lb')

        print("\nSorted by price (merge sort):")
        for fruit in sorted_by_price:
            print(f"  {fruit['name']}: ${fruit['price_per_lb']}")

    demonstrate_mergesort()

Cool! What’s the catch? The catch is that merge sort requires additional space of at least the length of the list in order to work, because it needs to break the starting list into another list of the same size. Quick sort, by comparison, sorts the items in place, and so does not require this additional space. No big deal if you’re dealing with just a few (hundred) items in a system with plenty of memory, but add a few (hundred thousand) more on a system with limited storage and merge sort might not be the best idea.

## Summary of Sort Algorithms

Just like that you have come to the end of the second part of the book! If you’ve made it this far you’re in some very good shape for a job interview. Consider sitting with this section for a little bit, or going back through Section I to see if some of the ideas you might have glossed over the first time make more sense now. You might even see them in a different context!

## Example Questions

### Anagrams

### Partitioning

### Optimization
