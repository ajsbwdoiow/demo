## 计算器 MCP
基于 Model Context Protocol (MCP) 的数值计算器，提供了简单的加减乘除、幂运算、平方根运算和整数阶乘运算。


## 工具列表
| name | description |
| ----------- | ----------- |
| add  | 执行浮点数加法运算 |
| subtract | 执行浮点数减法运算 |
| multiply | 执行浮点数乘法运算 |
| divide|执行浮点数除法运算 Args: b: 除数（必须非零）|
| power | 计算幂运算 |
| sqrt | 计算平方根 |
| factorial | 计算整数阶乘 |

## inspector
```
npx @modelcontextprotocol/inspector uvx mcp_calculator_kel
```

## MCP 服务器配置
```
{
  "mcpServers": {
    "mcp_calculator_kel": {
        "command": "uvx",
        "args": [
          "mcp-calculator-kel@latest"
        ]
      }
  }
}
```

