import argparse
from .server import mcp

def main():
    """MCP Weather Server: Get current weather information for any location."""
    parser = argparse.ArgumentParser(
        description="Get current weather information for any location."
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()