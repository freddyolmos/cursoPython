import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_contacts():
    return """
        <h1>Hola mundo</h1>
    """

def run():
    store.get_requests()

if __name__ == '__main__' :
    run()
