# Stacks and Queues

Building on the concept of linked lists explored in Chapter 5, we can now move on to two more advanced and widely used data structures: stacks and queues. By the end of this chapter you will understand the difference between the two, the applications of each, how to implement them both from their native versions and in code and how to answer questions about them in interviews.

Stacks and queues are two kinds of data structures that keep things in a certain order. They are both similar to arrays, but with a few key differences. In an array, you can add things pretty much wherever you want. In stacks and queues you only add things to one end or the other, and usually always from the same end.

## FIFO and LIFO

FIFO and LIFO stand for "first in, first out" and "last in, first out," two concepts that describe the primary difference between each data structure.

The queue is a FIFO data structure, meaning that the first element added to the queue is the first one to be removed. Think of people waiting in line at a grocery store. Assuming no one rude comes along, the first person in line at a grocery store is the first person to be checked out.

The stack is a LIFO data structure that works the opposite way. In a stack the last element added to the stack is the first one to be removed. You can think of a stack like a stack of pancakes. All of the pancakes in a stack of pancakes are one on top of the other, and the last pancake added to the stack is the first one to be eaten.

\<Diagram of a stack and a queue TK\>

This might seem like a trivial difference, but it turns out to have tremendous implications depending on the problem you’re trying to solve.

## PUSH and POP

When dealing with stacks and queues, there are specific terms used to describing adding things too and removing them from the data structure. Generally, adding something to a stack or queue is called *pushing* and removing something is called *popping*.

\<Diagram of push and pop TK\>

So let’s say we have a simple stack of integers, which looks like this:

If I *push* the number 4 onto the stack, it will look like this:

If I *pop* the stack twice, we will remove the 4 and the 7 and it will look like this:

Some operations will return the value that was popped, while others will not.

I’m going to start by looking the built-in Python list, which can be used as a stack or a queue.

``` python
stack = []
stack.append(5)
stack.append(3)
stack.append(2)
stack.append(8)
stack.append(7)
stack.append(4)

print(stack.pop())
print(stack.pop())
print(stack)
```

This will output:

    4
    7
    [5, 3, 2, 8]

Let’s go over this line by line. I begin with an empty list as a stack, which I name "stack." I could have named it anything; there is nothing special about the name. I only used it to illustrate that I am using the list as a stack.

I then \_push_ed the numbers 5, 3, 2, 8, 7, and 4 onto the stack, using the built-in Python `append` method. Next I \_pop_ed the stack twice, which removes the last two elements from the stack, and returns them to the `print` function. Finally, I print the stack to show it’s contents, which now contain the numbers 5, 3, and 2.

Let’s do the same thing using a list as a queue.

``` python
queue = []
queue.append(5)
queue.append(3)
queue.append(2)
queue.append(8)
queue.append(7)
queue.append(4)

print(queue.pop(0))
print(queue.pop(0))
print(queue)
```python

This will output:

    5
    3
    [2, 8, 7, 4]

If you notice I’m doing essentially the same thing I did with the stack, but in the case of the queue I’m using the `pop` method with an argument of `0` to remove the first element from the list. The only difference between the two is how the items are being removed from the list. Are the items on the left side of the list being removed first `pop(0)`, or the right side `pop()`? That’s a highly contrived example, but it serves to illustrate the general idea.

The built-in Python list is not the most efficient way to implement a stack or a queue, but it is the most straightforward. The Python `collections` module has a `deque` class that is more efficient for queues, and the `queue` module has a `LifoQueue` class that is more efficient for stacks. By more "efficient" I mean that they are faster and use less memory than the same operations used above. This won’t matter if you’ve only got a few items as in the above example, but when dealing with considerable amounts of data, it can make a big difference.

In JavaScript you have even more options, as there are no built-in stack or queue classes. Instead you can use the `push` and `pop` methods of an array to implement a stack, and the `shift` and `unshift` methods to implement a queue.

Play around with these methods a bit to get a feel for how they work. You can even open a Python instance in your terminal or JavaScript console in your browser and try them out there.

> **Think about it:**
>
> Why are we only interested in FIFO and LIFO, and not FILO (first-in-last-out) or LILO?
>
> Some (mostly older) programming languages also have a method called PEEK, which allows you to look at the first/top element of a queue or stack without removing it. Why might you want to do this?

## Implementing stacks and queues

So far I’ve used list operations to describe stack functionality, but you might be asked in an interview to implement a stack from scratch. Before I show how to do that, I’m going to do the same old boring teacher thing (eye roll, please) and beg you to think about it on your own. If we create a custom "stack" class, what data and methods does it need to contain? What about a queue? Can a stack be implemented as a linked list? Can a queue be implemented as a stack?

While there is more than one way to solve the problem, this is certainly the bare minimum that you would need to implement a stack:

``` python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
            return self.items.pop()
```

This might seem like doing more work than is needed, especially since there’s nothing here you can’t already do with a list, but it’s good to understand this kind of basic implementation.

So what’s here? There’s in *init* method that initializes the stack with an empty list, waiting to be filled. There are two methods, `push` and `pop`, that add and remove items from the stack. What’s missing? Again, think about it for a moment.

One thing that’s missing is a method to check if the stack is empty. This is a big deal because if you try to pop an empty list your program will throw `IndexError: pop from empty list`. There are a few ways this can be addressed, but it’s as easy as adding an `is_empty` method to the class.

``` python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0
```python

Knowing how to implement a stack really helps see what’s going on in the Python list implementation. You can also easily extend this basic idea to add other methods, like `peek`, `size`, or `clear`. You can have a stack size limit by including a method to see if the stack is full. You can also add data-checking to allow only certain types of data into the stack. This very basic implementation gives access to a wide range of possibilities.

For instance, how can you use what you know about a stack to implement a queue? You can start with the basic stack class provided, but you’ll have to replace "push" and "pop" with "enqueue" and "dequeue" methods which will work a little differently.

``` python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0
```

Same basic functions, but they add and remove data to the `items` list in a different order than a stack.

## Developing Intuition: What are stacks and queues used for?

Stacks and queues are often used to indicate *priority* in the processing of data. It’s not hard to see why. Imagine an elevator that only goes to two floors, say the ground floor and the 10th floor. Ten people enter the elevator on the ground floor. Because of the way elevators — and society — are constructed, the last people to board the elevator will be the first ones to leave it. The elevator creates a priority by the way it is boarded. It’s simply impossible for the people who first board the elevator to exit first, as they will be furthest from the door. This is an example of a stack.

A queue is even easier to understand. We’ve all waited in line. It even seems "unfair" for people to cut in line; the first in must be the first out!

There are, of course, exceptions to these rules. Pause for a moment and try to think of a real-world exception to each.

There are a few ways to use stacks and queues in computer science, but most often they are used for assigning priority to tasks. They can be used to determine the priority of packets in a network or to determine tasks that must be completed before other tasks begin.

Is a for loop an example of a stack or a queue? What about a nested for loop? What about the browser event loop?

## Priority Queues

A priority queue is a data structure that is a combination of a queue and a heap which I’ll talk about in the next chapter. In addition to having a FIFO order, a priority queue also has a priority order. You can think of a priority queue like people in the Emergency Room at the hospital. During intake, patients are assigned a priority based on the severity of their condition. People who arrive in ambulances get to go to the front of the line, regardless of when they arrive. People who walk in the door with severe pain will be seen sooner than people who lost a Q-Tip in their ear. An order is still maintained though. The people who walk in with the in-ear Q-Tip first will be seen by the people who walk in with the in-ear Q-Tip later.

There are many ways to implement a priority queue, but one simplistic way to do it is to use a nested array (or Python list) where the first element is the priority and the second element is the data.

``` python
priority_queue = []
priority_queue.append([3, "low priority item"])
priority_queue.append([1, "high priority item"])
priority_queue.append([2, "medium priority item"])
```

In this example, the high priority item will be removed first, followed by the medium priority item, and finally the low priority item. This might lead you to wonder what the point is of using a queue at all, since we’re not following the FIFO order? Imagine this being a much larger set of data, like a network across which data packets are sent. This network might contain three levels of priority, but thousands, or even millions of packets. Assigning one of three priorities to each of these packets allows for more important packets like packets containing text to be sent before less important packages like packets containing images. You may have even been on a slow network and notice that text loads before images, or added priority to an image as a web developer to make sure it’s loaded no matter what. This allows programmers to impose at least a little bit of order on the chaos of all of the data flying hither and yon down the information superhighway.

## Example Questions

### Permutations, revisited

Back in Chapter 4 we discussed permutations, and I showed you a simple iterative solution for coming up with all the combinations of a set of items in an array.

Now that we’ve discussed stacks and queues, I’d like to show you how you can use a stack to more effectively solve the permutations problem:

``` python
def permute(arr):
    result = []
    stack = [(arr, [])]

    while stack:
        arr, path = stack.pop()
        if not arr:
            result.append(path)
        else:
            for i in range(len(arr)):
                stack.append((arr[:i] + arr[i+1:], path + [arr[i]]))

    return result

animals = ["lion", "tiger", "bear", "dog", "guppy"]
permutations = permute(animals)

for perm in permutations:
    print(perm)
```

### Balanced parentheses

Back in the days before all of the wonderful IDE’s that are available for free today, programmers had to write code in terminals or very simple text editors. If you’ve ever used `vim` or `emacs`, you know that they are not very good at telling you when you’ve made a mistake. Additionally, try writing some code in something like NotePad++ and you’ll seriously wonder how programmers ever got anything done.

One very typical mistake that was easy to make in those days was to lose track of parentheses. In a complicated parenthetical expression, it was easy to either forget to close an open parenthesis, or to add an extra one at the end. I was once working on a long program that would not compile and I ended up printing out the entire program and marking the parentheses with a highlighter to find my mistake. Now the editor will just highlight the matching parenthesis for you, or just go ahead a fix them without your even noticing.

It’s not magic that balances those parenthesis in your code editor though, it’s a stack. Specifically, it’s a stack of open parentheses. Every time you open a parenthesis, you push it onto the stack. Every time you close a parenthesis, you pop if off the stack.

If you finish with parenthesis still on the stack, you know you’ve forgotten to close something somewhere. If you try to pop a parenthesis off of an empty stack, you know you’re trying to close something that was never opened. If you end up with an empty stack, no more and no less, you can rest assured that your parentheses are balanced.

``` python
def is_balanced(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

# Usage
print(is_balanced("((()))")) # True
print(is_balanced("(()))")) # False
```

Can you generalize this example to other types of brackets? How can it be used to check not only parentheses `()`, but also brackets `[]` and curly-braces `{}`? Once you’ve got them properly "balanced", with the same numbers of openers and closers, how can you check that they are properly nested — brackets opened first are closed first?

> **The Terminal**
>
> This may be another one of my unpopular opinions, but I’m always truly amazed when I find a programmer who doesn’t know how to use a command-line terminal, and doesn’t seem to care. It’s not used anywhere near as much as it used to be (I once used to check my email in the terminal), but it’s still an absolutely necessary thing to know. While you certainly don’t have to read the Unix MAN pages from beginning to end or become a VIM ninja, any programmer should know how to navigate through a file system, create and delete files and directories, and run programs from the command line. It’s invaluable for not having to "context switch" between your editor and your terminal, and using it will give you lots of really, really boring stories to tell your grandkids. Also: it will absolutely make you a better programmer.

### Find items in order in a stack

Using an implementation of the basic stack class already discussed, create an algorithm that returns all of the items of a stack in order, without changing the stack itself. For instance, if you have a stack with the items \[2, 5, 1, 4, 3\], the algorithm should return \[1, 2, 3, 4, 5\] without modifying the original stack. You should only need to add a "peek" method to the basic stack class provided to accomplish this.

### Implement a queue using two stacks

Earlier in this chapter I suggested modifying the basic stack class to implement a queue. But a queue can also be implemented using two stacks. Can you think of what this would look like? It doesn’t need to be coded. Consider just drawing it out on paper, with a list of the methods required to accomplish the task. Again, you will only need to add a "peek" method to the basic stack class to accomplish this.

### String operations with stacks

This chapter may have suggested to you some way in which stacks can be used to manipulate strings. Can you think of how to use a stack to reverse a string? A palindrome checking question was given in Chapter 3. Can you think of a way to use a stack to check if a string is a palindrome?

### Implement a priority queue

Earlier I gave a description of a priority queue. Try mixing together a stack and a queue to create a priority queue.

### Using AI to think about Stacks and Queues

Now that you’ve (hopefully) used the code in this chapter to implement stacks and queues from scratch, consider going back and using the Python standard methods (`push()`, `pop()`, `peek()`, etc.) as well as the collections.deque and queue.LifoQueue classes to rebuild the examples in this chapter. Use AI to determine the advantages and disadvantages of each approach. Which runs faster? Which use more memory? Which is the most efficient? Which form is the most readable? Are there other reasons why you might prefer one approach over another? AI can help you reason through these questions, which will provide you with an understanding you can draw on should you be asked about them in an interview.
