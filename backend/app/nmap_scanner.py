import subprocess
import os
import uuid


def run_nmap(target):
    """
    Run Nmap service/version detection against an authorized target
    and save the result as XML.
    """

    os.makedirs("scans", exist_ok=True)

    scan_id = str(uuid.uuid4())[:8]
    output_file = f"scans/scan_{scan_id}.xml"

    command = [
        "nmap",
        "-sV",
        "-oX",
        output_file,
        target
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return {
        "scan_id": scan_id,
        "target": target,
        "return_code": result.returncode,
        "output_file": output_file,
        "stdout": result.stdout,
        "stderr": result.stderr
    }


if __name__ == "__main__":
    target = "127.0.0.1"

    result = run_nmap(target)

    print("Scan ID:", result["scan_id"])
    print("Target:", result["target"])
    print("Return Code:", result["return_code"])
    print("XML File:", result["output_file"])
    print("\nNmap Output:")
    print(result["stdout"])

    if result["stderr"]:
        print("\nNmap Errors:")
        print(result["stderr"])
