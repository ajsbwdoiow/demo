## 天气信息 MCP 服务器
基于 Model Context Protocol (MCP) 的天气信息服务器，提供获取指定位置当前天气信息的功能。


## 工具列表
| name | description |
| ----------- | ----------- |
| get_current_weather_tool  | 获取指定位置的当前天气信息 |

## inspector
```
npx @modelcontextprotocol/inspector uvx mcp-weather-server
```

## MCP 服务器配置
```
{
  "mcpServers": {
    "mcp-weather-server": {
        "command": "uvx",
        "args": [
          "mcp-weather-server@latest"
        ]
      }
  }
}
```

