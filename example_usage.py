from client import MarkdownTableToJsonTransformer
import json

def main():
    transformer = MarkdownTableToJsonTransformer()
    res = transformer.run_benchmark_table_transformer()
    print("Table Transformer Benchmark Result:")
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
