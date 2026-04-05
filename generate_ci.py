import yaml
import json
import sys

def generate_matrix(yaml_file):
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    repos = data.get("repos", [])

    # Convert to GitHub Actions matrix format
    matrix = {
        "repo": repos
    }

    return matrix


if __name__ == "__main__":
    yaml_file = sys.argv[1] if len(sys.argv) > 1 else "repos.yaml"

    matrix = generate_matrix(yaml_file)

    # Print JSON (important for GitHub Actions)
    print(json.dumps(matrix))