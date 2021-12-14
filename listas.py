valores=[]
for x in range(1,6):
    valores.append(int(input('digite um valor : ')))
print('o menor valor foi', min(valores))
print('na posição',valores.index(min(valores)))
print('o maior valor foi' , max(valores))
print(valores.index(max(valores)))
#solução mais simples, porém fiz sozinho, mostra quas etudo por completo, porém se o numero reptir a posição menor e maior fica do que aparece primeiro
# sei que poderia usar desta forma 
#valores=[]
#maior=0
#menor=0    
# for x in range (0,6):
#   valores.append(int(input('digite um valor: ')))
#    if x == 0:
#       maior=menor=valores[x]
#   else:
#       if valores [x] > maior:
#           maior=valores[x]
#       if valores [x] < menor:
#           menor= valores[x]
# for c, v in enumerate(valores):
#   if v==maior
#       print(f'c'#aqui vai mostrar sua posição)
#for c, v in enumerate(valores):
#   if v== menor:
#       print(f'c'#aqui vai mostrar sua posição)
