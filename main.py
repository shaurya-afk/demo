from fastapi import FastAPI
from service.stuff import willDo

app = FastAPI()

works = willDo()

def hello_world():
    print("Hello, World!\n")
    works.stuff_works("call a function, properly.")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/prod_test")
async def prod_test():
    return "works from live prod!"

@app.get("/about")
async def about():
    return "DEMO!!!!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)