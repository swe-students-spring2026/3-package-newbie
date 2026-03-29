import random
from typing import List, Dict

# Global joke storage
jokes: Dict[str, List[str]] = {
    "programming": [
        "Why do programmers hate nature? Too many bugs.",
        "Why do Java developers wear glasses? Because they don't C#.",
        "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'"
    ],
    "dad": [
        "I only know 25 letters of the alphabet. I don't know y.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ],
    "dark": [
        "I told my computer I needed a break, and it said: No problem — it froze."
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