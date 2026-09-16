import datetime
import socket

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="python-app")


@app.get("/api/v1/info")
def info():
    return {
        "time": datetime.datetime.now(datetime.UTC).strftime("%I:%M:%S%p  on %B %d, %Y"),
        "hostname": socket.gethostname(),
        "message": "You are doing great, little human da nu",
        "deployed_on": "kubernetes",
        "env": "${{values.app_env}}",
        "app_name": "${{values.app_name}}"
    }


@app.get("/api/v1/healthz")
def health():
    # Do an actual check here
    return {"status": "up"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
