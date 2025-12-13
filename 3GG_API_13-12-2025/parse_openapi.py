import json,yaml
import logging


class APIResponseError(Exception):
    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status

log_file = r"C:\Users\ROYDEN\OneDrive\Desktop\New folder\TelcoLearn\3GG_API\logger.txt"
err_file = r"C:\Users\ROYDEN\OneDrive\Desktop\New folder\TelcoLearn\3GG_API\error.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

url = r"C:\Users\ROYDEN\OneDrive\Desktop\New folder\TelcoLearn\3GG_API\oapi_5.yaml"

logging.info("Starting OpenAPI parsing")

try:
    with open(url, 'r') as file:
        oapi = yaml.safe_load(file)
    if not oapi:
        raise APIResponseError("YAML file is empty or unreadable")    
    op = []
    metadata = {}
    for key in oapi['info']:
        metadata[key] = oapi['info'][key] 

    for key in oapi['servers'][0]:
        metadata[key] = oapi['servers'][0][key]
    op.append(metadata)

    method_count = {}
    endpoints_with_resp = 0
    endpoints_without_resp = 0
    request_response_map = []
    auth_methods = oapi.get("components", {}).get("schemas", {})
    paths = oapi.get("paths")

    for path, methods in paths.items():
        for method, details in methods.items():
            if method.lower() in ["get", "post", "put", "delete", "patch"]:
                
                method_count[method.upper()] = method_count.get(method.upper(), 0) + 1

                responses = details.get("responses", {})
                if responses:
                    endpoints_with_resp += 1
                else:
                    endpoints_without_resp += 1

                request_response_map.append({
                    "path": path,
                    "method": method.upper(),
                    "responses": list(responses.keys())
                })
                entry = {
                    "path": path,
                    "method": method.upper(),
                    "tags": details.get("tags"),
                    "responses": responses
                }
                op.append(entry)
                logging.info(f"Extracted endpoint: {method.upper()} {path}")
    for k,v in oapi.get("components", {}).get("schemas", {}).items():
        schema_entry = {
            "schema_name": k,
            "schema_details": v
        }
        op.append(schema_entry)

    if not op:
        raise APIResponseError("No endpoints FOUND")

    md = r"C:\Users\ROYDEN\OneDrive\Desktop\New folder\TelcoLearn\3GG_API\metadata_5.json"    
    with open(md, 'w') as f:
        json.dump(op, f, indent=4)
    print(op)

    logging.info("Metadata JSON saved successfully")

    summary = {
        "http_method_count": method_count,
        "endpoints_with_responses": endpoints_with_resp,
        "endpoints_without_responses": endpoints_without_resp,
        "authentication_methods": list(auth_methods.keys()),
        "request_response_map": request_response_map,
        "total_endpoints": len(request_response_map)
    }
    
    logging.info("Generating summary file")

    summary_file = r"C:\Users\ROYDEN\OneDrive\Desktop\New folder\TelcoLearn\3GG_API\summary_5.json"
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

except FileNotFoundError as e:
    with open(err_file, "a") as ef:
        ef.write(str(e) + "\n")
    logging.error("YAML file not found")
    raise APIResponseError("YAML file not found on disk")

except APIResponseError as e:
    with open(err_file, "a") as ef:
        ef.write("APIResponseError: " + str(e) + "\n")
    logging.error(f"APIResponseError: {e}")
    print("ERROR:", e)

except Exception as e:
    with open(err_file, "a") as ef:
        ef.write("Unexpected Error: " + str(e) + "\n")
    logging.error(f"Unexpected error: {e}")
    raise APIResponseError("Unknown error occurred while processing YAML")