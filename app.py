from fastapi import FastAPI
import uvicorn
import json

#Init
app = FastAPI(debug=True)

#Data
with open("municipality.json") as f:
    municipalities = json.load(f)

#route
@app.get('/api/v1/municipality')
async def get_municipality():
    return {  
        "isSucsess": True,
        "municipality" : municipalities
    }

@app.get('/api/v1/municipality/{code}')
async def get_municipalityByCode(code):
    return {
        "isSuccess": True,
        "municipality" : [ m for m in municipalities if m["code"] == code ]
    }

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1",port="8000")