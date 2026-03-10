print("Olá, bem vindo ao restaurante!")
print("O que deseja comer?")
cardapio={
    "carnes":[
        ("bife" , 25.50),
        ("Frango" , 20.00),
        ("Pernil",  30.50),
    ],
    "frutos_mar":[
        ("lula", 35.00),
        ("pirarucu", 40.00),
        ("tilapia", 50.00),
    ],
    "sobremesas":[
        ("petit gateau", 30.00),
        ("bomba de pistache", 35.00),
        ("morango do amor", 15.00),
    ],
}
escolha=int(input(" 0 = carnes , 1 = frutos_mar , 2 = sobremesa"));
if escolha==0:
    print("Carnes:")
    for item in cardapio["carnes"]:
        print(f"- {item[0]}: R${item[1]:.2f}")

elif escolha==1:
    print("\nFrutos do Mar:")
    for item in cardapio["frutos_mar"]:
        print(f"- {item[0]}: R${item[1]:.2f}")

elif escolha==2:
    print("sobremesas:")
    for item in cardapio["sobremesas"]:
        print(f" - {item[0]}: R${item[1]:.2f}")

