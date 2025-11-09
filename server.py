from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Store latest sensor data
latest_data = {}

@app.get("/")
def home():
    return {"message": "ESP32 FastAPI Server is running successfully 🚀"}

@app.post("/data")
async def receive_data(request: Request):
    global latest_data
    try:
        data = await request.json()
        latest_data = data  # Save it for future GET requests
        print("✅ Received new data:", data)
        return {"status": "success", "received": data}
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=400)

@app.get("/data")
def get_latest_data():
    if latest_data:
        return {"status": "success", "latest_data": latest_data}
    else:
        return {"status": "empty", "message": "No data received yet"}
