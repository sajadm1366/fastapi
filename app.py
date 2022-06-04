from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/add/{first_number}/{second_number}")
def add(x: float, y: float):
    return x + y