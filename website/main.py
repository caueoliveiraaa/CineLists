"""
This is the entrypoint of the website.
This website displays and orgnizes movies and series.
"""


import uvicorn
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI(title='Cine List', description='CRUD for movies')
templates = Jinja2Templates(directory="templates")


def load_movies() -> list:
    path = Path(__file__).parent / 'database' / 'movies.json'

    with open(path) as file:
        movies_data = json.load(file)

    movies_list = [
        {"index": index, **movie_data}
        for index, movie_data in movies_data.items()
    ]

    return movies_list


@app.get('/')
def root() -> dict:
    return {"status": 200}


@app.get('/movies', response_class=HTMLResponse)
def get_movies(request: Request):
    movies = load_movies()
    return templates.TemplateResponse(
        "movies.html", {"request": request, "movies": movies})


def main() -> None:
    try:
        uvicorn.run(app, host='0.0.0.0', port=8000)
    except KeyboardInterrupt:
        print('Program exited')
        exit()
    except Exception as error:
        print(f'Error: {error}')


if __name__ == '__main__':
    main()
