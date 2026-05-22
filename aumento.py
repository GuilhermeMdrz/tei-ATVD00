h = int(input("HORAS TRABALHADAS: "))
valorh = float(input("VALOR DA HORA: R$"))
s = h * valorh
sbonus = (1 + h**1.5 / valorh**2.5) * s
print(f'SALÁRIO BASE: R${s:.2f}')
print(f'SALÁRIO BONIFICADO: R${sbonus:.2f}')