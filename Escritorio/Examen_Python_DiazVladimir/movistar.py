import json
def abrirJSON():
    dicFinal={}
    with open("./dic_filtro.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./dic_filtro.json",'w') as outFile:
        json.dump(dic,outFile)
    

abrir=abrirJSON

def munu():
    print("############################")
    print("#####---bienvenido a movistar---#######")
    print("############################")
    print("como quieres ingresar")
    print("1. cliente")
    print("2. operador")
 
    print("4. Cerrar programa")


def planes():
    print("que plan quieres")
    print("1. plan1:30mb")
    print("2. plan2:500mb")
    print("3. plan3:1gb")
    plan=input(":")
    if plan=="1":
        print
        
def cliente():
    num=input("identificacion")
    for i in range (len(abrir["movistar"]["cliente"])):
        if num == abrirJSON(["movistar"]["cliente"][i]["numIden"]):
            print("que quieres hecer")
            print("1.ver años en el servicio")
            print("2. ver palnes")
            print("3. ver tu plan ")
            opc=input(":")
            if opc=="1":
                print(f"tuas años cun nuestro servicio son {abrir["movistar"]["clientes"][i]["añosServ"]}")
            if

            
            
            

            

