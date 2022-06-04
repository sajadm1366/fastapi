from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


@app.get("/add/{first_number}/{second_number}")
def add(x: float, y: float):
    total = x + y
    return {"total": total}

if __name__=="__main__":
    uvicorn.run(app)