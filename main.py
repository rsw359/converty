from fastapi import FastAPI
from converty import make_conversion

app = FastAPI()

@app.post("/convert/{conversion}")
async def convert(conversion: str):
    result = await make_conversion(conversion)
    print(result)
    return {'result': result}

