import pytest
import joke_center


# ---------- Fixtures ----------
@pytest.fixture(autouse=True)
def reset_jokes():
    # Reset data before each test
    joke_center.jokes.clear()
    joke_center.jokes.update({
        "programming": [
            "Why do programmers hate nature? Too many bugs.",
            "Why do Java developers wear glasses? Because they don't C#."
        ],
        "dad": [
            "I only know 25 letters of the alphabet. I don't know y."
        ]
    })


# ---------- get_joke ----------

def test_get_joke_valid_category():
    # Should return a valid string
    joke = joke_center.get_joke("programming")
    assert isinstance(joke, str)
    assert len(joke) > 0


def test_get_joke_invalid_category():
    # Should return error message
    result = joke_center.get_joke("unknown")
    assert result == "No jokes found for this category!"


def test_get_joke_empty_category():
    # Category exists but empty
    joke_center.jokes["empty"] = []
    result = joke_center.get_joke("empty")
    assert result == "No jokes found for this category!"


# ---------- add_joke ----------

def test_add_joke_success():
    # Add joke to existing category
    result = joke_center.add_joke("programming", "New joke")
    assert result == "Joke added to programming!"
    assert "New joke" in joke_center.jokes["programming"]


def test_add_joke_new_category():
    # Add joke to new category
    result = joke_center.add_joke("new_cat", "Hello joke")
    assert "new_cat" in joke_center.jokes


def test_add_joke_empty():
    # Reject empty joke
    result = joke_center.add_joke("dad", "")
    assert result == "Joke cannot be empty!"


def test_add_joke_none():
    # Reject None input
    result = joke_center.add_joke("dad", None)
    assert result == "Joke cannot be empty!"


# ---------- delete_joke ----------

def test_delete_joke_success():
    # Delete existing joke
    joke = joke_center.jokes["dad"][0]
    result = joke_center.delete_joke("dad", joke)
    assert result == "Joke deleted!"


def test_delete_joke_not_found():
    # Joke not in category
    result = joke_center.delete_joke("dad", "not exist")
    assert result == "Joke not found!"


def test_delete_joke_invalid_category():
    # Category does not exist
    result = joke_center.delete_joke("unknown", "joke")
    assert result == "Category not found!"


# ---------- list_categories ----------

def test_list_categories():
    # Should return list of categories
    categories = joke_center.list_categories()
    assert isinstance(categories, list)
    assert "programming" in categories


# ---------- get_random_joke ----------

def test_get_random_joke():
    # Should return a string
    joke = joke_center.get_random_joke()
    assert isinstance(joke, str)


def test_get_random_joke_empty():
    # No jokes available
    joke_center.jokes.clear()
    result = joke_center.get_random_joke()
    assert result == "No jokes available!"


# ---------- get_all_jokes ----------

def test_get_all_jokes():
    # Should return list
    jokes = joke_center.get_all_jokes("programming")
    assert isinstance(jokes, list)


# ---------- stats ----------

def test_get_stats():
    # Should return stats dict
    stats = joke_center.get_stats()
    assert "total_categories" in stats
    assert "total_jokes" in stats


# ---------- multiple jokes ----------

def test_get_multiple_jokes():
    # Should return up to n jokes
    jokes = joke_center.get_multiple_jokes("programming", 2)
    assert len(jokes) <= 2


def test_get_multiple_jokes_invalid():
    # Invalid category returns empty list
    jokes = joke_center.get_multiple_jokes("unknown", 2)
    assert jokes == []