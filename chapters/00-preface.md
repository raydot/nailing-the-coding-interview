# Preface

# Why I Wrote This Book

In 2008 my wife and I decided to move from New York to San Francisco for a variety of reasons, but one of the biggest was that *surely* I could easily find a job in a tech company. I’d been working in internet, web, and multimedia technologies for my entire (short) career, I had been teaching computer programming to graduate students, and the Bay Area was vibing big with opportunities for people with my kinds of smarts. On the advice of a friend in the industry, I sent my resume out to several placement agencies, all of which said I was exactly the kind of person companies were looking for and that I could start interviewing right away. And I did. Companies were interested in me almost immediately. I even turned down several initial interviews because surely I could land a job with the "big guys" — Google, Facebook, Apple, etc.

Finally, the chance came. Huge role, huge company — not one of the ones I just mentioned but still huge — and I knew this was going to be a walk in the park. Heck, cancel all the rest of the interviews you have scheduled, because you’re not going to want to look at anyone else. I put on my best suit, took a long train ride to Mountain View, and walked into the lobby of the company before being sat down in a room with a huge whiteboard on one wall.

I was soon joined by an incredibly cranky, scruffy tech bro who didn’t know why I was there, didn’t know why he was there, and who said, "Let’s just do an easy one. How would you build a machine that could count out change?"

*Um…​what?*

"You know, change." He moved over to the whiteboard and wrote in a scrawling hand: *\$17.31* "Like say I buy something for 17.31. You give me a twenty. How would you build a machine that would give me the right change?" He poked the marker cap onto the back of the pen and held it out to me.

*Uh…​well I would…​well first of all the amount of change is \$3.59…​you mean count the money out?*

"\$2.69. So how do you give me the change?"

*Um well I would…​*

And then I don’t remember what I said after that. Something stupid. A `for/loop`. You’d have to keep track of the dollars. The quarters. The dimes and nickels and pennies.

He rolled his eyes at me. "Obviously. But how many of each?"

*Keep, uh, dividing by ten?*

He took the pen back from me, capped it, and walked out of the room without even attempting to hide his disgust. "We’ll let the agency know what we think." That whole encounter took less time than it took me to walk from the street to the conference room. Tech Bro didn’t ask me a single question about me, my prior work experience, or how smart I was.

The moment I walked out of the building I got on the phone and called the agency. I knew I’d blown it, and I tried defending myself to the recruiter — who was not the one making the hiring decision. "So I don’t know, that guy was cranky and I think he was mad about something and I think it’s recursion? Modulo? Tell them I know it’s modulo!"

She promised to find out what they thought, but I was far from optimistic. I looked around the corporate campus and everyone suddenly looked so much smarter than me. I felt as if they were all sitting there eating their lunches in smug, silent contempt of the dodo from New York who couldn’t even count change.

Of course I didn’t get the job.

While I would like to tell you I learned my lesson from that particular interview, I did not. I thought it was a one-off. Forget that guy. He was having a bad day. He doesn’t know what he’s doing.

But then I had another such interview, and another, and a third. All for companies that I thought would simply just hand me the job on the spot.

At one company, as I was leaving I could see the guy who had just finished interviewing me shaking his head as he told the recruiter what a waste of time I was. At another, I tried to bluff my way through the tech interview saying, "Well we don’t need to do this I don’t think, let me tell you about some of the stuff I’ve done. For instance, I taught computer programming in New York!"

The interviewer walked out the door without saying another word to me.

What I didn’t know at the time was that hiring practices were changing. Rather than relying on personal dynamics or team fits, companies were asking coding questions in interviews. Sure they’d get around to all of that other stuff, but first and foremost you had to rip some code. Over the next ten years, I watched with fascination as this practice grew larger and larger. Is it the best way to hire people? I don’t know. I can see both sides of the argument. But it’s clearly here to say, and people who want jobs in tech have got to be prepared for it.

This book is for those people.

# Who Should Read This Book

A common question I see asked often in chat forums goes something like this: "I’ve been studying LeetCode for a few weeks now, and I can’t even answer the most basic questions. Should I quit?" The reason for this usually turns out to be because the question asker has assumed that LeetCode is the place to begin. It isn’t. Without a basic knowledge of data structures and algorithms — commonly known as "DSA" — you won’t get far on LeetCode at all. It’s like trying to swim against a strong ocean current. You’ll make no headway and only tire yourself out until you can’t swim at all.

This is not an isolated problem, because many people have learned computer programming on their own, or from "bootcamps," or from YouTube videos, or even in school. All of these are great ways to learn, and they can even be enough to get started in a career and maybe even get a decent job, but it’s difficult to progress from there without more advanced knowledge.

This book is the DSA primer you might not have gotten if you don’t (or even if you do) have a computer science degree, or if you got one in the days before coding questions became required for most programming jobs. Coding boot camps, for instance, are a great way to gain some basic knowledge about how to get started as a developer, but they aren’t necessarily focused on teaching the broader concepts covered by DSA. This book aims to bridge that gap.

# How to use this Book

The primary goal of this book is to help you get a job. The secondary goal of this book is to help you *develop intuition* about how to solve coding problems. Developing intuition is a vital skill for programmers because it allows you to reason more quickly and accurately about the problems you’re trying to solve.

When I first decided to try to really learn math as an adult, outside of school, I was given some really good advice by a very smart person. She told me not to worry so much about the specifics of equations, but instead to try to understand what the equation is trying to do. $`y=1/x`$, for instance, must describe a limit since x can never reach zero because anything over zero is undefined. I can see that graph in my head. If I can’t see it exactly, I can at least understand the basic idea it’s trying to convey.

x is a number that will get smaller and smaller and smaller but will never hit zero, so it describes a curve that glides along the y-axis, peaking at one, before it turns to never reach zero along the x-axis. I’m not a human calculator, I just found a way to understand what anything over zero must represent. It forms a picture in my mind that I can understand.

I tell my students, "Don’t start coding before you understand what you’re trying to do." Because if you don’t you’re going to be just like the x in that graph. You can push yourself further and further and further along an axis towards your goal, but you’ll never reach it.

If instead you stop for a moment and try to take a concept and put it into words that you can understand, then you’ll be more prepared to see when it’s useful in a coding interview. If you pause and try to really unpack what it’s saying and what it’s trying to do, you won’t have to memorize it because you can simply re-create it from your understanding. This will also build your skill at *pattern recognition*, which is a vital skill for being able to solve complex problems under pressure.

"I see that x at the bottom of the fraction, so I know x can never be zero. Because it’s in the denominator of the fraction I know that the bigger the number gets, the smaller the equation gets. 1/1 is pretty small, 1/10,000 is even smaller and 1/1,000,000,000 is tiny. Aha! This equation must describe a limit approaching zero!"

I didn’t look that up, I didn’t memorize that, I only have a general idea of what the resulting graph might look like. I just used my understanding and a little bit of intuition to explain that example, and I’m pretty sure I’m right. The more you can break down the ideas in this book, into understandable, recognizable, and digestible chunks, the sooner you’ll master the ideas needed to prevail. If all you do it try to memorize a bunch of abstract concepts, you’ll be like the x in that graph, pushing yourself further and further along an axis towards your goal but never reaching it.

There will be several sections in this book that will be labeled "Developing Intuition" that are designed to help you develop this skill. I encourage you to take your time with these sections, and to really try to understand what they’re saying.

# Have a Plan

My first job as a computer programmer — long before coding tests became the norm — began with a phone call on Friday afternoon. Would I be willing to come down on the following Tuesday and interview for a position with a newly formed tech company? I eagerly said yes, hung up the phone, and realized I had no idea how to do what they were hiring me for. So I went into the storeroom at work and "borrowed" the manual for the software I was expected to know how to use. I read the whole book from cover to cover twice over the weekend, and somehow managed to string together a small demo that convinced the company to give me the job. I’ve been a programmer ever since.

My advice to you: Don’t do that.

You have to give yourself enough time to be able to not only read about DSA, but to sit down and write some code and try some things and hopefully really absorb the content this book has to offer.

To that end, I advise coming up with a plan that you can realistically accomplish. Maybe you already have some knowledge of DSA, and maybe it will only take you six weeks for this book to sink in. If you’re like me and maybe you like to spend more time with things to feel like fully understand them then perhaps a schedule of 15 weeks is more appropriate. Or maybe you’re starting from a place where it will take you more than a year. I can’t say. I don’t know you, and I can’t see you. But I do want to help you.

Sit down soon and maybe skim through this book one time. Take a moment to estimate how long it will take to read it through and work through all the problems. Maybe you already know some of the things in each chapter. Maybe you can already tell that some chapters will go quicker than others. Whatever you decide, write down how long you think it will take. Seriously, take out a pen and a piece of paper, and write it down. This gives you a baseline for measuring your progress.

Then build a plan around that longer time period. Will you put two hours a day into this book? 15 minutes on the bus ride to work? Marathon two-day sessions every weekend? Figure that part out and write it all into a calendar — preferably one that you can easily modify.

As you work through the first several chapters, check back in with this plan. Is it going faster or slower than you think? Maybe everything is going exactly as you planned — great! But if the time is not what you thought it was, go ahead and readjust your calendar to make a more realistic estimate.

The other thing that matters is consistency. However you plan to study, make sure you make it a habit.

After you’ve honed in on a realistic assessment, you’ll have some way to track your progress. You’ll also know when you can start looking for work, and when you can plan to attend an interview and be effective. The more diligent and patient and careful you are in your planning, the more likely you are to reach your goal.

If this is a Friday and you have the interview on Tuesday, good luck!

# How This Book is Organized

This book progresses in a common sense fashion, beginning with simpler concepts and then building on those concepts to get to more advanced ideas.

The first small section of this book covers some introductory basics. There’s also a section on Big-O notation, which is a way to describe how long it takes for an algorithm to run. Big-O scares a lot of people, and it’s my hope that I’ve covered the subject in a way tha makes it easy to understand.

Armed with your knowledge of Big-O, you’re ready to proceed into Part One of the book, which covers the basics of data structures. You’ll use the knowledge gained in Part One to tackle the subjects presented in Part Two, which covers algorithms. Specifically, algorithms that work with the data structures you’ve learned about in Part One, and also the algorithms you’re likely to encounter in a coding interview. Part Three will cover an assortment of topics related to DSA, but that you’re probably not going to encounter at the coding interviews this book is targeting. Still, it can serve as an introduction to these more advanced topics, and should be an adequate starting point for trying these sorts of problems on your own. Part Three also covers my new favorite teaching tool, AI, and shows how you can use it to both study and solve coding problems.

The several sections in this book that begin with the heading "Developing Intuition" are written to get you to come to an understanding that will never leave you. They try to make the abstract concepts in this book more concrete, and to give you a way to understand them that will stick with you for the rest of your life. Take some extra time with these. Putting in a little effort in the short term might save you lots of time in the long run because you won’t have to struggle to understand what you’re being asked.

One last note: this book is not a comprehensive guide to data structures. The focus of the book is on the coding interview, and how to prepare for it. Pretty much every subject covered in this book has been covered in much greater depth somewhere else. I strongly encourage you to seek out those resources, and to approach the infinite amount of computer science knowledge available with curiosity, an open mind, and a willingness to learn. I am only your guide. The path you choose to take is up to you.

# Conventions Used in This Book

The following typographical conventions are used in this book:

*Italic*  
Indicates new terms, URLs, email addresses, filenames, and file extensions.

Constant width  
Used for program listings, as well as within paragraphs to refer to program elements such as variable or function names, databases, data types, environment variables, statements, and keywords.

**`Constant width bold`**  
Shows commands or other text that should be typed literally by the user.

*Constant width italic*  
Shows text that should be replaced with user-supplied values or by values determined by context.

> > 💡 **TIP**
>
> > This element signifies a tip or suggestion.

> > 📝 **NOTE**
>
> > This element signifies a general note.

> > ⚠️ **WARNING**
>
> > This element indicates a warning or caution.

# Using Code Examples

All code examples from this book are available in the GitHub repository:

<https://github.com/raydot/nailing-the-coding-interview>

The code examples are organized by chapter and are free to use for learning and practice. You're encouraged to experiment with them, modify them, and use them as a foundation for your own projects.

This book is here to help you succeed in coding interviews. The code examples are provided under an open license - feel free to use them in your learning, practice problems, and interview preparation. Attribution is appreciated but not required.

# How to Contact the Author

Have questions, found an error, or want to provide feedback? Here's how to reach out:

- **GitHub Issues**: Report errors or suggest improvements at <https://github.com/raydot/nailing-the-coding-interview/issues>

- **GitHub Discussions**: Ask questions or discuss topics at <https://github.com/raydot/nailing-the-coding-interview/discussions>

- **Website**: Visit the book's website for updates and additional resources

Your feedback helps make this book better for everyone!

# Acknowledgments

To Momma and the Boy, because they know why. Also thanks Dad, for getting me on the plinth in the first place.
