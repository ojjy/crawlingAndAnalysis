from pymongo import MongoClient


def search_movie(db):
    target_movie = db.movie.find_one({'title': '월-E'})
    print(target_movie['rank'])

    target_movies = db.movie.find({'point': target_movie['point']})
    for idx in target_movies:
        print(idx['title'])

def update_movie(db):
    target_movie = db.movie.find_one({'title': '월-E'})
    target_point = target_movie['point']
    db.movies.update_many({'point': target_point}, {'$set': {'point': '0'}})


if __name__ == "__main__":
    client = MongoClient('127.0.0.1', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
    db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.
    print("test")
    search_movie(db)
    update_movie(db)