import json

def handler(request, response):
    from urllib.parse import parse_qs

    # Enable CORS
    response.headers['Access-Control-Allow-Origin'] = '*'

    # Parse query params
    query_params = parse_qs(request.query_string.decode())
    names = query_params.get("name", [])

    # Load student data
    with open("q-vercel-python.json") as f:
        data = json.load(f)

    marks = [data.get(name, None) for name in names]

    return response.json({"marks": marks})
