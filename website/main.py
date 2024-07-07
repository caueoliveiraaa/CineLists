"""
This is the entrypoint of the website.
This website displays and orgnizes movies and series.
"""


import uvicorn

from fastapi import FastAPI

app = FastAPI(title='Cine List', description='CRUD for movies')
  

@app.get('/')
def root() -> dict:
    return { "status": 200 }


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
