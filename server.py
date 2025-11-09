from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Streamlit to fetch data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_data = {}

@app.post("/update")
async def update_data(request: Request):
    """Receive JSON data from ESP32"""
    global latest_data
    data = await request.json()
    latest_data = data
    print("Received data:", data)
    return {"status": "ok", "received": data}

@app.get("/latest")
async def get_latest():
    """Streamlit fetches this"""
    if not latest_data:
        return {"status": "no_data"}
    return latest_data
