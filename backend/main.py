from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import psycopg2

# dont hardcode the sql

app = FastAPI()

class Post(BaseModel):
    postId:int
    username: str
    description: str | None = None
    time: str | None = None
    ref: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello/{user}")
def read_item(user: str,):
    return {"Message": "hello {user}"}


@app.get("/getpost")
def get_post(postId: int):
    try: 
        conn = psycopg2.connect(
            database="test", 
            user="postgres", 
            host='localhost',
            password="postgres",
            port=5432
        )
        
        cur = conn.cursor()

        sql = 'SELECT * FROM posts WHERE postId = %s'
        values = (postId,)
        cur.execute(sql, values)
        result = cur.fetchone()  # fetch one row

        conn.close()

        if result:
            # Map result to a dictionary (optional)
            return {
                "postId": result[0],
                "username": result[1],
                "description": result[2],
                "time": result[3],
                "ref": result[4]
            }
        else:
            return {"message": "Post not found."}

    except Exception as e:
        print("Error fetching post:", e)
        return {"error": "Failed to fetch post."}


@app.post("/init")
def init_db():
    try:
        conn = psycopg2.connect(database = "test", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
        
        cur = conn.cursor()
        sql = """
            CREATE TABLE posts (
                postId INT PRIMARY KEY,
                username VARCHAR(50),
                description TEXT,
                time TIMESTAMP,
                ref VARCHAR(100)
            );
            """
        
        cur.execute(sql)
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)
        print("init failed")


@app.post("/createpost")
def create_post(post: Post):
    print(post)
    try:
        conn = psycopg2.connect(database = "test", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
        
        cur = conn.cursor()
        now = datetime.datetime.now()

        sql = 'INSERT INTO posts (postId, username, description, time, ref) VALUES (%s, %s, %s, %s, %s)'
        values = (post.postId, post.username, post.description, now, post.ref)
        cur.execute(sql, values)
        conn.commit()
        conn.close()

    except Exception as e:
        print("create failed")
        print(post, e)



@app.delete("/deletepost")
def delete_post(post: Post):
    try:
        conn = psycopg2.connect(database = "test", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
        
        cur = conn.cursor()

        postId = post.postId
        sql = 'delete from posts where postid = %s'
        values = (postId)
        cur.execute(sql, values)
        conn.commit()
        conn.close()

    except:
        print("delete failed with post")
        print(post)

