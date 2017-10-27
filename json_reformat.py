import json
from pprint import pprint

with open('/home/callum/Documents/vPanelDB/vPanelDB/gene_with_protein_product.json') as data_file:
    data = json.load(data_file)

for i, gene in enumerate(data['response']['docs']):
    print('{"model": "vPanelDBapp.hugogene",')
    print('"pk": %s, ' % i)
    print('"fields": {')
    print('"symbol": "%s",' % gene['symbol'])
    print('"locationSortable": "%s",' % gene['location_sortable'])
    print('"ensemblGeneID": "%s"' % gene.get('ensembl_gene_id', 'Unavaliable'))
    print('}')
    print('},')