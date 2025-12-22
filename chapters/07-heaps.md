# Heaps

Congratulations, you’ve made it to heaps! This is a fantastic thing because heaps are the entrance to the "open seas" of data structures, where you leave behind more abstract, theoretical concepts and start working with practical, real-world data structures that have a wide range of applications. (Ok, that might be a bit of a stretch, but you get the general idea) By the end of this chapter you will understand what a heap is, what it’s used for, and how to implement one. You will also understand how heaps relate to trees and graphs, and how to use them build better search and sort algorithms.

## Heap Definition

A heap is a data structure that expands on the idea of stacks and queues by adding an additional layer of organization to data. Adding this layer means that data can be kept in a specific order, depending on the type of heap being used.

The most common type of heap is the "max heap," or it’s mirror image counterpart, the "min heap." These are data structures that are organized in such a way that the largest (or smallest) element is always kept at the top or the heap.

There’s more to a heap than that, but as the wise man in the forest once said, "In order to understand the heap, you must first understand the tree."

## Trees

While trees will be covered in much greater depth in chapter 9, this is a great place to start building a foundation of understanding. I’m going to move away from "code" for a moment and talk about the concept of a tree in a more general way.

In computer science a tree is a data structure that is used to organize data in a hierarchial way. The concept comes from the fact that data in tree form can best be understood as an upside-down tree, with the "root" at the top and the "leaves" at the bottom. Why it isn’t called something else, I’ll never know.

\<DIAGRAM OF A TREE TK\>

            50
          /    \
       10      63
      /  \    /  \
    5    15  60   75

A tree is made up of nodes (items) and edges (connections). If you’ve studied any graph theory — which we’ll get to in Chapter 10 — these terms may sound familiar. In this tree example — commonly known as a "binary tree" — the root of the tree (at the top) is 50, and the leaves of the tree are 5, 15, 60, and 75. In this particular tree, the root (50) has two children (10 and 63), and each of those children has two children of its own. The leaves of the tree are the nodes that have no children.

Conversely, except for the root each node in the tree has a parent. The parent of a node is the node that is directly above it in the tree. In the example above, the parent of 60 is 63, and the parent of 63 is 50.

What makes this particular tree a binary tree is that each node of data has a smaller value to the left and a larger value to the right. In fact, if you read the tree from left to right horizontally, you’ll see that the values are in ascending order: 5, 10, 15, 50, 60, 63, 75. Any new values added to the tree will need to be added in a way that keeps things in this order — but we’ll get back to that in Chapter 9.

There is a close relationship between heaps, trees, and graphs, which is what I meant earlier when I said that heaps are the entrance to the "open seas" of data structures. Keep this image of a binary tree in mind as we consider a heap.

## Heaps and Trees

A heap can be thought of as almost a flat tree, with data organized in a way that makes it easy to find either the largest or smallest element. The rules for organizing data in a heap keep the data in a specific order depending on the type of heap being used. A heap that keeps the maximum element at the top is called a "max heap," and a heap that keeps the minimum element at the top is called a "min heap." Let’s revisit the tree example above and this time turn it into a max heap.

\<DIAGRAM OF A HEAP TK\>

            75
          /    \
       63      60
      /  \    /  \
    50   15  10   5

This now is the same data but with a different organization. The way this data is organized, and what makes it a "max" heap, is that the largest element is always at the top of the heap. In a max heap, instead of the values ascending from left to right as in the tree example, the values are organized in such a way that the largest value is always at the top. Instead of having a smaller value to the left and a larger value to the right, a heap is organized so that each parent contains a value that is larger than its children.

Now you can’t store data in a tree shape, of course, and if you fed the two above diagrams into a computer it wouldn’t really know how to handle them. So instead, let me consider the heap as a "flat tree" and see what it looks like as a linear data structure. I’ll start with a Python list:

```python
heap = [75, 63, 60, 50, 15, 10, 5]
```

As a heap, this list contains some organizational rules that keep the data the way it needs to be so that the values remain in the correct order. Every child in a heap has a parent, and the parent can be taking the child’s index, subtracting one, and dividing by two. Or:

```python
parent = (child - 1) // 2
```

To find the parent of 15, for instance, start with the index value of 15 which is 4. Subtract one from four to get three, and then divide by two to get one (remember that in Python that the `//` operator rounds down to the nearest integer).

```python
parent = (4 - 1) // 2 # step 1
parent = 3 // 2 # step 2
parent = 1 # step 3
```

Looking at list element 1, the parent of 15 is 63. Go ahead and try this "trick" with any other element in the list and I think you’ll find that it works. (If it didn’t, I wouldn’t have told you about it.)

From this simple idea it’s easy to build up some rules to implement a heap in code.

## Inserting into a Heap

Let’s return to our existing heap, once again in a tree view.

\<DIAGRAM OF A HEAP TK\>

            75
          /    \
        63      60
      /  \    /  \
    50   15  10   5

I want to add a new value to this heap, and the value I want to add is 1. Stop for a moment and think about where you would add this value to the heap. There is only one place for it to go in order to maintain all of the rules we’ve discussed so far. In this case, and in every other case, a new value is always added to the end of the heap. The heap is then "heapified" to make sure it remains a heap. After inserting the 1 at the end of the list, the heap now looks like this:

\<DIAGRAM OF A HEAP TK\>

            75
          /    \
        63      60
       /  \    /  \
      50   15 10   5
     /
    1            <--- New value

Have we maintained all of the rules we’ve learned so far?

1.  The largest value is at the top of the heap.

2.  Each parent contains a value that is larger than its children.

In list form our heap now looks like this:

```python
heap = [75, 63, 60, 50, 15, 10, 5, 1]
```

Can we find the parent of 1 using the formula we discussed earlier?

```python
parent = (7 - 1) // 2
parent = 6 // 2
parent = 3
```

The parent of 1 is 50, which is correct.

That was an easy one. What if we want to add the value 67 to the heap? Looking at the heap, where would you add the value 67?

\<DIAGRAM OF A HEAP TK\>

            75
          /    \
        63      60
       /  \    /  \
      50   15 10   5
     /  \
    1    67

As always, the new value is added to the end of the heap, but now the heap is clearly out of order! 67 is larger than both its parent, 50, and its grandparent, 63.

Fortunately, there is a simple way to fix this. After adding a value to the end of a heap it is necessary to "bubble up" the value to its correct position. (I didn’t make up the term "Bubble Up," but I drank a lot of it when I was a kid.)

The steps involved in bubbling up a value are:

1.  Add the new value to the end of the heap.

2.  Compare the new value to its parent.

3.  If the new value is larger than its parent, swap the new value with its parent.

Applying this to the heap with the new value 67:

1.  Add 67 to the end of the heap.

2.  Compare 67 to its parent, 50.

3.  67 is larger than 50, so swap 67 and 50.

                75
              /    \
            63      60
           /  \    /  \
          67   15 10   5
         /  \
        1    50

4.  Compare 67 to its new parent, 63.

5.  67 is larger than 63, so bubble up again, swapping 67 and 63.

                75
              /    \
            67      60
           /  \    /  \
          63   15 10   5
         /  \
        1    50

Now the heap is back in order and all is right in the kingdom.

Before considering other cases, I’d like to stop for a moment and consider what this looks like in code. Here is a Python class that implements the heap I’ve been discussing. It prints the heap, inserts the value 67, bubbles it up, and prints the heap again:

```python
class Heap:
    def __init__(self, input_list=None):
        self.heap = []
        if input_list:
            self.heap = input_list.copy()

    def get_parent(self, index):
        return (index - 1) // 2

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def display(self):
        return self.heap

    def _bubble_up(self, index):
        parent = self.get_parent(index)

        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)


# Test the implementation
heap = Heap([75, 63, 60, 50, 15, 10, 5, 1])
print("Initial heap:", heap.display())
heap.insert(67)
print("After inserting 67:", heap.display())
```

Breaking this code down method by method, the first four are pretty straightforward:

The `init` method initializes the heap with an optional input list.

The `get_parent` method returns the parent of a given index.

The `insert` method adds a new value to the heap and calls the `_bubble_up` method to maintain the heap property. It passes in the index of the new value which, being appended to the end of the heap, is the last index found at `len(self.heap) - 1`.

The `display` method returns the heap, which can be passed to the `print` function in order to be displayed.

This leaves us with the `_bubble_up` method, which is the most interesting (in both name and function) and important part of the code.

```python
def _bubble_up(self, index):
    parent = self.get_parent(index)

    if index > 0 and self.heap[index] > self.heap[parent]:
        self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
        self._bubble_up(parent)
```

This incredibly useful five lines of code does all the work of bubbling up a value in the heap. It does this by comparing an item to its parent, and swapping the two if the item is larger than its parent. I’m not sure how I could suddenly become my own mother, so the family metaphor breaks down a bit here, but you get the idea.

> **recursion**
>
> This book doesn’t get to recursion until Chapter 11, but you’re encountering it here in the `_bubble_up` method. Recursion is a programming technique where a function calls itself. That might sound like crazy talk, but that’s what happens. The function "recurses" down the tree of calls until it (hopefully) finds a stopping point, at which point it "unwinds" back up the tree and returns the results.
>
> An analogy I heard a long time ago is like newscasters on the news. There will be a news anchor who will read off a news story and then maybe call on a reporter in the field. That reporter will begin to report the story and then call out for a video to be played that was taken earlier. When the video ends, the scene goes back to the reporter, who ties up the story and then sends the broadcast back to the anchor.
>
> There’s a lot more to it than that, but keep that basic idea in mind when you see a function calling itself. In the case of `_bubble_up`, it will keep calling itself with the parent of the current index until `index > 0 and self.heap[index] > self.heap[parent]` is no longer true which means the element is in its proper place in the heap.

Earlier I said a property of a heap is that it stays "heapified." Also called "heap order," this refers to the property that each parent contains a value that is larger than its children. This simultaneously keeps the largest value at the top of the heap and makes it possible to find the largest value in the heap in constant time. So while a heap is a data structure, it’s comprised of a collection of algorithms that maintain the heap order property.

We’ve looked at inserting, so now let’s look at removing values from a heap.

## Deleting from a Heap

Deleting an item from a heap is like adding an item, but in reverse. The item is removed from the heap and then the heap is "bubbled down" so that it maintains the heap order property.

The process of bubbling down is a little more complicated for this simple reason: when bubbling up an item it’s always going to be replaced with its parent. An item bubbling down, however, could be replaced with _either_ of its children.

Before I showed the way to find the parent of a child in a heap:

`parent = (child - 1) // 2`

For a parent to find either of its children in a heap, the formulas are:

The left child of a parent is found at: `left_child = 2 * parent + 1` The right child of a parent is found at: `right_child = 2 * parent + 2`

It may have occurred to you that perhaps a value could be located that is a left child when it should be a right child, or vice versa. That’s the genius of the heap data structure — it can’t happen. The reason why is because a heap must always filled in from left to right, and the left child is always filled in before the right child. As such, a heap cannot have a parent that is missing a left child and has a right child (and of course while bubbling down you must account for this). There are also no gaps allowed in the heap structure, so if a value is removed from the heap it must be replaced with the last value in the heap. There won’t multiple levels in the heap that jump from left child to left child without rebalancing the heap. This also means that all of the left children in a heap are located at odd indexes, and all of the right children are located at even indexes.

Just so there’s no confusion, I kept using words like "must" and "cannot" and "allowed" in that description. What I mean are, these are the rules that must be followed for a data structure to be considered a heap. If you don’t follow these rules your code probably won’t crash or throw an error, but you’ll get some unwanted results.

The basic rules are:

1.  A parent must always be larger than its children in a max heap, and smaller than its children in a min heap.

2.  The heap must be filled in from left to right (or right to left if that fits the solution better, but in some consistent order).

3.  The heap must be filled in without any gaps.

As long as these rules are followed the heap will always stay heapy — I mean happy — and in proper (min or max) heap order.

With all of that now firmly in mind, hopefully, let’s consider the process of removing a value from a heap. A heap is a priority-based data structure, meaning the values are ordered by a priority determined by the programmer. As such the first value in a array representing a max heap — the top item in the heap tree — always represents the largest value in the heap. (In a max heap, anyway. In a min heap it’s the other way around. The first item in the array and/or the top item in the tree is always the smallest value in the heap.)

This leads to a straight-forward process for removing a value from a heap in first-in, first-out order:

1.  Remove the first value in the heap.

2.  Replace the first value with the last value in the heap.

3.  Bubble down the new first value to its correct position.

If this sounds to you a lot like the "pop" method for a stack or a queue, that’s because that’s pretty much what it is. The only difference is that a heap needs to make sure it maintains its items in heap order, which is why the pop here comes with a "bubble down." (It might also lead you to wonder if early computer scientists chewed an awful lot of gum, but I digress.)

Here’s an example of a class that only has one purpose: to remove the top value from a max heap. In other words, to use the heap as a queue. It does so while using "bubble down" to maintain the heap order property:

```python
class MaxHeapPopper:
    def get_left_child(self, index):
        return 2 * index + 1

    def get_right_child(self, index):
        return 2 * index + 2

    def _bubble_down(self, index):
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)
```

## Developing Intuition: What are heaps used for?

Between the math that’s used to keep a heap organized and the clever methods that have been developed to access and manipulate the data in a heap, it’s an incredibly useful data structure. Heaps can be used to create the priority queues that were discussed in Chapter 6. They are the basic foundation of Dijkstra’s algorithm, which is used to find the shortest path between two nodes in a graph (think, cities on a map) that will be discussed in Chapter 10. They can also be used for sorting, as will be discussed in Chapter 12. There will be other examples later in this chapter. As you go though these examples, always try to see how the heap is working, and maintaining order "behind the scenes" of the problem at hand.

## Heaps and Heaps of Heaps

Hopefully it’s clear that a min heap is just a max heap with the values reversed. There are other ways to create heaps. One example is a "min-max heap," which is a heap that alternates between min and max heaps. Two heaps can be combined to create a heap that maintains a median value, which is useful to know in doing statistical analysis. There are binomial heaps, fibonacci heaps, heaps with more than two children per node, and heaps that are used to manage other heaps. All of these have the same thing in common and that is that they maintain the heap order as items are added to them.

## Thinking Strategies

Here are some more ideas involving heaps. Try to look at these questions from two perspectives. The first perspective is the idea of problems that are specifically about heaps. The second perspective is the idea of problems that can be solved with or without heaps, but where knowledge of how heaps work might be used to either better solve the problem or to expand the answer.
You can carry this reasoning into the "Sample Interview Problems" section at the end of the the chapter.

If you need to, be sure and review some of the simple math ideas behind the heap that were provided in the "Heaps and Trees" section earlier in this chapter.

### Is it a heap?

_Given an array, determine if it is a heap._

There are a few ways this question might be asked in an interview. The question might additionally require a determination to be made about the type of heap — is it a max or min heap? There also might be some version of converting a max heap into a min heap, or vice versa.

While these are easy tasks to do by sight, how could an algorithm be used to make this determination?

Instead of jumping into code, let’s take a look at "what is a heap" in plain English:

1.  Start at the first element in the array.

2.  Compare the element to its parent.

3.  If the element is larger than its parent, return false.

4.  If the element is smaller than its parent, move to the next element.

5.  If the end of the array is reached, return true.

(Does this specific algorithm determine whether the item is a max heap or a min heap? Think about it for a moment before reading on.)

Remember, the question starts with an array, so the first element in the array is the root of the heap. After that, each element can find its parent by using the formula `parent = (child - 1) // 2`, as mentioned earlier in the chapter.

Here is a Python function that implements this algorithm:

```python
def is_heap(arr):
    for i in range(1, len(arr)):
        parent = (i - 1) // 2
        if arr[i] > arr[parent]:
            return False
    return True
```

### Is it a max heap or a min heap?

Building on the previous idea (the algorithm given above is for a min heap), how could you determine whether a heap is a min heap or a max heap? The idea is simply to flip the comparison around. If the element is _smaller_ than its parent, return `false`.

There could be a trick involved with this question though. What does it mean if the some elements are larger than their parents and some are smaller? This could mean that it’s one of the special flavors of heap I mentioned above, or it could mean that the heap is not a heap at all.

### Convert max heap to min heap

_Given a max heap, convert it to a min heap._

This question takes a little bit of thinking about how a heap is organized. The largest value in a max heap is always at the top of the heap, but now it must be moved down to the leaves. Similarly and conversely, the smallest value in a max heap is down in the leaves, but now it must be moved to the top. Extending this logic, it’s quite possible that any number of heap values could already be exactly where they need to be.

Don't overthink it though. (Actually it was me who did the overthinking, so never mind.) It's an easy conversion once you know the trick that stems from these observations. Here is the code that converts a max heap to a min heap:

```python
def max_to_min(arr):
    needs_converting = True
    while needs_converting:
        needs_converting = False
        for i in range(1, len(arr)):
            parent = (i - 1) // 2
            if arr[i] < arr[parent]:
                arr[i], arr[parent] = arr[parent], arr[i]
                needs_converting = True
    return arr
```

### Here’s an array, make it a heap

This is a fairly straightforward thing to do. Take the elements in the array one at a time and keep swapping them until everything is in the right place. It’s fairly similar to the approach to converting a max heap to a min heap covered in the last section, in fact.

```python
def heapify(arr):
    needs_heapifying = True
    while needs_heapifying:
        needs_heapifying = False
        for i in range(1, len(arr)):
            parent = (i - 1) // 2
            if arr[i] > arr[parent]:
                arr[i], arr[parent] = arr[parent], arr[i]
                needs_heapifying = True
    return arr
```

There is also a recursive way to do this, but I want to keep things simple for now. Feel free to see if you can come up with the recursive solution on your own!

### Top k Elements in an Array

_Given an array in heap form, find the k largest (or smallest) elements in the array_

This is a perfect question for a heap, as the items are already sorted in order. In fact, the code is pretty much a one-liner:

```python
def get_k_largest(heap_array, k):
    return heap_array[:min(k, len(heap_array))]
```

If you’re a little confused by `[:min(k, len(heap_array))]`, remember from Chapter 4 that `:` is the slice operator in Python. `[:3]` is the same as `[0:3]` and will return the first three elements in a list. So this line of code says "return all of the items from the beginning of the array to which ever is smaller: k or the length of the array."

That doesn’t seem like much of an interview question does it? Of course you know how to slice an array. You read Chapter 4! So let’s look at a few of the wrinkles involved.

Wrinkle \#1: What if the array is not in heap form?

If the array is not already in heap form you’ll have to "heapify" it first, using the "heapify" method discussed above.

Wrinkle \#2: What if the array is a min heap?

If the array is a min heap, you’ll have to convert it into a max heap first, also using the code described above.

Wrinkle \#3: Instead of returning the values, how can you remove the values while keeping the rest of the array in heap form?

That’s an easy one, just use the `MaxHeapPopper` class discussed above, and call the "pop" method k times.

## Sample Interview Problems

Here are some sample interview problems that involve heaps:

### Question 1: Kth Largest Element in an Array

Find the kth largest element in an unsorted array without sorting the entire array.

**Example:**

```
Input: [3, 2, 1, 5, 6, 4], k = 2
Output: 5

Input: [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

**Solution:**

```python
import heapq

def findKthLargest(nums, k):
    # Use a min heap of size k
    # The top of the heap will be the kth largest element
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        # Keep only k largest elements
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

# Usage
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
```

**Why this works:** Instead of sorting the entire array (O(n log n)), we maintain a min heap of size k. As we iterate through the array, we keep only the k largest elements in the heap. The smallest element in this heap is the kth largest element overall.

**Time Complexity:** O(n log k) - we iterate through n elements and each heap operation takes O(log k)
**Space Complexity:** O(k) - the heap stores at most k elements

---

### Question 2: Merge k Sorted Lists

Merge k sorted linked lists into one sorted linked list.

**Example:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,1,3,4,4,5,6]
```

**Solution:**

```python
import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Min heap to store (value, list_index, node)
    # We need list_index to break ties when values are equal
    min_heap = []

    # Add the first node from each list to the heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst.val, i, lst))

    # Create a dummy node to simplify the result list
    dummy = ListNode(0)
    current = dummy

    # Process the heap
    while min_heap:
        val, idx, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        # Add the next node from the same list to the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, idx, node.next))

    return dummy.next

# Usage
# Create test lists: [1,4,5], [1,3,4], [2,6]
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

result = mergeKLists([list1, list2, list3])
# Result: 1->1->2->1->3->4->4->5->6
```

**Why this works:** A min heap allows us to always get the smallest element across all k lists in O(log k) time. We maintain a heap of the current head of each list, pop the smallest, add it to the result, and push the next node from that list.

**Time Complexity:** O(n log k) - where n is the total number of nodes across all lists, and each heap operation takes O(log k)
**Space Complexity:** O(k) - the heap stores at most k nodes at a time

---

### Question 3: Top K Frequent Elements

Given an integer array, return the k most frequent elements. You may return the answer in any order.

**Example:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [4,1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Solution:**

```python
import heapq
from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequencies using a hash map
    freq_map = Counter(nums)

    # Step 2: Use a min heap of size k
    # Store (frequency, number) tuples
    min_heap = []

    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        # Keep only k most frequent elements
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Extract elements from the heap
    result = []
    while min_heap:
        freq, num = heapq.heappop(min_heap)
        result.append(num)

    return result

# Usage
print(topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print(topKFrequent([4,1,1,1,2,2,3], 2))  # [1,2]
```

**Why this works:** This combines a hash map (to count frequencies) with a min heap (to find the k most frequent). The heap stores only k elements, so we don't need to sort all unique elements.

**Time Complexity:** O(n + m log k) - where n is the number of elements and m is the number of unique elements. Counting takes O(n), and heap operations take O(m log k)
**Space Complexity:** O(m) - for the hash map storing frequencies, and O(k) for the heap

---

### Question 4: Find Median from Data Stream

Design a data structure that supports adding integers from a data stream and finding the median at any time.

**Example:**

```
addNum(1)
addNum(2)
findMedian() -> 1.5

addNum(3)
findMedian() -> 2.0
```

**Solution:**

```python
import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for the smaller half (use negative values)
        self.small = []
        # Min heap for the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to max heap (small) first
        heapq.heappush(self.small, -num)

        # Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the heaps (small should have at most 1 more element)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

# Usage
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())  # 1.5

mf.addNum(3)
print(mf.findMedian())  # 2.0
```

**Why this works:** We use two heaps to partition the data stream into two halves. The max heap (small) stores the smaller half, and the min heap (large) stores the larger half. This allows us to find the median in O(1) time.

**Time Complexity:** O(log n) for addNum, O(1) for findMedian
**Space Complexity:** O(n) - storing all numbers across both heaps
