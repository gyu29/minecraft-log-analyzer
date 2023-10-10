import re

# Define a regular expression pattern to extract key-value pairs from the log data
pattern = r'--(\w+), ([^,]+)'

# Read the log file
with open('launcher.log', 'r') as log_file:
    log_data = log_file.read()

# Extract key-value pairs using regex
log_info = dict(re.findall(pattern, log_data))

# Display the extracted information
for key, value in log_info.items():
    print(f'{key}: {value}')
