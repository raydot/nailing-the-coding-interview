# Arrays

Arrays are usually the first data structure that programmers learn about, sometimes well before coming to the concept of data structures. Widely used in some form or another in just about every programming language, arrays are a vital data structure for any programmer to understand.

In interviews a firm knowledge of arrays is essential. It’s important not only to be aware of the built in array functions in a given languages, but to understand the ideas behind them and how to replicate that functionality in your own code.

This chapter will explain how to do all of that, and hopefully by the end there will be a firm understanding of arrays at a level that makes them an invaluable tool in your interview toolbox.

An array can simply be thought of as a linear list of items, a vector addition to a sole variable. Now instead of `x` and `y` and `z` existing as the sole entities in the variable universe, arrays add indexes to variables, and allow for the storage of multiple values in a single variable. This grouping allows for relationship to form between pieces of data, much like amino acids form proteins, notes form a melody, ingredients form a recipe, or words form a sentence.

In this chapter we’ll cover the basics of arrays, from the foundational computer science behind them to how to access and manipulate their elements.

## Arrays

Arrays are the simplest linear data structure. In less abstract languages like C++ or Java, arrays are manipulated directly from their addresses in computer memory by pointers. For our purposes, we will only consider arrays as being manipulated and addressed by the abstraction known as the array’s "index." I mention this abstraction as something to keep in the back of your mind when you consider the original purpose of some of the data structures and operations you’re about to encounter.

<div class="sidebar">

<div class="title">

Levels of Abstraction

</div>

Programming languages can be categorized by levels (or layers) of abstraction, which means abstraction away from the underlying hardware and chipset that a computer uses to store data and instructions. "Low-level" programming languages, like Assembly, are only one level of abstraction from the hardware that makes up a computer, and can be used to manipulate a computer’s hardware directly using what is known as "machine code."

Low-level languages tend to make more sense to computers than humans, though, and it was realized long ago that abstractions were needed to connect human thinking and language to computer actions. "High-level" languages, like C++, take human-readable language and compile it into machine code instructions that can be used to manipulate a computer’s chipset directly. There’s a higher abstraction than this though. "Interpreted" languages, sometimes referred to as "scripting languages", contain an even higher level of abstraction, as these languages don’t interact with the computer chipset at all. Scripting languages are instead fed to an application, like a web browser, that attempts to "interpret" their instructions into machine code. It’s well worth your time to understand layers of abstraction as a programmer, and it goes far beyond what can be explained in a single side note.

</div>

### Array Terminology

Arrays are close in equivalence to what is known in mathematics as a "set." A set is a list of items that have some relation to one another, that can be represented by a single notation. (Arrays are "close" to sets because in mathematics a set cannot contain duplicate items, while in programming an array can.)

In strongly typed languages, arrays can only contain the same type of data, but in weakly typed languages, arrays can contain mixed data types. Arrays have some special terminology related to their specific use:

Element, index, set

\<diagram of an array TK.\>

We looked at a simple example of an array in Chapter 3, "Strings," with an image showing how string is an array of characters.

GRAPHIC:

\[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 \]

In their original versions, and as is still the case in languages like C++, arrays worked hand-in-hand with data "pointers", or reference objects that "point" to specific memory addresses. Once an array is created in C++, the programmer can "dereference" each address in memory to get the value stored there. Because a pointer points to a specific type of data, incrementing a pointer moves it in memory the length of that piece of data.

In C++, for instance, an integer usually (but not always!) occupies four bytes of memory. So pointing a pointer at the beginning of an array and then incrementing it by one moves it over four bytes — to the beginning of the next item in the array. Because this type of array manipulation has become language-specific, we’re not going to use pointers in this book. We’ll instead settle for array items simply being referenced by their index numbers.

\<GRAPHIC TK of array with index numbers\>

The length of an array is one of its most important properties. Many array operations take the length of an array into account for their operations. Most programming languages will throw an error if you try to access an element in an array that is beyond the array’s "scope," or length.

<div class="sidebar">

<div class="title">

Weakly- vs. Strongly-Typed Languages

</div>

The difference between weakly-typed and strongly-typed languages comes down to how strict the language requires programmers to be when creating, passing, and mixing data. In strongly-typed languages, like C/C++ or Java, data mixing is not allowed without creating specific data types to support the mixing. In weakly typed languages, this mixing is allowed, accepted, and even encouraged!

If you’ve used Typescript you’re used to a hybrid of both, with Typescript being a language that adds strong data typing to Javascript. There’s some controversy over whether this is desirable or should even be allowed. Is Typescript a useful tool or simply meant to make Javascript more palatable for coders coming from more strongly-typed languages, like Java?

In C++ an array must be of a specific data type, and only that data type is allowed in the array. Here is an integer array in C++. It can only be used to hold five integer values, no more, and no other type of data is allowed.

`int intArray[5] = {33, 22, 11, 18, 96}`

In weakly-typed JavaScript, all different types of data can be mixed together, and the language interpreter doesn’t mind at all:

`mixedArray = [33, 22, 3.15159, "hello", false]`

The reasons for these differences are logical, of course, and mostly have to do with the way memory is allocated by different programming languages.

</div>

### Array Indexing/Numbering

In most programming languages, arrays are numbered — or "indexed" from zero. This is because arrays are meant to be thought of as contiguous elements in a computer’s memory, as explained in the section on pointers, above. If arrays started counting from 1, there would be space unaccounted for in that first position in the memory that exists between 0 and 1. It’s the same reason why the 19th century starts in 1800. You have to account for the First Century somehow, and no one wants to be from the "Zeroeth Century."

That means the first element in the array `testArray` is located at array index 0. If `testArray = [21, 31, 41, …​]` then `testArray[0]` is where to find 21, `testArray[1]` is where to find 31, `testArray[2]` is where to find 41, etc.

``` python
testArray = [21, 31, 41]
print(testArray)[0]
`21`
print(testArray)[1]
`31`
print(testArray)[2]
`41`
```

It’s not uncommon for programmers to use an "offset" variable to account for the difference in counting from 0, but it’s pretty easy to just add or subtract 1, as needed.

``` python
someArray = []
for i in range(len(someArray)):
    print("The item at position", i + 1, "is", someArray[i])
```

Python also allows for the selection of elements in an array by passing in a range that takes a "slice" of the array. The slicing approach was covered in the last chapter. The first number in the range is the index of the first element we wish to select while the second number is one more than the index of the second element.

``` python
arr = [1, 2, 3, 4, 5, 6, 7]
print(arr[3:5])
# prints [4, 5]
```

Python also allows for the omission of one or the other numbers in the range, meaning "all numbers from here" or "all numbers to here":

``` python
arr = [1, 2, 3, 4, 5, 6, 7]
print(arr[2:])
# prints [3, 4, 5, 6, 7]
print(arr[:3])
# prints [1, 2, 3]
```

You can also pass negative values when requesting array items, which means to select from the end of the array instead of the beginning.

``` python
arr=[1, 2, 3, 4, 5, 6, 7]
print(arr[-2])
# prints 6
print arr[-3:]
# prints [5, 6, 7]
```

### Arrays and For Loops

When I taught an introductory Java class, I used to tell my students that "arrays and for loops go together like peanut butter and jelly." What I mean by this is that they go together well, as a for loop is one of the easiest ways to traverse through an array by index, as shown in the example just above.

One day when I was giving this example, a student cringed and said "Ew, why would you mix peanuts with something sweet?!" I realized this was something that was not commonly done in her culture, and that not all foods are American foods. So if "peanut butter and jelly" makes you cringe, please feel free to pick your own food analogy: "Rice and beans", "fish and rice," "flour and butter", or any two foods that blend together well in your mind will do. The point is if you have to iterate over an array (peanut butter), use a for loop (jelly)!

### Arrays and Pointers

It’s a little beyond the scope of the book, but I’m going to spend just a moment on how arrays work under-the-hood, to give you a better sense of what’s actually going on.

An array is actually composed of not one but TWO pieces of data, the one you have control over and the one managed by the programming language. As I mentioned in "Weakly- vs. Strongly-Typed Languages," above, in strongly-typed languages data is allocated by type, and the type determines the size of the data in memory.

In C, a strongly-typed language, an `int` data type allocates four bytes, or 32 bits, to hold an integer value. This idea behind this is to allow programmers to use only the amount of memory they need, and no more. If you have a variable that will never go above the value 10, for instance, you might prefer using a `short` data type, which is comprised of 2 bytes, or 16 bits. The obvious disadvantage to this approach is that while you might be able to control your program you can’t control its users, and if a user enters a number that exceeds the size of the data block allocated to it, unexpected results can occur.

In JavaScript or Python, which are loosely typed languages, the script interpreter takes anything you give it, allowing the programmer to mix-and-match in memory, while minimizing the "unexpected results" I just mentioned. This does not mean that data types/sizes are not allocated though! It just happens behind-the-scenes, and the programmer doesn’t have to worry about it. A JavaScript `Number` is 64-bits in memory while an integer in Python usually occupies 32-bits — both of which are a lot more memory than needed to handle most numbers! Both languages have slightly different methods that allow allocated data chunks to scale to whatever value they’re being asked to support.

So what does this have to do with arrays?

When you initialize an array, with values, the array allocates space in memory consistent with those values. If you have ten integers in your array, there will be ten integer-sized chunks allocated in memory. With all of these different data types in a single place, how does a computer know what the "next" data value is? If a given value is a one-bit boolean number, how far away is the next value in memory? Is it one byte away from the last? Four? Eight?

This is where pointers come into play. A programming language will allocate a pointer for each item in an array, and instead of incrementing data values by some fixed number, it will increment by the size of the pointer representing that value. Strongly-typed languages will even allow programmers to do what’s called "pointer arithmetic," which can be used to create complex data-access algorithms, like the kind used in databases.

In Python and Javascript though, while you can use pointers if you want to, kinda, you really don’t have to and probably shouldn’t. Arrays in these languages should be left to the language, and even though it’s using pointers behind the scene you usually don’t have to worry about managing them directly.

Having said all of that, we will be returning to the concept of pointers as we progress through this book, with an expanded explanation coming in the very next chapter.

### Modifying (or not Modifying) Arrays

In strongly-typed languages, arrays can’t be modified in length or data type once created. This constraint leads to the desired outcome of an array always being exactly what the programmer says they are. On the other hand, this constraint leads to a certain inflexibility in managing the data in a program, because once an array is set in size and type it can’t be further modified. The rise of web programming created a generation of programmers that didn’t need or want to worry about data types in their arrays since their code was meant to run in browsers and might contain wild mixtures of user input, api calls, pieces of HTML and/or CSS, and unicorns and ice cream. So shouldn’t the management of data be the browser’s problem? And if the browser can handle it, shouldn’t browser programming languages be able to handle it too?

In that way where all old things become new again in computer programming, there has been a recent shift towards "functional programming," which insists that programmers regain control of arrays and not simply modify them according to their moods. The last chapter talked about "side effects," which is modifying original copies of data in a way that can’t be easily reversed. In "pure" functional programming you should not modify an array at all, but create a new copy every time you add or remove something from it. This keeps the array in a certain state and ensures that past states can be re-created from older copies. If you’ve ever worked with a library like Redux you might be used to this approach.

In the programming interview, make sure you understand what you’re being asked to do, and treat your arrays with intention. Don’t just blithely and blindly push information into and out of an array without understanding the problem you’re being asked to solve.

<div class="formalpara">

<div class="title">

Deep vs. Shallow Array Copies

</div>

Additionally, in some languages you can’t simply copy an array, because the copy will copy not the array but will only copy its pointers (see section "Arrays and Pointers", above). The pointers in the copy will continue to point to the data to which the original array was told to point. This means that modifying the data in the new array will modify the data in the old array, and vice-versa. This type of copy is called a "shallow" copy, as opposed to a "deep" copy. It’s important to know which type of copying your language supports, and how to get a deep copy if you need a deep copy (or a shallow copy, if that’s what you want instead).

</div>

### Basic Array Functions

Most languages contain a library of functions for arrays and questions about these functions are fairly commonly found in coding tests. These are functions that allow programmers to modify arrays in ways that make them more useful to programmers.

As you read through these examples, keep in mind that these functions — and really any functions — are not created by magic. They have been added to the language by programmers trying to make their jobs easier by making the language more useful. As you read about array functions, try to think of how you might create them yourself. Or better still, create them yourself and look inside the language specification to see how the problem has actually been solved.

Array functions fall into two general categories: modifying array data and retrieving array data. As mentioned earlier, the length of the array is important for making most of these operations work properly.

<div class="sidebar">

<div class="title">

Arrays vs. Objects vs. Tuples vs. ???

</div>

In the beginning was the array, and no other data type could be used for grouping related data.

Recently many programming languages have added "objects" as primitives, which are data types where the information is relational. Items in an object can be indexed by more than just a number, and can actually be specifically named. We will explore this idea more deeply when we get into hashes in the next chapter. In some languages, like JavaScript, there is no "array" primitive data type — all arrays are actually objects!

If that’s not already confusing enough, most modern programming languages, like Python, have realized the need to combine multiple data types in new and more useful ways. In addition to arrays, Python contains lists, tuples, and dicts, all of which are array-like data structures with specific properties for specific uses.

This book uses the term "array" to represent the general concept, but will use language specific terminology (such as Python’s "list") when discussing an array concept from the point of view of a specific language.

This book is not geared toward teaching primitive data types, so make sure you understand the different types and functions available in your specific language.

And remember, if you don’t see an array data type or function you like, you can always create your own!

</div>

Array modification functions include the following operations:

`length()` Retrieve the length of the array, usually to do something else with it. Sometimes shortened to `len()`

``` python
demoArray = [1, 2, 3, 4, 5]
print(len(demoArray)) # returns '5'
```

`for` loops Every programming language contains a function that allows for simple iteration, or "counting." Iteration is a process that has been available in programming languages from the very beginning, as it’s essential to making computers work.

`for/in` Some programming languages — usually the weakly-typed ones — support `for/in` operations, which automatically consider the length of an array in iteration.

``` python
items = ["loaf of bread", "container of milk", "stick of butter"]
for item in items:
    print(item)
```

`push() / pop()` These functions are called different things in different languages but they are for pushing an element into the end (or beginning) of an array and for retrieving an element from the beginning (or end) of an array.

`reverse()` Many programming languages contain a function for reversing a string. I showed you how to build your own reverse function in the last chapter. How does that solution compare to the built-in function of your preferred programming language? How do you know?

<div class="example">

<div class="title">

Building Your Own Built-In Functions

</div>

Knowing how to program basic built-in functions is useful because you can see how they work and because the techniques in built-in functions usually contain processes that optimize those functions. These functions are often added to programming languages because of how often they’re used, and this means they’re the basis for a lot of programming interview questions. So download the source, dig through the source code, read the spec, reverse engineer, and figure out how to program them yourself!

</div>

### Multi-dimensional Arrays

While most of the arrays programmers work with are one-dimensional, there are many times when a two-, three- or more dimensional array may be needed to solve a problem. These arrays are commonly called "nested arrays" because they contain arrays within arrays. For instance, the multiplication table example, above, is a two-dimensional array, and arrays with multiple (x, y, z) values are used extensively in creating 3D models for games or visualization. In this case the array becomes *nested*, with sub-arrays, each of which represents the values along a given dimension. A multidimensional array might also be called a "matrix," a concept we’ll return to in the problems at the end of this chapter. Here is a two-dimensional array that could be used to represent the state of a Tic-Tac-Toe board.

``` python
tic_tac_toe_2d = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)]
]
```

This bit of pseudocode contains an array containing three arrays, each of which contain three values. The number at each position represent the (row, column) that each position occupies in the two dimensional array. To access the value at any position, you have to pass two numbers to the array, like so:

``` python
square = tic_tac_toe_2d[0][2]
```

### Spread Operator

The spread operator is one of those things to know that really shows you’ve been paying attention. You can use the spread operator in a few different ways, but it’s invaluable for combining arrays and passing array data into functions:

Here a Python example of a simple use of the spread operator to pass an array into a function:

``` python
def sum(n1, n2, n3):
    return a + b + c

values = [10, 11, 12]
print(sum(*values))
```

This code sample will output the value `33`. Notice the (overloaded) star operator in the function call:

`sum(*values)`

The \* operator used in the this fashion will "spread" the values into the function call.

Here’s an example of a kind of reverse use, splitting a single piece of data into individual parts — in this case converting a string into a list of each individual character:

``` python
spread_hello = [*"hello"]
print(spread_hello)
```

This code will output the value `['h', 'e', 'l', 'l', 'o']`.

Python 3.5 and later even supports the use of the spread operator with Python dictionaries, which can be used to combine dictionaries or pass dictionary data into functions. Note the use of the double star operator in the function call:

``` python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined_dict = {**dict1, **dict2}
print(combined_dict)
```

This code will output the value `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`.

Are there other ways to do this? Yes. Are there cooler ways to do this? I just don’t think so.

JavaScript also supports the spread operator, and it can be used in a similar way to Python. Instead of the `*` operator, JavaScript uses the `…​` operator. You’re not reading that wrong, it actually is three dots.

``` javascript
function sum(n1, n2, n3) {
    return n1 + n2 + n3;
}

let values = [10, 11, 12];
console.log(sum(...values));
```

Similar to the example above, this code will output the value `33`.

JavaScript also supports the reverse case, splitting a single piece of data into multiples:

``` javascript
let spread_hello = [..."hello"];
console.log(spread_hello);
```

As you might expect, this code will output the value `['h', 'e', 'l', 'l', 'o']`.

The spread operator is great for instance of passing data into functions when you might not know what you’re expecting. Here is a common use for passing props in a React component, where some of the props are required and some are optional:

``` javascript
function SpreadComponent({requiredProp1, requiredProp2, ...optionalProps}) {
    return (
        <div>
            <h1>{requiredProp1}</h1>
            <h2>{requiredProp2}</h2>
            <p>{optionalProps.optionalProp1}</p>
            <p>{optionalProps.optionalProp2}</p>
        </div>
    );
}

let props = {
    requiredProp1: "RP1",
    requiredProp2: "RP2",
    optionalProp1: "OP1",
    optionalProp2: "OP2",
    optionalProp3: "OP3"
};

// Usage:
<SpreadComponent {...props} />
```

Note the two different uses of the spread operator in this example. The first is in the function definition, where the spread operator is used with `…​optionalProps` to collect all the optional props into a single object. You can pass in as many optional props as you want, and give them all custom names, and once the function is invoked they will all be collected into the `optionalProps` object.

The second use of the spread operator is in the function call, where the spread operator is used with `{…​props}` to pass all the props into the function. This spread operator in this instance "spreads" the props object into the function call, and the function will receive the props as if they were passed in individually.

### `argv` and `argc`, the Prime Directive of arrays

If you’re a frontend programmer you might go your whole career without ever once encountering "argv" and "argc," but if you’re a backend programmer you’re going to see them all the time. "argv" stands for "argument vector," and it is a list of arguments that can be passed into a program at runtime. "argc" stands for "argument count," or a count of the number of arguments that have been passed to the argument vector.

While they’re commonly used in C and C++, they’re available in Python and JavaScript, and can be a valuable too for passing data to a program at runtime. Node.js, for example, supports the use of `process.argv` to pass data into a a program "on the fly" at runtime:

``` javascript
console.log(process.argv);
```

It’s unlikely you’ll ever be asked about `argv` and `argc` in a programming interview, but they’re great tools to have in the box.

### JSON (JavaScript Object Notation)

JavaScript Object Notation, or JSON, is being used more and more often these days across all programming languages. It a great way to represent data that’s easy to read and immediately understand because it follows a form not too dissimilar from an outline.

``` json
{
  "animals": [
    {
      "species": "Carcharodon carcharias",
      "common_name": "Lion",
      "name": "Leopold"
    },
    {
      "species": "Canis lupus",
      "common_name": "Wolf",
      "name": "Eleanor"
    },
    {
      "species": "Elephas maximus",
      "common_name": "Asian elephant",
      "name": "Winston"
    }
  ]
}
```

JSON is often used an an intermediate data representation, because of the way in which is can readily be converted between platforms — data in a database, and data on a webpage, for example.

This chapter won’t go too deeply into it, but JSON can be considered as a form of a nested array. We’ll look at JSON more closely in the next chapter, when we talk about hashes.

## Array Searching, Sorting, and Manipulation

Now that you know the basics of using arrays with built-in functions, this next section will focus on essential algorithms for working with data in arrays. Much of computer programming is about searching, sorting, and manipulating data, and many programming interviews will require you to understand the basics of how to implement these algorithms. Even if you aren’t directly asked questions about these algorithms, they are incredibly useful tools to have in your programming toolbox and they can be used to solve many different types of programming problems.

### Sorting

Sorting is just what it sounds like: sorting data according to a given criteria.

Yes, most programming languages have a function named `sort()`, but in the context of an interview this is something you might be asked to do.

<div class="sidebar">

<div class="title">

The AlgoRhythmics

</div>

Only on YouTube: There is a collection of videos featuring Hungarian folk dancer computer scientists demonstrating common algorithms, including the Bubble Sort this chapter is about to cover.

You can see for yourself at: <https://www.youtube.com/@AlgoRythmics>

</div>

Let’s start with the most straightforward sort algorithm to understand, Bubble Sort. We’ll assume we have an array of integers that we wish to sort in ascending order.

The way Bubble Sort works is by going through an array and comparing each element with the one next to it. If the element on the left is larger than the element on the right, the elements are swapped.

This only sorts the largest element in one pass though.

So the algorithm returns to the beginning of the array and starts again, this time stopping one element before the end of the array. It repeats this process until the array is sorted.

Hopefully you see this requires nested for loops, and that the runtime of the algorithm is O(n^2). For example:

``` python
def bubble_sort(arr):
    n = len(arr)
    # Loop through all array elements
    for i in range(n):
        # The last i elements are already sorted
        for j in range(0, n - i - 1):
            # Loop through the array from 0 to n-i-1
            # Swap if the element found is greater than the one next to it
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example usage
arr = [21, 38, 25, 16, 27, 9, 12, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
# Output: def bubble_sort(arr):
    n = len(arr)
    # Loop through all array elements
    for i in range(n):
        # The last i elements are already sorted
        for j in range(0, n - i - 1):
            # Loop through the array from 0 to n-i-1
            # Swap if the element found is greater than the one next to it
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example usage
arr = [21, 38, 25, 16, 27, 9, 12, 90]
bubble_sort(arr)
print("Sorted array:", arr)
# Output: Sorted array: [11, 12, 22, 25, 34, 64, 90]
```

Bubble Sort is so inefficient that it’s rarely used in practice, but we have to start the conversation somewhere. Let’s look at a slightly more practical algorithm, the Insertion Sort algorithm.

Insertion Sort has the advantage over Bubble Sort in that it sorts the array in a single pass, placing elements into position as it goes along. It does taking elements one at a time and moving them to the left until they are in the correct position.

Here is an example of Insertion Sort in Python:

``` python
def insertion_sort(arr):
    # move through the entire array
    for i in range(1, len(arr)):
        # key is the item we wish to sort
        key = arr[i]
        # j is the index of the item to the left of the key
        j = i - 1
        # Swap left until either the key is in the correct position
        # or we reach the beginning of the array
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the key in the correct position
        arr[j + 1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print("Sorted array is:", sorted_arr)
```

We will see sorting algorithms suited more towards specific data structures or problem as we progress through this book, and will cover sorting algorithms in more detail in Chapter 12.

### Searching

Searching is when you find an item or items in a set of data. As with sorting, we’ll talk more about search in Chapter 12, but we can start the conversation here in our discussion of arrays. The main differences that determine the difference in whether of not to prefer a given search algorithm is the quantity of data being searched, and whether or not that data is in a specific order to start.

To try to gain some intuition for the differences in search algorithms, consider this simple example. Let’s say you decided to go to the pound to get a puppy. There are one hundred kennels containing dogs to choose from. You walk past all the kennels and you see a dog you just love named "Harry."

The animal trainer who works at the pound hands you a stack of papers and says you have to find Harry’s paper to take him home. The papers aren’t sorted. Right off the bat it would clearly be easier to search through the stack if the papers were already sorted. But stop for a moment and think about how you’re going to do that? Are you just going to page through the papers from A-H until you find Harry? Start the search at Z? Something else? Would you search through the papers the same way if there were only 10? Or 10,000? But it’s not any of those things; it’s a stack of 100 unsorted papers. So how are you going to go about finding "Harry?" Stop and consider these questions for a moment before moving on.

Let’s start with a simple search: the binary search. You may have used this one before if you’ve ever played "Guess the Number." Someone says to you, "I’m thinking of a number between one and 100 and if you can guess the number in 6 guesses or fewer, I’ll give you \$5. After every guess I’ll tell you if my number is higher or lower than the one you choose." Does it matter that you’re told whether or not the number is higher or lower after every guess? Why? How would you go about solving this problem?

Even people who have never played the game before will quickly come up with winning strategies. It doesn’t make a lot of sense to guess numbers in ascending order from 1 because that would give you only about a 5% chance to guess the number before running out of guesses. You’re also only going to guess numbers based on the clues provided to you by the person who makes the offer. If you guess 71, and she tells you it’s going to be higher than 71, it makes no sense to guess 20 on the next turn.

The foolproof way to win this game every time is by conducting a binary search. The reason it’s called a binary search is because every guess reduces the remaining number pool into two parts, and then eliminates one of them from further consideration.

Following this strategy, your first guess should be 50. It cuts the remaining number pool in half. If the person says "higher" you know the number is between 51 and 100. If the answer is "lower" then it’s between 1 and 49.

The response you get is "lower," so you need to cut the space in half again. You guess 25. The response you get is "lower" and so you cut the space between 1 and 25 right down the middle with a guess of 13. "Higher" is the response, so you guess 19. "Higher" again, so you guess 22. "Higher" one last time and you’ve guessed the number: 23.

That might have seemed like a lot of guesses, but you couldn’t have done any better without luck. (And I deliberately chose a number that would take several guesses to find.)

In fact, 7 guesses is the maximum number of guesses you’ll need to guess any number between 1 and 100 using binary search.

The great thing about binary search is it scales logarithmically. Go back and look at the O(log n) graph in Chapter 2 if you don’t remember what it looks like. Because it grows logarithmically, every time the number of inputs doubles, the number of guesses required to get the answer only increases by one. If someone wants to play this game with you using a number between 1 and 1,000,000, you are guaranteed to guess the number in 20 guesses of fewer using binary search.

Here is a simple implementation of binary search to guess a number between 1-100. This is not meant to be a complete application, just some basic code to illustrated the big idea.

``` python
def binary_search(arr, target):
    left = 0
    right = 100
    # Make guess, receive feedback in the
    # form of "Higher" or "Lower"
    while left <= right:
        # Split the remaining guess space in half
        guess = left + (right - left) // 2
        if guess == target:
            print ("Winner!")
        elif arr[mid] < target:
            left = guess + 1
        else:
            right = guess - 1
```

Now that I’ve covered the basics, let’s see how this could be used to find the position of a value in an array. The numbers 1-100 have a property that makes them perfect for binary search, in that they’re already sorted in order. Given a number between 1-100, I can be assured that every number to the "left" of that number on the number line is smaller, and every number to the right is larger. The leads to an important consideration when using binary search: the data must be *sorted* for the algorithm to work.

Consider this array:

``` python
array = [21, 3, 47, 10, 40]
```

How could you use binary search to find the array position of the number 10? What would your first guess be? If you guess position three, the number 47, then the binary search answer would be "lower", but the number 10 is not lower than 47.

This is something to keep in mind when choosing the right algorithm for an interview response. If the data is not sorted, then binary search will not work. If the data must first be sorted, then the Big O of the sorting algorithm becomes as much of a factor as the Big O of the searching algorithm.

There are algorithms that work with unsorted data and, as mentioned above, we’ll be taking a look at some of these in Chapter 12.

### Sliding Windows

Many problems that involve subsets of strings can be solved using the so-called "sliding window" technique. Just like it sounds, the technique involves moving a data "window" over a string, and collecting, analyzing, or manipulating the data in that window.

In languages that support them, the sliding window technique is implemented using data pointers. In languages that don’t support pointers the technique requires the coder to create their own pointers, but fortunately that’s not a terribly difficult thing to do. A pointer is just a variable that contains the location of another variable. You can think of it like this: imagine you’re looking at a row of lockers. You can’t see what’s in the lockers, but you can see the numbers on the front of the lockers. In front of the lockers stands a robot who knows what’s in each locker. You ask can ask the robot two questions: "What’s in locker x?" "Which locker contains item x." In this analogy, the robot is the pointer, the lockers are the array, and the contents of the lockers are data.

You use a type of pointer when iterating over a for loop, with a variable that is usually named `i`.

``` python
for i in range(len(arr)):
  print(arr[i])
```

In this case, `i` is the pointer that will go down the line of "lockers" represented by the array `arr`, and "open" (also called "dereference") each locker to see what’s inside, returning the contents to the "print" function. Keep this analogy in mind as you go over the sliding window problem. The sliding window is literally a window — or multiple windows — that allow us to see what’s in the lockers. You can assign logical conditions to these windows, and use them to solve problems that involve subsets of strings.

Example Sliding Window Problem:

*Given an array of integers, find the two adjacent integers with the largest sum.*

Array: \[22, 1, 21, 12, 7, 19, 9, 3, 8, 17, 2, 20\]

Looking the array over quickly it’s not too hard to see that the two adjacent integers with the largest sum are 21 and 12, which add up to 33.

Let’s start by solving this problem with a brute force solution. In this case, a nested for loop is great place to start. In this solution, the variables `i` and `j` are used as the "pointers", and because j always equals `i + 1`, the sum of any two adjacent integers can be calculated by adding `arr[i]` and `arr[j]`, which comprise the two-element "window" that is moved over the array:

``` python
def largest_sum(arr):
  largest = 0
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] + arr[j] > largest:
        largest = arr[i] + arr[j]
  return largest
```

Great start, but it’s not the most efficient solution. Nested for loops should always come under consideration for optimization, as their runtime is O(n^2) — the dreaded "quadratic." So how can we do better? Do we really need to use two for loops? Can we just run that single comparison "window" over the array and get the same result? Let’s try it!

``` python
def largest_sum(arr):
  largest = 0
  for i in range(len(arr) - 1):
    if arr[i] + arr[i + 1] > largest:
      largest = arr[i] + arr[i + 1]
  return largest
```

Excellent! We’ve eliminated the nested for loop, and now the runtime of the function is now the preferable "linear" time of O(n).

So that’s a simple example of the sliding window technique. Let’s look at a more complicated example. Now the interviewer asks you to find the longest substring within a given string that contains only unique characters. For instance, if you’re given the string:

"abbcaabdcbb"

The answer is "abdc", because it’s the longest substring that contains only unique characters.

Let’s first try to get this with a brute force solution:

``` python
def longest_unique_substring(s):
  longest = 0
  for i in range(len(s)):
    for j in range(i + 1, len(s)):
      if len(set(s[i:j])) == j - i:
        if j - i > longest:
          longest = j - i
  return longest

someVar = "abbcaabdcbb"
print(longest_unique_substring(someVar))
```

This might be an example of where the brute force solution is a little more brutal than it needs to be, but I wanted to take a moment to talk about the `set()` data type. A "set" in math and logic is a group of related but *distinct* items, be they words, number, objects, etc. The days of the week are a set, as are the months of the year. Notice that the days of the week are distinct, there aren’t two Tuesdays, thank goodness.

`set()` (or `new Set()` in JavaScript) is a function that creates an empty set. If you pass it an array, it takes the array and returns one of each unique element in that array. What’s returned is probably not going to be in any kind of determined order. For instance, here’s what happened when I just ran the line of code:

``` python
>>> print (set ("abcdeabcdeabcde"))

{'d', 'a', 'b', 'c'}
```

Correct! But why in that order? I don’t really know, and I don’t think it matters.

Additionally, you cannot add duplicate values to a set. For instance:

``` python
# Create an empty set
numbers = set()

# Add a number
numbers.add(1)
print(numbers)  # Output: {1}

numbers.add(2)
print(numbers)  # Output: {1, 2}

# Try to add an existing number again
numbers.add(1)
print(numbers)  # Output: {1, 2} (no change!)

# Check if number exists
print(1 in numbers)  # Output: True
```

Why I’m discussing this is because you might be asked about using `set()` to solve problems related to uniqueness, and sometimes it absolutely is the right tool for the job. In this case, however, it’s not. Can you see why?

Consider the run time of the `longest_unique_substring()` function above. Using `set()` to iterate repeatedly over chunks of items in the string can be considered a third nested loop, and so the runtime of the function is now O(n^3), which is a shape I didn’t even mention in the section on Big O because hopefully you won’t come across it all that often. So if you’re asked "Why didn’t you use `set()`," be careful, it’s a trick question! Let’s see how sliding windows can help solve this problem more effectively.

``` python
def longest_unique_substring(s):
    longest_length = 0
    start = 0
    longest_start = 0
    char_index_map = {}

    for end in range(len(s)):
        char = s[end]
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        if end - start + 1 > longest_length:
            longest_length = end - start + 1
            longest_start = start

    return s[longest_start:longest_start + longest_length]

test_var = "abbcaabdcbb"
print(longest_unique_substring(test_var))  # Output: "abdc"
```

### Python List Comprehensions

Python has an insanely useful paradigm called "list comprehension" that allows you to create lists in a single line of code. It combines a for loop and a conditional statement into a single line of code. JavaScript can also do this using the `map`, `reduce`, and `filter` functions, but it’s hard to beat Python’s approach for simplicity. While list comprehension problems will not show up in LeetCode questions, using it to solve problems in an interview is a great way to show that you have a good grasp of the Python language.

The basic syntax of a list comprehension is:

    `[expression for item in iterable if condition]`

Here, for instance, is a simple list comprehension that creates a list of the squares of the numbers from 1 to 10:

``` python
squares = [x**2 for x in range(1, 11)]
print(squares)
```

This code will output:

`[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`

Let’s say we want to go back over that list and cube any even number. That can be done with a list comprehension as well:

``` python
cubes = [x**3 if x % 2 == 0 else x for x in squares]
print(cubes)
```

This code will output:

`[1, 64, 9, 4096, 25, 46656, 49, 262144, 81, 1000000]`

List comprehension can even be used to combine two more lists into a single list, for example:

``` python
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

# Combine the two lists into a third list using a list comprehension
combined_list = [(x, y) for x, y in zip(list1, list2)]

print(combined_list)
```

This will output:

`[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]`

### Sample Questions

Here are some questions about arrays that are commonly asked in interviews. The same problem might come with a different description, so make sure you focus on the general idea without getting too bogged down in the specific problem. These questions can be found as exercises on most programming interview websites, so get in some practice if you can.

#### Container With Most Water (2 Pointer Solution)

This problem comes in a few different forms, but the idea is that you’re given an array of integers that represent the height of a series of walls. Which two walls can be used to create the container that holds the most water?

As always, spend a moment trying to reason this problem out before attempting to answer. You can’t solve a problem you don’t understand.

You have two axis that determine the shape of the container. The x-axis is the distance between the two walls, and the y-axis is the height of the shorter of the two walls that make up the sides. Why shorter? Because if the water was the same height as the taller wall, it would simply spill over the top of the shorter wall.

So the x-axis, the distance, is determined by the distance between the two "walls" in the array.

Clearly this question has little to do with walls and water. It’s really about finding the maximum area of a rectangle — width times height — that can be formed by two lines on a graph. This is the kind of reasoning you can do out-loud during the interview to show your thought process.

From here the brute force solution should suggest itself: check the area of the rectangle formed by every "wall" in the array against every other rectangle and return the biggest one. That approach would look something like this:

``` python
def max_area(heights):
    # Start with a variable to hold the maximum area
    max_area = 0
    # Get the length of the array
    n = len(heights)

    # Iterate over all pairs of lines
    for i in range(n):
    # remember to use i + 1 so you don't compare a line
    # to itself
        for j in range(i + 1, n):
            # Calculate the width between the "walls"
            width = j - i
            # Determine the height of the shorter side of the container
            container_height = min(heights[i], heights[j])
            # Calculate the area of the container
            current_area = width * container_height
            # Update the maximum area if the current area is larger
            max_area = max(max_area, current_area)

    return max_area

# Example usage
heights = [3, 16, 7, 19, 1, 12, 8, 5, 14, 10]
print(max_area(heights))  # Output: 80
```

Two things are immediately apparent about this solution: 1. It gives the area, but not the two walls that make up the container. 2. It’s a brute force solution, with a runtime of O(n^2), which can likely be improved.

I’ll leave the solution to \#1 up to you, but let’s think for a moment about the solution to \#2. At this point the interviewer might even give you a hint: "Since the maximum width is the leftmost and rightmost wall, maybe you can optimize by working from the outside in."

In other words, you don’t have to compare every wall to every other wall. You can start with the outermost walls and work your way in, comparing the area of the container formed by the two walls. This can be determined by using the "two pointer" technique, which is commonly used on certain array problems.

For "pointers" we can use two variables called "left" and "right" that start at the beginning and end of the array, respectively. By incrementing the left pointer while decrementing the right pointer, we can bring the two walls together until we have found our solution.

The code for our new and improved approach might look something like this:

``` python
def max_area(heights):
    # Start with a variable to hold the maximum area
    max_area = 0
    # Initialize the left pointer
    left = 0
    # Initialize the right pointer, accounting for the
    # zero-based index
    right = len(heights) - 1

    # while the walls are not touching
    while left < right:
        # This part is similar to the previous solution
        width = right - left
        container_height = min(heights[left], heights[right])
        current_area = width * container_height
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage
heights = [3, 14, 7, 19, 1, 12, 8, 5, 16, 10]
print(max_area(heights))  # Output: 80
```

This solution is much more efficient, bringing our runtime down from O(n^2) to O(n). (Reason through why this is the case if it’s not obvious to you already.) It also makes it report on the values chosen, since that only requires printing the values for "left" and "right," should you be asked to do so.

The two-pointer technique is a valuable technique for solving array-based problems, and we will see it again later in this book.

#### Two Sum / Three Sum

The Two Sum problem is a *classic* interview question where you are given a target number and an array of numbers, and asked to find the two numbers in the array that add up to the target number.

The Three Sum problem is a variation of the Two Sum problem where you are given a target number and an array of numbers, and asked to find the three numbers in the array that add up to the target number.

For example:

Array: \[2, 31, 5, 90, 7, 11, 15\] Target Number: 9

The solution to this number is \[0, 4\], because 2 + 7 = 9.

Before you start answering this problem, you will want to be sure to ask the interviewer if there are any specific constraints on the problem. For instance, are there multiple answers to the problem? Is the problem guaranteed to have a solution? Does the order of the solution matter? Are there any constraints on the numbers in the array?

Once again, let’s start with a brute force solution to Two Sum, using nested for loops:

``` python
def two_sum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None
```

This algorithm loops through the array twice, comparing each number to every other number in the array. Notice in line 3 that the second loop starts at `i + 1`, because there’s no need to check the same number against itself. Hopefully it doesn’t come as much of a surprise to find this code runs in O(n^2) time, or that nested for loops is not the most efficient way to solve this problem.

So how can we do better?

``` python
def two_sum(array, target):
    num_index = {}
    for i, num in enumerate(array):
        if target - num in num_index:
            return [num_index[target - num], i]
        num_index[num] = i
    return None
```

Python contains a built-in function called `enumerate()` that can be used to loop over an array and return both the index and the value of each item in the array. If you’re familiar with Javascript, `enumerate()` is similar to using the `map()` function with an index parameter.

A similar implementation in JavaScript might look like this:

``` javascript
function twoSum(array, target) {
    const numIndex = {};
    let result = null;

    array.map((num, i) => {
        const complement = target - num;
        if (complement in numIndex) {
            result = [numIndex[complement], i];
        }
        numIndex[num] = i;
    });

    return result;
}
```

In both cases the code sets up a "compliment," which is the difference between the target number and the current number in the array. The Python version uses a dictionary to store the index of the compliment, while the JavaScript version uses an object. In both cases the code checks to see if the compliment is in the dictionary or object, and if it is, returns the index of the compliment and the current index. If the compliment is already in the dictionary (or object), the current number is a match, and the function returns the indexes of the two numbers that add up to the target number. Pretty straightforward, right?

By working with a running compliment, the function can find the answer in a single pass thorough the array, which I hope you immediately recognize as O(n) time.

The Three Sum problem is a little tricker, but it can be solved using a similar approach. I’m going to skip the brute-force method because it will involve three nested for loops, or O(n^3) time, and since we’ve already seen an improvement we will never go back.

Here is a Python solution to the Three Sum problem:

``` python
def three_sum(array, target):
    for i in range(len(array)):
        num_index = {}
        new_target = target - array[i]
        for j in range(i + 1, len(array)):
            if new_target - array[j] in num_index:
                return [i, num_index[new_target - array[j]], j]
            num_index[array[j]] = j
    return None
```

This works similar to the solution for Two Sum, but there is an additional loop thrown in to account for the third number in the array. This bumps the runtime up to O(n^2), which is still faster than O(n^3), but not as fast as O(n) time.

Think about it: can the Three Sum problem be solved in O(n) time?

There’s one additional way to solve this problem using pointers, called the two-pointer technique that I discussed in the container problem. Since you’ve already seen that technique, I’ll provide you with the code and allow you to reason through it on your own:

``` python
def three_sum(array, target):
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target:
                return [i, left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None
```

Think it through: What is the runtime of this solution? What advantages does it have over using nested for loops?

#### Array Rotation

Array rotation questions are good ways to test how a candidate approaches the logic of a problem, as there are many different ways in which an array rotation can be accomplished. "Rotation" in the context of arrays simply means moving all of the values to the left or right by a certain number of spaces. As items move to the right or end of the array, they wrap around to the left or beginning of the array. "Rotation" can also be referred to as "shifting" of "cycling" items in an array. For a very basic example of why it’s useful, shifting all of the digits of a binary number to the left multiples the number by two, while shifting to the right divides by two. Many programming languages have built-in operators for shifting bits, such as the `<<` and `>>` operators in Python.

`128 << 1 = 256`

`1024 >> 1 = 512`

For instance, an interview question might read,

"Given an array of integers, rotate the array to the right by k steps."

You should be given a positive integer for k. If you are given a negative integer, that should be a clear signal that it’s time to ask questions. Don’t just make the assumption that a negative integer means rotating the array to the left. It could also mean adding zeroes to the array, or have some other significance that is not readily apparent.

As usual, start by reasoning through the problem before you start coding. Python contains several built-in functions for pushing items into and returning items from an array, several of which we covered earlier in this chapter.

You may even know that Python has a built-in function for rotating an array, and if you’re familiar with it, you can ask the interviewer if it’s appropriate to use it for the answer. But that’s not what we’re here to learn.

The challenge with moving items in an array is that you have to be careful not to lose any of them. The items that go off to the right have to be accounted for in a way that makes it possible to move them back to the left. You might immediately be tempted to create an additional array to "hold" the values that are pushed off the end of the array, but this is a problem that can absolutely be solved "in place," which means not creating additional space to hold data in memory.

``` python
def rotate_array(arr, k):
    # Get the length of the array
    n = len(arr)

    # If k is greater than the length of the array, reduce k
    while k > n:
        k -= n

    for _ in range(k):
        # Pop off the last element and insert it at the beginning
        last_element = arr.pop()
        arr.insert(0, last_element)

    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_arr = rotate_array(arr, k)
print(rotated_arr)  # Output: [5, 6, 7, 1, 2, 3, 4]
```

Simple pimple! Take the last item off the array and push it back onto the array *k* number of times, problem solved!

What might be the cause of some confusion is these lines:

``` python
while k > n:
    k -= n
```

It may have occurred to you to wonder, can’t we simply subtract k from n so we know the number of times to rotate the array? So that works fine if the number of rotations is less than the length of the array, but what if it’s not? This leads us to our first optimization:

``` python
def rotate_array(arr, k):
    # Get the length of the array
    n = len(arr)

    # Use the modulo operator instead of a while loop.
    k = k % n

    for _ in range(k):
        # Pop off the last element and insert it at the beginning
        last_element = arr.pop()
        arr.insert(0, last_element)

    return arr
```

<div class="sidebar">

<div class="title">

Behold, the Modulo Operator!

</div>

If you’ve ever taken a course in computer programming, at some point you were probably introduced to the module operator, or *%*. The modulo operator is used to find the remainder of a division operation. In grade school, for example, you may have learned to write the answer to a long division problem using a remainder. "11 divided by 3 is 3 with a remainder of 2." or "11 *r* 2" Or, in computer terms, `11 % 3` will return `2`.

Everyone learns that…​and then forgets it! Who needs that? When will I need the remainder?

The modulo operation is actually incredibly useful in programming, and can be used to solve many different types of problems. You will see it used more than once in this book, so vow to make friends with it now if you haven’t already.

</div>

What is the purpose of the modulo operator in this case? Think of a case where the array is five items long (n), and you’re asked to rotate it 17 times (k). If you think about it, because a rotation always starts again where it ends, rotating an array three times is the same thing as rotating it once. You’ll get the exact same result, right?

By using modulo, you can skip those extra three rotations. All you need to do is focus on the modulo — remainder — of `k % n` and rotate the array that number of times.

In this case were n is 5 and k is 17, `k % n` = `2` and so the array only needs to be rotated twice.

Additionally, we can use a more "pythonic" approach by using slicing to solve the problem. As you may know (or recall from earlier in the book) in python we can slice items in an array by including the array index range in brackets. This brings us to the following solution:

``` python
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k is greater than the length of the array
    return arr[-k:] + arr[:-k]
```

Of course, as with most things involving computers, there is more than one way to solve the shifting problem. In addition to using slicing to solve the problem, we can also use an approach based on reversing the entire array, splitting into two pieces, and then reversing each piece.

``` python
def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    # Step 1: Reverse the entire array
    reverse(arr, 0, n - 1)

    # Step 2: Reverse the first k elements
    reverse(arr, 0, k - 1)

    # Step 3: Reverse the remaining n - k elements
    reverse(arr, k, n - 1)

    return arr
```

There’s not really an advantage to reversing over slicing, as both run in O(n) time. But both approaches are worth knowing about as they may come up as solutions to other problems as well.

#### Permutations

"Permutations" involves putting every item in a set of items into every possible combination in relation to other items. For instance, here are all of the permutations of the array \["cat", "dog", "mouse"\]:

Exciting stuff, no? I’ve given a simple example here, but permutations can be used to solve many types of programming problems. They’re especially useful when you’re looking for an optimal solution to a problem, as they can quickly generate all possible combinations which can then be quickly used to determine which solution is best.

When it comes to permutations there are two primary questions involved: 1. Given a starting set of data, how many permutations can be created? 2. How can you generate all of the permutations?

There may be additional questions involving the creation of permutations given certain conditions (like, you can’t put the cake into the oven before you mix the batter), or considering a reduced set of items (if you have six pairs of sneakers, how many combinations can you make only using three of them at a time) but in this section we’re going to focus only the two questions above.

The answer to the first question is simple: it’s the factorial of the number if items in the set. You might remember factorials from high-school math class, but if you don’t, a factorial of 5 is written as:

5!

And represents the product of all of the positive integers from 1 to 5:

1 x 2 x 3 x 4 x 5 = 120

So if you have a set of 5 items, there are 120 possible permutations — combinations — of those items.

So how can we generate permutations? Permutations is a problem that I’ll return to throughout the book, as the solutions will become both more sophisticated and easier to implement as we further explore data structures and algorithms.

In the mean time, let’s start with this awfully iterative approach:

``` python
def permute(arr):
    result = []
    n = len(arr)
    c = [0] * n  # Initialize the counter array
    result.append(arr.copy())

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]  # Swap for even index
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]  # Swap for odd index
            result.append(arr.copy())
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return result

animals = ["lion", "tiger", "bear", "dog", "guppy"]
permutations = permute(animals)

for perm in permutations:
    print(perm)
```

This will print out:

\['tiger', 'bear', 'lion', 'dog', 'guppy'\] …​ etc …​

These permutations are generated by an algorithm known as Heap’s algorithm. (Believe it or not, that’s a persons name that has nothing to do with the heaps we’ll discuss in chapter 7. A computer programmer named Heap? What’s next, a poker player named Moneymaker?) I’ve provided a simple and non-recursive implementation of this algorithm which works by using an array index and a "counter" array to keep track of the permutations.

At the start of the program the counter array is initialized to all zeroes, and first permutation — the array we start out with — is added to the results array. The algorithm then iterates through the candidate array using the index `i` and the counter index `c[i]`. For each iteration, the algorithm checks if the counter is less than the index, and if it is, it swaps the first element of the array with the element at the index, based on whether the index is even or odd. The counter index is then incremented, and the algorithm starts over at the beginning of the array. If the counter is greater than the index, the counter is reset to zero and the index is incremented. That’s a lot to understand, but if you code it in and play with it for a bit it’s pretty easy to see what it’s doing.

What is the running time of this algorithm? (Hint, I’ve already told you, above.)

If you don’t understand don’t worry too much as I’ll come back to this question again in later chapters and with a more efficient solution.

The last three examples in this chapter are going to cover games. Everyday games are useful for testing algorithmic knowledge because they can be used to cover a discrete problem set with rules that are usually well known.

We’re going to cover three games in these last examples: Tic-Tac-Toe, Chess, and Sudoku. In this section I’m going to talk through the reasoning of building from simpler principles to a bigger idea, breaking each problem down into smaller and smaller steps until it consists of a number of relatively simple problems.

It’s my hope that you can follow my reasoning in a way that shows you how you can build up your ideas during an interview, and the kinds of things you’ll need to take into consideration as you do. While it’s fairly unlikely that you will be asked to complete one of these takes in total during an in-person interview, you might be asked to complete a portion of one of them as a test of your reasoning and problem-solving skills, and the ways in which you respond to feedback. Or you might be asked to solve a similar complex task, and hopefully these examples give you an idea of how to proceed with confidence.

#### Winning Tic-Tac-Toe

Tic-Tac-Toe (also called "Noughts and Crosses") is a great game for improving your knowledge of programming concepts because it has simple rules and a limited number of outcomes. There are only two players, and the game can go no more than nine moves long. xkcd, the best computer programming comic ever, \[has mandatory coverage of the subject\](<https://xkcd.com/832/>).

Depending on how you choose to count, there are roughly a quarter-million possible games of Tic-Tac-Toe, which isn’t really a lot for a computer. It’s even less when you consider that most of those games are duplicates of each other, since nearly 90% of them are rotations or reflections of the same game board. This section will give some ideas on how to get started, but it won’t cover the logic of the game in its entirety. That exercise is left up to the reader!

It’s easy to create a simple turn-based game of Tic-Tac-Toe in pretty much any programming language. Once you’ve got the basic game play set up, then next problem is to determine the four states of the game: 1. Player Turn 2. Player X wins 3. Player O wins 4. Draw

Once you’ve got that down, you can begin to think of how to create a computer opponent that can play the game. Beyond simply making random moves, the complexity of computer play generally involves three levels, in order of difficulty to implement: 1. Always make a move that blocks an opponent win 2. Always make a move that wins the game 3. Always make the best move

For this question we’re going to focus on four basic parts of play: 1. Determining if a player has won or the game is a draw 2. Determining how to play a blocking move 3. Determining how to play a winning move

Tic-Tac-Toe is often used to ask array questions in interviews because the game board can be represented in two primary ways: as a one-dimensional, 9-element array, or as a two-dimensional, 3x3 array. The 1-D array is easier to work with, but the 2-D array is more intuitive for humans to understand, so we’ll stick with that representation in this question.

Let’s consider this game only from the point of view of player "X", the first player to play.

A one dimensional array of a Tic-Tac-Toe board looks as you’d expect, a list of nine moves:

``` python
tic_tac_toe_1d = ['X', 'O', 'X', ' ', 'O', ' ', ' ', 'X', 'O']
```

Again, just because it’s easier to work with, we’re going to use the dimensional representation, which would look like this:

``` python
tic_tac_toe_2d = [
    ['X', 'O', 'X'],
    [' ', 'O', ' '],
    [' ', 'X', 'O']
]
```

A computer has no way of knowing how to play Tic-Tac-Toe, of course, and so doesn’t know what a winning move looks like. Here is a two-dimensional list of the winning moves by list, column, and diagonal. By checking against this list, the computer can determine whether or not it’s won or is about to win (or lose!) a game of Tic-Tac-Toe, or if the game has resulted in a draw:

``` python
winning_combinations = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]
```

This list can be used to check and see if there is a winner, starting with this brute-force approach:

``` python
def check_winner(board, player):
    for combination in winning_combinations:
        all_match = True
        for i, j in combination:
            if board[i][j] != player:
                all_match = False
                break
        if all_match:
            return True
    return False
```

This code takes the representation of the board, and the letter of the player to evaluate. It then sets the boolean `all_match` to True, changing it to False if no match is found among the winning combinations.

``` python
def check_winner(board, player):
    for combination in winning_combinations:
        if all(board[i][j] == player for i, j in combination):
            return True
    return False
```

#### N-Queens

The queen is the most powerful piece in chess. She can move across the board in a single bound down any rank, file, or diagonal.

The N-Queens problem is a classic of computer science that involves placing N queens on an N x N chess board in a way that no queen can attack any other on her rank, file, or diagonal. So of course, there’s an algorithm for it!

I’ll start by designing the board as a two-dimensional array, or matrix, with a "1" to represent a queen and a "0" to represent an empty space.

It’s important when you work on algorithms that have the potential to become complex that you start with the simplest thing that could possibly work. So before we build to a full 8x8 chess board, let’s start with a quarter of that, a 4x4 board.

One way to represent that board might similar to what we did in the tic-tac-toe example, using a matrix.

``` python
chess_board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
```

From here it’s simple, right? Just check every array to make sure it only contains a single "1", then some check every column to make sure of the same and then check every diagonal. Those first two seem pretty straightforward, but the third might not be quite so easy. Take a moment to think about it before you read on.

Let’s start with the easy one, checking each row to make sure it only contains a single "1."

``` python
def check_matrix(matrix):
    for row in matrix:
        if row.count(1) != 1:
            return False
    return True
```

If you pass in this matrix, it will return True, and so we have a match!

``` python
valid_matrix = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
```

If you pass in this matrix it will also return true:

``` python
also_valid_matrix = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1]
]
```

…​but what you may have noticed is that while this matrix works well for the row checks, it is an invalid solution to the N-Queens problem because two "1’s" appear in the first column.

Let’s try now to add column checks. First we’ll start by just checking the columns for a single "1", as we did with the rows.

``` python
valid_matrix = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
```

This one is a little tricker, but the idea is exactly the same: counting the number of "1’s" in a column to make sure there is one and only one in each.

``` python
def check_columns(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for col in range(num_cols):
        count = 0
        for row in range(num_rows):
            if matrix[row][col] == 1:
                count += 1
        if count != 1:
            return False
    return True
```

I’ll let you test this one on your own. Again, we run into a similar problem as with the row solution. The matrix…​

``` python
also_valid_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
]
```

…​will pass the column test, but is not a valid solution to the N-Queens problem because there are two queens in the first row that can attack each other.

At this point you can proceed in one of two ways. You can try to bring the row and column checks together into a single function, or you can try to solve the diagonal problem first. Think about it for a moment. Which do you choose? Why?

While I could make a case for either approach, for the purposes of pedagogy I’m going to solve the diagonal problem before integrating the three solutions. This one takes a bit of tricky reasoning.

One important thing to realize before you attack this problem is that the diagonals run in not one but two directions. If you only check the diagonals from top-left to bottom-right, you might come up with a solution that is valid in only one direction. For instance:

``` python
invalid_diagonal_matrix = [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]
```

If I’m only checking the diagonals from top-left to bottom right, I will get a valid solution even though the diagonal formed by the 1s in the second, third, and fourth rows clearly make this an invalid solution, forming a diagonal that goes from column 2 in the fourth row to column 4 in the second.

With that in mind, let’s start by checking top-left to bottom right diagonals first. It might help to first draw a picture that helps you see the seven diagonals that run from top-left to bottom-right on a 4x4 matrix.

From there, perhaps it’s useful to use a coordinate system to see what the position of each diagonal is in the matrix. You may have already noticed that the single-digit diagonals — the one in the top-left corner and the one in the bottom-right corner — don’t need to be checked. Let’s write out the list of the five remaining left-to-right diagonals:

From \[0, 2\] to \[1, 3\] From \[0, 1\] to \[2, 3\] From \[0, 0\] to \[3, 3\] \# — the longest! From \[1, 0\] to \[3, 2\] From \[2, 0\] to \[3, 1\]

\<IMAGE TK\>

Now that we have the coordinates of the diagonals, we can use this to establish a pattern that allows us to write a function to check them.

``` python
def check_diagonals(board):
    num_rows = len(board)
    num_cols = len(board[0])

    for start in range(num_rows + num_cols - 1):
        count = 0
        for i in range(max(0, start - num_cols + 1), min(num_rows, start + 1)):
            if board[i][start - i] == 1:
                count += 1
        if count > 1: # There's more than one queen in the diagonal!
            return False
    return True
```

What about top-right to bottom-left, the so-called "anti-diagonals?" It’s a little tricker, but the idea is the same, just in reverse.

``` python
def check_anti_diagonals(board):
    num_rows = len(board)
    num_cols = len(board[0])

    for start in range(num_rows + num_cols - 1):
        count = 0
        for i in range(max(0, start - num_cols + 1), min(num_rows, start + 1)):
            j = num_cols - 1 - (start - i)
            if 0 <= j < num_cols and board[i][j] == 1:
                count += 1
        if count > 1:
            return False
    return True
```

At this point can you see how you could combine the diagonal and anti-diagonal checks into a single function? It’s an intermediate step but I encourage you to try to figure it out. Is it "better" to combine the two functions into one, or to keep them separate?

Now that it’s possible to check in all three directions, here is an algorithm that combines all three checks into a single function:

``` python
def check_board(board):
    return check_rows(board) and check_columns(board) and check_diagonals(board) and check_anti_diagonals(board)

def check_rows(board):
    for row in board:
        if row.count(1) != 1:
            return False
    return True

def check_columns(board):
    num_rows = len(board)
    num_cols = len(board[0])

    for col in range(num_cols):
        count = 0
        for row in range(num_rows):
            if board[row][col] == 1:
                count += 1
        if count != 1:
            return False
    return True

def check_diagonals(board):
    num_rows = len(board)
    num_cols = len(board[0])

    for start in range(num_rows + num_cols - 1):
        count = 0
        for i in range(max(0, start - num_cols + 1), min(num_rows, start + 1)):
            if board[i][start - i] == 1:
                count += 1
        if count != 1:
            return False
    return True

def check_anti_diagonals(board):
    num_rows = len(board)
    num_cols = len(board[0])

    for start in range(num_rows + num_cols - 1):
        count = 0
        for i in range(max(0, start - num_cols + 1), min(num_rows, start + 1)):
            j = num_cols - 1 - (start - i)
            if 0 <= j < num_cols and board[i][j] == 1:
                count += 1
        if count > 1:
            return False
    return True
```

That’s a longish piece of code, but it solves the problem. It was reasoned from the first basic problem to the last and more complex, and solved by breaking the larger problem into a series of smaller steps. This is great way to reason through and answer an interview question.

#### Valid Sudoku

Sudoku is a popular numbers game that you can find in newspapers, puzzle books, and online. It’s a simple idea with many variations. The player is given a 9x9 grid of squares that is further subdivided into 9 3x3 grids of squares. Into each grid square the player can place a number from 1 to 9. The player must complete the grid from a set of starting hint numbers such that no number is repeated in any row, column, or 3x3 grid in the 9x9 grid of squares.

This leads to a number of potential interview questions, but let’s start with an easy one: Given a 9x9 grid with some or all of the squares filled in, is the grid valid per the rules of Sudoku? In other words, does the grid contain any repeated numbers in any row, column, or 3x3 grid?

Note that the question does not ask if the solution is the correct solution or a unique solution or a preferred solution, nor does it ask you to solve the puzzle. It just asks for an algorithm that determines if the presented grid is valid.

When presented with this question, it’s likely that you will be given a grid to check, so in this particular case you probably won’t have to create your own data structure to represent the grid.

I’m gonna take a second to reason through it though. What is your idea of how the data can be structured? Three ideas come to mind immediately: 1. An array/list of all 81 numbers in the grid. 2. Representing each puzzle section with a 3x3 matrix of 3x3 matrices, or 3 lists of 3 lists of 3 numbers. 3. A 9x9 matrix of numbers, or 9 lists of 9 numbers.

Looking at the pros and cons for each, we can "goldilocks" the solution. The first solution is easy to think about as a line, but you have to put some work in to converting the values of a 1D array into those of the 2D array that represents the Sudoku board. It’s good to know how to turn 1D into 2D and 2D into 1D, so I’m going to take this golden (see what I did there?) opportunity to provide an example. It’s a fairly common operation in graphics programming, or perhaps programming large amounts of tabular data. For the purposes of this particular exercise I’m going to start by shrinking the problem space down to a 4x4 grid.

1D: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`

2D: `[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]`

Let’s start with converting a position in 1D into a position in 2D. For starters, consider that as with most things array we will count from zero. So the 4x4 grids rows and columns are numbered 0-3, and not 1-4 as they might be in tabular form or a newspaper puzzle. Don’t forget this little discrepancy, as it can cause some peculiar problems.

If the goal is to turn this one-dimensional array into a two-dimensional, 4x4 array, how can we select the number 11, which would be the third number in the third row of the 4x4 grid? All it takes is a little modulo arithmetic.

`11 // 4 = 2` and `11 % 4 = 2`

So the number 11 is in the second row and third column of the 4x4 grid, counting from zero, or the third row and third column counting from 1.

To convert from 2d to 1d, we can use the formula `row * num_cols + col`, where `row` is the row number (counting from zero), `num_cols` is the total number of columns, and `col` is the column number (again, counting from zero).

So in this case, `2 * 4 + 2 = 10`, which is the correct index for the number 11 in the 1D grid.

Having to account for all of this math to convert a 1D array into rows and columns and back again probably rules out the first solution as the best one for this problem.

The second solution neatly aligns with the layout of the Sudoku board, which usually includes heavy lines around the nine 3x3 grids that make up the puzzle. So what are the pros and cons of this solution?

That data structure might look like this:

``` python
board = [
    # Grid 0 (top left)
    [[5,3,0],
     [6,0,0],
     [0,9,8]],

    # Grid 1 (top middle)
    [[0,7,0],
     [1,9,5],
     [0,0,0]],

    # Grid 2 (top right)
    [[0,0,0],
     [0,0,0],
     [0,6,0]],

    # Grid 3 (middle left)
    [[8,0,0],
     [4,0,0],
     [7,0,0]],

    # Grid 4 (center)
    [[0,6,0],
     [8,0,3],
     [0,2,0]],

    # Grid 5 (middle right)
    [[0,0,3],
     [0,0,1],
     [0,0,6]],

    # Grid 6 (bottom left)
    [[0,6,0],
     [0,0,0],
     [0,0,0]],

    # Grid 7 (bottom middle)
    [[0,0,0],
     [4,1,9],
     [0,8,0]],

    # Grid 8 (bottom right)
    [[2,8,0],
     [0,0,5],
     [0,7,9]]
]
```

This is actually a 3D data structure, or a list of lists of lists. It might be a little easier to work with in terms of rows and columns, but it’s not really ideal for checking whole rows or columns, as you would have to pull from each grid element individually. It’s great for handing the internal structure of a 3x3 grid, but that’s that’s only one of the things that makes up a Sudoku board. Here is, for example, the amount of code required to read the second column of the 9x9 Sudoku board:

``` python
def get_column(board, col_num):
    column = []
    grid_col = col_num // 3  # (0 for cols 0-2, 1 for 3-5, 2 for 6-8)
    internal_col = col_num % 3  # Which column within each grid?

    for grid_row in range(3):
        for row in range(3):
            grid_index = grid_row * 3 + grid_col
            column.append(board[grid_index][row][internal_col])

    return column
```

Ok, so that works, but it’s a lot of code to return a single column, and also it’s a but confusing. In fact, when I was writing this code I wrote the algorithm the way I was pretty sure I needed to, and watched my computer spit out the wrong answer. Except it hadn’t. What had happened is I had got confused about what the "column" looked like given the data structure, I’d created, and I was reading the wrong line of numbers. I had to get my head around that in order to continue which I take as proof that even if this data structure offers some advantages — and I’m not sure it does — it can be confusing to reason about and so it’s likely the wrong tool for the job.

Ok so the first idea was too much math and the second idea was too much code, can we find a data structure that’s just right? Let’s try the 9x9 matrix.

``` python
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
```

This looks promising. It keeps the rows in the same order they’ll be in on the Sudoku board. The columns can be chosen by iterating via the appropriate index. This one is just right!

Again, I’d imagine that if you were given this as an interview question you’d be given the data structure, but it’s always good to think about these kinds of things because it can help you reason through the problem. And there are valid reasons to consider the 1D and 3D data structures, just not for this particular problem.

Back to the interview question itself: is this a valid Sudoku board?

From the instructions you’ve been given, you have three distinct things to consider: 1. No number can be repeated in a row. 2. No number can be repeated in a column. 3. No number can be repeated in a 3x3 grid.

You might want to try coding this on your own before looking at the solution, but I’m going to work on these one function at a time. Here is my first attempt at checking for repeated numbers in a row. As always, I ask you to think about how you might solve this problem before looking at the solution:

``` python
def check_row(board, row_num):
    row = board[row_num]
    seen = []
    for num in row:
        if num != 0:
            if num in seen:
                return False
            seen.append(num)
    return True
```

This is a fairly straightforward solution. Go down the row, put numbers into a list, and if a number repeats, return False because the board is invalid. Remember that you have to account for the 0, because a 0 means a value that is not yet present in the row. If the program sees it as a number in a row, it will return False, even though it’s not a repeated number.

It’s not hard to build this up into a similar solution for checking a column. The column just needs a little help from a helper function since the data structure is not in a natural column format:

``` python
def get_column(board, col_num):
    column = []
    for row in board:
        column.append(row[col_num])
    return column

def check_column(board, col_num):
    column = get_column(board, col_num)
    seen = []
    for num in column:
        if num != 0:
            if num in seen:
                return False
            seen.append(num)
    return True
```

Last of all, each 3x3 grid needs to be checked. Unsurprisingly, this check is pretty similar to the row and column checks, but with a little more math to get the right numbers in the right places. In fact, it uses the same math we looked at earlier when we were considering a one-dimensional array:

``` python
def check_grid(board, grid_num):
    grid = []
    start_row = (grid_num // 3) * 3
    start_col = (grid_num % 3) * 3
    for i in range(3):
        for j in range(3):
            grid.append(board[start_row + i][start_col + j])

    seen = []
    for num in grid:
        if num != 0:
            if num in seen:
                return False
            seen.append(num)
    return True
```

This would be a pretty good interview answer, but there are three exercises to consider from here:

1.  Combine these three functions into a single function that checks the whole board.

2.  Earlier in the chapter I talked about the "set" data structure in Python. Remember that a Python set is a collection of unique elements. Rewrite the loop that checks for repeated numbers using a Python set. Break it down into two tasks — first see what happens when you try to add repeated numbers to a set and then use a set data structure to check for duplicates in a row. Does this change the time complexity of the function?

3.  Can you write a function that actually solves the Sudoku board? That’s a degree of difference harder than simply considering a valid board, but just think about it for now. I will be returning to this problem later in the book.

### AI Exercise

As I explained earlier, games are great for coming up with algorithmic problems because they have known rules and a finite number of outcomes. AI assistants are good with specific solutions, but they’re not always so good with the broader picture. Modelling a game using ChatGPT, Claude, or Github Copilot will give you a pretty good sense of the ways human programmers can leverage AI to solve problems.

Pick a game you’re familiar with that hasn’t been mentioned in this chapter and use a programming assistant to create a playable version of it in Python. Work through the considerations of not only the gameplay, but also how to represent the elements of the game. This might require the use of a Python graphics library, like Pygame, or some clever ASCII art that represents the game board. You can also try to create a game with a computer opponent, a game that can be played over a network, or a game that can be played on a web page. Make sure your AI is knowledgeable about any libraries you use, which you can usually find out by just asking it questions like "Do you know about Pygame?" or "Are you familiar with the Python socket library?" You can also ask it for suggestions for better ways to do things, and maybe you’ll gain some knowledge of a library you’ve never used before along the way. The most important part: have fun!
