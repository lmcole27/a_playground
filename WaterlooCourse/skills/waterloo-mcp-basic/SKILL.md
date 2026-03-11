---
name: waterloo-mcp-basic
description: Smoke-test and debug a local Node.js MCP server over stdio. Use when a user needs to verify tools are discoverable/callable, connect via MCP Inspector, troubleshoot proxy/connection errors, or validate basic request/response behavior for an MCP server script.
---

# Waterloo Mcp Basic

Use this skill to validate that a local MCP server starts, exposes tools, and can be called from a client UI.

## Quick Workflow

1. Confirm dependencies and entrypoint.
2. Start the MCP server over stdio.
3. Connect with MCP Inspector.
4. Run tool smoke tests.
5. Debug connection failures using terminal logs.

## Commands

Run from the project root:

```bash
npm install
npm run mcp
```

Start Inspector in a separate terminal:

```bash
npx @modelcontextprotocol/inspector
```

Open Inspector in Chrome:

```bash
open -a "Google Chrome" http://localhost:6274
```

## Inspector Connection Settings

- Transport: `stdio`
- Command: `node`
- Args: absolute path to the MCP server file (for example, `/abs/path/mcp-server.js`)
- Optional CWD: project root

## Smoke Tests

- Call `ping` and expect `pong`.
- Call `greet` with `{"name":"Liam"}` and expect `Hello, Liam!`.

## Debug Checklist

- Keep the terminal running Inspector open and read its logs first.
- Verify the server file path is absolute and exists.
- Ensure only one Inspector/proxy instance is active when troubleshooting.
- Kill stale sessions if needed: `pkill -f mcp-inspector`.
