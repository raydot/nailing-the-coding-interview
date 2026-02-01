# Trees

Trees is a concept that can make some coder’s heads spin; especially those who did not go through a computer science program. To some extent I think the reason why is that trees (and graphs, which we’ll cover in the next chapter) are usually introduced in the context of other courses a future programmer might be taking that involves mathematical or set-theory-like definitions.

Given how useful trees are, and the extent to which they can separate the sheep from the wolves in the programming world, I’m taking it as a personal challenge to make trees accessible in this chapter.

## Trees Definition

We’ve already come across trees in two different contexts in this book. I discussed them in chapter 4 when I introduced the binary search algorithm, and I discussed them in 7 in the context of heaps.

## Building Intuition: What are trees used for?

An example of a tree you use every single day, and you might even be using it right now, is the document object model (DOM) in your web browser. The DOM represents every single element on an HTML page as a node in a tree. If you’ve done any HTML programming this will make intuitive sense to you. For instance, in HTML every tag that is "opened" must eventually be "closed" with a corresponding tag. That’s the tree structure in a nutshell.

PICTURE OF DOM AS TREE TK

## Reasoning about Trees

A tree most people are familiar with is a tournament bracket. A tournament bracket lists all of the teams (or players) in a tournament and their match-ups. When each round is completed the winner moves on the the next round.

The reason I mention a tournament bracket is because it makes it easy to see the relationship between trees and logarithms. Assuming the tournament is "single-elimination", meaning each team has to win its match or be eliminated, the number of rounds in the tournament is equal to the logarithm of the number of teams.

If you take the "sweet sixteen" round of a tournament, a round where there are 16 teams left, the logarithm of 16 is 4. This means there are 4 rounds left in the tournament. This is illustrated by following the path from the "Happy Crocodiles" all the way to the championship game.

## Tree Height

This logarithmic relationship is only maintained if the tournament is "balanced", mean that each team has one chance of winning. If there are eight teams on one side of the bracket and only two on the other, or eight teams on one side and 64 on the other, the logarithmic relationship no longers holds.

Because of this the height of a tree in relationship to the number of nodes is important, as it becomes a way to check if the tree is balanced. The height of a tree is the number of edges from the root node to the furthest leaf node. The height of a tree determines how long it will take to search through the tree.

Does this mean that shorter trees are faster than taller trees? Can’t we just put all of the nodes right under the root? Again, this breaks the logarithmic relationship. There is no method by which you can half the number of candidates in every search, and now the O(n log n) bonus you get from a tree turns back into O(n) when the tree is flattened.

## Binary Search Trees

Because it’s one of the easiest trees to understand and reason about, this chapter will primarily focus on binary search trees (BSTs). Later we will get to other types of trees in the hope it whets your appetite for trying to understand trees further, but binary search trees are the main branch for this chapter’s purposes. They are also the most commonly used tree and if you’re asked about a tree in an interview, chances are it will be a BST.

A binary search tree is comprised of nodes that are formed by following a simple set of rules:

- Each node has a single value

- Each node has a "left child" and a "right child"

- The value of a node’s left child is always less than the value of its "parent" node

- The value of a node’s right child is always greater than the value of its parent node

- Each node can have zero, one or two "children"

From that simple rule, a BST can be created that might like this:

            88
          /    \
        60      93
       /  \    /  \
      43   67 70   99
     /  \         /
    10   22     96

In this BST the "root" node is the one at the top, which represents the value 88 in this BST.

Start by considering the "left" side of the tree, contains the left child of the root node, and all of its "descendants":

          60
        /    \
      43      67
     /  \
    10   22

Now let’s consider the left side of this tree and all of its descendants:

        43
      /    \
    10      22

You have probably started to see a pattern, here. Each child node forms the root of a tree of its own, and so do its children, until you reach the "bottom" of the tree. (HINT: This just might mean recursion!)

At the bottom of the tree the nodes 10 and 22 are called "leaf" nodes, because they have no children.

The right side of the tree is similar to the left side, but it contains the right child of the root node and all of its descendants:

          93
        /    \
      70      99
     /
    96

    Continuing down the left side of this tree:

        70
      /
    96

The left child of the root node is 60, and the right child is 93. Following the tree down to the bottom the children of 60 are 43 and 67, and the children of 43 are 10 and 22.

> > 📝 **NOTE**
>
> > What’s with all the quotes?
>
> I threw quotes around a lot of the terms up above the first time they appeared in text to remind us all that trees are the able-to-be-understood-by-humans representation of the underlying data structure.
>
> Way, way down the stack at the level at which the code is being processed by the computer, these relationships are represented by pointers or references and have neither spacial nor familial relationships to each outside of their physical positions in memory.
>
> In other words, if you could somehow shrink yourself down the size of an electron and walk along the surface of your computer’s memory, (shout out to _TRON_, the movie that made me want to be a computer programmer) you may search far and wide but you will not find a actual tree, parent, or child.
>
> Now that we’ve had that discussion, I will stop using the quotes.

            88
          /    \
        60      93
       /  \    /  \
      43   67 70   99
     /  \         /
    10   22     96

One of the great things about a binary search tree is it’s pretty easy to get it right. I used to think along the lines of "what if I throw the number 68 in there? It’s between 68 and 70 and will surely have to violate the rules!" Nope. Remember that smaller things go left and larger things go right. So 68 will start be going to the left of 88. From there it will go right of 60 before gracefully falling into place to the left of 67.

What if you have a number that is already in the tree? There are a few ways to think about this, but for the purposes of the BST’s in this book, if you already have a number in the tree then it’s represented, and you don’t need another one. We will ignore the possibility of duplicates for now.

Armed with these rules I strongly suggest building a few trees on your own. Don’t do it with code, do it on paper. Or do it on an erasable whiteboard. Practice adding and removing nodes from a tree, and also consider other types of data. How does a tree work with letters? What about words? Can you create a lopsided tree, by using really, really big numbers? What about really, really small numbers? Can you add negative numbers? Can you make a tree out of something not readily sorted, like colors, or flavors? Does a tree still work for these? Playing around like this will definitely help build your intuition for binary search trees, and, it’s actually kind of fun.

## What a tree looks like in code

In order to store data in a tree, a data structure must be create to represent the relationships between the nodes.

As the node is the basic building block of a tree, it’s a good place to start.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

Why so much code for a node? As I’ve implied by drawing all of those awesome pictures in this chapter, a node contains both data and relationships. Those relationships can be represented in a few different ways, but it’s best to start simple.

`self.value` represents the data stored in the node. `self.left` and `self.right` represent the relationships between the node and its children.

If this code looks familiar to you, it’s because it should be. Here is the code I used to create a linked list node in chapter 5:

```python
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

These two functions for creating a node are essentially identical. There "left" and "prev" and "right" and "next" are just variable names. They are not reserved keywords. There is nothing special about them. As Gertrude Stein was rumored to have said, "A node is a node is a node." In both case the names are just being used to represent the relationships between the nodes in a way that’s understandable to humans.

Where the two data structures are different is in the relationship between the nodes. Linked lists are linear and only point forwards and backwards. Trees are a two-dimensional hierarchical structure that can point left, and right.

There are algorithmic ways to insert data into a tree, but I’m going to just "hard code" the tree in the example above for now, just to make it clear what’s going on:

```python
# Creating a tree at the root
root = TreeNode(88)

# Populate the left subtree
root.left = TreeNode(60)
root.left.left = TreeNode(43)
root.left.right = TreeNode(67)
root.left.left.left = TreeNode(10)
root.left.left.right = TreeNode(22)

# Populate the right subtree
root.right = TreeNode(93)
root.right.left = TreeNode(91)
root.right.right = TreeNode(99)
root.right.right.right = TreeNode(101)
```

The result is a Python object that more-or-less looks like this:

```python
{
    "value": 88,
    "left": {
        "value": 60,
        "left": {
            "value": 43,
            "left": {
                "value": 10,
                "left": None,
                "right": None
            },
            "right": {
                "value": 22,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 67,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 93,
        "left": {
            "value": 91,
            "left": None,
            "right": None
        },
        "right": {
            "value": 99,
            "left": None,
            "right": {
                "value": 101,
                "left": None,
                "right": None
            }
        }
    }
}
```

Can you recreate this tree as a Python nested list? As a Python dictionary?

With that code representation of a tree, we’re ready to break down the operations that can be performed on a tree.

## Tree Operations

As I mentioned earlier, we covered some basic tree operations when we discussed heaps in chapter 7. Now it’s time to dig deeper and learn about all of the fundamental operations needed to work with trees which is, after all, where the magic happens.

### Traversal

Traversal means visiting each node in a tree. As mentioned earlier, trees don’t actually live in a tree format in code, but reside nested structures like objects or dictionaries. You certainly could use a nested for loop and to go through a tree that way, that way, but doing so deprives you as all of a trees benefits and properties, glamor and romance.

Here are some more tree-like ways of visiting every node in a tree. There are three primary ways to traverse a tree:

- In-order traversal: Start at the left child the visit the root and then visit the right child.

\<ILLUSTRATION OF IN-ORDER TRAVERSAL TK\>

- Pre-order traversal: Start at the root and then visit the left child and then the right child.

\<ILLUSTRATION OF PRE-ORDER TRAVERSAL TK\>

- Post-order traversal: Start at the left child, then visit the right child and then visit the root.

\<ILLUSTRATION OF POST-ORDER TRAVERSAL TK\>

Looking at the example from earlier in the chapter:

            88
          /    \
        60      93
       /  \    /  \
      43   67 91   99
     /  \            \
    10   22           101

The in-order traversal of this tree results in this array of numbers which, not at all coincidentally, is also the sorted order of the numbers in the tree:

```
[10, 22, 43, 60, 67, 88, 91, 93, 99, 101]
```

Pre-order and post-order traversals have much more specific uses, some of which will be explored before the end of this chapter.

Assuming this binary search tree exists in an array format, here is an example of how to traverse it in-order, using a stack to keep track of the nodes that have been visited:

```python
def in_order_traversal_iterative(root):
    result = []
    stack = []
    current = root

    while current or stack:
        # Reach the leftmost node of the current subtree
        while current:
            stack.append(current)
            current = current.left

        # Current is now None, pop from stack and visit
        current = stack.pop()
        result.append(current.value)

        # Now visit right subtree
        current = current.right

    return result
```

There is a much more effective way to traverse a tree using recursion, which looks like this:

```python
def in_order_traversal(tree):
    if tree is None:
        return []
    return in_order_traversal(tree.left) + [tree.value] + in_order_traversal(tree.right)
```

I’m just gonna leave that there and let you ponder it, but we’ll come back to this idea in chapter 11.

### Insertion

Inserting a node into a tree involves first finding the correct location an a new node and then adding it to the tree. This process is very similar to inserting a node into a heap, as was shown in Chapter 7. There one big difference is that in a heap the new node is always added to the bottom of the heap tree, which is then restructured to maintain the heap. In a binary search tree, both steps are accomplished at the same time new nodes are added at the top (root) and then moved into place.

\<ILLUSTRATION OF INSERTION TK\>

Here is a function that can be used to build the binary search tree we’ve been discussing in this chapter:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Create a new node
        new_node = TreeNode(value)

        # If there is no root, the tree is empty,
        # so set the new node as the root
        if self.root is None:
            self.root = new_node
            return

        # Start inserting at the root
        current = self.root

        # Climb down the tree until the correct
        # position is found for the new node
        while True:
            # If the value is less than the root, go left
            if value < current.value:
                # If there is no left child, this must be the place
                # to insert the new node
                if current.left is None:
                    current.left = new_node
                    return
                # Otherwise, move to the left child
                current = current.left

            # Same process again for the right child
            elif value > current.value:
                # If there's no right child, then this must be the place
                # to insert the new node
                if current.right is None:
                    current.right = new_node
                    return
                # Otherwise, move to the right child
                current = current.right

            # Otherwise the value is already in the tree,
            # and we have sworn to ignore duplicates
            # so we can just return
            else:
                return

    # Print the BST nodes in sorted order
    # using in-order traversal as discussed above
    def in_order_traversal(self):
        result = []
        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.value)

            current = current.right

        return result

bst = BinarySearchTree()

# Try moving the numbers around, or adding new ones, you'll always get a tree!
values = [88, 60, 43, 10, 22, 67, 93, 91, 99, 101]
for value in values:
    bst.insert(value)

# Test the in-order traversal (should print sorted values)
print(bst.in_order_traversal())
```

That bit of code above is a complete implementation of a binary search tree. It’s worth playing around with for a while to see how it works. Can you come up with an algorithm that will print the values in "tree" from?

### Deletion

Removing a node from a tree presents a bit more of a challenge. This is because the position of the node can affect the structure of the tree. If a value is removed from the middle of the tree, then the existing children will have to move up, parents will get new children, havoc will ensue. Fortunately, there are only three cases to consider.

1.  The node to be deleted is a leaf node (no children).

2.  The node to be deleted has one child.

3.  The node to be deleted has two children.

The first case is the simplest. If the node is a leaf then it can simply be snipped off the tree with no further consequences. That could be accomplished by simply doing something like this:

```python
def delete_leaf_node(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return None
    return node
```

Case two is a wee bit trickier, but not by much. If the node to be deleted only has one child, then the child can simple be moved up to take the place of the parent. All of the other children will remain in place, and balance will be restored to the kingdom. This can be accomplished with a function like this:

```python
def delete_node_with_one_child(node):
    if node is None:
        return None
    if node.left is None:
        return node.right
    if node.right is None:
        return node.left
    return node
```

The third case presents a bit of a challenge. What to do if the node to be deleted has two children. If that’s the case then a lot of nodes need to move up. But there’s a simple trick that can be used to solve the problem easily. When the parent is deleted either the left child or the right child needs to be moved up to take its place. This can be done by either finding the largest value in the left child, or the smallest value in the right child, moving it up to become the parent.

This is a bit of a tricky operation, but it can be with the help of a function that finds the largest value in a tree:

```python
def find_largest_value(node):
    if node is None:
        return None
    while node.right is not None:
        node = node.right
    return node.value
```

With that function in place, the node is ready to be swapped out and deleted:

```python
def delete_node_with_two_children(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return None
    if node.left is not None and node.right is not None:
        # Find the largest value in the left child
        largest_value = find_largest_value(node.left)
        # Move it up to take the place of the parent
        node.value = largest_value
        # Delete the original parent
        node.left = delete_node_with_one_child(node.left)
```

### Balancing

Something I was confused about when I first started with trees is the idea that something in the algorithm needs to "balance" the tree. Like, I don't want to end up with a tree that looks like this:

            88
          /
        60
       /
      43
     /
    10

If you insert values in sorted order—say 10, then 43, then 60, then 88—you'll get exactly the unwanted (more on that in a second) structure shown above. Each new value goes to the right of the previous one, creating a linked list masquerading as a tree.

Why that's unwanted is because the performance benefits of a tree depend on its height. A balanced tree with n nodes has a height of O(log n), which means searching, inserting, and deleting all take O(log n) time. An unbalanced tree can have a height of O(n), which means all those operations degrade to O(n) making it no better than a linked list.

#### Keeping Trees Balanced

Fortunately, there are aa few things you can do to keep your trees ever green:

**1. Insert in Random Order**

If you have control over the insertion order, randomizing it can help. Instead of inserting [10, 43, 60, 88] in sorted order, shuffle them first. This won't guarantee balance, but it makes severe imbalance much less likely.

**2. Use a Self-Balancing Tree Variant**

This is where AVL trees and Red-Black trees (mentioned earlier in this chapter) come in. These variants add extra rules and perform "rotations" after insertions and deletions to maintain balance.

- **AVL trees** track the height of each subtree and rebalance when the difference exceeds 1
- **Red-Black trees** assign colors to nodes and enforce color rules that guarantee the tree never gets too tall

These variants are a bit more complex to implement, but they guarantee O(log n) operations even in the worst case.

**3. Rebuild the Tree**

If you have an unbalanced tree, you can rebuild it into a balanced one. Here's the approach:

1. Do an in-order traversal to get all values in sorted order
2. Build a new tree by recursively choosing the middle element as the root
3. The left half becomes the left subtree, the right half becomes the right subtree

This takes O(n) time but gives you a perfectly balanced tree. Like this:

```python
def build_balanced_tree_from_array(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    node = TreeNode(arr[mid])
    node.left = build_balanced_tree_from_array(arr[:mid])
    node.right = build_balanced_tree_from_array(arr[mid + 1:])
    return node

def balance_tree(root):
    # Step 1: Get sorted values via in-order traversal
    values = in_order_traversal(root)

    # Step 2: Build balanced tree from sorted array
    return build_balanced_tree_from_array(values)
```

#### What You Need to Know for Interviews

Some ways trees and balancing might come up in an interview:

- **Basic BSTs** can become unbalanced. If asked to implement one, implement what we've shown in this chapter.
- If an interviewer asks "what happens if values are inserted in sorted order?", the correct answer is "the tree builds itself into a linked list with O(n) operations instead of O(log n)."
- If they ask how to fix it, mention self-balancing variants (AVL, Red-Black) or the rebuild approach above.
- Most interview problems assume you're working with a reasonably balanced tree, or they focus on traversal/manipulation rather than insertion order. But it never hurts to double-check.

The good news? You rarely need to implement self-balancing logic from scratch in an interview. Understanding that the problem exists and knowing the solutions is usually enough. So keep calm, and rip trees.

> **If Trees are so great, why don’t programming languages already have them?**
>
> Excellent question!
>
> There are a few "native" trees in some programming languages, like Java’s `TreeSet` and `TreeMap` or `set` and `map` in the C++ Standard Template Library, but most programming languages do not have a native implementation of trees.
>
> The reason, I suspect, is simple. Most trees are created for a very specific purpose, like the DOM in a web browser or the file system on your computer.
>
> Because of the need for such specific functions and data, a more generic tree implementation would likely have to be modified to work with specific sets of data, or would be difficult to optimize for specific use cases.
>
> In other words: pretty useless.
>
> That doesn’t mean they’re not important, though. It just means that if you get to the point where you’re sure you need a tree, it will also be crystal clear to you exactly what it needs and how to build your own. Good thing the rules for creating trees are so simple!

## Tries

Tries (rhymes with "fries") are a type of tree that is used to store strings. They are used in applications like spell checkers and autocomplete, and are a great way to store a large number of strings in a way that is easy to search.

Unlike all of the trees we’ve discussed so far, tries are not binary trees. A single node in a trie can have multiple children, and the nodes are not necessarily ordered in any specific way.

\<Image of trie TK\>

The structure of a trie is determined by the strings that are stored in it. This makes them great for creating relationships between small pieces of data, like letters in a word. This makes them highly applicable to problems like spell checking and autocomplete, and they are also used extensively in natural language processing. The same things that make tries great for string manipulation make them not-so-great for larger types of data, and you would certainly not want to use them for databases or graphics processing.

If you want to build your own custom auto-complete algorithm for your web site, surely a trie library will be involved. Here is a very basic example of a trie in Python:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

In this example each "node" of the tree is represented by a `TrieNode` object. This object contains a dictionary of children, which allows for multiple children for node. It also contains a boolean value that indicates whether or not the node is the end of a word. In this way it bears some resemblance to a linked list, but with multiple children for each node. This allows for the strings stored in a trie to be easily searched and manipulated.

    class Trie:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            current = self.root

            # Traverse the trie character by character
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]

            # Mark the end of the word
            current.is_end_of_word = True

        def search(self, word):
            current = self.root

            # Traverse the trie character by character
            # If character doesn't exist, word is not in trie
            for char in word:
                if char not in current.children:
                    return False
                current = current.children[char]

            # Return True if we've reached the end of a word
            return current.is_end_of_word

Here each word is inserted into the tree one character at a time, with each character being a node in the tree. Bear in mind that the variable names "char," "word," and "children" are just variable names. They could be anything. There’s no special reserved trie magic in Python.

\<Image of trie node TK\>

Tries will store words one character at a time, with words that share starting characters sharing nodes in the tree. The words "stamp," "stand," and "start" would all share the same starting nodes of "st." "Stamp" and "stand" would share the "sta" node, and "start" would have its own "star" node — which it would share with "stare" and "startle," should they be added to the trie.

Here are some helper functions that can be added to the already defined `Trie` class that it can use to find words based on their starting characters:

```python
    def starts_with(self, prefix):
        current = self.root

        # Traverse the trie character by character
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True

    def get_suggestions(self, prefix):
        suggestions = []
        current = self.root

        for char in prefix:
            if char not in current.children:
                return suggestions
            current = current.children[char]

        # Collect all words starting from this node
        self._collect_words(current, prefix, suggestions)
        return suggestions

    def _collect_words(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)

        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, suggestions)
```

Play around with this code and add some print statements and see if you can get it to work as an autocomplete algorithm. This code is most of the way there, and shouldn’t require too much tinkering to get it to work. Another idea is to add a function that visualizes the trie, so you can see how it works. Last of all, how would you delete a word from a trie? We will return to tries in Chapter 12, so it will be worth your time to play around with them now.

## Other Types of Trees

The intended target audience for this book is likely either only going to be asked about trees in the more general way in which I’ve already described then, or they’ll already have domain-specific knowledge of the trees that can be used to solve specific problems. So I’m only going to cover a few of the more common tree types generally, and I encourage you go online or use AI if you want to learn more about them.

### B-Trees

B-Trees can be used to store data that is easy to search, update, and delete. The defining characteristic of a B-Tree is that it is a self-balancing tree that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.

### Red and Black Trees

Red and black trees are similar to the binary search trees described in this chapter, with a few added rules to help keep them balanced. Red and black trees are primarily used in places where data is being constantly added and removed, like a database or file system.

In a red and black tree, it should not surprised you to find that each node is — wait for it! — red or black. Because of these additional rules, red and black trees are more self balancing than binary search trees

### AVL Trees

AVL trees are another type of self-balancing binary search tree. The work similarly to red and black trees and are also used with data that requires a lot of addition and deletion, but contain a different set of rules that balance them. AVL trees are primarily concerned with the height of the tree, and will balance by spreading out nodes to keep the tree from getting too tall. This might seem like a silly thing, but because trees can generally be searched in O(log n) time, the smaller the n, the faster the search.

## Example Questions

### Balancing trees

I said earlier in the chapter that binary search trees are self-balancing, but that’s a bit of an oversimplification for two reasons. First of all, binary search trees are only self-balancing if they’re constructed in a way that maintains the self-balancing properties. This construction has to extend to the insertion and deletion of nodes, and all that might entail in terms of moving nodes around. The second reason is that I chose binary search trees because they’re both widely used and also because they’re among the easiest trees to construct and understand.

While not only binary search trees but other types of trees like red and black trees and AVL trees are self-balancing, there are other types of trees that are not. My first question for you is: Why? What could the possible advantage be to using a tree that is not self-balancing?

My second question is: How would you go about balancing a tree that is not self-balancing, should it be required? This is a concept that’s been covered in one way way or another in earlier chapters, and so I’m going not going to provide the answer here.

The hint I’ll give it to consider the chapter on heaps and the upcoming chapter on graphs. If you’re still stuck, have a look at the AI section at the end of this chapter and see if what’s suggested there can help you come up with a solution.

### Finding height of tree

Write an algorithm to find the height of a binary tree. This one sounds complicated, but it’s actually pretty simple. Remember that the height of a tree is the number of edges from the root node to the furthest leaf node. I recommend you try to write it yourself before looking at the solution below, but I’ll give you a hint: the solution uses recursion.

```python
def find_height(node):
    if node is None:
        return -1  # Return -1 for null nodes to count edges correctly
    left_height = find_height(node.left)
    right_height = find_height(node.right)
    return 1 + max(left_height, right_height)
```

### Tree longest path

Write an algorithm to find the longest path in a binary tree. If you’ve found the height of a tree then you’re not too far off from finding the longest path.

The longest path in a binary tree is also called the "diameter" of the tree. It's the number of edges in the longest path between any two nodes in the tree. This path doesn't necessarily pass through the root—it could be entirely within a subtree.

Here's how:

1. For each node, calculate the height of its left and right subtrees
2. The longest path through that node is the sum of both heights
3. Track the maximum path found across all nodes

```python
def longest_path(root):
    # Track the maximum diameter found
    max_diameter = [0]

    def height(node):
        if node is None:
            return 0

        # Recursively find height of left and right subtrees
        left_height = height(node.left)
        right_height = height(node.right)

        # Update max diameter if path through this node is longer
        # The path through this node is left_height + right_height
        max_diameter[0] = max(max_diameter[0], left_height + right_height)

        # Return height of this subtree
        return 1 + max(left_height, right_height)

    height(root)
    return max_diameter[0]
```

**Why this works:** The algorithm does a post-order traversal, calculating heights from the bottom up. At each node, it considers whether the path through that node (connecting its left and right subtrees) is the longest path seen so far. The time complexity is O(n) since we visit each node once.

### Merging trees

Much like we did with linked lists in chapter 5, we can merge two binary trees by combining their structures and values.
A very real use case might arise from one company acquiring another, and needing to merge their employee contact databases. It just so happens that both companies maintain their contact lists as binary search trees.
Isn't that convenient?
How can the two company contact lists be merged into a single list?
The process involves these steps:

1. Extract the sorted values from both trees into arrays using in-order traversal
2. Merge the two sorted arrays into one sorted array
3. Build a new balanced binary search tree from the merged array, using the `build_balanced_tree_from_array()` function from earlier in this chapter

Seems pretty straightforward, right?

```python
def merge_bsts(tree1, tree2):
    # Step 1: Get sorted values from both trees
    values1 = in_order_traversal(tree1)
    values2 = in_order_traversal(tree2)

    # Step 2: Merge two sorted arrays
    merged_values = merge_sorted_arrays(values1, values2)

    # Step 3: Build balanced tree from merged array
    return build_balanced_tree_from_array(merged_values)

def merge_sorted_arrays(arr1, arr2):
    # Two-pointer merge (like merge sort)
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
```

Challenge yourself: What is the time complexity of this algorithm? Hint: think about the time complexity of each step. What about the space complexity? It's unlikely two merged companies would have duplicate employees, but what if they did? How could you modify this algorithm to handle duplicates? How would that change the time and space complexity?

## Interview Patterns

### Validate Binary Search Tree

This is a question that comes up often in technical interviews. It's LeetCode problem #98.

**Interviewer:** "Given the root of a binary tree, determine if it's a valid binary search tree."

**You:** "Just to clarify—does a valid BST mean that for every node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater?"

**Interviewer:** "Exactly. And assume all values are unique."

**You:** "Assume all nodes are unique: got it. My first instinct is to check each node against its immediate children, so I'll start there. Let me think through an example..."

```python
# This DOESN'T work - only checks immediate children
def is_valid_bst_wrong(node):
    if not node:
        return True

    # This only checks direct children, not all descendants
    if node.left and node.left.value >= node.value:
        return False
    if node.right and node.right.value <= node.value:
        return False

    return is_valid_bst_wrong(node.left) and is_valid_bst_wrong(node.right)
```

(I'm of course not suggesting you deliberately write incorrect code just to look like a genius for fixing your own mistake, but sometimes it's okay to start with a simpler approach and then refine it as you go.)

You: "Actually, this fails for a tree like [5, 1, 6, null, null, 4, 7] where 4 is in the right subtree of 5 but is less than 5. I need to track valid ranges for each node."

```python
def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    # Empty tree is valid
    if not node:
        return True

    # Current node must be within the valid range
    if node.value <= min_val or node.value >= max_val:
        return False

    # Left subtree: all values must be < node.value
    # Right subtree: all values must be > node.value
    return (is_valid_bst(node.left, min_val, node.value) and
            is_valid_bst(node.right, node.value, max_val))
```

💡 Key Insight

Please notice that each node doesn't just need to satisfy its parent—it needs to satisfy ALL of its ancestors. By passing down min/max bounds, your algorithm ensures every node respects the entire path from root.

⚠️ Common Mistake

If you only check immediate children (left < node < right) you might miss structural violations deeper in the tree. A node in the right subtree must be greater than ALL ancestors on the left path.

### Invert Binary Tree

This one's a bit more tricky, but it's a classic problem. You can find it on LeetCode as problem #226.
There's more about recursion in Chapter 11.

**Interviewer:** "Given the root of a binary tree, invert it. Find a way to swap every left and right child."

**You:** "So if I have a tree where the root is 4 with left child 2 and right child 7, after inverting, 2 should be on the right and 7 on the left?"

**Interviewer:** "Correct. And this applies recursively to all subtrees."

**You:** "This feels like a natural fit for recursion. I haven't read chapter 11 yet but I'll swap the children at each node, then recursively invert the subtrees."

```python
def invert_tree(root):
    # Base case: empty tree or leaf node
    if not root:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert both subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root
```

Interviewer: "Good. What's the time and space complexity?"

You: "The time complexity is O(n) since we visit every node once. The space complexity is O(h) for the recursion stack, where h is the height—O(log n) for balanced trees, with O(n) being the worst case for skewed trees."

Interviewer: "Could you do this iteratively?"

You: "Yes, using a queue for level-order traversal:"

```python
def invert_tree_iterative(root):
    if not root:
        return None

    queue = [root]

    while queue:
        node = queue.pop(0)

        # Swap children
        node.left, node.right = node.right, node.left

        # Add children to queue for processing
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root
```

💡 Key Insight

Tree problems often have both recursive and iterative solutions. Recursive is usually cleaner for tree structure, but iterative avoids stack overflow on very deep trees, and in some cases can be more efficient.

⚠️ Common Mistake

Forgetting to return the root node. Many tree problems expect you to return the modified tree, not just modify it in place. It's a good idea to put on your functional programming pants in solving these problems.

## Exercises:

1. Validate Binary Search Tree: Given a binary tree, create a function that determines if it's a valid BST. Keep in mind that all left descendants must be less than the node, and all right descendants must be greater.

2. Lowest Common Ancestor: Given a BST and two nodes, find their lowest common ancestor (the deepest node that has both nodes as descendants). Can you use this as a building block for other algorithms?

3. Level Order Traversal: Given a binary tree, return the values of nodes at each level. For example, return [[root], [level1_nodes], [level2_nodes]]. Hint: Use a queue.

4. Symmetric Tree: Write a function that determines whether a binary tree is a mirror of itself (symmetric around its center). For example, [1,2,2,3,4,4,3] is symmetric.

5. Path Sum: Given a binary tree and a target sum, determine if there exists a root-to-leaf path where the sum of node values equals the target.

6. Serialize and Deserialize Binary Tree: Design an algorithm to serialize a binary tree to a string and deserialize it back to the tree structure. This is very useful for saving/loading tree data.

## Big O Analysis of Tree Operations

Understanding the time complexity of tree operations is crucial for interview success:

| Operation             | BST Average | BST Worst Case | Balanced Tree | Notes                                                                 |
| --------------------- | ----------- | -------------- | ------------- | --------------------------------------------------------------------- |
| Search                | O(log n)    | O(n)           | O(log n)      | Average assumes balanced tree; worst case is degenerate (linked list) |
| Insert                | O(log n)    | O(n)           | O(log n)      | Must traverse to find insertion point                                 |
| Delete                | O(log n)    | O(n)           | O(log n)      | Find node + restructure; two-child case most complex                  |
| In-order traversal    | O(n)        | O(n)           | O(n)          | Must visit every node once                                            |
| Pre-order traversal   | O(n)        | O(n)           | O(n)          | Must visit every node once                                            |
| Post-order traversal  | O(n)        | O(n)           | O(n)          | Must visit every node once                                            |
| Find min/max          | O(log n)    | O(n)           | O(log n)      | Go all the way left (min) or right (max)                              |
| Find height           | O(n)        | O(n)           | O(n)          | Must check all paths to leaves                                        |
| Level-order traversal | O(n)        | O(n)           | O(n)          | BFS approach, visits every node                                       |
| Balance tree          | O(n)        | O(n)           | O(n)          | Traverse + rebuild; creates new balanced tree                         |

**Key Interview Insights:**

- **Balance Matters:** Basic BST operations degrade from O(log n) to O(n) when a tree becomes unbalanced. Self-balancing trees (AVL, Red-Black) _guarantee_ O(log n).
- **Height = Performance:** Tree height determines search/insert/delete time. Balanced tree height is O(log n); unbalanced can be O(n).
- **Traversal Always O(n):** In any structure tree, visiting all nodes takes O(n) time.
- **Space Complexity:** Recursive operations use O(height) stack space.
- **Worst Case Scenario:** Inserting sorted data into basic BST creates linked list (O(n) operations). It's important to consider insertion order.

**When to use trees:**

- Need sorted/searchable data with O(log n) operations
- Hierarchical relationships (DOM, file systems, org charts)
- Range queries (find all values between x and y)
- Prefix matching (tries for autocomplete)
- Priority-based processing (heaps)
- Maintaining sorted order while allowing insertion/deletion

**Tree vs Other Structures:**

- **vs Arrays:** Trees allow O(log n) insert/delete vs O(n) for arrays, but arrays have O(1) index access
- **vs Hash Tables:** Trees maintain order and allow range queries; hashes are faster (O(1)) but unordered
- **vs Linked Lists:** Trees provide O(log n) search vs O(n) for lists, but more complex to implement

## Using AI to Study Trees

Not so long ago, or so it seems, I was following a computer science tutorial on a fairly well-known online learning platform that primarily specializes in mathematics. I already knew a decent amount about trees, but I’m a big fan at getting multiple takes on the same topic, so I followed the tutorial. At the end, as a "stretch goal," the chapter question was "Write an algorithm that can draw a tree." I'm going to suggest something low-tech: take out paper and pencil or use a dry-erase board and draw some trees. Putting hand-to-paper will really, really help cement tree structures in your mind.

Once you've done that, and you really feel you have an understanding, try using AI to help you build more intuition that bridges code to structure. Draw a tree the way I did above, using / \ to represent connections.  
Ask AI to walk you visually through some of the ideas covered in this chapter.  
Have it walk you visually through merging, sorting, and traversing.
Have it take you through these operations with some of the different types of trees we've covered.  
Do that a few times and once you feel you've really got a grasp of the differences between tree types and operations, return to the visualization problem. Can you write a small Python or JavaScript application that visualizes what's in this section. It could be an invaluable tool for really understanding trees.
