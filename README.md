# 😂 Joke Center

![CI](https://github.com/swe-students-spring2026/3-package-newbie/actions/workflows/python-package.yml/badge.svg)

A fun and extensible Python package that provides jokes for developers.
This project demonstrates how to design, test, package, and distribute a Python library using modern software engineering practices.

---

## 📦 PyPI

👉 [PyPI](https://pypi.org/project/joke-center-wszms384/)

Install the package via:

```bash
pip install joke-center-wszms384
```

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

## 🔧 Usage

```python
import joke_center

# Get a joke
print(joke_center.get_joke("programming"))

# Add a joke
joke_center.add_joke(
    "programming",
    "Debugging is like being the detective in a crime movie where you are also the murderer."
)

# Get random joke
print(joke_center.get_random_joke())

# List categories
print(joke_center.list_categories())
```

👉 Full example program:
[Demo Code](https://github.com/swe-students-spring2026/3-package-newbie/blob/main/main.py)

---

## 📚 API Documentation

### `get_joke(category="programming")`

Return a random joke from a given category.

```python
joke_center.get_joke("dad")
```

---

### `add_joke(category, joke)`

Add a new joke to a category.

```python
joke_center.add_joke("dad", "I'm afraid for the calendar. Its days are numbered.")
```

---

### `delete_joke(category, joke)`

Delete a joke from a category.

```python
joke_center.delete_joke("dad", "Some joke")
```

---

### `list_categories()`

Return all available categories.

```python
joke_center.list_categories()
```

---

### `get_random_joke()`

Return a random joke across all categories.

```python
joke_center.get_random_joke()
```

---

### `get_all_jokes(category)`

Return all jokes in a category.

```python
joke_center.get_all_jokes("programming")
```

---

### `get_multiple_jokes(category, n=1)`

Return up to `n` random jokes.

```python
joke_center.get_multiple_jokes("dad", 2)
```

---

### `get_stats()`

Return statistics about the joke database.

```python
joke_center.get_stats()
```

---

## 🧪 Testing

Run tests using:

```bash
pipenv run python -m pytest
```

---

## 🛠️ Development Setup

### 1. Install pipenv

```bash
pip install pipenv
```

### 2. Create virtual environment

```bash
pipenv install
```

### 3. Install development dependencies

```bash
pipenv install pytest --dev
pipenv install build --dev
pipenv install twine --dev
```

---

## 🧪 Run Tests

```bash
pipenv run python -m pytest
```

---

## 📦 Build Package

```bash
pipenv run python -m build
```

---

## 🚀 Publish to PyPI

```bash
pipenv run twine upload dist/*
```

You will need to provide your PyPI API token when prompted.

---

## ⚙️ Project Configuration

This project uses `pyproject.toml` for package configuration.

Example:

```toml
[project]
name = "joke-center-wszms384"
version = "0.4.0"
description = "A fun Python package that provides jokes for developers"
```

---

## 🔐 Environment Variables

This project does **not require any environment variables**.

However, if publishing to PyPI, you must create a token:

* Go to: [Create API Token](https://pypi.org/manage/account/token/)
* Use `token` as input value when uploading

---

## 📂 Example Configuration File

No `.env` file is required.

If needed in the future, you can create:

```bash
.env.example
```

Example content:

```env
PYPI_TOKEN=your_token_here
```

---

## ⚠️ Notes

* Data is stored **in-memory only** (not persistent)
* Not thread-safe
* Global state is mutable

---

## 📊 CI / Build Results

Latest workflow results:

* ![Github Actions Workflow](https://github.com/swe-students-spring2026/3-package-newbie/blob/main/images/action1.png)
* ![Github Test Jobs](https://github.com/swe-students-spring2026/3-package-newbie/blob/main/images/action2.png)

---

## 👨‍💻 Contributor

* [Cheng Hua](https://github.com/wszms384)

---

## 📄 License

GPL v3 License
