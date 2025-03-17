import json

GENRES = {1: "Фэнтези", 2: "Антиутопия", 3: "Классика", 4: "Мистика", 5: "Детектив", 6: "Научная фантастика",
          7: "Сказка"}
DECADES = {1: "1860-е", 2: "1880-е", 3: "1890-е", 4: "1920-е", 5: "1930-е", 6: "1940-е", 7: "1950-е", 8: "1960-е",
           9: "1980-е", 10: "1990-е", 11: "2000-е", 12: "2010-е"}


def load_books(filename="books.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)["books"]


def recommend_books(books, genre=None, decade=None):
    return [
        f"{book['title']} - {book['author']} ({book['age_category']})"
        for book in books if (genre is None or book["genre"] == genre) and (decade is None or book["year"] == decade)
    ]


def main():
    books = load_books()

    print("Выберите жанр: " + ", ".join([f"{num}. {genre}" for num, genre in GENRES.items()]))
    genre_choice = int(input("Введите номер жанра: "))
    genre = GENRES.get(genre_choice)
    if genre is None:
        print("Ошибка: некорректный номер жанра.")
        return

    print("\nВыберите десятилетие: " + ", ".join([f"{num}. {decade}" for num, decade in DECADES.items()]))
    decade_choice = int(input("Введите номер десятилетия: "))
    decade = DECADES.get(decade_choice)
    if decade is None:
        print("Ошибка: некорректный номер десятилетия.")
        return

    recommendations = recommend_books(books, genre, decade)

    if recommendations:
        print("\nРекомендованные книги:\n" + "\n".join(f"- {book}" for book in recommendations))
    else:
        print("\nНет книг, соответствующих выбранным параметрам.")


if __name__ == "__main__":
    main()
