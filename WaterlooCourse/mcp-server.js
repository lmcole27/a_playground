const { McpServer } = require("@modelcontextprotocol/sdk/server/mcp.js");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio.js");
const { z } = require("zod");

const server = new McpServer({
  name: "waterloo-course-mcp",
  version: "1.0.0",
});

server.tool(
  "ping",
  "Quick health check for the server.",
  {},
  async () => ({
    content: [{ type: "text", text: "pong" }],
  }),
);

server.tool(
  "greet",
  "Return a greeting for a provided name.",
  { name: z.string().min(1) },
  async ({ name }) => ({
    content: [{ type: "text", text: `Hello, ${name}!` }],
  }),
);

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((error) => {
  console.error("MCP server failed to start:", error);
  process.exit(1);
});
