import json
from urllib.parse import parse_qs

def handler(request):
    # Enable CORS in response headers
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json"
    }

    # Parse query parameters
    query_params = parse_qs(request["queryString"] or "")
    names = query_params.get("name", [])

    # Load student data from JSON file
    try:
        with open("api/q-vercel-python.json") as f:
            data = json.load(f)
        marks = [data.get(name, None) for name in names]
        body = json.dumps({"marks": marks})
        status_code = 200
    except Exception as e:
        body = json.dumps({"error": str(e)})
        status_code = 500

    return {
        "statusCode": status_code,
        "headers": headers,
        "body": body
    }
