import random

# Global joke storage
jokes = {
    "programming": [
        "Why do programmers hate nature? Too many bugs.",
        "Why do Java developers wear glasses? Because they don't C#."
    ],
    "dad": [
        "I only know 25 letters of the alphabet. I don't know y.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
}


# Get jokes of a certain category
def get_joke(category="programming"):
    if category not in jokes:
        return "No jokes found for this category!"
    return random.choice(jokes[category])


# Add jokes
def add_joke(category, joke):
    if not joke:
        return "Joke cannot be empty!"

    if category not in jokes:
        jokes[category] = []

    jokes[category].append(joke)
    return f"Joke added to {category}!"

# List all categories
def list_categories():
    return list(jokes.keys())


# Get random jokes (across categories)
def get_random_joke():
    all_jokes = []
    for category in jokes.values():
        all_jokes.extend(category)
    return random.choice(all_jokes)