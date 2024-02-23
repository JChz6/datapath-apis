from flask import Flask
from controllers.movies_controller import get_movies, get_movie, add_movie, update_movie, delete_movie

app = Flask(__name__)

# Definir las rutas y asignarlas a las funciones del controlador
app.route('/movies', methods=['GET'])(get_movies)
app.route('/movies/<int:movie_id>', methods=['GET'])(get_movie)
app.route('/movies', methods=['POST'])(add_movie)
app.route('/movies/<int:movie_id>', methods=['PUT'])(update_movie)
app.route('/movies/<int:movie_id>', methods=['DELETE'])(delete_movie)

if __name__ == '__main__':
    app.run(debug=True)
