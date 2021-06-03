import json
import copy

def read_ipynb(notebook_path):
	with open(notebook_path, 'r', encoding='utf-8') as f:
		return json.load(f)

first = read_ipynb('Cannon.ipynb')
second = read_ipynb('Matthew.ipynb')
third = read_ipynb('Serene.ipynb')
fourth = read_ipynb('Aayushma.ipynb')

final = copy.deepcopy(first)
final['cells'] = first['cells'] + second['cells'] + third['cells'] + fourth['cells']



def write_ipynb(notebook, notebook_path):
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f)

write_ipynb(final, 'combined.ipynb')

