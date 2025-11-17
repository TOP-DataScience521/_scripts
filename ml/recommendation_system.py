from sklearn.neighbors import NearestNeighbors

from recommendation_init import *


# модель с реализованными алгоритмами и функциями расчёта расстояний между векторами
model = NearestNeighbors(
    n_neighbors=10,
    algorithm='brute',
    metric='cosine',
    n_jobs=-1
)
# выполнение расчётов расстояний между всеми векторами
model.fit(movies_ratings_filt_csc)


mask_search = movies_ref_filt['title'].str.contains('Matrix')

# >>> movies_ref_filt.loc[mask_search]
#       movie_id                    title loc_title  year
# 1219      2571              Matrix, The       NaN  1999
# 2125      6365     Matrix Reloaded, The       NaN  2003
# 2198      6934  Matrix Revolutions, The       NaN  2003

vector_search = movies_ratings_filt_csc[1219].reshape(1, -1)
result = model.kneighbors(vector_search)

# >>> result[0]
# array([[0.        , 0.22982441, 0.25401128, 0.27565617, 0.27760886,
#         0.28691008, 0.29111012, 0.31393358, 0.31405926, 0.31548004]])
# >>>
# >>> result[1]
# array([[1219, 1370,  588,  601,  160,  959, 1292, 1930, 1600, 2236]])


# >>> movies_ref_filt.loc[result[1].flat]
#       movie_id                                              title loc_title  year
# 1219      2571                                        Matrix, The       NaN  1999
# 1370      2959                                         Fight Club       NaN  1999
# 588       1196     Star Wars: Episode V - The Empire Strikes Back       NaN  1980
# 601       1210         Star Wars: Episode VI - Return of the Jedi       NaN  1983
# 160        260                 Star Wars: Episode IV - A New Hope       NaN  1977
# 959       2028                                Saving Private Ryan       NaN  1998
# 1292      2762                                   Sixth Sense, The       NaN  1999
# 1930      4993  Lord of the Rings: The Fellowship of the Ring,...       NaN  2001
# 1600      3578                                          Gladiator       NaN  2000
# 2236      7153     Lord of the Rings: The Return of the King, The       NaN  2003

