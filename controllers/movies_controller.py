from flask import Flask, request, jsonify
import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST
import os

app = Flask(__name__)

'''DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')


if None in [DB_NAME, DB_USER, DB_PASSWORD, DB_HOST]:
    raise EnvironmentError("Faltan variables de entorno.")
'''

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)




# Método GET
#para recibir TODA tabla

@app.route('/movies', methods=['GET'])
def get_movies():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_movies;')
    movies = cursor.fetchall()
    cursor.close()
    return jsonify(movies)

# Método GET
#para buscar uns película por ID
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(movie_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_movies WHERE id = %s;', (movie_id,))
    movie = cursor.fetchone()
    cursor.close()
    return jsonify(movie)

# Método POST
#para agregar registros a la tabla
#el id es autoincremental
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    cursor = conn.cursor()
    
    cursor.execute('SELECT MAX(id) FROM my_movies;')
    last_id = cursor.fetchone()[0]
    new_id = last_id + 1 if last_id is not None else 1
    
    cursor.execute('INSERT INTO my_movies (id, nombre, autor, descripcion, fecha_estreno) VALUES (%s, %s, %s, %s, %s);',
                   (new_id, data['nombre'], data['autor'], data['descripcion'], data['fecha_estreno']))
    
    conn.commit()
    cursor.close()    
    return jsonify({'id': new_id})

# Método PUT
# para actualizar un registro específico
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('UPDATE my_movies SET nombre=%s, autor=%s, descripcion=%s, fecha_estreno=%s WHERE id=%s;',
                   (data['nombre'], data['autor'], data['descripcion'], data['fecha_estreno'], movie_id))
    conn.commit()
    cursor.close()
    return jsonify({'respuesta': '***Registo actualizado!***'})

# Método DELETE
#para borrar un elemento con su id
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(movie_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM my_movies WHERE id=%s;', (movie_id,))
    conn.commit()
    cursor.close()
    return jsonify({'respuesta': 'Película eliminada para siempre'})

if __name__ == '__main__':
    app.run(debug=True)
