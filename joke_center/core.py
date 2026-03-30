import random
from typing import List, Dict

# Global joke storage
jokes: Dict[str, List[str]] = {
    "programming": [
        "Why do programmers hate nature? Too many bugs.",
        "Why do Java developers wear glasses? Because they don't C#.",
        "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
        "There are only 10 types of people in the world: those who understand binary and those who don't.",
        "Debugging: Removing the needles from the haystack.",
        "Why did the developer go broke? Because he used up all his cache.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "I would tell you a joke about recursion, but you would have to understand recursion first."
    ],

    "dad": [
        "I only know 25 letters of the alphabet. I don't know y.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I used to play piano by ear, now I use my hands.",
        "Why don't eggs tell jokes? They'd crack each other up.",
        "I’m reading a book on anti-gravity. It’s impossible to put down.",
        "Did you hear about the restaurant on the moon? Great food, no atmosphere."
    ],

    "dark": [
        "I told my computer I needed a break, and it said: No problem — it froze.",
        "Why don’t graveyards ever get overcrowded? People are dying to get in.",
        "I have a joke about time travel… but you didn’t like it.",
        "My computer beat me at chess, but it was no match for me at kickboxing."
    ],

    "tech": [
        "Why was the computer cold? It forgot to close its Windows.",
        "Why did the smartphone go to therapy? It lost its connection.",
        "Why did the server break up with the client? Too many requests.",
        "Cloud computing is just someone else's computer."
    ],

    "pun": [
        "I'm on a seafood diet. I see food and I eat it.",
        "I used to be a baker, but I couldn’t make enough dough.",
        "I’m afraid for the calendar. Its days are numbered.",
        "I once got fired from a canned juice company. Apparently I couldn’t concentrate."
    ],

    "science": [
        "Why can't you trust atoms? Because they make up everything.",
        "Why did the physicist break up with the biologist? There was no chemistry.",
        "Schrödinger’s cat walks into a bar… and doesn’t.",
        "Why are chemists excellent for solving problems? They have all the solutions."
    ],

    "random": [
        "Why did the bicycle fall over? Because it was two-tired.",
        "What do you call fake spaghetti? An impasta.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why did the coffee file a police report? It got mugged."
    ]
}


# ---------- Helper ----------
def _validate_joke_input(joke: str):
    # Check if joke is valid
    if not isinstance(joke, str) or not joke.strip():
        return False
    return True


# ---------- Core Features ----------

# 1. Get a joke by category
def get_joke(category: str = "programming") -> str:
    if category not in jokes or not jokes[category]:
        return "No jokes found for this category!"
    return random.choice(jokes[category])


# 2. Add a joke
def add_joke(category: str, joke: str) -> str:
    if not _validate_joke_input(joke):
        return "Joke cannot be empty!"

    if category not in jokes:
        jokes[category] = []

    jokes[category].append(joke.strip())
    return f"Joke added to {category}!"


# 3. Delete a joke
def delete_joke(category: str, joke: str) -> str:
    if category not in jokes:
        return "Category not found!"

    try:
        jokes[category].remove(joke)
        return "Joke deleted!"
    except ValueError:
        return "Joke not found!"


# 4. List all categories
def list_categories() -> List[str]:
    return list(jokes.keys())


# 5. Get a random joke from all categories
def get_random_joke() -> str:
    all_jokes = [j for category in jokes.values() for j in category]

    if not all_jokes:
        return "No jokes available!"

    return random.choice(all_jokes)


# 6. Get all jokes in a category
def get_all_jokes(category: str) -> List[str]:
    return jokes.get(category, [])


# 7. Get statistics
def get_stats():
    return {
        "total_categories": len(jokes),
        "total_jokes": sum(len(v) for v in jokes.values())
    }


# 8. Get multiple jokes
def get_multiple_jokes(category: str, n: int = 1):
    if category not in jokes or not jokes[category]:
        return []

    return random.sample(jokes[category], min(n, len(jokes[category])))