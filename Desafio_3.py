import json

with open("../faturamento_diario.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

dia_s = list()
valore_s = list()

for k in dados:
    if (k['dia']) and (k['valor']) != 0:
        dia_s.append(k['dia'])
        dia_s.append(k['valor'])
    if (k['valor']) != 0:
        valore_s.append(k['valor'])

som_a = sum(valore_s)
quant_i = len(valore_s)
medi_a = (som_a / quant_i)
max_valor = max(valore_s)
min_valor = min(valore_s)
dia_maior = list()
for p in dados:
    if p['valor'] >= medi_a:
        dia_maior.append(p['dia'])


for t in dados:
    if t['valor'] == max_valor:
        print('O maior valor foi no dia', (t['dia']), 'com', (max_valor))

for r in dados:
    if r['valor'] == min_valor:
        print('O menor valor foi no dia', (r['dia']), 'com', (min_valor))

print('Em', len(dia_maior), 'dias do mes o valor foi maior que a média mensal')
