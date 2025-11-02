# Linked Lists

This chapter is an "in-between" chapter as we turn from the simple, one-dimensional data structures most languages already provide us to the more complex, multi-part, multi dimensional data structures. These data structures allow you to both tackle more complex problems as well as allowing you to tackle simpler problems in more efficient ways.

I will start with a quick review of pointers, and then we’ll see how pointers can be used to build a data structure called a linked list. Then I’ll move on to talking a bit about object-oriented programming in Python, and how classes and objects can be used to build linked lists. We’ll also talk about what linked lists can be used for and the types of problems they can be used to solve. Linked lists are a gateway data structure, as the concepts you learn in building linked lists are common to many other more advanced data structures. Pointers and classes are also foundational concepts in algorithms and data structures, so try to pay attention to the overall concepts, much like I asked you to focus on the "shapes" of the graphs of Big O notation in chapter 2.

From my own experience, I can tell you this is where a lot of programmers start to lose interest. This can seem like an abstruse concept that you’ll never have any use for in the real world. Well you might not, but because, again, they build a strong foundation for more advanced concepts, I suggest hanging in there until the end of this chapter. Slow down and take your time with any concepts you don’t understand. Type in the code examples an run them, and try to answer all of the end-of-chapter exercises. I promise you, it will be worth it.

## Pointers Refresher

As mentioned in Chapter 4, pointers "point" to objects stored in memory. They do so by storing the memory address of the object they point to. Pointers are a powerful tool in programming, but they can be a bit tricky to work with and understand.

A pointer is like a sign post on a road. A sign with a gas tank on it and an arrow pointing to the right can be used to indicate that the nearest gas station is in that direction. Notice that the sign is not the gas station, or the gas, or even the direction, but simply a representative indication of these concepts.

\<diagram of pointers TK\>

While pointer manipulation is definitely something to worry about in programming languages that directly manipulate a computers memory, like C or :cpp:, languages like Python and Javascript take care of memory management on their own, and so pointer manipulation is not something you have to worry about. In this chapter, like in the last chapter, I’m using the term "pointer" to refer to a reference to an object in memory. Linked lists are so called because they are comprised of a list of "nodes" that are "linked" to one another by references. Print out the `next` attribute of a node, and you’ll see something like `<main.Node object at 0x7f8e3c7b4b50>`. This is the memory address of the next node in the list. You don’t have to account for this, you don’t have to reference this, you don’t have to store this or manage this, but it’s good to understand that this is what’s going on behind the scenes in Python.

## Python Classes and Objects

This book is not going to get into the details of object-oriented programming, but you should have a basic understanding of classes and objects in Python if you want to be a Python programmer. Even though its popularity has faded over the last decade or so, it’s a good idea to have at least a general understanding of the object-oriented programming paradigm.

In object-oriented programming (and all of its myriad derivatives and variations), you define classes that are like blueprints for objects. A class "describes" an object, and each object created is an instance of a class. In other words, a class might be thought of as a blueprint for a house, and an object as the house (or houses) that are built from that blueprint.

Classes primarily contain two things: data and methods. Data is the information stored in the object, and that the object uses to do its work within the program. Methods are functions that are defined within the class and can be called on in order to do work on the data.

Keeping with the house analogy, the data might be the number of rooms in the house, the names of the people who live there, the color of the walls, the amount of electricity used each month, etc. The methods might be things like "turn on the lights," "open the garage door," "flush the toilet," etc.

That’s an incredibly simplistic view of object-oriented programming, but keep it in mind as you go through this chapter. From this simple idea entire systems of thought have arisen, and while this book will not go too much further than the basic idea of classes and objects, methods and data, if you’re interested in a deeper dive into object-oriented programming, there are many resources available to you.

Let’s look at one more example in code. Let’s say we want to define a class called *Dog* that has a name, age, and breed. The dog can do three things: eat, sit, and speak.

Here’s what that might look like in Python:

``` python
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def eat(self):
        # Do something that programmatically represents eating
        print(f"{self.name} is eating.")

    def sit(self):
        # Do something that programmatically represents sitting
        print(f"{self.name} is sitting.")

    def speak(self, sound):
        # Do something that programmatically represents barking
       if sound == "talk":
           print(f"{self.name} says 'I am a {self.breed} and I am {self.age} years old.'")
       else:
           print(f"{self.name} says 'Woof!'")
```python

Now that the dog class has been defined, we can create as many dogs as we want by "instantiating" the class into an object and asking each object to do things. Notice that, once create, each dog object contains its **own** data and methods that are independent of all of the other dogs' data and methods. This gives you some idea of the power of object-oriented programming.

``` python
dog1 = Dog("Penny", 3, "Poodle")
dog2 = Dog("Ellie", 7, "Skye Terrier")
dog3 = Dog("Cinder", 2, "Black Lab")

dog1.eat()
# outputs "Penny is eating."

dog2.sit()
# outputs "Ellie is sitting."

dog1.speak("bark")
# outputs "Penny says 'Woof!'"

dog3.speak("talk")
# outputs "Cinder says 'I am a Black Lab and I am 2 years old.'"

dog3.speak("bark")
# outputs "Cinder says 'Woof!'"
```python

Notice the use of the `self` keyword in the methods of the class. `self` can be thought of as a way in which an object refers to itself, as opposed to other object methods, object data, or other objects of the same class. `self` is defined and used a little bit differently in different languages, but in Python, it is always the first argument to a method in a class definition. It might also be called "this" or "me" in other languages, but same basic principle applies. Think about self like this: You have a name, and everyone refers to you by that name, but you (and everyone else) refer to yourself as "me" or "I." You can say "Can you help me figure this out?" to someone else, but you say "I need to figure this out mySELF" to yourself. `self` helps with the ambiguity of functions that might be available to the program as a whole, vs. functions that are kept separate within a given object.

*init* is a special method in Python that is called one time when a new object is created from a class. This is sometimes called a "constructor" method in other languages. It’s a special method that each class can contain that can be used to set up data the object needs upon creation. In the case of the Dog class, the *init* method is used to set the name, age, and breed of the dog that are passed to the dog object when it is created.

Again, this is an *incredibly* simplistic view of object-oriented programming, but it should be enough to get you through this chapter.

## The Basics of Linked Lists

A linked list is a data structure where data is stored in "nodes." Each node contains two things, a data element, and a pointer reference to the next node in the list. The data can be pretty much anything, but obviously some things make more sense than others.

Storing every word in a sentence in text as a linked list would probably not make much sense, for example, given that you can more easily do that with a string. If you had to store a list of names, however, and maybe keep it in sorted order, now a linked list can be a useful thing to have on hand.

The last node in the list points to *null* or a *null reference* which indicates the end of the list has been reached.

\<Picture of a linked list TK\>

Thinking about this in terms of object oriented programming, you can think of a linked list as a series of objects, each of which contains a data element and a reference (pointer) to the next object in the list.

## Linked List Nodes

Let’s start with the definition of a linked list node class in Python:

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```python

This is a simple class that defines a node in a linked list Here is how you can use this class to create a simple linked list with three nodes:

``` python
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)

node1.next = node2
node2.next = node3
```python

In this example, we create three node objects, each created from the `Node` class with a data element and a pointer to the next node in the list. Having an object representing each element of data is a pattern we’ll see often as we continue to dig into data structures.

Having created each of the nodes with its accompanying data, we then set the `next` pointer of each node to the next node in the list. It’s not necessary to set the `next` pointer of the last node in the list to `None`, as it is already set to `None` in the `init` method of the `Node` class.

\<Diagram of a linked list with three nodes TK\>

This simple example is known as a "singly linked list," because each node in the list "points" to the next node in the list, until the end is reached. It’s exactly like a line of people three people standing in a row, each person pointing to the person to the right. The last person in the line points to the wall, or to the end of the list.

To access the data in a linked list, you start at the head of the list and follow the `next` pointers until you reach the end of the list.

``` python
# current node we're interested in
# starting with node1
current = node1
while current is not None: # while we're not at the end of the list
    print(current.data)
    # set current to the next node in the list
    current = current.next
```

This code will print out the data in each node of the list, starting with the first node and ending with the last node.

Putting it all together in a simple Python program:

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node("First")
node2 = Node("Second")
node3 = Node("Third")

node1.next = node2
node2.next = node3

current = node1
while current is not None:
    print(current.data)
    current = current.next
```

Hopefully you’re not too surprised to find this program outputs:

`First` `Second` `Third`

If you’re stuck on anything at this point involving classes, objects, pointers, or linked lists, it’s worth going back and reviewing this chapter from the beginning. It’s important to have a solid understanding of these concepts before moving on to more complex data structures.

## Doubly Linked List

In a doubly linked list, each node contains a reference to the next node in the list as well as a reference to the previous node in the list.

Think for a moment…​why is this useful? In a singly linked list, you can only traverse the list in one direction, from the head to the tail. Every person in the line only points to the person to the right.

In a doubly linked list, you can traverse the list in either direction, from the head to the tail or from the tail to the head. You can move through the line of people in either direction. This useful difference comes with only one small change, the addition of a `prev` (for "previous") pointer in the `Node` class. Just like with the singly linked list, the last node in the list’s `next` points to `None`. Additionally, the `prev` pointer of the first node in the list points to `None`.

The implementation should not be too much of a surprise:

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

Here’s how you might create a doubly linked list with three nodes, and then read through the data from start to finish, and then back again to the start:

``` python
node1 = Node("First")
node2 = Node("Second")
node3 = Node("Third")

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

current = node1
while current is not None:
    print(current.data)
    current = current.next

print("")
current = node3
while current is not None:
    print(current.data)
    current = current.prev
```

This code will output:

`First` `Second` `Third`

`Third` `Second` `First`

This example is very procedural, so we’ll look at a more effective say to work with linked lists next.

## Developing Intuition: What are Linked Lists Used For?

Linked lists are used in many different ways in programming, primarily as a basic building block for more complex data structures. The basic ideas behind them a necessary to understand in order to build the stacks, queues, and heaps I’ll discuss in chapters 6 and 7. Again, as I mentioned earlier, linked lists are a gateway data structure, and understanding them will help you understand many other data structures. Keep in mind the overall concepts of pointers, classes, and objects as you work through the rest of this book.

## CRUD

> **CRUD**
>
> One common set of questions you might be asked in an interview is how to develop a CRUD application for a specific language.
>
> CRUD is an acronym that stands for Create, Read, Update, and Delete. The CRUD paradigm can be applied to programming in many different contexts. You can build a CRUD application in React, like a todo list. You can CRUD a database, to test your knowledge of SQL. You can build a RESTful CRUD API in Node, or perhaps in GraphQL with Apollo.
>
> Create: Create a new item in the database / Redux store / data structure. For example: "Pick up dog food from the pet store."
>
> Read: Read an item from the database / Redux store / data structure. For example there might be a list of TODO items that can be read from the database.
>
> Update: Update an item in the database / Redux store / data structure. Maybe you really meant to write "cat food" instead of "dog food." How can you access and update the item with your API.
>
> Delete: Delete an item from the database / Redux store / data structure. This one goes without saying, but it of course means deleting the item. If you’re standing in the pet store and you realize you don’t even have a pet, that item needs to go!
>
> Depending on the context in which the question is asked, you might also be responsible for implementing an interface for the CRUD application, or to add features like sorting, filtering, dating, checking for duplicates, pagination, etc.
>
> You should try to build a CRUD application for any language or framework you’re learning as it will give you a great foundation for understanding how to work with data in that language or framework.

It’s important to know how to create, read, update, and delete items in a linked list. Let’s go through each of these operations in turn.

### Create (Insert)

Translating the CRUD operations to linked lists, "Create" is the same as "Insert." Inserting an item into a linked list involves two steps. The first step is the one we’ve already covered, and that’s creating a node with the data you want to insert and setting the `prev` and `next` pointers of the new node to the appropriate nodes in the list.

The second step is to update the surrounding nodes to point to the new node.

\<Diagram of inserting a node into a doubly linked list TK\>

Here’s an example of inserting a node into a doubly linked list:

``` python
class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

node1 = Node("First")
node2 = Node("Second")
node3 = Node("Third")

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

new_node = Node("New Node")

# Insert the new node between node1 and node2
new_node.next = node2
new_node.prev = node1
node1.next = new_node
node2.prev = new_node

current = node1
while current is not None:
    print(current.data)
    current = current.next
```python

This code will output:

`First` `New Node` `Second` `Third`

### Read (Find)

How can you find a node in a linked list? You don’t have any kind of "index" to work with like you do with an array, when you can simply access the third item in the array by using `array[2]`. Additionally, what does it mean to "find" in a linked list? Does it mean the node? The data in the node? Something else?

Let’s just consider the singly linked list. You want to search the list for a node that contains a specific piece of data. Here’s a simple algorithm that will go through a linked list and return the first node that returns a that data, or "False" if the data is not found:

``` python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def find(head, data):
    current = head
    while current is not None:
      if current.data == data:
        return current
      current = current.next
    return False
```python

### Update

Given what’s already been discussed about reading and inserting nodes into a linked list, updating a node should be pretty straightforward. Again, what "update" means might be different in different contexts, but let’s say you want to update the first instance of a node with a specific piece of data, or return "False" if the data is not found.

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def update(head, data, new_data):
    current = head
    while current is not None:
        if current.data == data:
            current.data = new_data
            return True
        current = current.next
    return False
```

Nothing there should be too terribly surprising.

### Delete

Much like with the other three CRUD operations, if you know how to read, insert, and update nodes in a linked list, you should be able to delete a node as well. As usually, it involves finding the node you want, and then updating the surrounding nodes to skip past the node you want to delete.

\<Diagram of deleting a node from a singly linked list TK\>

What happens to the node you delete? It’s still in memory, but it’s no longer part of the list, and it will be garbage collected at some point in the future. Keep this in mind because there are some languages where you have to manually delete the node from memory, and if you don’t, you’ll have a memory leak, but with Python and Javascript, you don’t have to worry about that.

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete(head, data):
    current = head
    prev = None
    while current is not None:
        if current.data == data:
            if prev is None:
                head = current.next
            else:
                prev.next = current.next
            return True
        prev = current
        current = current.next
    return False
```

### Sorting a linked list

Ok, you’ve got a list of items, you’ve read them all in, and now you need to sort them. How do you do that with a linked list? Sorting a linked list is a bit more complex than sorting an array, mostly because you have to move the pointers around to keep the list in order. What would this look like if we tried to sort a linked list using the bubble sort algorithm we used to sort an array in chapter 4?

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort(head):
    if head is None:
        return None

    # We'll need to know the length of the list
    # so we can iterate through it
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next

    # We'll need to iterate through the list
    # multiple times to make sure it's sorted
    for i in range(length):
        current = head
        prev = None
        while current.next is not None:
            if current.data > current.next.data:
                # Swap the data in the nodes
                temp = current.data
                current.data = current.next.data
                current.next.data = temp
            prev = current
            current = current.next

    return head
```

Notice how the algorithm works. In the array bubble sort in Chapter 4 the data was actually swapped in place in the array. In the linked list bubble sort, the nodes — the array "places" — remain in place but the data itself is swapped between them. This is *not* the only way to sort a linked list, but it’s a good example of the idea of the bubble sort algorithm having a different effect on different data structures.

This code will sort a linked list in ascending order, but it’s clear how much overhead is involved with sorting a linked list. You have to know the length of the list in the first place, you have to go through the list multiple times, and you have to create several temporary variables to hold data and node references while you’re moving things around.

So this is a bad thing, right? Well not necessarily. As always it depends.

The reason I’m bringing this up is really to show that in the case of choosing the "best" way to do something, when it comes to linked lists, and most other data structures, the "cost" of doing things depends on not only the algorithm you choose but the data structure you’ve chosen.

Do things get any easier if we start with a doubly linked list?

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def bubble_sort(head):
    if head is None:
        return None

    # We'll need to know the length of the list
    # so we can iterate through it
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next

    # We'll need to iterate through the list
    # multiple times to make sure it's sorted
    for i in range(length):
        current = head
        prev = None
        while current.next is not None:
            if current.data > current.next.data:
                # Swap the data in the nodes
                temp = current.data
                current.data = current.next.data
                current.next.data = temp
            prev = current
            current = current.next

    return head
```

Well not really, because even though you can move through the list in either direction, you still have to go through the list multiple times to make sure it’s sorted. So even though you’ve chosen a slightly more complex data structure, you’re still stuck with essentially the same algorithm.

We are coming to more effective ways to sort and search data structure beginning in chapter 12, but whenever you’re trying to figure out the "best" way to do something, you need to make sure you take both the data structure and the algorithm into account. And just like arrays and for loops, some algorithms are better suited to some data structures than others.

### Merging linked lists

Now let’s try a more complex operation, merging two singly linked lists. Try reasoning through the logic of this code on your own.

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # Find the head of the merged list
    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    current = head
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1 is not None:
        current.next = head1
    if head2 is not None:
        current.next = head2

    return head
```

## Example Interview Questions

Honestly, the odds of your getting a linked list question in an interview are pretty low. The odds of being asked a question that knowledge of linked lists would help you answer are much higher. So this time there won’t be sample interview questions, but here are some exercises you should consider to consider to get your head around the idea of linked lists, nodes, pointers, and data.

- Consider all of the error-checking you might need to do in the CRUD operations for a linked list. For example, what if you try to delete a node that doesn’t exist? Combine the examples from this chapter into a generalized linked-list class that can handle everything you throw at it without crashing.

- Write a function that takes a linked list and returns the length of the list.

- Write a function that takes a linked list and returns the last node in the list.

- Re-write the data swapping version of the bubble sort algorithm to swap the nodes themselves instead of the data.

- Write a function that takes a linked list and returns the middle node of the list, and that works on any length of list.

- Write a function that takes a linked list and returns the nth node from the beginning or end of the list.

- Write a function that takes a linked list and returns the list in reverse order. Bonus points for using recursion. (Don’t worry if you don’t know what recursion is, I’ll get to that in chapter 11.)

- Write a function that takes a linked list and sorts the list in reverse order.

- A "circular" linked list is a linked list where the last node in the list points to the first node in the list. Can you think of a potential use for a circular linked list?

## AI Questions

In electrical or network engineering, signals are connected by wires that run to switches (like routers) or components (like lightbulbs). These can be considered as a kind of linked list, where the wires are the pointers and the switches and components are the nodes.

Using AI, build a game or simulation using linked lists that requires a progressive series of choices to be made. This can be like a "choose your own adventure" game, a "lemonade stand" type game, or a "build a city" kind of game. Whatever you choose, the idea must be that the player’s current state is directly influenced by all of the choices they’ve made up to that point.

Consider the path through the choices as a kind of "network," where the nodes are the choices and the pointers are the connections between the choices. Represent the path as a linked list. Explore the advantages and disadvantages of representing the data in this fashion. One of the advantages might be the creation of a path choice history, where the player can access all of the choices made up to that point. the history can even be used to allow the user to backtrack through the choices and choose different paths. One of the disadvantages might be the complexity involved in the maintaining the data structure, which will scale exponentially as the number of available choices grows.

Can you (and the AI) find a faster, more efficient way to represent the data?
