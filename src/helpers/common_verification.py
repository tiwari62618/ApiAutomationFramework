# common verification

# Http status code
# Headers
# Data verification
# Json schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code==expected_data, "Failed to match status code   "

def verify_reponse_key(key, expected_data):
    assert key==expected_data,"Failed to match the key"

def verify_json_key_not_null(key):
    assert key!=0,"Failed key is null"

def verify_json_key_greater_zero(key):
    assert key>0,"Failed key is not > 0"
