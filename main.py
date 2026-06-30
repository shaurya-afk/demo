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

@app.get("/me")
async def me():
    return "Hello from Nascent"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)