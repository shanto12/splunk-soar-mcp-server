# Splunk SOAR MCP Server

MCP server for Splunk SOAR integration.

## Setup
1. .env is pre-configured with your instance creds.
2. pip install -r requirements.txt
3. python mcp_server.py

## Usage
Configure in MCP client (e.g., VS Code mcp.json):
```json
{ "servers": { "splunk-soar": { "command": "python", "args": ["mcp_server.py"], "env": { "SPLUNK_URL": "${env:SPLUNK_URL}", "SPLUNK_TOKEN": "${env:SPLUNK_TOKEN}" } } } }
```

Tools: list_playbooks, run_action, get_incident.
