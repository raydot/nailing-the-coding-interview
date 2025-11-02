# Preparing for the Coding Interview

If you’ve looked for a job as a developer anytime over the past 10 years, you’ve almost certainly been asked to take a coding test. The very phrase, "coding test," strikes fear into the hearts of developers from Palo Alto to the Passaic. If this describes you, fear no longer. The book in your hands (or on your screen) is your guide to how to take and pass coding tests. With some time, effort, and energy this book will hopefully help you build the knowledge and skills needed to answer coding interview questions like a pro.

## During the Interview

There unfortunately is not a single way in which coding tests are administered by companies. What you are asked can change from company-to-company, and even from interviewer to interviewer. You might be put into a room and asked to solve three questions on your own in an hour, or the interviewer might say "Let’s solve a problem together" and take you through a team exercise. The question might be straightforward or it might be designed to bend your brain. You might be asked to enter your code into a computer or you might be asked to write on a whiteboard.

Coding interviews are primarily given in one of three ways:

1.  In person, with a computer

2.  In person, with a whiteboard

3.  Online using a platform like CoderPad or HackerRank

4.  Online with a whiteboard

Some companies will give longer tests that you can complete on your own time, but these usually ask you to build a project rather than solve coding problems, so they won’t be covered in this book.

If it’s just you and a coding test and a clock then spend a moment thinking about how to maximize your time. The questions will be of different difficulties. Oftentimes you will not be able to answer all of the questions in the time given. Do you feel more comfortable answering several hard questions or a single easy one? If it’s a group exercise, would you like to spend more time talking or more time coding?

> 💡 **TIP**
>
> Don’t stay silent during your interview! It’s ok to ask questions of the interviewer. If you’re not sure what the question is asking, ask for a clarification. If you’re stuck, ask for a hint. If you’re not sure whether or not something is allowed, ask. Communicating your thoughts out loud gives the interviewer a chance to see how you reason through a problem, and how you respond to feedback. Speaking is not only allowed, it’s encouraged!

## What Interviewers Are Looking For

While there’s not one single answer to this question, there are three primary things interviewers are looking for in a coding interview:

1.  What your approach is to problem solving

2.  How familiar you are with the language you’ll be using

3.  How you communicate with others

I’ve been in interviews where the interviewer wanted me to be a robot who could solve a specific problem in one hour. I’ve been in interviews where no matter what I did or said, I wasn’t going to get the job. Most of the time, however, the interviewer is kind and supportive. If they’re good at hiring, they should want you to succeed. Even if you’re not the best candidate for this particular position, maybe they’ll consider hiring you for another position.

The best way to show your interviewer that you’re a good candidate is to be yourself.

> **Sample Interview**
>
> I’m going to take a moment to demonstrate what might occur during a coding interview. This example is an in-person coding interview. The applicant and the interviewer are sitting at a table, with the applicant seated in front of a computer. The applicant’s code is projected onto a screen on the front of the room
>
> If the interview is done online, it will be given through a platform like CoderPad or HackerRank. You can set up your own free accounts on these platforms to practice. They all come with support for a variety of languages.
>
> Here is how a coding interview might go. This particular example is meant to show how you can communicate with the interviewer and express your ideas in a way that shows you understand the problem:
>
> Interviewer: "Let’s build a function that returns a number."
>
> You: "A function that returns a number. Does it matter what language I use?"
>
> Interviewer: "No, use a language you’re comfortable with."
>
> You: "Ok, I’m going to use JavaScript to write a function that returns a number."
>
> ```javascript
> function returnNumber() {
>   var number = 23
>   return number
> }
> ```
>
> Interviewer: "You got it! Now let’s try writing a function that returns the number passed to it, plus ten."
>
> You: "Ok, number plus ten, got it."
>
> ```javascript
> function returnNumber(number) {
>   var myNumber = number + 10
>   return myNumber
> }
> ```
>
> Interviewer: "Great! Now let’s try writing a function that returns the sum of two numbers."
>
> You: "Ok, a sum of two numbers. Any two numbers?"
>
> Interviewer: "Sure, any two numbers you want."
>
> _you type_
>
> ```javascript
> function returnSum(num1, num2) {
>   var sum = num1 + num2
>   return sum
> }
> ```
>
> Interviewer: "Great! Now can you show me how you write a function that returns the sum of all the numbers in an array?"
>
> You: "Ok. How many numbers in the array?"
>
> Interviewer: "Excellent question! Let’s say there are five numbers in the array."
>
> You: "Ok. I’m going to write a function that takes in an array of five numbers and returns the sum."
>
> _you type_
>
> ```javascript
> function returnSumOfArray(array) {
>   var sum = 0
>   for (var i = 0; i < 5; i++) {
>     sum += array[i]
>   }
>   return sum
> }
> ```
>
> Interviewer, "Ok, I’ve the idea you know what you’re doing. I’m just wondering, can you think of any improvements to your code?"
>
> You: "Hmm…​oh man, I always forget that the `var` keyword is no longer used in JavaScript. I can remove that. I’m also going to get rid of those semicolons. They’re optional."
>
> ```javascript
> function returnSumOfArray(array) {
>   var sum = 0
>   for (let i = 0; i < 5; i++) {
>     sum += array[i]
>   }
>   return sum
> }
> ```
>
> Interviewer: "Oh wow, I didn’t even notice that but you’re right, you were using some older JavaScript syntax. But I was looking for something that makes your code more efficient."
>
> You: "Hm. Well I could make the array work for any length of array, not just five numbers."
>
> Interviewer: "Wow, I didn’t catch that either! But let me give you hint. What I’m looking for is a little more…​functional."
>
> You: "Oh! Got it. You know, I know what you’re talking about but I usually use a `for` loop. But I think you can use a reducer function. I don’t quite remember the syntax, do you mind if I look it up?"
>
> Interviewer: "Not at all! Where would you go to do that?"
>
> You: "For something like this I usually go to MDN. I’m going to do a Google search for 'JavaScript array reduce' and see what I find."
>
> Interviewer: "Where would JavaScript programmers be without MDN? Sure, go ahead."
>
> ```javascript
> function returnSumOfArray(array) {
>   return array.reduce((acc, curr) => acc + curr)
> }
> ```
>
> Interviewer: "Ok that’s good…​but you just kinda copied and pasted that. Can you explain what is going on in that function?"
>
> You: "Sure! The function takes in the array. I pass two arguments to the reduce function, `acc` and `curr`. `acc` stands for the accumulator, which holds the sum of all the numbers in the array. `curr` is the current number to be added to the sum. So this function adds the current number to the accumulator and returns the sum."
>
> Interviewer: "Ok, but what’s that funny `⇒` thing you used?"
>
> You: "Oh, that’s an arrow function. I know it’s a way to write a function…​I think it’s just for `reduce` and maybe `map`? Actually, I’m not really sure."
>
> Interviewer: "It’s not just for reduce, but you’re right, it is a way to write a function. It’s kind of a shorthand for JavaScript functions, and you can use it pretty much anywhere you have a function. We have a few minutes left, can you think of anything else you can add?"
>
> "Would it be ok if a added a test for the function?"
>
> Interviewer: "Wow, great idea! Our dev team is very much test-driven so please go right ahead."
>
> You: "I don’t need to spend a lot of time doing this, but here’s just a simple check. Normally I might do something using Jest, but why don’t I just write write a simple test function that checks if the function returns the sum of the array `[1, 2, 3, 4, 5]`?"
>
> ```javascript
> function testReturnSumOfArray() {
>   var testArray = [1, 2, 3, 4, 5]
>   var result = returnSumOfArray(testArray)
>   if (result === 15) {
>     console.log('Test passed!')
>   } else {
>     console.log('Test failed!')
>   }
> }
> ```
>
> Interviewer: "Perfect addition, and clever approach. Well, I think I have a pretty good sense of your skills. Thanks so much for coming in today."
>
> You: "Thank you so much for taking the time! I hope to hear back from you soon."
>
> Ok, simple example. But consider all of the ways in which your communication tells the interviewer about your skills.
>
> 1.  You repeated the task back to the interviewer
>
> 2.  You asked questions to clarify the problem
>
> 3.  You asked for feedback on your approach
>
> 4.  You demonstrated that you know how to search for a solution
>
> 5.  You demonstrated value-added improvements to your code by adding a test
>
> 6.  You remained calm and polite
>
> 7.  You demonstrated the limits of your knowledge without being defensive or deceitful
>
> If your interview went like this I can’t say you’d get the job for sure, but you’d certainly be in the running!

There are a lot of resources online about how to present yourself in interviews from how to write a resume to how to dress to how to speak. Spend some time looking at these so you’re not surprised by what you find once you get into the interview room.

## Backup Plan

Things don’t always go the way we expect, even (especially) when they seem like they will. Most jobs have more than one applicant so going in the odds are you won’t get the job. Expect it. Don’t take it personally. You might know exactly why you didn’t get the job or you might have no idea. Don’t take it personally, it really doesn’t matter and likely has little to do with you as an individual. The only thing you can do is regroup, figure out how to improve, and figure out what to do differently the next time. After you leave the interview, take a moment and reflect. Write down the questions if you can remember them. Go home and look up anything you didn’t understand. Fortify yourself for the next time. The re-plan, re-apply, and expect to do better the next time!

## The Importance of Doing the Work

There is no learning without doing. You can read this book many times over but unless you have a photographic memory, you will have a hard time learning data structures and algorithms without going through the exercises and trying things out for yourself.

It’s incredibly important that you sit down in front of a computer and try the things you need to learn from this book. At the end of most chapters I will give ideas for ways to expand on the concepts that have been covered on your own. As someone who always skips over these kinds of things, I’m asking you not to skip over these things. Spend some time with the ideas. If they’re too easy, find a way to modify them to suit your skill level, or find a LeetCode problem that utilizes them. If they’re too hard, break them down into smaller problems that you can solve — an idea I’ll come back to more than once in this book.

I also suggest you "grow before you know," which means working on problems that seem a little more challenging than you can handle. The more you push yourself, the faster you’ll learn. It’s an uncomfortable feeling, and I suggest you get used to it!

## What about AI?

When I started this book, ChatGPT was on version 3 and newspapers were predicting it was going to mean the end of everything from work to joy to humanity. That hasn’t happened, but it absolutely has changed the way coders work. When I started I proposed to my editor that I would make sure to add a little blurb about AI to the end of every chapter. Less than a year later, and that would not serve the purpose of this book at all. I have gone back through the book and added plenty of information to this book that can help with with coding interviews. This information takes one of three forms:

1.  How to use AI for problem solving, much in the same way you would use it at work

2.  How to use AI to help you learn the concepts in this book

3.  How to use AI to help you prepare for coding interviews

The end of chapter sections still remain, but they have mostly been rewritten to fit with these goals.

There is one thing I absolutely must stress. If this book is in your hands and you have not yet figured out how to integrate AI into your coding workflow, you’re not getting your next job. It’s being used pretty much everywhere, and I have several LLM’s at my fingertips throughout the day that I switch between depending on the problem I’m trying to solve.

If you don’t know how to get started, do an online search, find a tutorial, read on O’Reilly book, or watch a YouTube video. Once you’ve got your AI set up, go ahead and ask it how it can help you with the content of this book. But don’t put it off.

While there is a lot of great information out there about AI there is also a lot of very, very bad information. It’s not a fad, and it’s not going to go away. It’s only by starting to use it that you can see for yourself how it can help you, and how to put it to work in moving your career forward.

You might be wondering whether to bother learning data structures and algorithms at all, given that AI can do so much of the work for you. Every six months since 2022 or so I’ve seen a new article about how AI is going to replace programmers. Then I think back to how many no-code solutions I’ve seen come and go. FrontPage was going to replace developers, Dreamweaver was going to replace developers, WordPress was going to replace developers…​and throughout it all we have yet to be replaced.

If nothing else, learning DSA will give you an advantage. Even if the computer writes all the code for you, AI still does not have an advantage when it comes to understanding the problem space. While it can come up with appropriate solutions it’s not always so good at coming up with optimal solutions. And, it can hallucinate. Developers these days are taking an approach to AI I’ve best heard summed up as "Trust, but verify." So, yes, you should still learn data structures and algorithms, so you can be trusted to verify.
