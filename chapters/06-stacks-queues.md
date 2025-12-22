# Stacks and Queues

Building on the concept of linked lists explored in Chapter 5, we can now move on to two more advanced and widely used data structures: stacks and queues. By the end of this chapter you will understand the difference between the two, the applications of each, how to implement them both from their native versions and in code and how to answer interview questions about them.

Stacks and queues are two kinds of data structures that keep things in a certain order. They are both similar to arrays, but with a few key differences. In an array, you can add things pretty much wherever you want. In stacks and queues you only add things to one end or the other, and usually always from the same end.

## FIFO and LIFO

FIFO and LIFO stand for "first in, first out" and "last in, first out," two concepts that describe the primary difference between each data structure.

The queue is a FIFO data structure, meaning that the first element added to the queue is the first one to be removed. Think of people waiting in line at a grocery store. Assuming no one rude comes along, the first person in line at a grocery store is the first person to be checked out.

The stack is a LIFO data structure that works the opposite way. In a stack the last element added to the stack is the first one to be removed. You can think of a stack like a stack of pancakes. All of the pancakes in a stack of pancakes are one on top of the other, and the last pancake added to the stack is the first one to be eaten.

<Diagram of a stack and a queue TK\>

This might seem like a trivial difference, but it turns out to have tremendous implications depending on the problem you’re trying to solve.

## PUSH and POP

When dealing with stacks and queues, there are specific terms used to describing adding things to and removing them from the data structure. Generally, adding something to a stack or queue is called _pushing_ and removing something is called _popping_.  
You also have to consider whether the data is added to the beginning or the end of the list.  
These two considerations combined are what make a data structure FIFO or LIFO.  
Pushing and popping may have other names like "enqueue" or "append" or "dequeue" or "shift."  
Some commands will return a value from a list without removing it from the list as well.
These differences mostly have to do with the specific language and implementation of the data structure, but the concepts are the same.
Please make sure you keep these subtle differences in mind as you read through this chapter.

\<Diagram of push and pop TK\>

So let’s say we have a simple stack of integers, which looks like this:

If I _push_ the number 4 onto the stack, it will look like this:

If I _pop_ the stack twice, we will remove the 4 and the 7 and it will look like this:

Some operations will return the value that was popped, while others will not.

I’m going to start by looking the built-in Python list, which can be used as a stack or a queue.

```python
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

I then pushed the numbers 5, 3, 2, 8, 7, and 4 onto the stack, using the built-in Python `append` method. Next I popped the stack twice, which removes the last two elements from the stack, and returns them to the `print` function. Finally, I print the stack to show its contents, which now contain the numbers 5, 3, and 2.

Let’s do the same thing using a list as a queue.

```python
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
```

This will output:

    5
    3
    [2, 8, 7, 4]

If you notice I’m doing essentially the same thing I did with the stack, but in the case of the queue I’m using the `pop` method with an argument of `0` to remove the first element from the list. The only difference between the two is how the items are being removed from the list. Are the items on the left side of the list being removed first `pop(0)`, or the right side `pop()`? That’s a highly contrived example, but it serves to illustrate the general idea.

The built-in Python list is not the most efficient way to implement a stack or a queue, but it is the most straightforward. The Python `collections` module has a `deque` class that is more efficient for queues, and the `queue` module has a `LifoQueue` class that is more efficient for stacks. By more "efficient" I mean that they are faster (from $O(n)$ with pop(0) to $O(1)$ deque.popleft()) and use less memory (space) than the same operations used above. This won’t matter if you’ve only got a few items as in the above example, but when dealing with considerable amounts of data, it can make a big difference.

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

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
```

This might seem like doing more work than is needed, especially since there’s nothing here you can’t already do with a list, but it’s good to understand this kind of basic implementation.

So what’s here? There’s in _init_ method that initializes the stack with an empty list, waiting to be filled. There are two methods, `push` and `pop`, that add and remove items from the stack. What’s missing? Again, think about it for a moment.

One thing that’s missing is a method to check if the stack is empty. This is a big deal because if you try to pop an empty list your program will throw `IndexError: pop from empty list`. There are a few ways this can be addressed, but it’s as easy as adding an `is_empty` method to the class.

```python
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
```

Knowing how to implement a stack really helps see what’s going on in the Python list implementation. You can also easily extend this basic idea to add other methods, like `peek`, `size`, or `clear`. You can have a stack size limit by including a method to see if the stack is full. You can also add data-checking to allow only certain types of data into the stack. This very basic implementation gives access to a wide range of possibilities.

For instance, how can you use what you know about a stack to implement a queue? You can start with the basic stack class provided, but you’ll have to replace "push" and "pop" with "enqueue" and "dequeue" methods which will work a little differently.

```python
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

Stacks and queues are often used to indicate _priority_ in the processing of data. It’s not hard to see why. Imagine an elevator that only goes to two floors, say the ground floor and the 10th floor. Ten people enter the elevator on the ground floor. Because of the way elevators — and society — are constructed, the last people to board the elevator will be the first ones to leave it. The elevator creates a priority by the way it is boarded. It’s simply impossible for the people who first board the elevator to exit first, as they will be furthest from the door. This is an example of a stack.

A queue is even easier to understand. We’ve all waited in line. It even seems "unfair" for people to cut in line; the first in must be the first out!

There are, of course, exceptions to these rules. Pause for a moment and try to think of a real-world exception to each.

There are a few ways to use stacks and queues in computer science, but most often they are used for assigning priority to tasks. They can be used to determine the priority of packets in a network or to determine tasks that must be completed before other tasks begin.

Is a for loop an example of a stack or a queue? What about a nested for loop? What about the browser event loop?

## Priority Queues

A priority queue is a data structure that is a combination of a queue and a heap which I’ll talk about in the next chapter. In addition to having a FIFO order, a priority queue also has a priority order. You can think of a priority queue like people in the Emergency Room at the hospital. During intake, patients are assigned a priority based on the severity of their condition. People who arrive in ambulances get to go to the front of the line, regardless of when they arrive. People who walk in the door with severe pain will be seen sooner than people who lost a Q-Tip in their ear. An order is still maintained though. The people who walk in with the in-ear Q-Tip first will be seen by the people who walk in with the in-ear Q-Tip later.

There are many ways to implement a priority queue, but one simplistic way to do it is to use a nested array (or Python list) where the first element is the priority and the second element is the data.

```python
priority_queue = []
priority_queue.append([3, "low priority item"])
priority_queue.append([1, "high priority item"])
priority_queue.append([2, "medium priority item"])
```

In this example, the high priority item will be removed first, followed by the medium priority item, and finally the low priority item. This might lead you to wonder what the point is of using a queue at all, since we’re not following the FIFO order? Imagine this being a much larger set of data, like a network across which data packets are sent. This network might contain three levels of priority, but thousands, or even millions of packets. Assigning one of three priorities to each of these packets allows for more important packets like packets containing text to be sent before less important packages like packets containing images. You may have even been on a slow network and notice that text loads before images, or added priority to an image as a web developer to make sure it’s loaded no matter what. This allows programmers to impose at least a little bit of order on the chaos of all of the data flying hither and yon down the information superhighway.

### Permutations, revisited

Back in Chapter 4 we discussed permutations, and I showed you a simple iterative solution for coming up with all the combinations of a set of items in an array.

Now that we’ve discussed stacks and queues, I’d like to show you how you can use a stack to more effectively solve the permutations problem:

```python
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

Back in the days before all of the wonderful IDEs that are available for free today, programmers had to write code in terminals or very simple text editors. If you’ve ever used `vim` or `emacs`, you know that they are not very good at telling you when you’ve made a mistake. Additionally, try writing some code in something like NotePad++ and you’ll seriously wonder how programmers ever got anything done.

One very typical mistake that was easy to make in those days was to lose track of parentheses. In a complicated parenthetical expression, it was easy to either forget to close an open parenthesis, or to add an extra one at the end. I was once working on a long program that would not compile and I ended up printing out the entire program and marking the parentheses with a highlighter to find my mistake. Now the editor will just highlight the matching parenthesis for you, or just go ahead and fix them without your even noticing.

It’s not magic that balances those parenthesis in your code editor though, it’s a stack. Specifically, it’s a stack of open parentheses. Every time you open a parenthesis, you push it onto the stack. Every time you close a parenthesis, you pop it off the stack.

If you finish with parenthesis still on the stack, you know you’ve forgotten to close something somewhere. If you try to pop a parenthesis off of an empty stack, you know you’re trying to close something that was never opened. If you end up with an empty stack, no more and no less, you can rest assured that your parentheses are balanced.

```python
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

Can you generalize this example to other types of brackets? How can it be used to check not only parentheses `()`, but also brackets `[]` and curly-braces `{}`? Once you’ve got them properly "balanced", with the same numbers of openers and closers, how can you check that they are properly nested — brackets opened first are closed first? The full solution is left as an exercise in the Example Interview Questions section.

> **The Terminal**
>
> This may be another one of my unpopular opinions, but I’m always truly amazed when I find a programmer who doesn’t know how to use a command-line terminal, and doesn’t seem to care. It’s not used anywhere near as much as it used to be (I once used to check my email in the terminal), but it’s still an absolutely necessary thing to know. While you certainly don’t have to read the Unix MAN pages from beginning to end or become a VIM ninja, any programmer should know how to navigate through a file system, create and delete files and directories, and run programs from the command line. It’s invaluable for not having to "context switch" between your editor and your terminal, and using it will give you lots of really, really boring stories to tell your grandkids. Also: it will absolutely make you a better programmer.

## Example Interview Questions

While stacks and queues might seem simple, they're the foundation for many common interview problems. Here are four questions that you might see in an interview:

### Question 1: Valid Parentheses (Generalized)

Write a function that determines if a string containing parentheses `()`, brackets `[]`, and braces `{}` is valid. A string is valid if:

- Every opening bracket has a corresponding closing bracket of the same type
- Brackets are closed in the correct order
- Every closing bracket has a corresponding opening bracket of the same type

**Example:**

```
Input: "({[]})"
Output: True

Input: "([)]"
Output: False (brackets are not properly nested)

Input: "((("
Output: False (missing closing brackets)
```

**Solution:**

```python
def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        elif char in pairs.values():  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

# Usage
print(is_valid("({[]})"))  # True
print(is_valid("([)]"))    # False
print(is_valid("((("))     # False
```

This code uses a stack to track opening brackets. When it encounters a closing bracket, it checks if it matches the most recent opening bracket (top of stack). If the stack is empty at the end, all brackets were properly matched and nested.

**Time Complexity:** O(n) - iterate through the string once
**Space Complexity:** O(n) - worst case, all opening brackets go on the stack

### Question 2: Min Stack

Design a stack that supports push, pop, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `push(val)` - pushes the element val onto the stack
- `pop()` - removes the element on the top of the stack
- `top()` - gets the top element of the stack
- `get_min()` - retrieves the minimum element in the stack

All operations must run in O(1) time.

**Example:**

```
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)
stack.get_min()  # Returns 1
stack.pop()
stack.get_min()  # Returns 2
```

**Solution:**

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # Push to min_stack if it's empty or val is <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        # If popped value was the min, pop from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# Usage
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)
print(stack.get_min())  # 1
stack.pop()
print(stack.get_min())  # 2
```

**Why this works:** This code maintains two stacks - one for all values and one that only tracks minimums. The min_stack always has the current minimum at the top. New minimums are pushed onto `min_stack`. Current minimums, can be popped off the `min_stack`.

**Time Complexity:** O(1) for all operations
**Space Complexity:** O(n) - in worst case (descending order), min_stack has all elements

### Question 3: Implement Queue Using Two Stacks

Implement a queue using only two stacks. The queue should support:

- `enqueue(x)` - add element to the back of the queue
- `dequeue()` - remove element from the front of the queue
- `peek()` - get the front element without removing it
- `is_empty()` - check if the queue is empty

**Example:**

```
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()  # Returns 1
queue.peek()     # Returns 2
```

**Solution:**

```python
class QueueWithStacks:
    def __init__(self):
        self.stack_in = []   # For enqueue operations
        self.stack_out = []  # For dequeue operations

    def enqueue(self, x):
        self.stack_in.append(x)

    def dequeue(self):
        self._move_if_needed()
        if not self.stack_out:
            return None
        return self.stack_out.pop()

    def peek(self):
        self._move_if_needed()
        if not self.stack_out:
            return None
        return self.stack_out[-1]

    def is_empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def _move_if_needed(self):
        # Only move elements when stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

# Usage
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.peek())     # 2
```

**Why this works:** This code used one stack for incoming elements and another for outgoing. To dequeue, it transfers all elements from `stack_in` to `stack_out` (reversing their order). This makes the oldest element end up on top of `stack_out`. The code only transfers when `stack_out` is empty, making the operation amortized O(1).

**Time Complexity:**

- Enqueue: O(1)
- Dequeue/Peek: O(1) amortized (occasionally O(n) when transferring, but each element is moved at most once)

**Space Complexity:** O(n) - storing n elements across two stacks

### Question 4: Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

In RPN, operators follow their operands. For example, `3 4 +` means `3 + 4`.

**Example:**

```
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6 (integer division)
```

**Solution:**

```python
def eval_rpn(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            # Pop two operands (note the order!)
            b = stack.pop()
            a = stack.pop()

            # Perform operation
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                # Python 3 division truncates toward zero
                result = int(a / b)

            stack.append(result)
        else:
            # It's a number, push it onto the stack
            stack.append(int(token))

    return stack[0]

# Usage
print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6
```

**Why this works:** RPN is designed for stack-based evaluation. This code pushes numbers onto the stack, and when it encounters an operator, it pops the required operands, performs the operation, and pushes the result back. The final result is the only element left on the stack.

**Time Complexity:** O(n) - process each token once
**Space Complexity:** O(n) - worst case, all tokens are numbers pushed onto the stack

## Exercises

Now that you've seen some common patterns, try these exercises to deepen your understanding:

1. **Find items in order in a stack:** Using an implementation of the basic stack class already discussed, create an algorithm that returns all of the items of a stack in order, without changing the stack itself. For instance, if you have a stack with the items [2, 5, 1, 4, 3], the algorithm should return [1, 2, 3, 4, 5] without modifying the original stack. You should only need to add a "peek" method to the basic stack class provided to accomplish this.

2. **String operations with stacks:** Can you think of how to use a stack to reverse a string? A palindrome checking question was given in Chapter 3. Can you think of a way to use a stack to check if a string is a palindrome?

3. **Implement a priority queue:** Earlier I gave a description of a priority queue. Try mixing together a stack and a queue to create a priority queue.

4. **Implement a stack using queues:** If you can implement a queue using two stacks, can you implement a stack using two queues? What are the trade-offs?

5. **Next Greater Element:** Given an array of integers, for each element find the next greater element to its right. If no greater element exists, return -1. For example, [4, 5, 2, 10] returns [5, 10, 10, -1]. Can you solve this using a stack?

## Big O Analysis of Stack and Queue Operations

Understanding the time complexity of stack and queue operations is crucial for interview success:

| Operation    | Stack (list) | Stack (deque) | Queue (list) | Queue (deque) |
| ------------ | ------------ | ------------- | ------------ | ------------- |
| Push/Enqueue | O(1)         | O(1)          | O(1)         | O(1)          |
| Pop/Dequeue  | O(1)         | O(1)          | O(n)\*       | O(1)          |
| Peek/Top     | O(1)         | O(1)          | O(1)         | O(1)          |
| Is Empty     | O(1)         | O(1)          | O(1)         | O(1)          |
| Search       | O(n)         | O(n)          | O(n)         | O(n)          |

\* Using `pop(0)` on a Python list requires shifting all remaining elements, making it O(n)

### Choosing the Right Data Structure

**Choosing a Stack:**

- LIFO ordering is needed
- Recursion is implemented iteratively
- Expressions are parsed (parentheses matching, RPN)
- Undo/redo functionality is implemented
- Backtracking algorithms are used

**Choosing a Queue:**

- FIFO ordering is needed
- Breadth-first search (BFS) algorithms are used
- Tasks are scheduled
- Print jobs are managed
- Asynchronous requests are handled

**Choosing a Deque:**

- Efficient operations on both ends are needed
- A queue is implemented in Python (use `collections.deque`)
- Sliding window problems are solved
- Palindromes are checked

**Key Interview Insight:** In Python, preferably use the optimized `collections.deque` for queue implementations. Using `list.pop(0)` is a common mistake that results in O(n) performance instead of O(1).

## AI Exercise

Now that you've learned about stacks and queues, use an AI assistant to build a **Text Editor with Undo/Redo Functionality**.

Your text editor should support:

1. **Type text** - Add characters to the document
2. **Undo** - Revert the last change
3. **Redo** - Reapply an undone change
4. **Display current text** - Show the current state of the document

**Implementation requirements:**

- Use two stacks: one for undo history and one for redo history
- Each "action" should be stored as a state or command
- Typing new text after an undo should clear the redo stack

**Questions to explore with your AI:**

- How do you represent each action/state?
- What happens to the redo stack when you type after an undo?
- How would you extend this to support more complex operations (cut, paste, formatting)?
- What are the memory trade-offs of storing full states vs. storing commands?
- How do real text editors (like VS Code) implement undo/redo?

**Bonus challenges:**

- Add a maximum undo history size
- Implement "undo groups" (multiple characters typed quickly count as one undo)
- Add support for cut/copy/paste operations
- Implement a "save point" feature that marks the current state

As you work through this, pay attention to how the AI suggests handling edge cases (empty undo stack, redo after new typing) and ask it to explain the Big O complexity of each operation.
