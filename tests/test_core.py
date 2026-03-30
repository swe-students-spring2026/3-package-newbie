import pytest
import joke_center


# ---------- Fixture ----------
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


# get_joke

def test_get_joke_valid():
    joke = joke_center.get_joke("programming")

    assert isinstance(joke, str)
    assert len(joke) > 0
    assert joke in joke_center.jokes["programming"]


def test_get_joke_invalid():
    result = joke_center.get_joke("unknown")

    assert isinstance(result, str)
    assert result == "No jokes found for this category!"
    assert "unknown" not in joke_center.jokes


def test_get_joke_empty_category():
    joke_center.jokes["empty"] = []
    result = joke_center.get_joke("empty")

    assert result == "No jokes found for this category!"
    assert isinstance(result, str)
    assert len(joke_center.jokes["empty"]) == 0


# add_joke

def test_add_joke_success():
    before = len(joke_center.jokes["programming"])
    result = joke_center.add_joke("programming", "New joke")

    assert result == "Joke added to programming!"
    assert len(joke_center.jokes["programming"]) == before + 1
    assert "New joke" in joke_center.jokes["programming"]


def test_add_joke_new_category():
    result = joke_center.add_joke("new_cat", "Hello joke")

    assert result == "Joke added to new_cat!"
    assert "new_cat" in joke_center.jokes
    assert "Hello joke" in joke_center.jokes["new_cat"]


def test_add_joke_invalid_inputs():
    result1 = joke_center.add_joke("dad", "")
    result2 = joke_center.add_joke("dad", None)

    assert result1 == "Joke cannot be empty!"
    assert result2 == "Joke cannot be empty!"
    assert len(joke_center.jokes["dad"]) == 1  # no change


def test_add_joke_strip():
    joke_center.add_joke("programming", "  spaced joke  ")

    assert "spaced joke" in joke_center.jokes["programming"]
    assert "  spaced joke  " not in joke_center.jokes["programming"]
    assert any(j == "spaced joke" for j in joke_center.jokes["programming"])

# delete_joke

def test_delete_joke_success():
    joke = joke_center.jokes["dad"][0]
    before = len(joke_center.jokes["dad"])

    result = joke_center.delete_joke("dad", joke)

    assert result == "Joke deleted!"
    assert len(joke_center.jokes["dad"]) == before - 1
    assert joke not in joke_center.jokes["dad"]


def test_delete_joke_not_found():
    result = joke_center.delete_joke("dad", "not exist")

    assert result == "Joke not found!"
    assert len(joke_center.jokes["dad"]) == 1
    assert "not exist" not in joke_center.jokes["dad"]


def test_delete_joke_invalid_category():
    result = joke_center.delete_joke("unknown", "joke")

    assert result == "Category not found!"
    assert "unknown" not in joke_center.jokes
    assert isinstance(result, str)


# list_categories

def test_list_categories():
    categories = joke_center.list_categories()

    assert isinstance(categories, list)
    assert "programming" in categories
    assert len(categories) >= 2


# get_random_joke

def test_get_random_joke():
    joke = joke_center.get_random_joke()

    all_jokes = [j for v in joke_center.jokes.values() for j in v]

    assert isinstance(joke, str)
    assert joke in all_jokes
    assert len(joke) > 0


def test_get_random_joke_empty():
    joke_center.jokes.clear()
    result = joke_center.get_random_joke()

    assert result == "No jokes available!"
    assert isinstance(result, str)
    assert len(joke_center.jokes) == 0


# get_all_jokes

def test_get_all_jokes_valid():
    jokes = joke_center.get_all_jokes("programming")

    assert isinstance(jokes, list)
    assert len(jokes) > 0
    assert jokes == joke_center.jokes["programming"]


def test_get_all_jokes_invalid():
    jokes = joke_center.get_all_jokes("unknown")

    assert jokes == []
    assert isinstance(jokes, list)
    assert len(jokes) == 0

# get_stats

def test_get_stats():
    stats = joke_center.get_stats()

    total = sum(len(v) for v in joke_center.jokes.values())

    assert isinstance(stats, dict)
    assert stats["total_categories"] == len(joke_center.jokes)
    assert stats["total_jokes"] == total


# get_multiple_jokes

def test_get_multiple_jokes_normal():
    jokes = joke_center.get_multiple_jokes("programming", 2)

    assert isinstance(jokes, list)
    assert len(jokes) <= 2
    assert all(j in joke_center.jokes["programming"] for j in jokes)


def test_get_multiple_jokes_edge_cases():
    jokes1 = joke_center.get_multiple_jokes("programming", 0)
    jokes2 = joke_center.get_multiple_jokes("programming", 100)

    assert jokes1 == []
    assert len(jokes2) == len(joke_center.jokes["programming"])
    assert isinstance(jokes2, list)


def test_get_multiple_jokes_invalid_category():
    jokes = joke_center.get_multiple_jokes("unknown", 2)

    assert jokes == []
    assert isinstance(jokes, list)
    assert len(jokes) == 0