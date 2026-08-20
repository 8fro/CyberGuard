from fastapi import FastAPI
from pydantic import BaseModel

from .nmap_scanner import run_nmap
from .nmap_parser import parse_nmap_xml


app = FastAPI(title="CyberGuard")


class ScanRequest(BaseModel):
    target: str


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


@app.post("/scan")
def start_scan(request: ScanRequest):
    scan = run_nmap(request.target)

    if scan["return_code"] != 0:
        return {
            "status": "failed",
            "scan_id": scan["scan_id"],
            "target": scan["target"],
            "error": scan["stderr"]
        }

    findings = parse_nmap_xml(scan["output_file"])

    return {
        "status": "completed",
        "scan_id": scan["scan_id"],
        "target": scan["target"],
        "findings": findings
    }
