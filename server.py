from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Temporary variable to store the latest ESP32 data
latest_data = {}

@app.get("/")
def home():
    return {"message": "ESP32 FastAPI Server is running successfully 🚀"}

# Receive sensor data from ESP32
@app.post("/data")
async def receive_data(request: Request):
    global latest_data
    try:
        data = await request.json()
        print("📩 Received data:", data)
        latest_data = data  # Save latest data
        return {"status": "success", "received": data}
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=400)

# Endpoint for Streamlit to GET the latest data
@app.get("/data")
def get_data():
    if latest_data:
        return {"latest_data": latest_data}
    else:
        return {"message": "No data received yet 😴"}
