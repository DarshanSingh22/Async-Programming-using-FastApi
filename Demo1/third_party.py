from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/third-party-endpoint/sleep")
def third_party_endpoint():
    time.sleep(5)
    return {"data": "third party response"}