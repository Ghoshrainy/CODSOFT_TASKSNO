import pandas as pd

from src.recommender import (
    load_books,
    create_similarity_matrix,
    recommend_books,
    recommend_by_preference
)


DATA_FILE = "data/books.csv"
OUTPUT_FILE = "outputs/recommendations.csv"


def main():

    books = load_books(DATA_FILE)

    similarity_matrix = create_similarity_matrix(books)

    print("\n📚 BOOK RECOMMENDATION SYSTEM")
    print("-" * 40)

    print("\nAvailable Books:\n")

    for i, title in enumerate(books["title"], start=1):
        print(f"{i}. {title}")

    try:
        choice = int(
            input("\nEnter the number of a book you like: ")
        )

        if choice < 1 or choice > len(books):
            print("❌ Invalid book number.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    selected_book = books.iloc[choice - 1]["title"]

    recommendations = recommend_books(
        books,
        similarity_matrix,
        selected_book
    )

    print(f"\nRecommendations based on: {selected_book}")
    print("-" * 60)

    for i, book in enumerate(recommendations, start=1):
        print(
            f"{i}. {book['title']} "
            f"by {book['author']} "
            f"| Match: {book['match_score']}%"
        )

    recommendations_df = pd.DataFrame(
        recommendations
    )

    recommendations_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"\n✅ Recommendations saved to: "
        f"{OUTPUT_FILE}"
    )

    print("\n" + "=" * 60)
    print("🔎 PERSONALIZED PREFERENCE SEARCH")
    print("=" * 60)

    preference = input(
        "\nEnter a topic, genre, or author you prefer: "
    )

    preference_results = recommend_by_preference(
        books,
        preference
    )

    if preference_results.empty:
        print(
            f"\n❌ No books found for: {preference}"
        )
    else:
        print(
            f"\n📖 Recommendations for: {preference}"
        )
        print("-" * 60)

        for i, (_, book) in enumerate(
            preference_results.iterrows(),
            start=1
        ):
            print(
                f"{i}. {book['title']} "
                f"by {book['author']} "
                f"| Rating: {book['rating']}"
            )

    print("\n" + "=" * 60)
    print("📊 RECOMMENDATION SUMMARY")
    print("=" * 60)

    print(f"Selected Book: {selected_book}")
    print(f"Preference: {preference}")
    print(
        f"Recommendations Generated: "
        f"{len(recommendations)}"
    )
    print(
        f"Preference Matches: "
        f"{len(preference_results)}"
    )


if __name__ == "__main__":
    main()