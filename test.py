import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta.",
    "How does the moon cut his hair? Eclipse it.",
    "What do you call a can opener that doesn't work? A can't opener.",
    "How many tickles does it take to make an octopus laugh? Ten-tickles."
]

def tell_joke():
    joke = random.choice(jokes)
    print("Hey there! Here's a joke for you:")
    print(joke)

if __name__ == "__main__":
    tell_joke()
