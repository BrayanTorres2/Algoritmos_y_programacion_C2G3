#Entradas
a=input()
b=str(input())
c=input()
#Caja negra
mensaje=""
if(a=="vertebrado"):
    if(b=="ave"):
        if(c=="carnivoro"):
            mensaje="aguia"
        else:
            mensaje="pomba"   
    else:
        if(c=="onivoro"):
            mensaje="homem"

        else:
            mensaje="vaca" 
else:
    if(b=="inseto"):
        if(c=="herbivoro"):
            mensaje="lagarta"
        else:
            mensaje="pulga" 
    else:
        if(c=="onivoro"):
            mensaje="minhoca"
        else:
            mensaje="sanguessuga"   
#salida                 
print(mensaje)
