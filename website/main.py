from fastapi import FastAPI
import uvicorn

app = FastAPI(title='Cine List', description='CRUD for movies')
  

@app.get('/')
def root():
    return {"status": 200}


if __name__ == '__main__':
    try:
        uvicorn.run(app, host='0.0.0.0', port=8000)
    except KeyboardInterrupt:
        print('Program exited')
        quit()
    except Exception as error:
        print(f'Error: {error}')
        