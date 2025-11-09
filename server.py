from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

latest_data = {}  # Global variable to store last sensor data

@app.get("/")
def home():
    return {"message": "ESP32 FastAPI Server is running successfully 🚀"}

@app.post("/data")
async def receive_data(request: Request):
    global latest_data
    try:
        data = await request.json()
        latest_data = data  # Store last received data
        print("Received data from ESP32:", data)
        return {"status": "success", "received": data}
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=400)

@app.get("/latest")
def get_latest_data():
    """
    Returns the most recent sensor data received from ESP32
    """
    if not latest_data:
        return {"status": "waiting", "message": "No data received yet"}
    return {"status": "ok", "data": latest_data}
