from fastapi import FastAPI

from .nmap_parser import parse_nmap_xml

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


@app.get("/scan-result")
def scan_result():
    return parse_nmap_xml("scans/first_scan.xml")
