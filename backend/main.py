from fastapi import FastAPI



app = FastAPI()

@app.get('/')
def faran():
    return {"message":"Faran is good boy"}

