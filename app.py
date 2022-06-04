from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


@app.get("/add/{first_number}/{second_number}")
def add(x: float, y: float):
    return x + y

if __name__=="__main__":
    uvicorn.run(app)