from fastapi import FastAPI

app = FastAPI(title="CyberGuard")


@app.get("/")
def root():
    return {
        "project": "CyberGuard",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
