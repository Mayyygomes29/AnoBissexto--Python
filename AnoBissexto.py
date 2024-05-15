from datetime import date

#Verifica se o ano é bissexto
ano = int(input("Digite um ano: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print("Bissexto")
else:
    print("Ano normal")