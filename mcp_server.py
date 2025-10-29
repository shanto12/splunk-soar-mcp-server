import os
from dotenv import load_dotenv
import requests
import base64
from mcp import Server, Tool, types

load_dotenv()

SPLUNK_URL = os.getenv("SPLUNK_URL")
SPLUNK_TOKEN = os.getenv("SPLUNK_TOKEN")

def splunk_api_call(endpoint, method="GET", data=None):
    headers = {"Authorization": f"Bearer {SPLUNK_TOKEN}"}
    url = f"{SPLUNK_URL}/rest/soar/{endpoint}"
    response = requests.request(method, url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

server = Server("splunk-soar-mcp")

@server.tool()
async def list_playbooks() -> str:
    """List all available playbooks in Splunk SOAR."""
    try:
        data = splunk_api_call("playbooks")
        return types.TextContent(content=str(data))
    except Exception as e:
        return types.ErrorContent(message=str(e))

@server.tool()
async def run_action(playbook_id: str, action_params: dict) -> str:
    """Run a Splunk SOAR action with parameters."""
    try:
        data = {"playbook_id": playbook_id, "params": action_params}
        result = splunk_api_call("actions/run", method="POST", data=data)
        return types.TextContent(content=str(result))
    except Exception as e:
        return types.ErrorContent(message=str(e))

@server.tool()
async def get_incident(incident_id: str) -> str:
    """Retrieve details for a Splunk SOAR incident by ID."""
    try:
        data = splunk_api_call(f"incidents/{incident_id}")
        return types.TextContent(content=str(data))
    except Exception as e:
        return types.ErrorContent(message=str(e))

if __name__ == "__main__":
    server.run(transport="sse")  # Or "stdio" for local
