import pytest

from sniffer import sniff_schema


class TestSniffSchema:
    def test_string_value(self):
        json_data = {
            "message": {
                "key1": "value1",
            }
        }
        expected_output = {
            "tag": "",
            "description": "",
            "type": "object",
            "required": False,
            "properties": {
                "key1": {
                    "type": "string",
                },
            },
        }
        assert sniff_schema(json_data) == expected_output

    def test_integer_value(self):
        json_data = {
            "message": {
                "key1": 1,
            }
        }
        expected_output = {
            "tag": "",
            "description": "",
            "type": "object",
            "required": False,
            "properties": {
                "key1": {
                    "type": "integer",
                },
            },
        }
        assert sniff_schema(json_data) == expected_output

    def test_list_of_strings(self):
        json_data = {
            "message": {
                "key1": ["value1", "value2"],
            }
        }
        expected_output = {
            "tag": "",
            "description": "",
            "type": "object",
            "required": False,
            "properties": {
                "key1": {
                    "type": "string",
                    "enum": ["value1", "value2"],
                },
            },
        }
        assert sniff_schema(json_data) == expected_output

    def test_list_of_dicts(self):
        json_data = {
            "message": {
                "key1": [
                    {"key2": "value2"},
                    {"key3": "value3"},
                ],
            }
        }
        expected_output = {
            "tag": "",
            "description": "",
            "type": "object",
            "required": False,
            "properties": {
                "key1": {
                    "type": "array",
                    "items": {
                        "tag": "",
                        "description": "",
                        "type": "object",
                        "required": False,
                        "properties": {
                            "key2": {
                                "type": "string",
                            },
                        },
                    },
                },
            },
        }
        assert sniff_schema(json_data) == expected_output

    def test_nested_dicts(self):
        json_data = {
            "message": {
                "key1": {
                    "key2": {
                        "key3": "value3",
                    },
                },
            }
        }
        expected_output = {
            "tag": "",
            "description": "",
            "type": "object",
            "required": False,
            "properties": {
                "key1": {
                    "tag": "",
                    "description": "",
                    "type": "object",
                    "required": False,
                    "properties": {
                        "key2": {
                            "tag": "",
                            "description": "",
                            "type": "object",
                            "required": False,
                            "properties": {
                                "key3": {
                                    "type": "string",
                                },
                            },
                        },
                    },
                },
            },
        }
        assert sniff_schema(json_data) == expected_output

    def test_empty_dict_value(self):
        json_data = {
            "message": {
                "key1": {},
            }
        }
        expected_output = {
            "tag": "",
            "description": "",
            "type": "object",
            "required": False,
            "properties": {
                "key1": {
                    "tag": "",
                    "description": "",
                    "type": "object",
                    "required": False,
                    "properties": {},
                },
            },
        }
        assert sniff_schema(json_data) == expected_output
