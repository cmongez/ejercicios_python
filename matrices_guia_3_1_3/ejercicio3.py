# 3. Crear un Arreglo [10][4] en el cual simula un bus, tendrá que darle de forma automática los números de asiento y luego mostrarlo por pantalla 
# de la siguiente forma

# 1	2		3	4
# 5	6		7	8
# 9	10		11	12
# 13	14		15	16
# 17	18		19	20
# 21	22		23	24
# 25	26		27	28
# 29	30		31	32
# 33	34		35	36
# 37	38		39	40

nroAsiento = 1

autobus = []
for i in range(10):
    filaAsientos = []

    for i in range(4):
        filaAsientos.append(nroAsiento)
        nroAsiento = nroAsiento + 1

    autobus.append(filaAsientos)

for fila in autobus:
    for asiento in fila:
        print(asiento, end="\t")
    print()