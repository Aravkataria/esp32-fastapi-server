from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "ESP32 FastAPI Server is running successfully 🚀"}

# POST endpoint to receive sensor data from ESP32
@app.post("/data")
async def receive_data(request: Request):
    try:
        data = await request.json()
        print("Received data:", data)
        return {"status": "success", "received": data}
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=400)

# Optional: GET endpoint for testing from Streamlit or browser
@app.get("/data")
def get_info():
    return {"message": "Use POST /data to send sensor JSON from ESP32"}
