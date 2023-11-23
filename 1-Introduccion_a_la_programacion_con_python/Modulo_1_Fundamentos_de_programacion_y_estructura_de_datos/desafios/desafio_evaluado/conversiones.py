import sys

sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
peso_chileno = float(sys.argv[4])

conversion_sol_peruano = sol_peruano*peso_chileno
conversion_peso_argentino = peso_argentino*peso_chileno
conversion_dolar_americano = dolar_americano*peso_chileno

print(f"Los {peso_chileno} pesos equivalen a: ")
print(f" {conversion_sol_peruano} Soles")
print(f" {conversion_peso_argentino} Pesos Argentinos")
print(f" {conversion_dolar_americano} Dólares Americanos")