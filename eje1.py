class Email():
    __idCuenta=""
    __Dominio=""
    __TipoDominio=""
    __Pass=""

    def __init__(self, idCuenta, Dominio, TipoDominio, Pass):
            self.__idCuenta = idCuenta
            self.__Dominio = Dominio
            self.__TipoDominio = TipoDominio
            self.__Pass = Pass

    def ingresoDatos(self,nombre):

            cuentaCorreo=self.__idCuenta+"@"+self.__Dominio+"."+self.__TipoDominio
            return print("Estimado:", nombre ,"te enviaremos tus mensajes a la dirección:", cuentaCorreo)


    def retornaMail(self):
            cuentaCorreo=self.__idCuenta+"@"+self.__Dominio+"."+self.__TipoDominio
            return print("\n",cuentaCorreo)

    def getDominio(self):
            return print("\nDominio: ", self.__Dominio)

    def modificarPass(self):
            print("\n***MODIFICACIÓN CONTRASEÑA***")

            Pass=input("Ingrese Contraseña Actual:")
            if (self.__Pass==Pass):
                print("Ingrese Nueva Contraseña:")
                Passnew=input()
                self.__Pass=Passnew
                print("Nueva: ",self.__Pass)
                print("***MODIFICACIÓN REALIZADA***\n")
            else: print("La contraseña ingresada es incorecta")
            print("***MODIFICACIÓN NO REALIZADA***\n")
            
        
    def crearCuenta(self,correo):
            print("\n***CREAR CUENTA***")
            arroba=correo.find("@")
            punto=correo.find(".")
            fin=len(correo)
            self.__idCuenta=correo[0:arroba]
            self.__Dominio=correo[arroba+1:punto]
            self.__TipoDominio=correo[punto+1:fin]

          #  self.__Pass=input("Ingrese Contraseña: ")
            #print("***CUENTA CREADA***\n")
            
            


import csv
if __name__ == '__main__':

    
    arch=open("CuentasCorreo.csv")
    reader=csv.reader(arch,delimiter=',')
    emails=[]
    cuentas=[]
    unEmail=Email("","","","")
    for fila in reader:
        for i in range(len(fila)):

            unEmail=Email("","","","")
            unEmail.crearCuenta(fila[i])
            emails.append(unEmail)

            emails[i].getDominio()
            arroba=fila[i].find("@")
            cuentas.append(fila[i][0:arroba])
            
    nombre=input("Ingrese Nombre: ")
    idCuenta=input("Ingrese ID de Cuenta: ")
    Dominio=input("Ingrese Dominio: ")
    TipoDominio=input("Ingrese Tipo de Dominio: ")                
    Pass=input("Ingrese Contraseña: ")
    
    miCuenta=Email(idCuenta,Dominio,TipoDominio,Pass)
    miCuenta.ingresoDatos(nombre)

    miCuenta.retornaMail()
    miCuenta.getDominio()
    miCuenta.modificarPass()
    
    correo=input("\n Ingrese Cuenta de Correo: ")
    otraCuenta=Email("","","","")
    otraCuenta.crearCuenta(correo)
    
    idcuenta=input("Ingrese ID de Cuenta: ")
    print("id:",idcuenta)
    c=0
    for i in range(len(cuentas)):
        x=cuentas[i]
        if (idcuenta == x):
            c=0
            
    if (c == 0):
       print("El identificador ingresado se encuentra repetido")
    else:
       print("El identificador ingresado no se encuentra repetido")

    arch.close()        
