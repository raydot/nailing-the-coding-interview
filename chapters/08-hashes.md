# Hashes

Welcome to the hashes chapter! In this chapter I will talk about hashes, especially how to construct them with some examples of their primary uses. We will also discuss some common interview questions, of course! I’ll begin the discussion of hashes with an examination of something most programmers are already familiar with, and that’s key-value pairs.

## Key-Value Pairs

A key-value pair is a simple idea. It’s a data structure with two pieces: a key, and a value. The key if often a string, while the value can be any number of different data types.

Here are some examples:

`name: "Popeye the Sailor"`

`#age: 42`

`favorite color: "blue"`

`"likes_spinach": true`

`"favorite numbers": [11, 906, 7135825, 11]`

In the examples above I’ve mixed and matched the data types of the keys and values. The key can be a string, a number, or even a boolean, while the value can be a string, a number, a boolean, or even an array. It depends mostly on the language, the specific implementation of the data structure and in some cases even on the programmer’s preference.

Most computer languages have a data structure that uses key-value pairs, although they’re called something different in almost every language. You might already be familiar with one of the most widely used forms of key-value pairs, and that’s JavaScript Object Notation, or JSON. Here’s a simple sample of a JSON Document:

``` json
{
    "superObject": {
        "foods": {
            "itemOne": "pudding",
            "itemTwo": "mangoes",
            "itemThree": "brussels sprouts"
        },
        "animals": {
            "itemOne": "dogs",
            "itemTwo": "geese",
            "itemThree": "possums"
        },
        "people": "Farmer John",
        "funny numbers": [
            11,
            906,
            7135825,
            11
        ]
    }
}
```

In this JSON "object", the all of the data is stored in key-value pairs. The keys are the strings on the left side of the colons, in this case "superObject", "foods", "itemOne", "itemTwo", "itemThree", "animals", "people", and "funny numbers". The values are the strings on the right side of the colons, in this case "pudding", "mangoes", "brussels sprouts", "dogs", "geese", "possums", "Farmer John", and the array of numbers. In JSON, the keys are always strings, while the values can hold many different types of data.

The reason I put "object" in quotes earlier is because by itself, nothing in a JSON file is an object. It’s just text in string format. Load or "parse" it into a running program, however, and it’s easily accessible as a data structure of objects. The data must be "well-formed" though — you can’t just put in anything in any order and expect it to work.

``` javascript
const superObject = {
    "foods": {
        "itemOne": "pudding",
        "itemTwo": "mangoes",
        "itemThree": "brussels sprouts"
    },
    "animals": {
        "itemOne": "dogs",
        "itemTwo": "geese",
        "itemThree": "possums"
    },
    "people": "Farmer John",
    "funny numbers": [
        11,
        906,
        7135825,
        11
    ]
};

console.log(superObject.foods.itemOne); // "pudding" in JS dot notation
console.log(superObject["foods"]["itemOne"]); // "pudding" in JS bracket notation
```

To access JSON from JavaScript, you can either use dot notation, or bracket notation. For instance to access the value of "itemOne" in the "foods" object, you could use either the dot notation `superObject.foods.itemOne` or the bracket notation `superObject["foods"]["itemOne"]`.

Always keep in mind that the strings themselves are not objects, and the objects are not (necessarily) strings. The J in JSON stands for JavaScript, and JavaScript makes it easy to convert between the two (see the `JSON.parse()` and `JSON.stringify()` functions), but always keep in mind that they’re the same.

Because JSON is in a string format, it’s also easy to send it over the internet, and to build up complicated data structures from captured string data. Easy, yes. Efficient? Eh…​not so much. But we’ll get to that.

Even though the "J" stands for "JavaScript," JSON is an extremely versatile and widely accepted data-storage format. You might already be aware that in addition to JavaScript, JSON can also be read in Python (and Java, and Ruby, and C, and Go, and…​)

Python comes with its own built-in key-value pair data type called a "dictionary," along with its own set of functions to work with them.

``` python
superObject = {
    "foods": {
        "itemOne": "pudding",
        "itemTwo": "mangoes",
        "itemThree": "brussels sprouts"
    },
    "animals": {
        "itemOne": "dogs",
        "itemTwo": "geese",
        "itemThree": "possums"
    },
    "people": "Farmer John",
    "funny numbers": [
        11,
        906,
        7135825,
        11
    ]
}

print(superObject["foods"]["itemOne"]) # "pudding"
superObject.update({"people": "Farmer Jane"})
print(superObject["people"]) # "Farmer Jane"
```python

(Python also has a fantastic library for working with "dataframes" called Pandas, and if you’re interested in data science mixing Pandas with JSON is a great way to get started — check it out!)

> **XML, Ya Coulda Been a Contender**
>
> Back in the early 2000s, XML was the future. With its extensibility (the X in XML), its compatibility, its readability (sorta), and its wonderful, wonderful schemas it heralded the way forward in data storage. Everything could be uploaded, categorized, heirarchized, and stored and we were all assured a glitch-free future.
>
> XML was used in all kinds of applications, including rss feeds, web services, and even in web pages. You didn’t have to be a data scientist to use it, and it was easy to learn. There was even "XHTML", which was XML for web pages, a guarantee that any web page you wrote could be read by any browser, anywhere.
>
> So what happened?
>
> Simple: it wasn’t the easiest thing to work with. Sure, anyone could write an XML document, but in order to use it pretty much anywhere you had to parse it, and you could only parse it if everything was exactly right. This could many times require that you add an awful lot of markup to your markup, and it was a great way to slowly go insane.
>
> Meanwhile, good old HTML didn’t really complain much about bad syntax, databases were a lot more powerful while only being a little harder to work with, and polyfills were just a download away.
>
> And then along came JSON, which was easier to work with, pain-free to parse, and worked everywhere.
>
> The reason I bother to mention XML is because in addition to be a good example of a use for key-value pairs, it’s also a great example of how the road to obsolescence is paved with good intentions. Just because it’s "right," just because it’s "better," just because it’s "the future," none of that means anything if it’s not easy to use. It didn’t take long for someone to build a better-than-XML mousetrap, and you should keep such considerations in the back of your mind when you’re building your own data structures and libraries.

When it comes to key-value pair there are different names for both the data structures used, and the very concept itself. Key-value pairs are also called "name-value," "associative arrays," "maps", "dictionaries," and "hashes" in various programming languages. I wanted to give another example I suspect most people reading this book will be familiar with, and that’s the HTML attribute.

`<img src="rover.jpg" alt="A picture of a dog" width="800" height="600" />`

Surely it jumps right out at you like never before: HTML attributes are key-value pairs! They’re key-value pairs that can be used to modify the behavior of the HTML element to which they’re attached. Specifically, in this example, the keys are "src," "alt," "width," and "height," and the values are "rover.jpg," "A picture of a dog," "800," and "600."

Does this lead you to think of any other examples? I heard someone in the back say "CSS properties," and that’s 100% correct! If you’ve worked with CSS, CSS-in-JS, SASS, or any other flavor of CSS, you’ve worked with key-value pairs.

If you’re more of a backend person, you might be thinking of SQL, and you’d be right there too. If you’re all about that OS you might be thinking of environment variables, and on and on. Key-value pairs are everywhere, specifically everywhere you need a name to go with a value.

## Hash Definition

Great! So then, what’s a hash? A hash is closely related to key-value pairs, and in some languages they might even be the same thing. Specifically, a hash is a data structure that maps keys to values, but what a hash does that a key-value pair does not is specifically use "hash function" to determine where to store the key-value pair in memory. That, as it turns out, is kind of a big deal.

\<DRAWING OF HASH DOING ITS THING TK\>

Here’s an example of when you might use a hash. As a boy I was a huge fan of Hot Wheels cars, and I used to carry them around in a small "garage," which was really just a plastic case with a handle. When I opened up the case the garage had five "levels" of parking, with the levels really being plastic drawers inside the box. Additionally the draws themselves had various slots, some big and some small. Some would fit a single car and others could hold two or three.

I was very meticulous about which car went where, and I had a system. I don’t remember the system, but I remember that I had one. So if I wanted to find all of the race cars, or all of the utility cars, or all of the super cars, I could easily find them by pulling out the right drawer.

The garage could be considered as a kind of hash. Via the sorting system contained in my brain, each car belonged specifically on a certain level, or drawer. Once it was on the right level (drawer) I could easily find it by pulling out that drawer.

When it came to the slots within the drawers I was far less meticulous. As long as the car was on the right level, and within the right size slot on that level, I don’t really care where it went.

Additionally, I could easily add new cars to the garage, but only until the garage was full. Once that happened the only way I could add a new car was to take one out, and if I had enough new cars I had to find a new garage in which to put them.

(Shout out to my mom, when my son was old enough she gave him the garage. Where she kept it all those years I have no idea, but I remembered the cars and the levels!)

This is analogous to how a hash works, except replace my brain with a hashing algorithm, the garage with a hash table, the levels with "buckets," the drawers with "slots," and the cars with key-value pairs.

A hash table allows you to store data in key-value pairs within a larger, organized structure. A hashing algorithm is a way to determine what goes where, with the idea being that the key-value pairs — the data — is evenly spread across the hash table. This makes things quick to find and retrieve, because you can always "unhash" a piece of data to find out where it’s stored, and then go directly to that location. Instead of having to go drawer by drawer to find the car you’re looking for, you can go directly to the drawer where it’s stored.

The benefit of this is not apparent with the small examples I’ve shown thus far, but for large data sets it can be a huge time saver. Take the analogy of a large city without named streets. It would be very difficult to tell people where you live, and even harder for them to find it. Spend a few minutes driving around Downtown Boston and you’ll quickly see that it’s no way to live. Instead, we have named streets, and often times those streets are named in relationship to other streets — like New York City’s numbered grid system. Some streets might even include their orientation as a part of their name — "avenues" tend to run north and south, while "streets" run east and west. "Lanes" usually end in a cul-de-sac, while "roads" tend to be longer and straighter and go through multiple towns.

By understanding the system of roads, the grid, the highways, the landmarks, you can easily find your way around a city without having to know every single street, or stumble from place to place to find what you’re looking for.

Hash tables organize data in specific ways with the goal of making it easier to reference, and thus easier to find. This can bring the lookup times of data stored in a hash table from larger times like O(n^2) (looking for items using for loops) or O(n log n) (items stored in trees) to O(1), which is a huge time savings.

Getting a little less abstract, what a hash function does is take in some data, "hash" it into a value, and then use that resulting value to store the data in memory.

A very basic example might look like this:

INPUT KEY-VALUE PAIR: `name: "Popeye the Sailor"`

HASH KEY-VALUE PAIR: `"Popeye the Sailor" → 12345`

STORE HASH VALUE: `12345`

UNHASH HASH VALUE: `12345 → "Popeye the Sailor"`

The hash function begins by taking some input, in this case the string "Popeye the Sailor." It then applies a mathematical operation to the input, that results in the number 12345. The function stores "12345" in memory as a key, and also "Popeye the Sailor" as a value. When you are ready to retrieve the value, you can pass the key into the hash function, and it will return the value.

That’s the general idea, but let me break it down even more.

I don’t expect anyone is too confused by the idea of a function taking a string value. Focusing on the next step, what exactly does "mathematical operation" mean? There’s not any hard and fast rule, although some hashes are clearly better than others. In the example above I hashed by magic, no matter what string I entered the resulting value was going to be 12345. That’s because it’s an example, and I was trying to make a simple point.

In reality, one way a hash might work is by taking the ASCII value of each character in "Popeye the Sailor" and adding them together.

The ASCII value of "P" is 80, "o" is 111, "p" is 112…​etc. If you add these values together what you actually get is 1,629. From there I can use a modulo function, as discussed in Chapter 4. By using modulo I can guarantee that the resulting value is within a certain range, and that the value will be specific to each input. In this case, let’s say I store the value as `1629%23` or 18. I can then store the value "Popeye the Sailor" at the key 18, and when I want to retrieve it I can pass in 18 and get back "Popeye the Sailor."

Now if you’re the kind of person that teachers absolutely love to have in class, it may have occurred to you that it could be possible for two different strings to hash to the same value. This is absolutely true, and this is what’s called a "collision" in the wonderful world of hashing. Despite the horrible connotation a "collision" usually represents, it’s actually not a bad thing in the world of hashing. Good hashing algorithms expect collisions to happen, and have a way to deal with them.

Before we get to how to handle them there is one more thing to point out about hashing. It absolutely is a wonderful thing in terms of speed, but bear in mind that what you lose is space. Space is no longer as dear as it was when my career began and 256k was considered a luxury, but it’s still something to keep in mind. For every hash you create, you add on to the existing data the side of the hash itself, and if you have a lot of data that can add up quickly.

## Hash Functions

Let’s have a look at a simple hash function. I’ll show the code first and then go over it line by line.

``` python
def simple_hash(key, table_size):
    hash_value = 0
    for pos, char in enumerate(str(key)):
        hash_value += (ord(char) * (pos + 1))
    return hash_value % table_size

class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Using chaining for collision resolution

    def insert(self, key, value):
        index = simple_hash(key, self.size)
        # Handle collisions with chaining
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update existing key
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = simple_hash(key, self.size)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
```javascript

That’s a bit longer than most examples, so I’m going to go through it a function at a time.

``` python
def simple_hash(key, table_size):
    hash_value = 0
    for pos, char in enumerate(str(key)):
        hash_value += (ord(char) * (pos + 1))
    return hash_value % table_size
```javascript

`simple_hash` is a hashing function that works very similarly to the example I gave above with the only difference being that in addition to being passed the string to be hashed, it’s also passed a `table_size.` The `table_size` is the key (again, no pun intended) to handling collisions and space in a hash table, and I’ll be coming back to it before the end of this section.

Otherwise it’s exactly as I described in the "Popeye the Sailor" example. `simple_hash` takes in a string, converts it into a list of characters, convers each number into its ASCII value and adds them all together. It does have the additional multiplying the ASCII value of the character by its position in the string, which helps ensure that two different string that might be the same length and with the same characters in a different order, like "name" and "main," with nonetheless hash to different values. The value is generated by taking the sum of the final value and modulo-ing it by the `table_size`. This last step additionally insures that the value will not exceed the size of the table. It’s a bunch of simple calculations, but you can see that each one provides its own unique twist on the final value.

``` python
class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
```

The hash table — the thing that actually holds all of the key-value pairs — is created and maintained in the `SimpleHashTable` class. When the table is initialized the size is arbitrarily set to 10. The table is defined as a list of lists, and each list holds the key-value pairs that modulo to the same value.

``` python
    def insert(self, key, value):
        index = simple_hash(key, self.size)
        # Handle collisions with chaining
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update existing key
                return
        self.table[index].append([key, value])
```python

Now things are starting to get interesting. The `insert` function of the `SimpleHashTable` class takes in a key and a value, and then uses the `simple_hash` function to determine where to store the key-value pair. If I want to insert "Popeye the Sailor" into the hash table I do it by calling the insert function with the values "name" and "Popeye the Sailor."

But what if there’s already a key-value pair stored at that index? That’s where we get into the concept of a "collision" once again. This function provides a simple fix, it’s going to "chain" the new key-value pair to the existing one. What this means is that the new key-value pair is stored in a list along with the existing key-value pair. When you want to retrieve the value, instead of having to search through every key-value pair you’ve stored, you only have to search through the list of items that have specifically resolved to that index.

In this example the table size is only 10, but there’s no limit to how large the table size can actually be. Well that’s not exactly true, there is a limit, and that limit is the size of the memory of the computer running the operation. You might sense a trade-off here. Too small a table size and you’ll have a lot of collisions. If you’re storing a billion items in a table size of 10, sure you can search it ten time faster and in O(1) time, but you’re still going to have to look through one-hundred million items to find the one you want. Too large a table size and if you don’t run out of memory you’re still going to have to look though a lot of empty space to find what you’re looking for.

``` python
    def get(self, key):
        index = simple_hash(key, self.size)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
```python

What’s going on here in the `get` function of the `SimpleHashTable` class is that it’s doing the same thing as the `insert` function, but in reverse. It takes the key generated by the `simple_hash` function, and then searches through the list of key-value pairs stored at that index. When it finds the key it’s looking for, it returns the value. If it doesn’t find the key, it returns `None`.

Here’s an example of the `SimpleHashTable` in action:

``` python
hash_table = SimpleHashTable()
hash_table.insert("name", "Popeye the Sailor")
hash_table.insert("name", "Olive Oyl")
hash_table.insert("name", "Bluto")
hash_table.insert("name", "Wimpy")
print(hash_table.get("name")) # "Popeye the Sailor"
```python

## More Hash Collisions

Sometimes as a coder you have to be careful about your variable naming. Just this past week I was working on coding a footer for a client web page, and I named the CSS class that I was using to lay it out `.footer`. That doesn’t seem like it would be the end of the world except for the fact that HTML also contains a '\<footer\>' tag, which was being used on the page as well. My CSS class was being applied somewhere I didn’t intend, and that caused me a few problems before I finally figured it out.

The same thing can happen with a hash. Two different keys can be hashed to the same hash value, which then causes a "collision."

Before we get to two different keys being hashed to the same value, let’s stop and consider the reverse case for a moment. Can two different values hash to the same key?

Take this simple example:

``` python
happy_family = {
    "Dad": "Bob",
    "Mom": "Ming",
    "Child1": "Bob", #YES!
    "Child2": "Sally",
    "Child3": "Gunther",
    "Child3": "Bartholomew" #NO!
}
```python

I hope the answer that shot immediately to your head is "no." If it didn’t, just think about it for a moment. One person can live in a house, and then maybe that person gets married and has children and dogs and goldfish and they can all live at the same address, no problem. But the reverse case would cause pandemonium: if two different houses had the exact same address, the mail would never come, the sun would fall from the sky, and the world would slowly decline into an eternal nightmare.

In the example above, it’s perfectly fine for Bob to have a son and name him Bob too. A little confusing, and I’m sure this would quickly give rise to shortcuts like "Big Bob" and "Little Bob," but it’s not a problem.

But what the two instances of `Child3`? It just won’t work. Even between identical twins there’s usually some awareness of which one is "older," even if the difference is only a few seconds. Still and all, there’s one child born first (`Child3`) and one child born second (`Child4`, or, at least not `Child3`).

Python and JavaScript will both handle this example in the same way, they will simply overwrite the first instance of `Child3` with the second instance, and it will be like Gunther never existed. This is not simply because the language creators were trying to be helpful, it’s because this is simply how hashes work. Each key must be unique.

What does this have to do with collisions?

Say you have a hash that is based on character ascii character values. It will generate a unique value for most strings, but two strings like "lake" and "kale" will hash to the same value because they contain the same characters, just in a different order. This doesn’t make that hash functions useless though, because at the end of the day it comes down to how a hash function is implemented.

A widely used algorithm used to handle collisions is called "chaining," which is what I used in the `SimpleHashTable` example above.

## But I thought a hash was…​

Wait wait wait. Data storage? Cryptography? Shredded potatoes? How can all of these things be called a hash?

Think about it like this: a hash is a way to take some data, a little or a lot, and then use a little math to turn it in to a fixed size value. In the examples I’ve given so far I’m storing strings, and it’s a little bit of a disingenuous example because those examples might not give the greatest sense of the real power of hashes.

This is something to keep in mind when reading about coding examples. Because no author can possibly anticipate every single possible way in which a concept might conceivable be used, the examples can sometimes mislead in their simplicity.

Fortunately for me, the author, and you, the reader, we both have an imagination. Let’s use that to scale up the hash example:

Imagine building a hash able for DNA sequences. You could take a DNA sequence, like "ATCGGCTA", and then use a hash function to convert it into a fixed-size value, like 123456789. If there are a billion DNA sequences, you could store them all in a hash table with a size of 1,000,000, and then use the hash function to determine where to store each sequence. In doing so you can store more data in less space, retrieve it quickly, and check for duplicates.

## Building Intuition: What are hashes used for?

## Reasoning about Hashes

> **I ❤️ Lookup!**
>
> When I first started my career, back in the days when the Earth was still in black and white and had yet to cool, most video monitors were made with the now unfamiliar "cathode ray tube" technology. Most monitors were pretty much the same size: 640x480 pixels, and maybe a little more if you had a decent graphics card.
>
> The cable was a VGA cable, which converted the digital signal from the computer into an analog signal for the monitor. Most monitors were only capable of supporting a fixed number of colors, often no more than 256. You may have even at one point heard the term "web safe" colors, which is a reference to the 216 colors that would (hopefully) look exactly the same on any monitor.
>
> But what if your client had some fantastic new brand campaign, and their web page absolutely had to be in WidgetCo Blue®️? This required that you take the number of available colors and "map" them to the desired values on-screen. This would hopefully cause the monitor to display the colors you wanted as you wanted them, but this was entirely up to the graphics card in the user’s computer. Believe it or not for a short period in time going on a web page with a higher resolution than your computer’s on-board graphics card could actually crash your computer.
>
> The way this color conversion was accomplished was through a CLUT, or Color Look-Up Table. The CLUT was a hash table that took an existing color value and mapped it to a different one. Web-safe blue might be RGB(0, 0, 255), but WidgetCo Blue might be RGB(10, 140, 255). The CLUT would convert from one to the other, and the monitor would attempt to display the color as best it could. Sometimes the CLUT would even fail to unload when the browser was quit, and your monitor would display everything using the WidgetCo palette until the computer was restarted.
>
> While that problem has (thankfully) gone away, I still have a special fondness for lookup tables! Recently on a project we had a bunch of employee headshots that had been named according to several different naming conventions, but we need to associate the employee name with the appropriate headshot.
>
> Rather than re-name all the files, we create a JSON "lookup table" that mapped the employee name to the file name. This way, we could easily look up the employee name and get the file name, and then use that to display the headshot. It could support multiple photos and naming conventions for employee photos, and it was easy to update and maintain.

## Hashes and Encryption

Hashing is used all the time in encryption, and it’s a good way to create secure passwords. The way hashing works is that it takes a string and runs it through a hashing algorithm that returns a fixed-length string of characters. If you know the hashing algorithm, you can run it in reverse to get the original string.

For instance, running the following strings through the MD5 hashing algorithm: will return the following results:

"Hello, world!" 6cd3556deb0da54bca060b4c39479839

"Butterfly!" 8a2f51207269787badf21399163a54cb

"I’m glad I’m not a purple cow, though I have never seen one." 60d99c809d801d4c2c9603c42c017042

Every time you enter a given set of characters into the MD5 hashing algorithm, it will always return the same 32 character string. The string is comprised of sixteen hexadecimal characters, ("8A, 2F, 51, etc…​") which allows for a whopping 128 bits of information.

You might have noticed that all of the strings I ran through the algorithm returned the same length of 32 characters. This would be true whether I entered a single character, the entire works of Robert Frost, or the source code for Windows 95. No matter what you put in, the MD5 hashing algorithm will always return a 32 character string.

Because of this you may have seen it used to "verify" a downloaded file. Some web sites will provide you with a hash of the file which you can then run against the file to see if it matches. If it does, you know you’ve got what you’re expecting, and not some malicious code.

I chose MD5 for the example here because it’s an older protocol still in fairly wide use, but it was invented in the days where most computers ran on the AMD 486 chipset which, at its highest end, had a blazingly slow clock speed of 100 MHz. Now you can buy a palm-sized Raspberry Pi for \$15 that has a clock speed of 1.5 GHz (that’s 1,500 MHz) that can easily crack MD5 hashes in a matter of minutes. Please just take this as an example and not a best practice — and do not use MD5 to secure something important because it will not protect you against someone who knows what they’re doing. There are plenty of more modern and secure hashing algorithms out there, and I chose MD5 purely for its pedagogical value and little else.

``` python
import hashlib

# Create a hash object using MD5 algorithm
hash_object = hashlib.md5()

# Update the hash object with a message
hash_object.update(b"Hello, world!")

# Get the hexadecimal digest of the hash
hex_dig = hash_object.hexdigest()

print(hex_dig)
```python

I keep saying "hash!" and "hashing algorithm!" but what does that mean in the context of MD5, exactly? Recently I came across a clever example of it online. Someone posted a photo of a flyer trying to return a lost wallet. The advertisement said "If this is your wallet, please call the following number:"

Add this → 81562314 To your birthday → YYYYMMDD Call this number→ 91XXXXXXXX

This is a simple hashing algorithm that provides the "public key" of 81562314 to anyone, combine with the "private key" of the lost wallet’s owners birthday to give the result of a phone number to call. If you don’t know the birthday, you can’t get the phone number. Of course, there is a 1/365 chance that you can simple guess the birthday, but that’s a low enough chance that the method paired with other identifying factors (like the name or amount of money in the wallet) is fairly secure.

## Salts

Salts can be used in addition to hashing to make passwords even more secure. A salt is a random string of characters that is added to the password before hashing it. So even if two people have the same password, they will have different hashes because their salts will be different. This makes it much harder for someone to crack the password, because an intruder would need to know both the password and the salt in order to get the original string. It’s specifically useful against "rainbow tables," which are pre-computed hashes of common passwords. This doesn’t mean you should continue to use "unicorn123" as your password, but it does mean that if you do maybe a salt can make it a wee bit harder for someone to guess.

## Example Questions

### Word Count

This is an incredibly common interview question and it’s a great way to get your head around hashing. While the solution doesn’t use a hashing algorithm it does use a hash table.

Given a piece of text, count the frequency of each word in the text. For testing I’ve included some repetitive silly text that demonstrates how the algorithm works.

``` python
text = """
I like dogs. I have a dog. Dogs are fun. Dogs like to play.
Dogs are fun and play and run. Dogs like to run and play.
I like dogs and dogs like me. Dogs like toys. Dogs like treats too.
I like to play with my dog. I like to run with my dog.
Some dogs sleep all day. Some dogs run all day.
My friend has a dog.  All dogs are good dogs.
All dogs are friends.
"""

def word_count(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

result = word_count(text)

for word, count in result.items():
    print(f"'{word}': {count}")
```javascript

Notice the initialization of the Python dictionary (a type of hash table) named `word_count`. This function is simple: it checks to see if the word is in the dictionary. If it isn’t, it adds it with a count of 1. If it is, it increments the count by 1.

The result is a dictionary (which, again, is a kind hash table) with each word as a key and the count as a value. It’s a good technique to know because it can be used to solve a few different types of interview questions.

There are a few helper things in there that remove whitespace and punctuation from the text, but a hash table is the main data structure used to solve the problem.

It doesn’t have much to do with hashing, but as a stretch goal try playing with the output. Can you display it in a more interesting way? Sort the results by frequency? Alphabetically? Display only words that appear more than once?

### Anagrams

Anagrams are always fun things to solve and I’ve noticed them a lot lately on bumper stickers, as they’re a clever way to say how you feel without actually saying what you feel.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. One of the more famous examples is "Mr. Mojo Risin'" which is an anagram of "Jim Morrison." Another is "The Morse Code" which is an anagram of "Here come dots." For an example that was made popular sometime after 1968, the game "Words With Friends" is won by taking the letters in your hand and rearranging them to form a word on the board.

Anagram finding is a fantastic job for a hash table. The idea builds on the earlier word count example:

``` python
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Create a hash table to count character frequencies
    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    return all(count == 0 for count in char_count.values())
result = is_anagram("listen", "silent")
print(result)  # True, because "listen" is an anagram of "silent"
result = is_anagram("hello", "world")
print(result)  # False, because "hello" is not an anagram of "world"
```python

Can you come up with a way to connect Python to a dictionary API and use this code to return anagrams of your name? Or create an app that lets you cheat at "Words With Friends?" (If you get caught just tell your friends it’s a programming exercise. True friends will understand.)

### Palindromes Revisited

We’ve looked at how to solve the palindrome problem using a string and a stack, and maybe you want to go back and try the problem at the end of Chapter 6 if you haven’t already.

We can put a twist on the anagram problem by checking to see if a string is a palindrome by using a hash table. The general idea is to use a hash table to count the number of times each character appears in the string. If the string is a palindrome, then each character must appear an even number of times, except for one character which can appear an odd number of times. The thing to keep in mind here is that of course there could be a string that meets this criteria but is not a palindrome, like "aabbccd." This solution *could* be used to solve the string is a permutation of a palindrome, which might mean you’re on the right track.

``` python
def is_palindrome_permutation(s):
    char_count = {}
    for char in s:
        if char.isalnum():  # Ignore non-alphanumeric characters
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count <= 1
result = is_palindrome_permutation("Tact Coa")
print(result)  # True, because "Tact Coa" can be rearranged to "taco cat"
```

There’s not necessarily a use case for solving this exact problem, but it should give you some ideas. Other more computer science-y problems that could be solved with this technique might include encryption, compression, and even some types of data storage. I encourage you to think of examples of each of these and try to implement them using a hash table.

### Using AI to Study for Hash Problems

While most of what I’ve talked about in this chapter is very fundamental, hashing is pretty widely used and important to understand.

Using AI, determine a few different widely used hashing algorithms, and then write simple programs that implement each of them. Feed all of the program the same input. Can you come up with a way, using AI, to determine which algorithm is the best for a given input? Can you come up with a way to measure speed? Space? Collisions? Can you come up with a visual representation of a given hash algorithm that allows you to compare every one you’ve chosen?
