import json

lista_pizzas = [
    {"cuatroq":[pequenia,mediana,grande],[6000,9000,12000]},
    {"hawaiana":[pequenia,mediana,grande],[6000,9000,12000]},
    {"napolitana":[pequenia,mediana,grande],[5500.8500,11000]},
    {"pepperoni":[pequenia,mediana,grande],[7000,10000,13000]}
]
tipos_cliente = {
    "Estudiante diurno":0.88,
    "Estudiante vespertino":0.86,
    "Administrativo":0.9
}
lista_ventas = []


#Funcion 1:
def registrar_venta():
    pz = int(input("""
    1. Cuatro Quesos
    2. Hawaiana
    3. Napolitana
    4. Pepperoni
    Que tipo de pizza deseas?(1-2-3-4): """))
    if pz == 1:
        pz = "Cuatro Quesos"
    elif pz == 2:
        pz = "Hawaiana"
    elif pz == 3:
        pz = "Napolitana"
    elif pz == 4:
        pz = "Pepperoni"
    tam = int(input("""
    1. Pequenia
    2. Mediana
    3. Grande
Que tamaño deseas?(1-2-3): """))
    cant = int(input("Cuantas deseas?:"))
    cliente = input("Ingresa tu nombre:")
    desc = input("""
    A que categoria perteneces?
1. Estudiante diurno
2. Estudiante Vespertino
3. Administrativo""")                     
    orden = {f"{cliente}":[pz,tam,cant,desc]}
    lista_ventas.append(orden)
    des = input ("""
    Orden registrada correctamente
Deseas rgistrar otra orden?
1. Si
2. Volver al menu principal
3. Ir a pagar """)
    if des == 1:
        registrar_venta()
    elif des == 2:
        menu()
    elif des == 3:
        boleta()
    

#Funcion 2:
def mostrar_ventas():
    for i in lista_ventas:
        nombre = list (i.keys())[0]
        print (f"""
    Nombre: {nombre}
    {i[nombre][3]}
    Orden : {i[nombre][2]}, pizzas {i[nombre][0]} {i[nombre][1]}""")
    input("Pulsa enter para volver al menu:")
    menu()


#Funcion 3:
def buscar_orden():
    cliente = input ("Ingresa el nombre del cliente:")
    for i in lista_ventas:
        if list(i.keys())[0] == cliente:
            print (f"""
    Nombre: {list(i.keys())[0]}
    {i[cliente][3]}
    Orden : {i[cliente][2]}, pizzas {i[cliente][0]} {i[cliente][1]}""")
    input("Pulsa enter para volver al menu:")
    menu()
            

#Funcion 4:
def guardar_ventas():
    with open ("Ventas.json","w") as f:
        json.dump (lista_ventas,f)
        print ("Ventas guardadas")
        menu()

#Funcion 5:
def cargar_ventas():
    with open ("Ventas.json","r") as f:
        cargar = json.load(f)
        print (cargar)
        menu()


#Funcion 6:
def boleta():
    cliente = input ("Ingresa el nombre del cliente:")
    for i in lista_ventas:
        if list(i.keys())[0] == cliente:
            if i[cliente][0] == 1:
                print(f"""
:::::::::::::::::::::::::::Pizzas Duoc:::::::::::::::::::::::::::
    {i[cliente][2]} x {i[cliente][0]} {i[cliente][1]} = {i[cliente][2]*lista_pizzas[0][1][i[cliente][1]-1]}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Subtotal: {i[cliente][2]*lista_pizzas[0][1][i[cliente][1]-1]}
Descuento: {i[cliente][3]}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Total: {i[cliente][2]*lista_pizzas[0][1][i[cliente][1]-1]*tipos_cliente[i[cliente][3]]}""")
            elif i[cliente][0] == 2:
                print(f"""
:::::::::::::::::::::::::::Pizzas Duoc:::::::::::::::::::::::::::
    {i[cliente][2]} x {i[cliente][0]} {i[cliente][1]} = {i[cliente][2]*lista_pizzas[1][1][i[cliente][1]-1]}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Subtotal: {i[cliente][2]*lista_pizzas[1][1][i[cliente][1]-1]}
Descuento: {i[cliente][3]}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Total: {i[cliente][2]*lista_pizzas[1][1][i[cliente][1]-1]*tipos_cliente[i[cliente][3]]}""")
            elif i[cliente][0] == 3:
                print(f"""
:::::::::::::::::::::::::::Pizzas Duoc:::::::::::::::::::::::::::
    {i[cliente][2]} x {i[cliente][0]} {i[cliente][1]} = {i[cliente][2]*lista_pizzas[2][1][i[cliente][1]-1]}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Subtotal: {i[cliente][2]*lista_pizzas[2][1][i[cliente][1]-1]}
Descuento: {i[cliente][3]}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Total: {i[cliente][2]*lista_pizzas[2][1][i[cliente][1]-1]*tipos_cliente[i[cliente][3]]}""")
            elif i[cliente][0] == 4:
                print(f"""
:::::::::::::::::::::::::::Pizzas Duoc:::::::::::::::::::::::::::
    {i[cliente][2]} x {i[cliente][0]} {i[cliente][1]} = {i[cliente][2]*lista_pizzas[3][1][i[cliente][1]-1]}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Subtotal: {i[cliente][2]*lista_pizzas[3][1][i[cliente][1]-1]}
Descuento: {i[cliente][3]}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Total: {i[cliente][2]*lista_pizzas[3][1][i[cliente][1]-1]*tipos_cliente[i[cliente][3]]}""")
            else:
                print ("Error")
            input("Pulsa enter para volver al menu:")
            menu()


#Funcion 7:
def anular():
    cliente = input ("Ingresa el nombre del cliente:")
    for i in lista_ventas:
        if list(i.keys())[0] == cliente:
            lista_ventas.remove(i)
            print ("Orden anulada")
            menu()

#Funcion 8:
def salir():
    print ("Hasta pronto")
    exit

                

def menu():
    des = ("""
    1. Registrar venta
    2. Mostrar ventas
    3. Buscar orden
    4. Guardar ventas
    5. Cargar ventas
    6. Salir""")

try:
    while True:
        menu()
        des = int(input("Que deseas hacer?:"))

        if des == 1:
            registrar_venta()
        elif des == 2:
            mostrar_ventas()
        elif des == 3:
            buscar_orden()
        elif des == 4:
            guardar_ventas()
        elif des == 5:
            cargar_ventas()
        elif des == 6:
            boleta()
        elif des == 7:
            anular()
        elif des == 8:
            salir()

except ValueError:
    print ("Ingresa un valor valida")

    