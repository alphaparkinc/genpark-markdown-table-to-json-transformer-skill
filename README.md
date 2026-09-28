# genpark-markdown-table-to-json-transformer-skill

<div align="center">

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
[![MCP Compatible](https://img.shields.io/badge/MCP-100%25%20Compatible-purple.svg?style=for-the-badge&logo=anthropic)](https://genpark.ai/mcp)
[![GenPark AI](https://img.shields.io/badge/Verified%20By-GenPark%20AI-orange.svg?style=for-the-badge&logo=openai)](https://genpark.ai)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20(Stdlib%20Only)-brightgreen.svg?style=for-the-badge)](requirements.txt)

<p align="center">
  <b>Production-Grade Autonomous Web Browsing & Extraction Skill</b> • <b>100% Standard Library Python</b> • <b>Native Model Context Protocol (MCP)</b>
</p>

</div>

---

## ⚡ Overview & Architectural Significance

`genpark-markdown-table-to-json-transformer-skill` delivers zero-dependency, low-latency web automation, DOM semantic pruning, and execution trajectory evaluation primitives engineered strictly using Python 3.9+ standard library.

### 🌟 Key Architectural Capabilities
- **Zero External Dependencies**: Operates exclusively via pure Python (`html.parser`, `urllib.parse`, `re`, `math`, `json`). Zero pip install overhead, zero headless browser crashes.
- **Enterprise Web Agent Invariants**: Implements formal token-pruning algorithms, form auto-mapping, anti-crawler trap normalization, Markdown-to-JSON type inference, and trajectory Levenshtein distance evaluation.
- **Native Anthropic MCP Protocol**: Compliant with standard JSON-RPC 2.0 stdio MCP specifications for Claude Desktop, Cursor, and Windsurf.

---

## 🏗️ Architectural Topology & State Machine

```mermaid
flowchart TD
    RawWeb["Raw Web Page / DOM Ingress"] --> TrapFilter["URL Canonicalization & Anti-Crawler Trap Guard"]
    TrapFilter --> DOMPruner["HTML DOM Semantic Tree Pruner
(80%+ Token Reduction, Strips Scripts/Styles/SVG)"]
    
    DOMPruner --> FormMapper["Web Form Input Schema Auto-Mapper
(Attribute & Heuristic Profile Field Binding)"]
    DOMPruner --> TableParser["Markdown & HTML Table to JSON Transformer
(Type-Inferred Structured Record Generation)"]
    
    FormMapper --> AgentExecution["Autonomous Agent Browser Interaction"]
    TableParser --> AgentExecution
    
    AgentExecution --> TrajectoryEval["Synthetic Trajectory Evaluator
(Action Precision, Recall & Levenshtein Edit Distance)"]
    TrajectoryEval --> VerifiedTaskDone["Verified Benchmark Task Completion"]
```

---

## 🚀 Quickstart & Standalone Execution

### Local Python Client Usage

```python
from client import MarkdownTableToJsonTransformer

# Initialize engine
engine = MarkdownTableToJsonTransformer()

# Execute self-testing benchmark suite
result = engine.run_benchmark_table_transformer()
print("Execution Result:", result)
```

---

## 🔌 One-Click MCP Integration (Claude Desktop / Cursor)

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-markdown-table-to-json-transformer-skill": {
      "command": "python",
      "args": ["-u", "/path/to/genpark-markdown-table-to-json-transformer-skill/mcp_server.py"]
    }
  }
}
```

---

## 📦 Smithery.ai & PyPI Deployment

This skill contains pre-configured `smithery.yaml` and `pyproject.toml` manifests. Install directly via pip:

```bash
pip install git+https://github.com/alphaparkinc/genpark-markdown-table-to-json-transformer-skill.git
```

---

<div align="center">
  <sub>Maintained with ❤️ by <b><a href="https://genpark.ai">GenPark AI Engineering</a></b> • Powering Next-Gen Autonomous Web Agents 🌍</sub>
</div>
