# fastmcp-mre-breaking-task-group-with-invalid-arguments

When fastmcp (or maybe even the low level MCP server?) receives the `arguments` parameter as a string, then FastMCP begins to raise `RuntimeError: Task group is not initialized` for every endpoint call after.

The script `simple_echo_mre.py` uses `mcp.run_async` and raw httpx requests to reproduce this.

## Running this example

```sh
uv run --with=git+https://github.com/Sillocan/fastmcp-mre-breaking-task-group-with-invalid-arguments fastmcp-mre-breaking-task-group-with-invalid-arguments
```
