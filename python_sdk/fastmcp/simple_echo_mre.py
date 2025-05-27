# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "mcp==1.9.1",
# ]
# ///
"""
This example uses `mcp.fastmcp` to demonstrate the issue.
"""

import asyncio

import httpx
from mcp.server.fastmcp import FastMCP

# Create server
mcp = FastMCP("Echo Server")


@mcp.tool()
def echo(text: str) -> str:
    """Echo the input text"""
    return text


# ---- MRE below ----


async def breakit():
    """Passes `arguments` as a string which breaks the MCP fully"""
    payload = {
        "method": "tools/call",
        "params": {
            "name": "echo",
            "arguments": '{"text": "imnestedtext"}',  # NOTE: this is a string
        },
        "jsonrpc": "2.0",
        "id": 2,
    }

    async with httpx.AsyncClient() as client:
        breaking_response = await client.post(
            "http://127.0.0.1:8000/mcp/",
            json=payload,
            headers={"Accept": "application/json, text/event-stream"},
        )
        print(f"{breaking_response.status_code=} {breaking_response.text=}")

        get_response = await client.get(
            "http://127.0.0.1:8000/mcp/",
            headers={"Accept": "application/json, text/event-stream"},
        )
        print(f"{get_response.status_code=} {get_response.text=}")
        assert get_response.status_code < 300, "MCP is fully broken"


async def run_and_break_the_mcp():
    mcp.settings.stateless_http = True
    run_task = asyncio.create_task(mcp.run_streamable_http_async())
    await asyncio.sleep(1)  # allow time for the server to start
    try:
        await breakit()
    finally:
        # breakit should raise an exception - thus need for finally
        run_task.cancel()


def main():
    asyncio.run(run_and_break_the_mcp())


if __name__ == "__main__":
    main()
