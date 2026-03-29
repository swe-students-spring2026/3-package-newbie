import joke_center

# Test get_joke function

def test_get_joke_valid_category():
    # Should return a string when category exists
    joke = joke_center.get_joke("programming")
    assert isinstance(joke, str)
    assert len(joke) > 0


def test_get_joke_invalid_category():
    # Should return fallback message for unknown category
    result = joke_center.get_joke("unknown")
    assert result == "No jokes found for this category!"


def test_get_joke_randomness():
    # Calling multiple times should still return valid strings
    joke1 = joke_center.get_joke("dad")
    joke2 = joke_center.get_joke("dad")
    assert isinstance(joke1, str)
    assert isinstance(joke2, str)

# Test add_joke function

def test_add_joke_new_category():
    # Adding joke to a new category should create it
    result = joke_center.add_joke("new_category", "Test joke")
    assert result == "Joke added to new_category!"
    assert "new_category" in joke_center.list_categories()


def test_add_joke_empty_string():
    # Should reject empty joke input
    result = joke_center.add_joke("dad", "")
    assert result == "Joke cannot be empty!"


def test_add_joke_effect():
    # After adding, the joke should be retrievable
    joke_center.add_joke("programming", "Temporary test joke")
    jokes = [joke_center.get_joke("programming") for _ in range(10)]
    assert any("Temporary test joke" in j for j in jokes)


# ---------------------------
# Test list_categories function
# ---------------------------

def test_list_categories_type():
    # Should return a list
    categories = joke_center.list_categories()
    assert isinstance(categories, list)


def test_list_categories_content():
    # Should include default categories
    categories = joke_center.list_categories()
    assert "programming" in categories
    assert "dad" in categories


def test_list_categories_not_empty():
    # Should not be empty
    categories = joke_center.list_categories()
    assert len(categories) > 0


# ---------------------------
# Test get_random_joke function
# ---------------------------

def test_get_random_joke_type():
    # Should return a string
    joke = joke_center.get_random_joke()
    assert isinstance(joke, str)


def test_get_random_joke_not_empty():
    # Returned joke should not be empty
    joke = joke_center.get_random_joke()
    assert len(joke) > 0


def test_get_random_joke_multiple_calls():
    # Multiple calls should still return valid jokes
    jokes = [joke_center.get_random_joke() for _ in range(5)]
    assert all(isinstance(j, str) for j in jokes)