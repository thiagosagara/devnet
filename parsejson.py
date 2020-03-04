# Fill in this file with the code from parsing JSON exercise
import json
import yaml

#you want to load the JSON file into a string, using the json.load method.
#You are passing in the JSON data you read in the previous lines.

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
json_file.close()
print(ourjson)


print(ourjson['expires_in'])
#imprime apenas o token (vc passa a chave e espera o valor)
print("The access token from JSON is: %s" % ourjson['access_token'])


#voce pode usar o yaml tambem para fazer o serializing de um json

print("\n\n---")

print(yaml.dump(ourjson))
