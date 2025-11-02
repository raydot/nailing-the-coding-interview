# Functions and Recursion

Now that you’ve made it through 2/3 of the book, it’s time to talk about functions! "But wait," you say, "Haven’t we been talking about functions this entire time?" Indeed we have been using them, and I’ve even mentioned some things about them, but I think it’s very easy to be a programmer and use functions all the time without ever really understand some of the the more advanced concepts behind them. Indeed, one of the reasons this chapter is so far into the book is because with the understanding you’ve (hopefully) gained from previous chapters you are now ready and willing to look at functions in a whole new light. So let’s get down to it!

## Functions 101

Here comes the dry, boring part of what a function is:

<div class="informalequation">

``` math
f(x) = 2x
```javascript

If x = 1, then f(x) = 2 \* 1 = 2. If x = 2, then f(x) = 2 \* 2 = 4. If x = 3, then f(x) = 2 \* 3 = 6…​etc.

At least, that’s how you first may have learned about them in your high school algebra class. In one of those funny ways about how my particular brain works, I could not understand that concept at all in high school. In understood what `x` was, but what was `f`? What I failed to understand is that `f` was not a variable but the notation for a function, which is something that takes a value (or multiple values) and returns a result (or results) based on a computation (or computations) applied to that value (or values).

I’m being a bit smug with the pluralization, especially since the way you probably worked with mathematical functions was with a single value, but as a programmer, one value usually just doesn’t get the job done.

So let me expand my definition to now include programming. In programming a function is a block of code that takes a value (or values), transforms them according to a set of rules, and returns the result. Usually, but certainly not always, what’s returned is a single value.

Here is the same f(x) = 2x function in Python:

``` python
def two_x(value):
  return (2 * value)
```python

In this case, `two_x` is the function name, `value` is the value being passed in, and `2 * value` is the computation being applied to that value. The function then "returns" that value to the place from whence it was called. Because of this "return," a function can used to set a variable:

`double_value = two_x(value)`

## Black Boxes

In addition to the functions you write yourself, most programming languages come with a built in set of functions. For instance, throughout this book I’ve repeatedly used the "print" function in Python.

`print("Functions are fun!")`

In many languages, a print function has special characters that can be used to add in other types of information, dynamically, to the string being printed.

`print("The value of x is", x)` `print("The value of x is %d" % x)` `print(f"The value of x is {x}")`

Or, for a little JavaScript:

`print("The value of x is " + x)` `` print(`The value of x is ${x} ``)\` `console.log("The value of x is", x)` `` console.log(`The value of x is ${x} ``)\`

Wait, `console.log()`? That’s another function! A lot of people know how to use `console.log(),` but don’t realize that it is but one in a library of `console` functions which includes:

`console.error()` `console.warn()` `console.info()` `console.debug()` `console.table()`

Returning to the `print()` (or `log()` or `write()` or `output()` functions, they are real workhorses in many programming languages, as they’re the primary way for programmers to see what’s going on in their programs. All modern browsers and IDE’s contain robust debugging tools, but without looking it up I’m absolutely certain the \#1 debugging tool used by programmers is `console.log()`.

So what’s going on in `console.log()`? I’ll tell you: who cares? I put a value, expression, string, function into it, and I get a result out. I have never looked at the source code that explains it, because I don’t need to. The majority of functions we use are like this, and they can collectively be thought of as "black box" functions. You put something in, you get something out, and you don’t need to know what’s going on inside. Which is great, because it’s one less thing to worry about.

## You will be asked a question about functions

While there are many ways to define and describe functions I’ve never heard one more accurate than "functions are the building blocks of code." Functions are a primary and essential part of coding that you should absolutely expect to use in a coding interview. Even if you’re not asked a question about functions directly, you will almost certainly need to use a function to solve a harder problem.

## What is a function?

Functions are usually the first "advanced" things a programmer learns. Functions in programming are similar to the function equations you may have learned in high school algebra, which looked something like this:

f(x) = 2x

Learning about functions often included exercises to create tables of the expected results. The table for f(x) = 2x might look like this:

| x   | f(x) |
|-----|------|
| 1   | 2    |
| 2   | 4    |
| 3   | 6    |

Functions in programming perform a similar, um, function, allowing data passed in to be transformed in a way specified by the programmer. Here is the above-mentioned example high-school algebra function in Python:

``` python
def doubler-function(value):
  return (2 * value)
```python

Function implementations are language-specific, with C++ and Java requiring functions be set to data types, and JavaScript containing several ways to create functions, depending on what you’re trying to accomplish. In every language, however, functions are just like the ones you encountered in high-school algebra. They take a value (or values), transform them according to a set of rules, and return the result.

## Building Intuition: Reasoning about functions

## Function prototypes

In strongly typed languages, functions are usually defined by a *prototype*, a block of code that defines the function in terms of the data it can expect to receive and return. In this way, function prototypes are used to enforce type checking, to make sure that the values that are being passed to a function are what it expects to receive. This is an example function prototype in C:

``` c
// Function prototype
float multIntAndFloat(int num1, float num2);
```python

The first `float` in this prototype indicates that it will return a float. The `int` and `float` keywords preceding the two values being passed in means these values *must* be an int and a float. If you pass or return any other type of data, the compiler will return an error — or at least a warning, depending on the C implementation you’re using.

Weakly typed languages don’t require function prototypes, but there are ways to require them, of course. The Typescript programming language is probably the best current example of creating type-checking, for all data and not just functions, in JavaScript.

> > 💡 **TIP**
>
> > Try coming up with examples of situations in which it would be important to check data passed to a function. Are the checks limited to checking data types? If your language doesn’t support function prototyping, how can data checks in functions be enforced?

## Constructing functions

## Receiving function data

## Returning function data

## Arrow functions

The first time I saw a JavaScript arrow function I was sure it would be a passing fad. For one thing, how could you even have an operator that was an arrow comprised of two different characters? (You might be thinking of `==` but I did say "two different.")

Now, I find arrow functions to be absolutely invaluable, especially as they can be used with the classic "functional programming" functions, `map()`, `filter()`, and `reduce()`.

A JavaScript arrow function — and I’ll get to Python in a moment — is a way to write a function that immediately returns a value. For instance, going back to the earlier math example I gave of `f(x) = 2x`, you could write that as an arrow function in JavaScript like this:

`const doubler = (x) ⇒ 2 * x`

The arrow says "return" and keeps you from having to type it.

In Python, the (kinda, sorta) equivalent of an arrow function is a lambda function, which doesn’t have a fancy arrow but requires you to type out the word "lambda." Nowhere near as cool, but certainly equally useful:

`doubler = lambda x: 2 * x`

Arrow functions absolutely can be multi-line functions, simply by adding some curly braces:

``` javascript
const doubler_plus_two = (x) => {
  const result = 2 * x
  return result + 2
}
```javascript

All equally valid, but now you’ve lost the need not to type return, and you have a function doing two things (doubling x and adding 2) which is fine, but not really any different from what a function can already do.

## Closures

For the longest time you could not go on a programming interview without being asked, "What’s a closure?" Something funny about that, though, I’m not so sure a lot of interviewers knew either. One of the greatest texts on closures comes from the *You Don’t Know JavaScript* series by Kyle Simpson, and I highly recommended reading all of his books once you’re done with this one.

The problem with the question "What is a closure?" is that there’s not really a single correct answer. I mean there is, but it’s not a simple one. Because of this, I suspect a lot of people were told they were "wrong" in their response, when actually, they likely weren’t, not exactly.

Closures have to do with both the scope of data in an application, the way in which that data is defined in terms of that scope, and the way in which that data is used. It borrows ideas from both object-oriented and functional programming.

Object-oriented programming, for instance, is reliant on a concept called "encapsulation," which is the idea that object data should be kept "private," and only accessed through "public" methods.

In fact, Java (again, never to be confused with JavaScript) contains three different keywords to define the scope of data: `public`, `private`, and `protected`.

`public` means that the data can be accessed from anywhere in the program, very similar to so-called "global" variables. `private` means that the data can only be accessed from within the object, and not from outside. `protected` means that the data can be accessed from within the object, but also from any object that "inherits" from that object.

To give a real world example, let’s talk about money! Let’s pretend we are standing in a store and looking at an infinitely desirable item that costs \$1000. That’s a decent — but not unattainable — amount of money. The fact that the item costs \$1000 is "public," information available to everyone. You, me, the store clerk, people shopping online, banks, credit card companies, Square, whatever.

Ah, but then you say to me, "At that item is infinitely desirable, you should buy it!" Maybe we know each other well enough for me to say, "Eh, I’m sure I could use one, but I just can’t afford it." If I don’t know you so well but I want to impress you, I might say something like "I have two at home!" If we’re really trying to flex on one another, maybe I’ll say something like, "You know what, I think you should buy it for me!" Implicit in all of this deceit is the very simple idea that the amount of money in my wallet is "private" information. I might have \$1000 in my wallet, I might have \$5000 in my wallet. I might have no money at all. It’s private though. You don’t know, the clerk doesn’t know, the bank doesn’t know, and my mom doesn’t know.

The third case, "protected," works like this. Let’s say I’ve brought my son with me to the store, and he really, really wants the infinitely desirable object. He’s been saving his allowance, and he’s managed to save up \$800 for it, but before we left I promised him I would give him the last \$200. He’s ready to buy, but my arms are full because I’ve been shopping all day, so I say to him, "Why don’t you go into my pocket, take out my wallet, and grab \$200." This data is "protected." My son, my offspring, can go into my pocket to grab it, and now it’s his to use and in his pocket. (The analogy breaks down a little bit because if it’s computer data there’s no actual "transfer" and we can both have the \$200, but you get the idea.) He can go in and get it, but you can’t. The clerk can’t. The bank can’t. And, sorry Mom, but my mom can’t. It’s "protected," and only available to those who inherit from me.

With these ideas in mind you have a pretty good idea of what is meant by "encapsulation." The idea that data should only go to the places where it belongs, and that’s it. The idea behind this is that it makes it easier to reason about the code, and also that it makes it easier to avoid unintended consequences in your code, from functions unintentionally or intentionally changing data in an undesired fashion.

With all of that in mind, I do believe we were talking about closures.

Let’s start with this simple closure example in JavaScript  

``` javascript
function outerFunction() {
  const outerValue = "I'm the outer value"
  function innerFunction() {
    console.log(outerValue)
  }
  return innerFunction
}
```javascript

It’s been said that in JavaScript functions are "first-class", which means they can be passed around like any other data type. In this example, `outerFunction` is a function that returns `innerFunction`, which is a function that logs the value of `outerValue` to the console.

I don’t think the following will come as a surprise, none of the data inside this function is available from outside the function.

``` javascript
console.log(outerValue)
// Output: ReferenceError: outerValue is not defined
innerFunction()
// Output: ReferenceError: innerFunction is not defined
```javascript

Encapsulation at work! Neither of these values are available outside of `OuterFunction`. This is scope defined with the curly braces that surround the data. The data inside the function is "private," and can only be accessed from within the function.

``` javascript
const closure = outerFunction()
closure()
// Output: I'm the outer value
```

That’s the cool, closure part right there. If you look back at the `outerFunction` you’ll see that `innerFunction` is returning `outerValue`, which is a value that is no longer in scope. In addition to that, the `outerFunction` has finished executing, and yet the value of `outerValue` is still available to `innerFunction`.

This is a closure.

It allows you to do some interesting things like this:

``` javascript
function outerFunction() {
    let counter = 0
    function innerFunction() {
        counter++
        console.log(`Counter value: ${counter}`)
    }
    return innerFunction
}

const incrementCounter1 = outerFunction()
const incrementCounter2 = outerFunction()
incrementCounter1() // Output: Counter value: 1
incrementCounter1() // Output: Counter value: 2
incrementCounter2() // Output: Counter value: 1
```

It also allows you to use JavaScript key-value pairs to create objects consisting of "name":"function" pairs, each one of which is encapsulated using a closure into a single object that maintains its own state.

``` javascript
function createCounter() {
  let count = 0 // Private variable
  return {
    increment: function () {
      count += 1
      return count
    },
    decrement: function () {
      count -= 1
      return count
    },
    getValue: function () {
      return count
    },
  }
}

const counter1 = createCounter()
console.log(counter1.increment()) // 1
console.log(counter1.increment()) // 2
const counter2 = createCounter()
console.log(counter2.increment()) // 1
console.log(counter2.decrement()) // 0
```javascript

Lots of closure stuff happening here! First "count" is a private variable that is only available to the "increment," "decrement," and "getValue" functions inside the object. Second, the "inner" functions in the "name:function" object are returned from the function, and the functions inside the object are able to access the "count" variable even though the `createCounter` function that created it has finished executing. Third, once these objects are created they maintain their own state, so that each object created by the function has its own "count" variable that is separate from the others. And I didn’t have to use a single line of Redux!

It is of course possible to do a similar thing in Python using dictionaries:

``` python
def create_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def decrement():
        nonlocal count
        count -= 1
        return count
    def get_value():
        return count
    return {
        "increment": increment,
        "decrement": decrement,
        "getValue": get_value
    }
```javascript

The answer to "what is a closure?" All of the above. Specifically, a closure is a function that maintains a reference to the variables in the scope in which it was created, even after that scope has finished executing.

If you say, "A closure is an example of scope created using encapsulation," you’re not wrong. If you say, "The (lexical) scope is defined by the (functional boundaries) curly braces (indents in Python)," you’re not wrong. If you say, "It’s a way to maintain state in a functional programming paradigm," you’re not wrong. You might need to do a little more explaining along the lines of what’s really going on, but you’re not wrong, and don’t let anyone tell you otherwise.

## Anonymous functions

It is possible to define a function without a name, which is then called an "anonymous function." This is not meant to be mysterious, it’s just that sometimes the name doesn’t really add anything useful to the code. For instance you interact with strangers all the time without knowing their names. And they don’t know yours either. But that stranger likely knows how to do something that you need done, like "Do you have this in red?" or "Can you tell me how to get back on to the highway?"

It’s arrow functions and closures that make anonymous functions possible in JavaScript. For instance, you may have done something like this in JavaScript:

``` javascript
const myArray = [1, 2, 3, 4, 5]

const doubledArray = myArray.map(function (num) {
  return num * 2
})
console.log(doubledArray) // Output: [2, 4, 6, 8, 10]
```python

That mystery `function` is the anonymous function. It’s needed because you have to pass in and return the number you’re trying to double. This can also be done with an arrow function:

``` javascript
const myArray = [1, 2, 3, 4, 5]
const doubledArray = myArray.map((num) => num * 2)
console.log(doubledArray) // Output: [2, 4, 6, 8, 10]
```python

Be aware of the portability between the one-line and multi-line anonymous functions, which has tripped me up more than once. If the arrow function is used without curly braces, the return is implicit, and does not need to be stated. You can see that above in `map((num) ⇒ num * 2)`, where the return is implicit.

But what if you need to do something a little more complex?

``` javascript
const numArray = [1, 2, 3, 4, 5]
const nameArray = ["Arlo", "Bao", "Carlos", "Diana", "Eli"]

const result = numArray.map((num, index) => {
  return {
    number: num,
    name: nameArray[index]
  }
})
```python

This example still uses an arrow function, but there are now curly braces added because more than one line of code is needed to accomplish the task. Because the curly braces have been added, the implicit `return` goes away, and you will have to explicitly use the `return` keyword to return whatever it is you want to return.

## Passing functions to functions

Passing variables to a function is a a pretty simple thing to grasp, but some languages allow you to pass functions to functions. JavaScript treats functions as "first-class citizens" and this is yet another example.

There are a few reasons you might want to do this, and some of them will be explored further later in this chapter. For now I’m just going to cover the basic idea.

Here’s an example of passing a function to a function in Python:

``` python
def function_taking_function(func, value):
    return func(value)

def double(x):
    return x * 2

def triple(x):
    return x * 3

result = function_taking_function(double, 5)
print(result)  # Output: 10
result = function_taking_function(triple, 5)
print(result)  # Output: 15
```

That’s hardly the end of it. In any language that treats functions as "first-class" you can pass them anywhere you like. Building on the example above, here are functions that are stored in an array and then passed to a function.

``` python
def function_taking_function(func, value):
    return func(value)

def double(x):
    return x * 2

def triple(x):
    return x * 3

def quadruple(x):
    return x * 4

def quintuple(x):
    return x * 5

function_array = [double, triple, quadruple, quintuple]

for func in function_array:
    result = function_taking_function(func, 5)
    print(result)  # Output: 10, 15, 20, 25
```javascript

If you’ve never considered this it can be fun to play around with it as an idea. But this is one more of those things where just because you can, doesn’t necessarily mean you should. Piling functions up and passing them around can quickly make your code tricky to reason about, especially if those functions are returning things. If you adhere to the rule where each function should only be responsible for one thing, if you start storing functions in arrays, passing them to other functions, passing those functions to functions, it sounds like a memory leak waiting to happen.

Play with it at home, absolutely. If you want to do it at work, make sure it’s something that is well planned out and has the approval of at least one other developer — preferably the team lead. Don’t do it in a interview, unless you’re specifically asked to.

## Functions Advanced

## The mystical “this”

`this` really has more to do with object-oriented programming specifically and less with functions in general, but it is a related concept. In JavaScript, especially, the two blend together quite a bit.

In most object-oriented language, `this` can generically be thought of as what a function calls itself. Unless you’re one of those people that is cool enough to refer to yourself in the third person, ("Dave needs to go get some more coffee…​", nah) you likely refer to yourself as "I" or "me." And so do I (see what I did there?) refer to myself as "I" or "me." That’s what `this` is, an objects way of saying "I."

In JavaScript it gets a little bit tricker. Because of the way JavaScript handles object-orientatedness, `this` can mean an object calling itself, but it can also refer to the object that is calling the function.

In the following example, the function is a method of an object, so `this` refers to that same object — the one that is calling the function:

``` javascript
const obj = {
  name: "Dave",
  greet: function() {
    console.log(`Hello, my name is ${this.name}`);
  }
};
obj.greet(); // Output: Hello, my name is Dave
```javascript

But if a function is created outside of an object, then `this` refers to JavaScripts global object (or `undefined` in strict mode, because, don’t do that):

``` javascript
function greet() {
  console.log(`Hello, my name is ${this.name}`);
}
```python

## Constructor functions

Like `this,` a constructor also has more to do with OOP than functions in particular, but is also a related concept. A constructor function is a function that helps to set up a class or object in OOP. Here’s an example in Java, where the syntax is more clear than it is in most languages:

``` java
public class Robot {
    private String name;
    private int age;

    public Robot(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```python

That funny looking function that has the same name as the class definition, `Robot`, is the constructor function. When the class is created, the variables passed in to the constructor function help set up the class variables. Multiple robots can be generated like this:

``` java
Robot robot1 = new Robot("Lala", 5);
Robot robot2 = new Robot("Barney", 10);
Robot robot3 = new Robot("Peppa", 15);
```javascript

This works in much the same way as passing variables to a function does, but it only works if a constructor is defined in the first place.

## Generator functions

Generators and iterators are some fancy advanced theory that I have to be honest in saying I have yet to find a use case for. That probably has more to do with my own experience than their actual usefulness, and I’m sure they’re important in some corner of the programming world.

You can think of a generator function as a fancy for-loop:

``` javascript
function* generatorFunction() {
  yield 1;
  yield 2;
  yield 3;
}
const generator = generatorFunction();

console.log(generator.next().value); // Output: 1
console.log(generator.next().value); // Output: 2
console.log(generator.next().value); // Output: 3
```javascript

This generic generator function example tells you pretty much everything you need to know. The syntax involves adding a `*` to the function definition. The `yield` keyword is used to store the list of values in the function. The `next()` method is used to get the next value in the list, and the `value` property is used to get the value itself.

The analogy is that of a deli counter at a grocery store, where people take tickets to hold their place in line. The set of glowing red numbers on the wall is the iterator, and the ticket in your hand is the value. The `next()` method is the person behind the counter either pulling a string or clicking a remote to increase the number being called.

I’m not trying to throw shade at generators, but I don’t really see anything there that can’t be done with a `for` or `while` loop. I don’t work in big data or with large event streams, which is clearly my own personal failing and nothing a generator function has ever done to me or anyone else.

If you are asked about these in an interview, I’m going to guess you’re there because you already know exactly what they are.

## Factory functions

What’s better than a function? A function that can create other functions! This is the purpose of a factory function. Passing different variables to a function is a great way to tweak a function to your liking, but you can also create a function that creates other functions.

You might have a pickle factory, and all pickles are made the same way. You wanna pickle? Start with a cucumber, add some vinegar, wait a few months, and you gotta pickle! But after a while eating the same pickle is boring, and you might want to branch out. You might want a sweet pickle, a dill pickle, or a spicy pickle.

Here’s an example of how you can do this with a factory function in JavaScript:

``` javascript
function createPickle(type) {
  return {
    pickleType: type,
    makePickle: function() {
      console.log(`Making a ${this.type} pickle!`);
    }
  };
}

const dillPickle = createPickle("dill");
const sweetPickle = createPickle("sweet");
const spicyPickle = createPickle("spicy");

dillPickle.makePickle(); // Output: Making a dill pickle!
sweetPickle.makePickle(); // Output: Making a sweet pickle!
spicyPickle.makePickle(); // Output: Making a spicy pickle!
```javascript

## Callback functions

Some functions are meant to be called specifically when other functions complete. Functions called "callback functions" are passed in to functions to be called when that function is complete.

One of the most prevalent examples of this is the one used to illustrate `setTimeout()` in JavaScript. `setTimeout()` is a function that takes two arguments: a function to be called, and a value of how long to wait to call it.

``` javascript
function myCallback() {
  console.log("Another ten seconds gone!");
}

setTimeout(myCallback, 10000);
```javascript

This code will print the phrase "Another ten seconds gone!" to the console after 10 seconds.

Callback functions are very useful for timing events, but they are also an invaluable tool for asynchronous programming. Here is a JavaScript example of using a callback function to wait until data is returned from an API. This is great because instead of having to "poll" repeatedly to see if data has been returned from an API, you can just hand the task over to JavaScript and count on it to let you know either when something’s complete or when it’s never going to complete.

``` javascript
async function fetchData() {
  // Replace this with your actual API call
  const response = await fetch('https://some.api.com/stuff-you-want');
  const data = await response.json();
  return data;
}

// Use fetchData as a callback
async function main() {
  try {
    const result = await fetchData();
    console.log(result);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

main();
```javascript

## Function chaining

Ah jQuery, who remembers jQuery? For a brief, shining moment in the history of web development, jQuery was tha Alpha and the Omega, the All and the Everything, the only true way to write JavaScript. It looked a little funny at first, but once you got used to it you could bask in the glory of function chaining.

Function chaining is a way to call multiple functions from a single line of code in a way that allows each function to operate on the result of the function or functions that came before it.

For instance, in jQuery you could do something like this:

``` javascript
$('#coolElement')
  .addClass('active')
  .css('color', 'salmon')
  .css('padding', '12px 20px')
  .css('border-radius', '8px')
  .css('transition', 'all 0.3s ease-in-out')
  .fadeIn(1000);
```javascript

In this example the first line, `$('#coolElement')` is a jQuery "selector" that grabs the element from the DOM that has the ID of `coolElement`.

After that, manipulate away! Add a class, change the css, even add a fade in. There it is in one simple, elegant block of code.

This is function chaining, and it can be a useful way to write code — or, more precisely, code libraries. If you can come up with a discrete set of functions that can be applied in a consistent way to some hierarchy of data, function chaining is a great way to go.

The problem with this approach to creating a library is, like so many code fads, it becomes the hammer that turns everything into a nail. It was not uncommon to HTML pages containing hundreds of lines of jQuery all chained together. This made for a lot of "spaghetti code," that was not easy to change, scale, reason about. Let me be clear in saying that I loved jQuery, and I place the blame for its demise more on programmers who didn’t take the time to understand how to effectively use than on its otherwise good intentions. It was a fantastic way to get a lot of great stuff done in a hurry. In fact, it’s still maintained and used in projects today, and while I haven’t had a chance to use them the latest versions have had positive reviews.

What’s behind the magic of function chaining? There are a few related ways to do it, but the simplest way is to create a single piece of data, like an object, and then pass that object with its modification applied from function to function.

While I can’t claim to have ever peeked inside the jQuery source code, I imagine its basic operation looks something like this under the hood:

``` javascript
function getElement(selector) {
  const element = document.getElementById(selector);

  // Return an object containing only functions
  return {
    addClass: function(className) {
      element.classList.add(className);
      return this; // Return the object for chaining
    },

    css: function(property, value) {
      element.style[property] = value;
      return this; // Return the object for chaining
    },

    fadeIn: function(duration) {
      element.style.transition = `opacity ${duration}ms`;
      element.style.opacity = '1';
      return this; // Return the object for chaining
    }
  };
}

// Usage:
const $ = getElement; // Create a familiar alias

$('coolElement')
  .addClass('active')
  .css('color', 'salmon')
  .css('padding', '12px 20px')
  .css('border-radius', '8px')
  .css('transition', 'all 0.3s ease-in-out')
  .fadeIn(1000);
```

Or, to pass on the class-based approach and go with something entirely functional:

``` javascript
// Create pure functions that transform a value and return a new value
const addClass = (className) => (element) => {
  const newElement = { ...element };
  newElement.classList = [...(element.classList || []), className];
  return newElement;
};

const css = (property, value) => (element) => {
  const newElement = { ...element };
  newElement.style = { ...(element.style || {}), [property]: value };
  return newElement;
};

const fadeIn = (duration) => (element) => {
  const newElement = { ...element };
  newElement.style = {
    ...(element.style || {}),
    transition: `opacity ${duration}ms`,
    opacity: '1'
  };
  return newElement;
};

// Helper function to start the chain with the element
const getElement = (selector) => {
  // Mock representation of a DOM element,
  // But it gets the point across
  return { id: selector, classList: [], style: {} };
};

// Compose functions (right to left)
const compose = (...fns) => (x) => fns.reduceRight((acc, fn) => fn(acc), x);

// Pipe functions (left to right) - more intuitive for chaining
const pipe = (...fns) => (x) => fns.reduce((acc, fn) => fn(acc), x);

// Usage:
const elementTransformation = pipe(
  addClass('active'),
  css('color', 'salmon'),
  css('padding', '12px 20px'),
  css('border-radius', '8px'),
  css('transition', 'all 0.3s ease-in-out'),
  fadeIn(1000)
);

const transformedElement = elementTransformation(getElement('coolElement'));
console.log(transformedElement);
```python

Pretty cool, right? But you can see how it could easily get unwieldy. Now that you’ve been shown, use it wisely.

<div class="formalpara">

<div class="title">

Piping

    Piping has been around since the earliest days of Unix, which was created at Bell Labs in the 1960's.
    I've mentioned earlier in the book the importance of knowing at least a little bit of Unix and I'm not going to repeat that here other than to say that if you ignored that advice the first time, here it is again.

    In Unix, the output of any command-line operation can be passed or "piped" to the input of another.
    This is done using the "pipe" operator, which is the vertical bar `|` that can be found under the delete/backspace key on most keyboards.

    In my earliest days working as a web developer, one of the hats you had to wear was interacting with a server directly.
    The most widely used server software then and now was Apache, and the only way to interact with a server was via command line without a Graphical User Interface or "GUI" (think Windows, Mac OS, Ubuntu, etc...) it wasn't always easy to locate large files that may have been generated or placed on a server, perhaps causing it to run out of disk space.

    One of my favorite fellow programmers showed me how to use the unix `find` command to locate files by size, and then to pipe the output of that command to the Unix `wc` command, which counts the number of lines, words, and characters in a file.
    Because `find` returns each file matching a given criteria a line at a time, by piping the result to `wc` and focusing on the number of lines returned you could see the number of files that matched the criteria.

    For instance:
    [source, bash]

find /var/log -type f -size +100M \| wc -l

    This will search the `var/log` directory for files that are larger than 100 megabytes, and then pipe the output to `wc -l`, which will count the number of lines returned by the `find` command.
    My favorite fellow programmer was just giving me a one-off command to solve a specific problem, but he unknowingly introduced me to the idea of piping at the same time, which is a fantastic way to make all kinds of magical things happen in Unix.

## Side effects and functional programming

Entire books have been written on functional programming, and I suggest you read some of them. The main idea of functional programming is that there are only two things that belong in a program: data, and functions to act on that data. In functional programming functions should be "pure," meaning that they don’t have side effects.

This is a relatively easy paradigm to understand, but it’s a bit more of a challenge to master.

A "side effect" is data that is changed outside of the function. All a function should be expected to do is take data, modify data, and return the result. If a function is changing data in the global scope, for instance, that’s a side effect. Here is an example of what that means:

``` javascript
let globalVariable = 0
function incrementGlobal() {
  globalVariable += 1
}
incrementGlobal()
```javascript

Of course that would never happen because EVERYONE knows global variables are bad, right? I mean, my gosh, I wouldn’t be caught dead coding with one. Now that my secret is safe, `incrementGlobal()` is function that creates a side effect by changing the value of `globalVariable`, which is scoped outside of the function.

What’s the big deal? What if another function comes along and decides to do this:

``` javascript
let globalVariable = 0
function incrementGlobalMore() {
  globalVariable += 2
}
```python

Good luck keeping track of which function is changing the value of `globalVariable`, and when.

In functional programming the only way to change the value of a variable is to pass that variable to a function, and then return the result, like so:

``` javascript
let globalVariable = 0
function incrementGlobal(value) {
  return value + 1
}
globalVariable = incrementGlobal(globalVariable)
```python

The difference in this example is that `globalVariable` is not changed inside the function. When `incrementGlobal()` is called, there’s no worry that something somewhere else is going to be going the same thing to `globalVariable` at the same time.

One great thing about functional programming is it’s embrace of three incredibly useful functions: `map()`, `filter()`, and `reduce()`. All three of these functions take a function as an argument, and return new data — usually in the form of an array — after running the passed function against the data that’s passed in with it.

For instance, here is a use of filter to remove all of the green M&M’s from a bowl…​um…​array.

``` javascript
const mAndMs = [
  "red", "brown", "green", "yellow", "blue", "green", "red", "brown", "green"
]
const noGreens = mAndMs.filter((m) => m !== "green")

console.log(noGreens)
// Output: ["red", "brown", "yellow", "blue", "red", "brown"]
```javascript

In this example the function is passed in as an arrow function, the function being the logical condition `m !== "green"`.

## Currying

There’s a great photo of me reading Douglas Crockford’s "JavaScript: The Good Parts" to my 8-year-old son in a hotel room. I was trying to understand all of the new features of JavaScript that all of a sudden made it a "real" programming language, was also called "ECMAScript," contained new and exciting features like "closures," and was being used to build "single-page applications" that were "responsive" and "dynamic." Because of this I had taken the book with me on vacation, and my son asked me to read it to him.

I said, "It’s a grown-up book buddy, I really don’t think you’re gonna like it," but 1) We hadn’t brought anything else with us to read and 2) I’m not so sure he cared. The part I was reading was about "currying," which is a way to take a function that takes multiple arguments and turn it into a series of functions that each take a single argument. And for a good long time he was able to explain that — I suspect more because he remembered the exact words without understanding the concept.

Let’s see if I can do a better job this time around, and if you’re reading this book and you’re 8 you probably don’t need my help.

Currying (named after Haskell Curry, not the spice) is an idea that comes from functional programming and is a way to take a function that takes multiple arguments and turn it into a series of functions that each take a single argument. Another way to put that is to take a single function that might perform a lot of tasks and break it down in to a lot of smaller functions that each perform a single task. Which is actually a pretty good idea, and for a long time I adhered religiously to to idea that a single function should perform a single task, and only a single task.

Here’s a simple example of currying in Python, same simple example that’s given in many other places:

``` python
def add(x, y):
  return x + y

def add10(x):
    return add(x, 10)

print(add10(5))
# Output: 15
```python

In this example, `add10` is a curried function that takes a single argument, `x`, and returns the result of `add(x, 10)`. Which makes no sense whatsoever, because why couldn’t you just do (x + 10) and be done with it.

Let me see if I can come up with a more exemplary example, as all good examples are.

> **Functional Programming**
>
> Functional programming is a term that was quite trendy for a while, and it’s a very useful concept to understand. It’s yet another programming paradigm, like "object-oriented," and while it’s certainly not the only way to program or the only thing you should ever consider, it has some useful ideas that will definitely make you a better coder.
>
> The idea of functional programming is simply that everything is a function. All of the code in your program is either data, or a function to act on that data. Nothing is "imperative," meaning that you don’t tell the computer what to do, you tell it what you want done and it figures out how to do it. The challenge is while that’s an easy concept to (pretend to) understand, it’s quite a bit more challenging to actually put in into practice.
>
> At the heart of the functions in functional programming is the idea that functions should be "pure," meaning that they don’t have side effects. A side effect is code that changes something outside of the function — which should not be possible because there should be no "outside" of the function.
>
> This takes a lot of tools out of the box, specifically: global variables, data mutation, and loops. It also means that you can’t use recursion, because recursion is a side effect.
>
> The idea caught on when it was realized that JavaScript had a largish state management problem, and lead to the implementation of things like Redux. Over the past few years, however, we’ve all become a lot more sensible about state, and new libraries like React Hooks and Jotai have made it a lot easier to manage state more sensibly.
>
> It’s worth reading about and trying to get your head around at least the basics, and trying to solve programming problems like "FizzBuzz" in a purely functional programming language like Lisp or Haskell will certainly give you a whole new perspective on problem solving in programming — and I mean that in a good way.

## Higher Order Functions

Higher order functions are functions that return other functions as their result. Higher order functions were all the rage in React until the introduction of React Hooks, which just encapsulated what people were doing already with higher order functions.

Here’s a simple example of a higher order function in JavaScript:

``` javascript
function higherOrderFunction() {
  return function innerFunction() {
    console.log("Hello from the inner function!");
  };
}
const innerFunc = higherOrderFunction();
```javascript

This is an incredibly useful concept because it can be used to create functions "on the fly," that are much more flexible and usable than single purpose functions.

Like most things in programming, this should be used in moderation.

If you find yourself building a 100 line function that returns a 1000 line function, it’s probably a good time to question both your life and architecture choices.

That last example was pretty simple, but higher order functions can solve a lot of complex problems. One problem that I’ve had more than once is needing to create a functions where the things that will be passed to it will mostly be the same, but not always. For instance, you might want to create in inventory system that has to account for very different items, some of which will have very different properties. Consider a shoe catalog where most of the shoes come in different colors and sizes, but some might come with custom laces, some might come with engraving, some might have customizable sole colors, and some might have two or more of these features available.

One very stilted approach that I’ve taken more than once is to create a single function that takes in every possible property, along with flag values to indicate whether or not that property is available for that item. This can lead to some funky function signatures, can make it difficult to reason about the code, can make it difficult to scale the code, and yeah, I will confess to having done something like this at least once in my career.

``` javascript
function createShoeFactory(defaultOptions = {}) {
  // Base defaults for all shoes
  const baseDefaults = {
    customLaces: false,
    laceStyle: '',
    engraving: false,
    engravingInitials: '',
    customSole: false,
    customSoleColor: ''
  };

  // Return a function that creates shoes with those defaults
  return function createShoe(name, color, size, options = {}) {
    // Create the basic shoe with required properties
    const shoe = {
      name,
      color,
      size
    };

    // Apply customizations only if they exist
    const fullOptions = { ...baseDefaults, ...defaultOptions, ...options };

    // Only add custom properties that have been explicitly set
    Object.entries(fullOptions).forEach(([key, value]) => {
      // Only include non-default properties
      if (value !== baseDefaults[key]) {
        // For related properties, group them logically
        if (key === 'customLaces' && value === true) {
          shoe.laces = {
            custom: true,
            style: fullOptions.laceStyle
          };
        } else if (key === 'engraving' && value === true) {
          shoe.engraving = {
            enabled: true,
            initials: fullOptions.engravingInitials
          };
        } else if (key === 'customSole' && value === true) {
          shoe.sole = {
            custom: true,
            color: fullOptions.customSoleColor
          };
        } else if (!['laceStyle', 'engravingInitials', 'customSoleColor'].includes(key)) {
          // Add other non-related properties directly
          shoe[key] = value;
        }
      }
    });

    return shoe;
  };
}

// Usage examples
const standardShoe = createShoeFactory();
const nike = standardShoe('Air Max', 'black', 10);
console.log(nike); // Just name, color, size

const customShoe = standardShoe('Air Jordan', 'red', 11, {
  customLaces: true,
  laceStyle: 'round',
  engraving: true,
  engravingInitials: 'JBD'
});
console.log(customShoe);
// Has name, color, size, plus laces and engraving properties
```javascript

Add a few more styles, options, and features and this can get pretty out of control in a hurry. And remember, most of the shoes will only have a name, a color, and a size.

This can be dealt with by using a higher-order function that can "scale" as needed to accommodate the different properties of the shoes. Such a function might look a little more like this:

``` javascript
function createShoeFactory(defaultOptions = {}) {
  // Return a function that creates shoes with those defaults
  return function createShoe(name, color, size, options = {}) {
    // Create the basic shoe with required properties
    const shoe = {
      name,
      color,
      size
    };

    // Combine factory defaults with specific options
    const customizations = { ...defaultOptions, ...options };

    // Add laces if style is specified
    if (customizations.laceStyle) {
      shoe.laces = {
        style: customizations.laceStyle
      };
    }

    // Add engraving if initials are specified
    if (customizations.engravingInitials) {
      shoe.engraving = {
        initials: customizations.engravingInitials
      };
    }

    // Add custom sole if color is specified
    if (customizations.customSoleColor) {
      shoe.sole = {
        color: customizations.customSoleColor
      };
    }

    return shoe;
  };
}

// Usage examples
const standardShoe = createShoeFactory();

// Basic shoe
const basicNike = standardShoe('Air Max', 'black', 10);

// Custom shoe with special laces
const lacedShoe = standardShoe('Air Jordan', 'red', 11, {
  laceStyle: 'round'
});

// Custom shoe with engraving
const giftShoe = standardShoe('Dress Shoe', 'brown', 9, {
  engravingInitials: 'CLDK'
});

// Custom shoe with multiple features
const fullCustomShoe = standardShoe('Custom Elite', 'white', 10, {
  laceStyle: 'flat',
  engravingInitials: 'MVP',
  customSoleColor: 'gold'
});
```python

If you’re familiar with object-oriented programming this kind of resembles extending a bae class, which it kinda is.

## Building Intuition: Functions Ideas

## Functions and state

## Function refactoring

## Function composition

### “Program to an interface, not an implementation”

## Recursion

In the course of my career I’ve written a *lot* of recursive code, and all of it has one thing in common: it’s been some kind of exercise. I’ve been in a class and given a problem to be solved with recursion, I’ve been writing an exam and I promised there would be a problem that required recursion, or I’ve been in an interview and asked to solve a problem using recursion.

In that same span of time I don’t think I’ve ever written a single line of recursive code in a production environment. It’s hard to come up with, hard to maintain, and if you get it wrong it can end up creating a heck of a lot more problems than it solves.

So is recursion a useful concept? Or should it be left to academia and otherwise avoided?

The simple answer to that question is: yes!

While it’s rarely the best tool for the job, recursion is a very useful concept in terms of gaining a deeper understanding of how code works. It’s an absolutely invaluable way to reason about problems. The process used to come up with recursive solutions is identical to the process used to break larger problems into smaller, more manageable pieces.

I was a musician as a youth, and even though I always played rock songs, I worked with a teacher who taught me jazz. I loved it because playing jazz focused more on finesse, improvisation, and a broader musical understanding. When I got together with band band and we played rock, it was a lot easier to play those songs because I had a deeper understanding of music. (That’s not a value judgement by the way. I’m not saying either is "better." Plenty of people hate jazz, and while I think they’re making a huge mistake, I get it.)

It’s the same with recursion. Understanding how to break a problem down in the way that’s required to come up with recursive solutions is an invaluable skill for a programmer to have, even if you never use recursion in a production environment. That’s *why* it’s focused on so much in academia and in coding interviews — it’s a way to show an advanced understanding of ways to reason about code.

## Introduction to Recursion

Like functional programming, recursion is another programming paradigm that takes a moment to learn, and a lifetime to master. The idea of recursion is simple. A recursive function is a function that calls itself. That’s all there is to it. Why would a function want to call itself? Believe it or not there are lots of reasons, the primary one being that recursion can be used to break a larger problem down into smaller, more manageable pieces.

An example I read somewhere a while ago was that of the TV news, if it even still exists by the time this book comes out. On the news there will usually be an "anchor" who sits in the studio and reports all of the main news stories at a high level.

When it comes time to report the weather, the anchor will turn over reporting duties to the weather reporter, whose job is only to report on the weather-related stories of the day. But wait, a terrible tornado has blown over the town’s most prominent landmark! The weather reporter pulls up the doppler radar that shows a terrible storm passing over the center of town, but because a newscaster can’t be in two places at once the reporting function is then passed to an on scene reporter who has all of the details. But wait again! The on-scene reporter found an eyewitness who captured the whole thing with their phone five minutes before the broadcast started, and so now the reporting is passed to the control room that then plays back video of the event as it was happening live.

When the video concludes, the control "stack" can be said to "unwind." The control room will turn back to the on-scene reporter, who will make some sensational comments and then end with, "And now back to the weather room." The weather reporter will make some goofy comment that includes a pun and clear skies ahead and then say, "And now back to the anchor desk." The anchor will thank everyone for their amazing work and then turn to the next story.

To put is simply: the large problem of providing real-time information that covers various aspects of a single subject is broken down into smaller and smaller chunks by passing control down the hierarchy of reporters until the most detailed, essential piece of information is shown, and then control passed back up the hierarchy.

Same basic idea as recursion, as will be examined.

### The Elements of Recursion

There are a few basic elements to recursion that are important to understand. They’re important to understand because they will help to reason about whether or not a problem can be solved using recursion.

These three elements are: 1. Base case 2. Recursive case 3. Termination / Unwinding the stack

Each case will be defined here, but might not make sense without an example, so just focus on the general idea for now.

### Base Case

The base case is the simplest case of the overall problem that can be solved without recursion. In the example of the TV news, the base case is the anchor desk. The anchor desk can report the news without cutting away to anyone else further down the hierarchy.

### Recursive Case

The recursive case the aspect of the problem that can be repeatedly broken down. In the example of the TV news, the recursive case is the reporting. This can be handed off to other reporters with different areas of expertise or found in different locations.

### Termination / Unwinding the Stack

The termination case is the recursion reaching the end of the road. In the TV news example once the video was shown, there was nothing left to report. The end of the line was reached, and the hierarchy of reporters was unwound back to the anchor desk. In programming terms, unwinding the stack means terminating each recursive call and returning to the previous function in the stack until the original function is reached and the result returned.

### Example

The example everyone always ever gives with discussing recursion is the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two that proceeded it, starting with 0 and 1.

The first numbers in the Fibonacci sequence are:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144…​etc.

The Fibonacci sequence might seem silly, but it has the magical ability to show up pretty much everywhere in nature, and can be used to describe the growth of anything that grows in a spiral. This includes such wonderful things as pinecones, conch shells, romesco broccoli, and even parts of the human body.

Why the Fibonacci sequence is relevant to recursion is because the Fibonacci numbers can be calculated recursively. The Fibonacci sequence can be defined recursively as follows:

1.  The first number in the sequence is 0

2.  The second number in the sequence is 1

3.  The nth number in the sequence is the sum of the (n-1)th and (n-2)th numbers in the sequence.

Steps one and two are straightforward. What step three means is simply that any number in the Fibonacci sequence is the sum of the number before it and the number before that. This leads us to the recursive case of computing the Fibonacci sequence. In the above snippet, 55 is the sum of the two numbers before it, 34 and 21. But how did we get to 35? It was the sum of two numbers before it, 21 and 13. 13 is the sum of 8 and 5, and so on, which brings us all the way back to the base case of 0 and 1. 0 and 1 are not defined with recursion, they’re the two original numbers that helped to generate everything that follows. Once the base case it hit, the stack unwinds, and the next sequence in the Fibonacci sequence is returned.

This is what it looks like in Python:

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

This straightforward example hides an awful lot of complexity, but it’s a great place to get started. One thing to consider is that because every number in the Fibonacci stack has to be calculated fresh each time it’s run through, generating the Fibonacci sequence recursively runs in O(2^n) time. Slow!

## Reasoning about Recursion

Back in chapter 4, we discussed permutations, and I showed you a simple iterative solution for coming up with all the combinations of a set of items in an array. Then in chapter 6, we discussed stacks and queues, and I showed you how you can use one to more effectively solve the permutations problem. Now we’re in chapter 11, and it’s time to discuss how to use recursion to generate every combination of items in an array.

First, the code:

``` python
def permute(arr):
    result = []
    _permute_helper(arr, 0, len(arr) - 1, result)
    return result

def _permute_helper(arr, left, right, result):
    if left == right:
        result.append(arr.copy())
    else:
        for i in range(left, right + 1):
            arr[left], arr[i] = arr[i], arr[left]  # Swap
            _permute_helper(arr, left + 1, right, result)
            arr[left], arr[i] = arr[i], arr[left]  # Swap back
```

Here’s another example from chapter 7, where I talked about heaps. In that chapter I showed an example of the heap "bubble up" operation as a while loop.

``` python
def _bubble_up(self, index):
    current = index
    parent = self.get_parent(current)

    while current > 0 and self.heap[current] > self.heap[parent]:
        # Swap current with parent
        self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
        # Move up the heap
        current = parent
        parent = self.get_parent(current)
```

It stands to reason that once an item has been bubbled up, if it’s larger than its parent it can simply be bubbled up again. That sounds like a job for recursion! In this example, the while loop is replaced by a recursive call to `_bubble_up`:

``` python
def _bubble_up(self, index):
    parent = self.get_parent(index)

    if index > 0 and self.heap[index] > self.heap[parent]:
        self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
        self._bubble_up(parent)
```python

### When you (might) have a recursive pattern

The best way to determine if a problem can be solved recursively is to figure whether the problem can be broken down into smaller problems. That’s good advice for any problem, but when it comes to recursion if you can’t see that bigger picture, all the code in the world is not going to get you across the finish line.

Another note: it takes practice. When I first learned about recursion I saw it everywhere. This dog’s wagging tail? Recursion! This bowl of soup? Recursion! Except it wasn’t true in either case.

As I began to work more with recursion I began to get a better sense of what the pattern entailed, but it took practice and really trying to get a sense of all of the pieces of the puzzle.

### Don’t paint yourself into a corner!

After years of losing at chess I decided to finally follow a piece of advice I’d ignored for as long as I’ve been losing: "In order to get better at chess you have to do tactics puzzles." A tactics puzzle is a chess problem that has a very specific solution, and might be marked something like "mate in three moves" or "find a way to capture the knight." I started doing tactics puzzles and if there’s one thing I definitely started to get better at it was…​tactics puzzles.

The only problem with that is, when you’re actually playing a game of chess, the odds that the game will somehow spontaneously go in the exact direction of a tactics puzzle that you’ve already studied are pretty slim. Try telling that to the guy who’s been studying nothing but tactics puzzles! I began to believe that every move was "mate in two," or "win the knight," and as long as my opponent remained calm and didn’t go along with my plan, well, I continued to lose at chess. It was only by expanding my focus to other phases of the game — the opening, the middlegame, the endgame — that I could deploy my tactical knowledge in the service of larger ideas. Without the larger ideas, I wasn’t going to be winning too many games of chess.

The same can happen with recursion. The first time I worked with recursion I thought it was so fantastically brilliant that every problem absolutely must be able to be solved recursively. Well, it can’t. Not only is that not possible, but in many cases recursion isn’t even the best solution to the problem.

Write your code out first. Get it working as quickly and as simple as you can. But don’t paint yourself into a corner by trying to start with a recursive implementation, even if you can see one. Start by developing working code that allows you to explore the problem in a deep, complex way and then if recursion still suggests itself — go for it! I will return to this idea again in the discussion of Dynamic Programming in Chapter 13.

## Example Questions

### Factorial

### Fibonacci

### Making Change

### Reversing a String

## Example Questions

### Swap two numbers in place

### Refactor this function

"Refactor this function" is a very, very common interview question as it can really show and interviewer exactly how you think about code. The problem will take one of two forms: Either a function isn’t working and you have to get it to work, or a function is working but can surely be improved. Refactoring is such an important skill that entire books have been written about it.

Here is some real-world React production code that I’ve been pushing and pushing my team to fix, and I think it makes for a great interview question. It’s used to convert JSON data into values that can be passed to the d3.js library to create a data visualization.

Please spend a moment thinking about how you would approach this question before looking at the answer. How would you refactor this code to make it more readable, more maintainable, and more efficient?

``` javascript
graphicData = vizData ? (
  visData.map((obj) => ({
    name: obj.time,
    date: obj.date,
    value: obj.value,
    value2: obj.value2 ? obj.value2 : null,
    value3: obj.value3 ? obj.value3 : null,
    value4: obj.value4 ? obj.value4 : null,
    value5: obj.value5 ? obj.value5 : null,
    value6: obj.value6 ? obj.value6 : null,
    value7: obj.value7 ? obj.value7 : null,
  }))
) : (
  <></>
)
)
```
