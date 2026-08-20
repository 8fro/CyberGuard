import xml.etree.ElementTree as ET


def parse_nmap_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    host = root.find("host")
    port_element = host.find("./ports/port")
    service_element = port_element.find("service")

    result = {
        "target": host.find("address").get("addr"),
        "port": int(port_element.get("portid")),
        "protocol": port_element.get("protocol"),
        "state": port_element.find("state").get("state"),
        "service": service_element.get("name"),
        "product": service_element.get("product"),
        "version": service_element.get("version"),
        "extra_info": service_element.get("extrainfo"),
        "cpe": service_element.findtext("cpe"),
    }

    return result


if __name__ == "__main__":
    scan_result = parse_nmap_xml("scans/first_scan.xml")
    print(scan_result)
