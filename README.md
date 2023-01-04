# Running the Script

## To run the script, follow these steps

1. Make sure that you have Python and Poetry installed on your system. You can check if Python is installed by running the following command in your terminal `python --version`.

2. Open a terminal window and navigate to project directory
3. Create a new virtual environment for the project by running the following command: `poetry install`. This will create a new virtual environment and install the dependencies specified in the `pyproject.toml` file.
4. Activate the virtual environment by running the following command: `poetry shell`.
5. Navigate to the `scripts` directory.
6. Run the script using the following command: `python main.py path/to/json_file`. For example, if the JSON file you want to process is called `data.json` and is saved in a directory called `data`, you would run the script like this: `python script_name.py ../data/data.json`.

This will generate a JSON schema file based on the structure of the input JSON file, and save the schema file in the schema directory. The name of the schema file will be the base name of the input file, followed by _schema.json.

For example, if the input file is called `data.json`, the schema file will be called `data_schema.json`.

# Running tests

## To run the tests for the script, follow these steps

1. Make sure that you have activated the virtual environment for the project
2. To run the tests, open a terminal window and navigate to the directory. Then run the following command: `python -m pytest`. This will run the test class with all the functions in the `test_sniffer.py` file.
