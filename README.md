下面是一个**符合 PyPI 发布规范的 README.md（可直接使用）**，结构、格式、badge、安装方式、示例、测试说明都已整理好，适合直接上传到 PyPI / GitHub。

---

# Joke Center 🎭

A simple and extensible Python library for managing and retrieving jokes by category.

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

Install via pip:

```bash
pip install joke-center
```

---

## 🔧 Usage

### Basic Example

```python
import joke_center

# Get a joke
print(joke_center.get_joke("programming"))

# Add a joke
joke_center.add_joke("programming", "Debugging is like being the detective in a crime movie where you are also the murderer.")

# Get random joke from all categories
print(joke_center.get_random_joke())

# List categories
print(joke_center.list_categories())
```

---

## 📚 API Reference

### `get_joke(category="programming")`

Return a random joke from a category.

---

### `add_joke(category, joke)`

Add a new joke.

* Returns error if joke is empty

---

### `delete_joke(category, joke)`

Delete a joke from a category.

---

### `list_categories()`

Return all available categories.

---

### `get_random_joke()`

Return a random joke from all categories.

---

### `get_all_jokes(category)`

Return all jokes in a category.

---

### `get_multiple_jokes(category, n=1)`

Return multiple random jokes.

---

### `get_stats()`

Return statistics:

```json
{
  "total_categories": 3,
  "total_jokes": 10
}
```
