def make_request(url, method, payload=None):
    import http.client
    import json
    from urllib.parse import urlparse

    parsed_url = urlparse(url)
    connection = http.client.HTTPSConnection(parsed_url.netloc)

    headers = {
        "Content-Type": "application/json",
    }

    if method == "POST" and payload is not None:
        #payload = json.dumps(payload)
        headers["Content-Length"] = str(len(payload))
    else:
        method = "GET"
        payload = None

    connection.request(method, parsed_url.path, body=payload, headers=headers)
    response = connection.getresponse()
    response_text = response.read().decode()

    return response.status, response_text


def checkjson(json_string):
    import json
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False


url = "!!URL!!"
payload = '!!JSON!!'

if checkjson(payload):
    status, response_text = make_request(url, "POST", payload)
else:
    status, response_text = make_request(url, "GET")

print(response_text, status)

