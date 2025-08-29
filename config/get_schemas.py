import yaml
import sys
import os

def get_schemas():
    schemas_yml = os.path.join(os.path.dirname(__file__), "schemas.yml")
    print(f"Current directory: {os.getcwd()}")  # Debug on separate line
    print(f"Looking for: {schemas_yml}")      # Debug on separate line
    try:
        with open(schemas_yml, 'r') as file:
            data = yaml.safe_load(file)
            if data and 'schemas' in data and data['schemas']:
                return data['schemas']
            else:
                print("Error: No valid schemas found in schemas.yml", file=sys.stderr)
                sys.exit(1)
    except FileNotFoundError:
        print("Error: schemas.yml not found", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML in schemas.yml - {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    schemas = get_schemas()
    for schema in schemas:
        print(schema)  # Print each schema on a new line
