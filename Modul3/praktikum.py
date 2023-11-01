from collections import defaultdict

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time To Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "THe Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def getGenreCount(movies, genre):
    genre_movies = filter(lambda movie: movie["genre"].lower() == genre.lower(), movies)
    return genre, len(list(genre_movies))

def getAverageByYear(movies, year):
    ratings = [movie["rating"] for movie in movies if movie["year"] == year]
    if len(ratings) > 0:
        avg_rating = sum(ratings) / len(ratings)
        return year, avg_rating
    else:
        return year, 0  

def getHigherRate(movies):
    if not movies:
        return None
    higherRate = max(movies, key=lambda movie: movie["rating"])
    return higherRate

def getMovieByTitle(movies, title):
    found_movies = [movie for movie in movies if movie["title"].lower() == title.lower()]
    return found_movies

def getMovie(movies):
    title_to_search = input("Masukkan judul film yang ingin dicari: ")
    matching_movies = getMovieByTitle(movies, title_to_search)

    if matching_movies:
        for movie in matching_movies:
            title = movie["title"]
            year = movie["year"]
            genre = movie["genre"]
            rating = movie["rating"]
            print(f"Informasi Film: \n{title} ({year}), \nGenre: {genre}, \nRating: {rating}")
    else:
        print("Film tidak ditemukan.")

def main():
    while True:
        print("\nHere's Your Option: ")
        print("1. Count film by genre")
        print("2. Average rate film by year")
        print("3. Find the highest rate")
        print("4. Search Film")
        print("5. Exit")
        choose = int(input("What You Wanna Do? : "))

        if choose == 1:
            genreCounts = dict(map(lambda genre: getGenreCount(movies, genre), set(movie["genre"] for movie in movies)))
            for genre, count in genreCounts.items():
                print(f"Jumlah Film Genre '{genre}': {count}")
        elif choose == 2:
            averageRatingYear = {}
            for movie in movies:
                year = movie["year"]
                if year not in averageRatingYear:
                    averageRatingYear[year] = getAverageByYear(movies, year)
            for year, avg_rating in averageRatingYear.items():
                print(f"Rata-rata rating untuk tahun {year}: {avg_rating}")
        elif choose == 3:
            higherRate = getHigherRate(movies)
            title = higherRate["title"]
            year = higherRate["year"]
            genre = higherRate["genre"]
            rating = higherRate["rating"]
            print(f"Informasi Film Terbaik: {title} ({year}), Genre: {genre}, Rating: {rating}")
        elif choose == 4:
            getMovie(movies)
        elif choose == 5:
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()