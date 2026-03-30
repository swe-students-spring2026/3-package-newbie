import joke_center


def print_section(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def main():
    # 1. Get joke by category
    print_section("1. Get Joke by Category")
    print("Programming joke:", joke_center.get_joke("programming"))
    print("Dad joke:", joke_center.get_joke("dad"))
    print("Invalid category:", joke_center.get_joke("unknown"))

    # 2. Add joke
    print_section("2. Add Joke")
    print(joke_center.add_joke("programming", "Debugging is like being a detective in a crime movie where you are also the murderer."))
    print(joke_center.add_joke("new_category", "This is a new category joke"))
    print("After adding:", joke_center.get_all_jokes("programming"))

    # Invalid input
    print("Add empty joke:", joke_center.add_joke("programming", ""))

    # 3. Delete joke
    print_section("3. Delete Joke")
    joke_to_delete = joke_center.get_joke("dad")
    print("Deleting:", joke_to_delete)
    print(joke_center.delete_joke("dad", joke_to_delete))

    # Edge cases
    print("Delete non-existing:", joke_center.delete_joke("dad", "Not exist"))
    print("Delete invalid category:", joke_center.delete_joke("unknown", "joke"))

    # 4. List categories
    print_section("4. List Categories")
    print("Categories:", joke_center.list_categories())

    # 5. Get random joke
    print_section("5. Get Random Joke")
    print("Random joke:", joke_center.get_random_joke())

    # Empty case
    backup = joke_center.jokes.copy()
    joke_center.jokes.clear()
    print("Random joke (empty):", joke_center.get_random_joke())
    joke_center.jokes.update(backup)

    # 6. Get all jokes
    print_section("6. Get All Jokes")
    print("Programming jokes:", joke_center.get_all_jokes("programming"))
    print("Invalid category:", joke_center.get_all_jokes("unknown"))

    # 7. Get stats
    print_section("7. Get Stats")
    stats = joke_center.get_stats()
    print("Stats:", stats)

    # 8. Get multiple jokes
    print_section("8. Get Multiple Jokes")
    print("2 programming jokes:", joke_center.get_multiple_jokes("programming", 2))
    print("Too many requested:", joke_center.get_multiple_jokes("programming", 100))
    print("Zero requested:", joke_center.get_multiple_jokes("programming", 0))
    print("Invalid category:", joke_center.get_multiple_jokes("unknown", 2))


if __name__ == "__main__":
    main()