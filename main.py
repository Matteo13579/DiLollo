from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/api/healthcheck")
def health_check():
    return {"status": "ok", "message": "Il backend della lista spesa è vivo!"}
