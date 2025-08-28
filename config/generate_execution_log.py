import yaml
import os
import datetime
import json
from pathlib import Path

def generate_execution_log(layer, vars_json, schemachange_output, workspace):
    log_file = os.path.join(workspace, "execution_log.yml")
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Parse vars
    try:
        vars_dict = json.loads(vars_json)
        database_name = vars_dict.get("sf_database", "SF_DEVOPS_DEV_DB")
        schema_name = vars_dict.get("sf_schema", layer)
    except json.JSONDecodeError:
        vars_dict = {"sf_database": "SF_DEVOPS_DEV_DB", "sf_schema": layer, "new_var": f"{layer}_value"}
        database_name = "SF_DEVOPS_DEV_DB"
        schema_name = layer

    # Determine if scripts were applied
    applied = "true" if "scripts_applied=[1-9]" in schemachange_output else "false"

    # Generate new entry
    new_entry = {
        "version": "0.0.1" if not os.path.exists(log_file) else f"0.0.{int(Path(log_file).read_text().count('version:') + 1)}",
        "layer": layer,
        "location": os.path.join(workspace, layer, "migrations", "scripts"),
        "commit_msg": "No commit message",
        "timestamp": current_time,
        "applied": applied
    }

    # Load existing log or start fresh
    executions = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            data = yaml.safe_load(f) or {}
            executions = data.get("executions", [])

    # Prepend new entry
    executions.insert(0, new_entry)

    # Save updated log
    with open(log_file, 'w') as f:
        yaml.safe_dump({"executions": executions}, f, default_flow_style=False)

    print(f"Updated execution log with version {new_entry['version']} for {layer} (applied: {applied})")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python generate_execution_log.py <layer> <vars_json> <schemachange_output>")
        sys.exit(1)
    generate_execution_log(sys.argv[1], sys.argv[2], sys.argv[3], os.getenv("GITHUB_WORKSPACE", "/"))
