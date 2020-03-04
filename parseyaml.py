# Fill in this file with the code from parsing YAML exercise
'''
he following program uses PyYAML to parse a YAML file, 
extract and print data values, then output a JSON version of the file. 
It uses the safe_load() method to parse the file stream and normal Python data references 
to extract values from the resulting Python data structure, 
then uses the JSON module's dumps() function to serialize the Python 
data back out as JSON, to the terminal.
'''
#instale o pyyaml (pip3 install pyyaml)

import json
import yaml

yaml_file = open("myfile.yaml","r")

pythondata = yaml.safe_load(yaml_file)

print(pythondata['expires_in'])

print("The access token from YAML is: %s" % pythondata['access_token'])

print("\n\n")

print(json.dumps(pythondata))
