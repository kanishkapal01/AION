print("Welcome to AION")
print("Choose your laboratory: ")
x= int(input("1: Electro\n 2: Thermo\n 3: Quantum\n 4: Classical\n 5: Statistical" ))

if x == 3:
    import qutip as qu
    print(qu.sigmay())
