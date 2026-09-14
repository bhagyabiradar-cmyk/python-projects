movies = {
    "Inception": ["sci-fi", "thriller"],
    "Interstellar": ["sci-fi", "drama"],
    "Titanic": ["romance", "drama"],
    "Avengers": ["action", "sci-fi"],
    "Joker": ["drama", "thriller"],
    "The Notebook": ["romance", "drama"]
}

print("🎬 MOVIE RECOMMENDATION SYSTEM")
print("-" * 35)

genre = input("Enter your favorite genre: ").lower()

print("\nRecommended Movies:")

found = False

for movie, genres in movies.items():
    if genre in genres:
        print("🎥", movie)
        found = True

if not found:
    print("Sorry, no movies found for this genre.")

print("\nAvailable genres:")
print("Action, Sci-Fi, Thriller, Drama, Romance")