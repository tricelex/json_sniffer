import os
import sys
import json
from sniffer import sniff_schema


def main(json_file: str) -> None:
    with open(json_file, "r") as f:
        json_data = json.load(f)

    schema = sniff_schema(json_data)
    base_name = os.path.splitext(os.path.basename(json_file))[0]
    output_file = f"./schema/{base_name}_schema.json"

    with open(output_file, "w") as f:
        json.dump(schema, f, indent=2)


if __name__ == "__main__":
    json_file = sys.argv[1]
    main(json_file)
