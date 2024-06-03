import os
from dotenv import load_dotenv, dotenv_values
 
source_env_file_path = '/root/stellio-context-broker/.env'
load_dotenv(dotenv_path=source_env_file_path)

# Read variables from the source .env file
SERVER_IP = dotenv_values(SERVER_IP)

# Write variables to the new .env file
new_env_file_path = 'new_env_file.env'
with open(new_env_file_path, 'w') as f:
    for key, value in variables_to_pass.items():
        f.write(key + "=" + value + "\n")