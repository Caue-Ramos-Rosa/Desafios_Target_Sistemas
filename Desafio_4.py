print(str(rj_res + '%'))

mg_por = (mg*100 / soma)
mg_var = math.log10(mg_por)
mg_res =(f'O Estado de MG teve o percentual de {mg_por:.1f}')
print(str(mg_res + '%'))

es_por = (es*100 / soma)
es_var = math.log10(es_por)
es_res =(f'O Estado de ES teve o percentual de {es_por:.1f}')
print(str(es_res + '%'))

outros_por = (outros*100 / soma)
outros_var = math.log10(outros_por)
outros_res =(f'Os Outros Estados teve o percentual de {outros_por:.1f}')
print(str(outros_res + '%'))
