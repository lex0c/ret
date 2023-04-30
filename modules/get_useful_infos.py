def get_system_info():
    import platform, socket
    uname = platform.uname()
    system = uname.system
    release = uname.release
    version = uname.version
    machine = uname.machine
    processor = uname.processor
    hostname = socket.gethostname()
    return {
        "system": system,
        "release": release,
        "version": version,
        "machine": machine,
        "processor": processor,
        "hostname": hostname
    }


def get_mac_address():
    import uuid
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[i:i + 2] for i in range(0, 11, 2)])


def get_private_ip():
    import socket
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip


def get_public_ip():
    import http.client, json
    conn = http.client.HTTPSConnection("httpbin.org")
    conn.request("GET", "/ip")
    response = conn.getresponse()
    if response.status == 200:
        response_data = response.read().decode("utf-8")
        public_ip = json.loads(response_data)["origin"]
        return public_ip
    else:
        return None


def get_location_info(ip_address):
    import http.client, json
    conn = http.client.HTTPSConnection("ip-api.com")
    conn.request("GET", f"/json/{ip_address}")
    response = conn.getresponse()
    if response.status == 200:
        response_data = response.read().decode("utf-8")
        location_info = json.loads(response_data)
        return location_info
    else:
        return None


pub_ip = get_public_ip()

print({
    "sys": get_system_info(),
    "mac": get_mac_address(),
    "priv_ip": get_private_ip(),
    "pub_ip": pub_ip,
    "local": get_location_info(pub_ip)
})

