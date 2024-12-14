from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

# to get query
# queries are defined after / starting with ? separated by &
# ?skip=0&limit=2
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# https://stackoverflow.com/questions/63048825/how-to-upload-file-using-fastapi
# https://www.reddit.com/r/FastAPI/comments/14f43gp/how_to_upload_pdf_to_fastapi/