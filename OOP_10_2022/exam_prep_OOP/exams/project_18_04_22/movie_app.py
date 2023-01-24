from exams.project_10_04_2022 import Movie
from exams.project_10_04_2022 import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def user_in_collection(self, username):
        if username in [u.username for u in self.users_collection]:
            return True
        else:
            return False

    def find_user(self, username, ):
        for user in self.users_collection:
            if username == user.username:
                return user

    def find_movie(self, movie):
        for m in self.movies_collection:
            if m == movie:
                return m

    def register_user(self, username: str, age: int):
        if self.user_in_collection(username):
            raise Exception("User already exists!")
        current_user = User(username, age)
        self.users_collection.append(current_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if not self.user_in_collection(username):
            raise Exception("This user does not exist!")

        current_user = self.find_user(username)
        if movie not in current_user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        current_user = self.find_user(username)
        if movie not in current_user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_movie = self.find_movie(movie)
        for key, value in kwargs.items():
            current_movie.key = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        current_user = self.find_user(username)
        if movie not in current_user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_movie = self.find_movie(movie)
        self.movies_collection.remove(current_movie)
        current_user.movies_owned.remove(current_movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        current_user = self.find_user(username)

        if movie in current_user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in current_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        current_user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = self.find_user(username)
        if movie not in current_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        current_user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return f"No movies found."

        result = sorted(self.movies_collection, key=lambda m: (-m.year, m.title ))
        return '\n'.join([m.details() for m in result])

    def __str__(self):
        result_1 = []
        if self.users_collection:
            for user in self.users_collection:
                result_1.append(user.username)

        else:
            result_1 = ["No users."]

        result_2 = []
        if self.movies_collection:
            for movie in self.movies_collection:
                result_2.append(movie.title)

        else:
            result_2 = ["No movies."]

        return f"All users: {', '.join(result_1)}\nAll movies: {', '.join(result_2)}"

