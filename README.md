
# fastmcp-mre-breaking-task-group-with-invalid-arguments

When `mcp.server` receives the `arguments` parameter as a string, then FastMCP begins to raise `RuntimeError: Task group is not initialized` for every endpoint call after.

## Running this example for mcp python-sdk

To run using the mcp low level python sdk:

```sh
uv run --with=git+https://github.com/Sillocan/fastmcp-mre-breaking-task-group-with-invalid-arguments#subdirectory=python_sdk mre
```
