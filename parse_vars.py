import yaml
import json
import sys

def parse_vars(yml_path):
    with open(yml_path) as f:
        data = yaml.safe_load(f)
    vars_data = data.get('variables', {})
    return json.dumps({
        'database_name': vars_data.get('sf_database'),
        'schema_name': vars_data.get('sf_schema')
    })

if __name__ == '__main__':
    if len(sys.argv) > 1:
        yml_path = sys.argv[1]
        print(parse_vars(yml_path))
    else:
        print('Error: No YML path provided')
