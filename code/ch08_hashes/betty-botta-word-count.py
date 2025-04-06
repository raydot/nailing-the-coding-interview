text = """
I like dogs. Dogs are fun. Dogs like to play.
Dogs are fun and play and run. Dogs like to run and play.
I like dogs and dogs like me. Dogs like toys. Dogs like treats too.
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