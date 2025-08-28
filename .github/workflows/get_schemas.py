import yaml
import sys

def get_schemas():
    schemas_yml = "../schemas.yml"  # Relative to .github/workflows/
    print(f"Looking for: {schemas_yml}")  # Debug line
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
    print(" ".join(schemas))  # Output as space-separated list for shell parsing
