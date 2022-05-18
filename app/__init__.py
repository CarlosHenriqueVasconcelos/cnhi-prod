from flask import Flask
from app.functions.function import read_archive


app = Flask(__name__)

@app.get("/all")
def all_archives():
    result = read_archive()

    return {"resultData": result}