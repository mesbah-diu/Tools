import yaml

def list_api_endpoints(yaml_file_path):
    # Load YAML file
    with open(yaml_file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    # Ensure the YAML file has the expected structure
    if 'paths' not in data:
        print("No 'paths' section found in YAML file.")
        return

    # Extract endpoints and methods
    for path, methods in data['paths'].items():
        print(f"\nEndpoint: {path}")
        for method in methods.keys():
            print(f"  Method: {method.upper()}")

if __name__ == "__main__":
    # Example usage
    yaml_path = "spec.yml"  # Replace with your file name
    list_api_endpoints(yaml_path)
