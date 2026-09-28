import sys, json
from client import MarkdownTableToJsonTransformer

def main():
    engine = MarkdownTableToJsonTransformer()
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            req = json.loads(line)
            method = req.get("method")
            rid = req.get("id")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "tools": [
                        {"name": "transform_table", "description": "Transform markdown table to JSON.", "inputSchema": {"type": "object", "properties": {"markdown_text": {"type": "string"}}, "required": ["markdown_text"]}},
                        {"name": "run_benchmark_table_transformer", "description": "Run self-test.", "inputSchema": {"type": "object"}}
                    ]
                }
            elif method == "tools/call":
                tname = params.get("name")
                args = params.get("arguments", {})
                if tname == "transform_table":
                    out = engine.transform_table(args.get("markdown_text", ""))
                elif tname == "run_benchmark_table_transformer":
                    out = engine.run_benchmark_table_transformer()
                else:
                    out = {"error": f"Unknown tool {tname}"}
                res = {"content": [{"type": "text", "text": json.dumps(out)}]}
            else:
                res = {"error": "Unsupported method"}
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}), flush=True)
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}), flush=True)

if __name__ == "__main__":
    main()
