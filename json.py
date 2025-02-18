import json

# Load JSON data from file
with open("sample-data.json") as f:
    data = json.load(f)

# Header for the table
print("Interface Status")
print("="*80)
print("DN                                                 Description           Speed    MTU")
print("-"*80)

# Iterate through the data and extract relevant fields
for item in data['imdata']:
    dn = item['topSystem']['attributes']['dn']
    description = item['topSystem']['attributes'].get('description', 'inherit')
    speed = item['topSystem']['attributes'].get('speed', 'N/A')
    mtu = item['topSystem']['attributes'].get('mtu', 'N/A')

    # Format and print the row
    print(f"{dn:<50} {description:<20} {speed:<8} {mtu}")

