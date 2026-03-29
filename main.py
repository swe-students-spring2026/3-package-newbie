import joke_center

# Get jokes

print("Programming joke:", joke_center.get_joke("programming"))

# Add a new joke

print(joke_center.add_joke("dad", "I'm afraid for the calendar. Its days are numbered."))

# View categories

print("Categories:", joke_center.list_categories())

# Get random jokes

print("Random joke:", joke_center.get_random_joke())