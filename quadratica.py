a = int(input("Digite o valor do A: "))
b = int(input("Digite o valor do B: "))
c = int(input("Digite o valor do C: "))
delta = (b**2) - (4*a*c)
raizDelta = delta ** 0.5
raizUm = (-b + raizDelta) / (2*a)
raizDois = (-b - raizDelta) / (2*a)
print(f"Raiz Um: {raizUm}")
print(f"Raiz Dois: {raizDois}")