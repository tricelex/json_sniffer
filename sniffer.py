from typing import Dict, Any


def sniff_schema(json_data: Dict[str, Any]) -> Dict[str, Any]:
    schema = {
        "tag": "",
        "description": "",
        "type": "object",
        "required": False,
        "properties": {},
    }

    data = json_data["message"]

    for key, value in data.items():
        if isinstance(value, str):
            schema["properties"][key] = {"type": "string"}
        elif isinstance(value, int):
            schema["properties"][key] = {"type": "integer"}
        elif isinstance(value, list):
            if all(isinstance(elem, str) for elem in value):
                schema["properties"][key] = {"type": "string", "enum": value}
            elif all(isinstance(elem, dict) for elem in value):
                schema["properties"][key] = {
                    "type": "array",
                    "items": sniff_schema({"message": value[0]}),
                }
        elif isinstance(value, dict):
            schema["properties"][key] = sniff_schema({"message": value})

    return schema
