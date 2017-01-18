import yaml
import json

file_yaml = 'w1ex6_test.yaml'
file_json = 'w1ex6_test.json'

dict_1 = {
	'ipaddr': 	'172.26.0.1',
	'dname':	'jmad04r1',
	'model':	'srx240'
}

lista_1 = ['Testing', 1, 2, dict_1, 'End testing']

with open(file_yaml, "w") as file1:
        file1.write(yaml.dump(lista_1, default_flow_style=False))

with open(file_json, "w") as file1:
        json.dump(lista_1, file1)

 
