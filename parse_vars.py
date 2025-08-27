import yaml
import json
import sys

def parse_vars(yml_path):
    try:
        with open(yml_path) as f:
            data = yaml.safe_load(f)
        print(f"Raw data from {yml_path}: {data}", file=sys.stderr)  # Debug raw data
        vars_data = data.get('variables', {})
        if not vars_data:
            print("Warning: 'variables' key not found or empty", file=sys.stderr)
        return json.dumps({
            'database_name': vars_data.get('sf_database', 'default_db'),  # Default if missing
            'schema_name': vars_data.get('sf_schema', 'default_schema')   # Default if missing
        })
    except Exception as e:
        print(f"Error parsing {yml_path}: {e}", file=sys.stderr)
        return json.dumps({'database_name': 'default_db', 'schema_name': 'default_schema'})

if __name__ == '__main__':
    if len(sys.argv) > 1:
        yml_path = sys.argv[1]
        print(parse_vars(yml_path))
    else:
        print('Error: No YML path provided')
