__all__ = [
    'movies_ref_filt',
    'genres_ref',
    'ratings_ref',
    'movies_ratings_filt',
    'movies_ratings_filt_csc',
]

from pandas import DataFrame, read_csv
from scipy.sparse import csc_array

from pathlib import Path
from re import compile
from sys import path


script_dir = Path(path[0])

movies_raw_path = script_dir / 'recomm_movies.csv'
ratings_raw_path = script_dir / 'recomm_ratings.csv'

movies_ref_path = script_dir / 'recomm_movies_ref.csv'
genres_ref_path = script_dir / 'recomm_genres_ref.csv'
ratings_ref_path = script_dir / 'recomm_ratings_ref.csv'


# если таблицы уже были обработаны
if movies_ref_path.exists() and genres_ref_path.exists() and ratings_ref_path.exists():
    
    movies_ref = read_csv(movies_ref_path, index_col='movie_id', dtype='str')
    genres_ref = read_csv(genres_ref_path, index_col=0)
    ratings_ref = read_csv(ratings_ref_path, index_col=0)

# обработка
else:
    
    movies_raw = read_csv(movies_raw_path, index_col='movie_id')
    # movies_raw.index = movies_raw.index.astype('int32')
    
    ratings_raw = read_csv(ratings_raw_path)
    
    # puncs = ".,!?:;'/#&*–—"
    pat_title = compile(
        r'(?P<title>.+?)'
        r'(?: \(a\.k\.a\. .+?\))*'
        r'(?: \((?P<loc_title>(?!\d{4}).+?)\))?'
        r'(?: \((?P<year>\d{4})\))?'
    )
    
    movies_ref = DataFrame([], columns=['title', 'loc_title', 'year'])
    genres_ref = DataFrame([], columns=['movie_id', 'genre'])
    
    cnt = 0
    for movie_id, movie in movies_raw.iterrows():
        mo = pat_title.fullmatch(movie['title'])
        if mo:
            movies_ref.loc[movie_id] = {
                'title': mo['title'],
                'loc_title': mo['loc_title'],
                'year': int(mo['year']) if mo['year'] else None,
            }
        else:
            print(movie)
        for genre in movie['genres'].split('|'):
            genres_ref.loc[cnt] = {
                'movie_id': movie_id,
                'genre': genre,
            }
            cnt += 1
    
    # movies_ref.index = movies_ref.index.astype('int32')
    # genres_ref['movie_id'] = genres_ref['movie_id'].astype('int32')
    
    ratings_ref = ratings_raw.loc[:, ['user_id', 'movie_id', 'rating']]
    
    
    movies_ref.to_csv(movies_ref_path, index_label='movie_id')
    genres_ref.to_csv(genres_ref_path)
    ratings_ref.to_csv(ratings_ref_path)


# сводная матрица фильмов и пользовательских оценок
movies_ratings = ratings_ref.pivot(columns='user_id', index='movie_id', values='rating')

# маски для фильтрации фильмов и пользователей с малым количеством оценок
mask_users = movies_ratings.agg('count', axis=0) > 50
mask_movies = movies_ratings.agg('count', axis=1) > 5

movies_ratings_filt = movies_ratings.loc[mask_movies, mask_users]

# замена NaN значений вычислимыми арифметически нолями
movies_ratings_filt = movies_ratings_filt.fillna(0)



# 0 1 0 0 0 2 0
# 0 0 0 1 0 0 1
# 9 0 0 0 2 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 3 0

# координатный массив (COO array)
#  координаты строки: 0 0 1 1 2 2 4
# координаты столбца: 1 5 3 6 0 4 5
#           значение: 1 2 1 1 9 2 3
# размерность: (5, 7)

# массив сжатых строк (CSR array)
#        накопленное количество 
# ненулевых значений по строкам: 0 2 4 6 6 7
#            координаты столбца: 1 5 3 6 0 4 5
#                      значение: 1 2 1 1 9 2 3
# размерность: (5, 7)

# массив сжатых столбцов (CSC array)
#         накопленное количество 
# ненулевых значений по столбцам: 0 1 2 2 3 4 6 7
#              координаты строки: 2 0 1 2 0 4 1
#                       значение: 9 1 1 2 2 3 1
# размерность: (5, 7)



movies_ratings_filt_csc = csc_array(movies_ratings_filt)


for movie_id in set(movies_ref.index) - set(movies_ratings.index):
    mask_movies[movie_id] = False

movies_ref_filt = movies_ref.loc[mask_movies, :]
movies_ref_filt = movies_ref_filt.reset_index()

