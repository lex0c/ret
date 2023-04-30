def get_public_ip():
    import requests

    response = requests.get("https://httpbin.org/ip")

    if response.status_code == 200:
        public_ip = response.json()["origin"]

        print(public_ip)
    else:
        print(f"Error: Unable to fetch public IP address. Status code: {response.status_code}")

get_public_ip()
