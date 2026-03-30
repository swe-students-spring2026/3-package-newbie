# Joke Center 🎭

A simple and extensible Python library for managing and retrieving jokes by category.

---

## 🚀 Features

* Get random jokes by category
* Add and delete jokes dynamically
* Retrieve jokes across all categories
* List available categories
* Get multiple jokes at once
* Built-in statistics support
* Fully tested with `pytest`

---

## 📦 Installation

```bash
pip install joke-center-wszms384
```

---

## 🔧 Usage

```python
import joke_center

# Get a joke
print(joke_center.get_joke("programming"))

# Add a joke
joke_center.add_joke("programming", "Debugging is like being the detective in a crime movie where you are also the murderer.")

# Get random joke
print(joke_center.get_random_joke())

# List categories
print(joke_center.list_categories())
```

---

## 📚 API Reference

### `get_joke(category="programming")`

Return a random joke from the given category.

* Returns fallback message if category does not exist or is empty

---

### `add_joke(category, joke)`

Add a new joke to a category.

* Automatically creates category if not exists
* Strips leading/trailing whitespace
* Returns `"Joke cannot be empty!"` if invalid input

---

### `delete_joke(category, joke)`

Delete a joke from a category.

* Returns `"Category not found!"` if category does not exist
* Returns `"Joke not found!"` if joke is not in the category

---

### `list_categories()`

Return a list of all categories.

---

### `get_random_joke()`

Return a random joke across all categories.

* Returns `"No jokes available!"` if no jokes exist

---

### `get_all_jokes(category)`

Return all jokes in a category.

* Returns empty list `[]` if category does not exist

---

### `get_multiple_jokes(category, n=1)`

Return up to `n` random jokes from a category.

* If `n` > available jokes → returns all jokes
* If `n` = 0 → returns `[]`
* If category not found → returns `[]`

---

### `get_stats()`

Return statistics:

```json
{
  "total_categories": 7,
  "total_jokes": 34
}
```

---

## ⚠️ Notes

* Data is stored **in-memory only** (not persistent)
* Not thread-safe for concurrent writes
* Global state is mutable (functions modify shared data)

---

## 🧪 Testing

Run tests using:

```bash
python -m pytest
```

---

## 📄 License

GPL v3 License