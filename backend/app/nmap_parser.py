import xml.etree.ElementTree as ET


def parse_nmap_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    host = root.find("host")

    if host is None:
        return []

    address_element = host.find("address")

    if address_element is None:
        return []

    target = address_element.get("addr")

    findings = []

    for port_element in host.findall("./ports/port"):
        state_element = port_element.find("state")
        service_element = port_element.find("service")

        finding = {
            "target": target,
            "port": int(port_element.get("portid")),
            "protocol": port_element.get("protocol"),
            "state": state_element.get("state") if state_element is not None else None,
            "service": None,
            "product": None,
            "version": None,
            "extra_info": None,
            "cpe": None,
        }

        if service_element is not None:
            finding["service"] = service_element.get("name")
            finding["product"] = service_element.get("product")
            finding["version"] = service_element.get("version")
            finding["extra_info"] = service_element.get("extrainfo")
            finding["cpe"] = service_element.findtext("cpe")

        findings.append(finding)

    return findings


if __name__ == "__main__":
    scan_file = "scans/scan_82c5250b.xml"

    results = parse_nmap_xml(scan_file)

    print("Nmap Findings:")

    for finding in results:
        print(finding)
