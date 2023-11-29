from fastapi import FastAPI

app = FastAPI()

counter = 0

@app.get("/")
def read_root():
    global counter
    counter += 1
    return {"message": "Hello, This is a FastAPI Project!", "The number of times you have visited this web page is: ": counter}
