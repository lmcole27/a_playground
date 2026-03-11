# WaterlooCourse MCP Server

## 1) Install dependencies

```bash
cd /Users/lcole/Documents/a_playground/WaterlooCourse
npm install
```

## 2) Run the server

```bash
npm run mcp
```

This server runs over stdio and exposes two tools:
- `ping`
- `greet` (input: `name`)

## 3) Add to an MCP client

Example config entry:

```json
{
  "mcpServers": {
    "waterloo-course": {
      "command": "node",
      "args": ["/Users/lcole/Documents/a_playground/WaterlooCourse/mcp-server.js"]
    }
  }
}
```

If your client supports it, you can also use:

```json
{
  "mcpServers": {
    "waterloo-course": {
      "command": "npm",
      "args": ["run", "mcp"],
      "cwd": "/Users/lcole/Documents/a_playground/WaterlooCourse"
    }
  }
}
```
