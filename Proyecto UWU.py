import json                                                 #Aqui cargo los archivos json, no hay mucho misterio,
cargar=str(input('¿Desea cargar los archivos anteriores?\n'))
if cargar.lower()=='si':
    v=open("BACKUPEDIFICIO.json","r")                        #por medio del load confierto el archivo json en diccionario            
    q=open("BACKUPUSURIOS.json","r")
    EDIFICIO=json.load(v)
    USUARIOS=json.load(q)

else:
    v=open("tiposParqueaderos.json","r")
    q=open("usuarios.json","r")
    EDIFICIO=json.load(v)
    USUARIOS=json.load(q)



def tranformiceusuarios (USUARIOS):                                              #Aqui transformo las palabras automovil, a.electrico, motocicleta y discapacitados                    
    for x in range(len(USUARIOS['usuarios'])):                                   #En los numeros correspondientes (En el diccionario usuarios)       
        if USUARIOS['usuarios'][x][4]=='AutomÃ³vil':
            USUARIOS['usuarios'][x][4]=1
        elif USUARIOS['usuarios'][x][4]=='AutomÃ³vil ElÃ©ctrico':
            USUARIOS['usuarios'][x][4]=2
        elif USUARIOS['usuarios'][x][4]=='Motocicleta':
            USUARIOS['usuarios'][x][4]=3
        elif USUARIOS['usuarios'][x][4]=='Discapacitado':
            USUARIOS['usuarios'][x][4]=4
    return USUARIOS

def transformicepisos(EDIFICIO):
    for a in EDIFICIO.keys():
        for b in range(len(EDIFICIO[a])):                                                                                       #Aqui transformo las palabras automovil, a.electrico, motocicleta y discapacitados
            for c in range(10):                                                                                                 #En los numeros correspondientes (En el diccionario del edificio)  
                if EDIFICIO[a][b][c]!=1 and EDIFICIO[a][b][c]!=2 and EDIFICIO[a][b][c]!=3 and EDIFICIO[a][b][c]!=4:             #Recorro todo el diccionario con ciclos for                       
                    for z in range(6):                                                                                          #Tuve que tomar los caracteres diferentes por las tildes    
                        if 'AutomÃ³vil'==EDIFICIO[a][b][c][4]:
                            EDIFICIO[a][b][c][4]=1
                        elif 'AutomÃ³vil ElÃ©ctrico'==EDIFICIO[a][b][c][4]:
                            EDIFICIO[a][b][c][4]=2
                        elif 'Motocicleta'==EDIFICIO[a][b][c][4]:
                             EDIFICIO[a][b][c][4]=3
                        elif 'Discapacitado'==EDIFICIO[a][b][c][4]:
                             EDIFICIO[a][b][c][4]=4
                
    return EDIFICIO




def validacionregistro(USUARIOS):
    numeroidentificacion=eval(input('Ingrese su numero de identificacion: '))                       #Aqui valido si el coche ya esta registrado o no, 
    n=0                                                                                             #primero pido el numero de identificacion para no hacerlo tedioso                       
    for x in range(len(USUARIOS['usuarios'])):
        if USUARIOS['usuarios'][x][1]==numeroidentificacion:
            n=n+1
    if n==0:
        nombre=str(input('Ingrese sus nombres y apellidos: ')) 
        tipodeusuario=str(input('Ingrese su tipo de usuario: '))
        placa=str(input('Ingrese la placa de su vehiculo: '))
        tipovehiculo=eval(input('Ingrese su tipo de vehiculo:\n 1.Automóvil\n 2.Automóvil Eléctrico\n 3.Motocicleta\n 4.Discapacitado\n(Ingrese el numero del tipo de auto que tenga)\n'))
        plandepago=str(input('Ingrese su plan de pago:\n 1.Mensualidad\n 2.Diario\n(INGRESE LA PALABRA COMPLETA POR FAVOR)\n'))
        lista=[nombre,numeroidentificacion,tipodeusuario,placa,tipovehiculo,plandepago]
        USUARIOS['usuarios'].append(lista)
        return USUARIOS
    else:
        print('Usted ya registro un vehiculo')
        validacionregistro(USUARIOS)





def ingreso(USUARIOS):
    n=0
    placaingreso=str(input('Ingrese la placa de su vehiculo: '))                                                        #Primero, aunque no me lo hayan pedido en el trabajo, valido si el coche ya ha sido parqueado
    for a in EDIFICIO.keys():                                                                                           #si no es el caso luego verifico si la placa esta registrada                        
        for b in range(len(EDIFICIO[a])):
            for c in range(10):
                if EDIFICIO[a][b][c]!=1 and EDIFICIO[a][b][c]!=2 and EDIFICIO[a][b][c]!=3 and EDIFICIO[a][b][c]!=4:
                    for z in range(6):
                        if placaingreso==EDIFICIO[a][b][c][3]:
                            print('Ese automovil ya se encuentra aqui.')
                            return ingreso(USUARIOS)
    for x in range(len(USUARIOS['usuarios'])):
        if placaingreso==USUARIOS['usuarios'][x][3]:
            n=n+1
    if n==0:
        print('Su vehiculo no esta registrado...')
        tipovehiculo=eval(input('Ingrese su tipo de vehiculo:\n 1.Automóvil\n 2.Automóvil Eléctrico\n 3.Motocicleta\n 4.Discapacitado\n(Ingrese el numero del tipo de auto que tenga)\n'))
        lista=['???','???','Visitante',placaingreso,tipovehiculo,'Diario']
        USUARIOS['usuarios'].append(lista)
    return USUARIOS,placaingreso


















def ingreso2(EDIFICIO,placaingreso,USUARIOS):                                   #Aqui utilizo 6 contadores para numerar el numero de puestos disponibles.
    for y in range(len(USUARIOS['usuarios'])):                                  #Sumo los contadores recorriendo el diccionario con varios for anidados        
        if placaingreso==USUARIOS['usuarios'][y][3]:
            minilista=USUARIOS['usuarios'][y]
    disponibles1=0
    disponibles2=0
    disponibles3=0
    disponibles4=0
    disponibles5=0
    disponibles6=0
    if minilista[4]==1:
        for a in EDIFICIO.keys():
            for g in range(len(EDIFICIO[a])):
                for h in range(10):
                    if EDIFICIO[a][g][h]==minilista[4]:
                        if a=='Piso1':
                            disponibles1+=1
                        elif a=='Piso2':
                            disponibles2+=1
                        elif a=='Piso3':
                            disponibles3+=1
                        elif a=='Piso4':
                            disponibles4+=1
                        elif a=='Piso5':
                            disponibles5+=1
                        elif a=='Piso6':
                            disponibles6+=1
    if minilista[4]==2:
        for a in EDIFICIO.keys():
            for g in range(len(EDIFICIO[a])):
                for h in range(10):
                    if EDIFICIO[a][g][h]==minilista[4] or EDIFICIO[a][g][h]==1:
                        if a=='Piso1':
                            disponibles1+=1
                        elif a=='Piso2':
                            disponibles2+=1
                        elif a=='Piso3':
                            disponibles3+=1
                        elif a=='Piso4':
                            disponibles4+=1
                        elif a=='Piso5':
                            disponibles5+=1
                        elif a=='Piso6':
                            disponibles6+=1
    if minilista[4]==3:
        for a in EDIFICIO.keys():
            for g in range(len(EDIFICIO[a])):
                for h in range(10):
                    if EDIFICIO[a][g][h]==minilista[4]:
                        if a=='Piso1':
                            disponibles1+=1
                        elif a=='Piso2':
                            disponibles2+=1
                        elif a=='Piso3':
                            disponibles3+=1
                        elif a=='Piso4':
                            disponibles4+=1
                        elif a=='Piso5':
                            disponibles5+=1
                        elif a=='Piso6':
                            disponibles6+=1
    if minilista[4]==4:
        for a in EDIFICIO.keys():
            for g in range(len(EDIFICIO[a])):
                for h in range(10):
                    if EDIFICIO[a][g][h]==minilista[4] or EDIFICIO[a][g][h]==1:
                        if a=='Piso1':
                            disponibles1+=1
                        elif a=='Piso2':
                            disponibles2+=1
                        elif a=='Piso3':
                            disponibles3+=1
                        elif a=='Piso4':
                            disponibles4+=1
                        elif a=='Piso5':
                            disponibles5+=1
                        elif a=='Piso6':
                            disponibles6+=1
          
    return EDIFICIO,disponibles1,disponibles2,disponibles3,disponibles4,disponibles5,disponibles6,minilista 



def representacion(EDIFICIO,minilista):
    pisoelegido=eval(input('Ingrese el piso en el que desea dejar su auto: \n(Solo ingrese el numero del piso que desea)\n '))
    if pisoelegido==1:
        pisoelegido='Piso1'
    elif pisoelegido==2:
        pisoelegido='Piso2'
    elif pisoelegido==3:
        pisoelegido='Piso3'
    elif pisoelegido==4:
        pisoelegido='Piso4'
    elif pisoelegido==5:                                                      #Una vez el usuario elige su piso deseado creo un for que toma como rango el piso elegido,                                                                              
        pisoelegido='Piso5'                                                   #Para la representacion utilizo varios for con una lista a la cual se van añadiendo 'X' o 'O' Dependiendo de si esta libre o no el puesto                                                                                          
    elif pisoelegido==6:                                                      #Logro todo esto con condicionales y recorriendo el diccionario                                                                                  
        pisoelegido='Piso6'                                                                                                                                                                     
    else:                                                                                                                                                                                   
        print('Ese numero no esta en el menu')                                                                                                                                  
    print('','','','',1,'','','',2,'','','',3,'','','',4,'','','',5,'','','',6,'','','',7,'','','',8,'','','',9,'','','',10)
    for x in range(len(EDIFICIO[pisoelegido])):
        lista=[]
        if minilista[4]==4 or minilista[4]==2:
            for y in range(10):
                if minilista[4]==EDIFICIO[pisoelegido][x][y] or 1==EDIFICIO[pisoelegido][x][y]:     
                    lista.append('O')
                else:
                    lista.append('X')
            print(x+1,lista)
        else:
            for y in range(10):
                if minilista[4]==EDIFICIO[pisoelegido][x][y]:     
                    lista.append('O')
                else:
                    lista.append('X')
            print(x+1,lista)            
    return pisoelegido

def ocupa(EDIFICIO,minilista,pisoelegido):                                                                             #Ahora le pido al usuario que eliga una fila y una columna                              
    fila=eval(input('Ingrese la fila del lugar que desea: '))                                                          #Con ello puedo acceder facilmente al lugar donde el usuario desea ubicar su coche                                 
    columna=eval(input('Ingrese la columna del lugar que desea: '))                                                    #Pongo el -1 porque para acceder al diccionario se empieza desde 0. Pero para mayor comodidad para el usario le pido la fila y la columna desde 1                                            
    if minilista[4]==2 or minilista[4]==4:                                                                                                                  
        if minilista[4]==EDIFICIO[pisoelegido][fila-1][columna-1] or EDIFICIO[pisoelegido][fila-1][columna-1]==1:                                                   
            EDIFICIO[pisoelegido][fila-1][columna-1]=minilista #Aqui remplazo el puesto
            return EDIFICIO,fila,columna
        else:
            print('Ese sitio esta ocupado')
            return ocupa(EDIFICIO,minilista,pisoelegido)
    else:
        if minilista[4]==EDIFICIO[pisoelegido][fila-1][columna-1]:
            EDIFICIO[pisoelegido][fila-1][columna-1]=minilista
            return EDIFICIO,fila,columna
        else:
            print('Ese sitio esta ocupado')
            return ocupa(EDIFICIO,minilista,pisoelegido)

        

def validacionretiro(EDIFICIO):
    placaretiro=str(input('Ingrese la placa de su vehiculo: '))
    horas=eval(input('Ingrese su numero de horas que ha permanecido el vehiculo: '))
    n=0

    for a in EDIFICIO.keys():
        for b in range(len(EDIFICIO[a])):
            for c in range(10):
                if EDIFICIO[a][b][c]!=1 and EDIFICIO[a][b][c]!=2 and EDIFICIO[a][b][c]!=3 and EDIFICIO[a][b][c]!=4:         #Me sucedio un error y es que no puedo
                    for z in range(6):                                                                                      #Transformar una lista a int, no tengo idea porque                        
                        if placaretiro==EDIFICIO[a][b][c][z]:                                                               #Mi solucion fue convertir la lista a str                                    
                            lista=EDIFICIO[a][b][c]                                                                                                                     
                            n+=1                                                                                                    
                            if lista[4]==1:                                                                                                                         
                                  EDIFICIO[a][b][c]='AutomÃ³vil'                                                                                                                
                            elif lista[4]==2:                                                                   
                                EDIFICIO[a][b][c]='AutomÃ³vil ElÃ©ctrico'                                                   
                            elif lista[4]==3:                                                                           
                                EDIFICIO[a][b][c]='Motocicleta'
                            elif lista[4]==4:
                                EDIFICIO[a][b][c]='Discapacitado'
    for a in EDIFICIO.keys():
        for b in range(len(EDIFICIO[a])):                                       #Y aca transformo ese srt al numero correspondiente al tipo de auto         
            for c in range(10):                                                 #Todo esto con el fin de que cuando retiren el coche, el puesto que este ocupaba vuelva a ser del tipo que era (Automovil, discapacitados...)                                                                                                
                if EDIFICIO[a][b][c]=='AutomÃ³vil':                                                                                                                                                                     
                     EDIFICIO[a][b][c]=1                                                                                                
                elif EDIFICIO[a][b][c]=='AutomÃ³vil ElÃ©ctrico':                                                                                        
                     EDIFICIO[a][b][c]=1
                elif EDIFICIO[a][b][c]=='Motocicleta':
                     EDIFICIO[a][b][c]=3
                elif EDIFICIO[a][b][c]=='Discapacitado':
                     EDIFICIO[a][b][c]=1
                        
                            
    if n==0:
        print('Ese vehiculo no esta aqui')
    else:
        if lista[5].lower()=='mensualidad':
            print('No debe realizar un pago')                                                       #Aca miro que tipo de pago tiene y hago las operaciones correspondientes
        else:
            if lista[2].lower()=='estudiante':
                print('El valor a pagar es',horas*1000)
            elif lista[2].lower()=='profesor':
                print('El valor a pagar es',horas*2000)
            elif lista[2].lower()=='personal administrativo':
                print('El valor a pagar es',horas*1500)
            elif lista[2].lower()=='visitante':
                print('El valor a pagar es',horas*3000)



def representacion2(fila,columna,minilista,EDIFICIO,pisoelegido):
        for x in range(len(EDIFICIO[pisoelegido])):
            lista=[]                                                                                        #Es un copy paste de la reprensentacion 1 solo que esta es la reprensentacion con los puestos ocupados ya con la informacion de los coches
            if minilista[4]==4 or minilista[4]==2:
                for y in range(10):
                    if  EDIFICIO[pisoelegido][fila-1][columna-1]==EDIFICIO[pisoelegido][x][y]:      #Este es el añadido
                        lista.append(minilista)
                    elif minilista[4]==EDIFICIO[pisoelegido][x][y] or 1==EDIFICIO[pisoelegido][x][y]:     
                        lista.append('O')
                    else:
                        lista.append('X')
                print(x+1,lista)
            else:
                for y in range(10):
                    if  EDIFICIO[pisoelegido][fila-1][columna-1]==EDIFICIO[pisoelegido][x][y]:
                        lista.append(minilista)
                    elif minilista[4]==EDIFICIO[pisoelegido][x][y]:     
                        lista.append('O')
                    else:
                        lista.append('X')
                print(x+1,lista)   



def txt1(EDIFICIO):
    numest=0
    numprof=0
    numadm=0
    numvis=0
    for a in EDIFICIO.keys():
        for b in range(len(EDIFICIO[a])):
            for c in range(10):
                if EDIFICIO[a][b][c]!=1 and EDIFICIO[a][b][c]!=2 and EDIFICIO[a][b][c]!=3 and EDIFICIO[a][b][c]!=4:
                        if EDIFICIO[a][b][c][2].lower() =='estudiante':
                            numest+=1
                        elif EDIFICIO[a][b][c][2].lower() =='profesor':
                            numprof+=1
                        elif EDIFICIO[a][b][c][2].lower() =='personal administrativo':
                            numadm+=1
                        elif EDIFICIO[a][b][c][2].lower() =='visitante':
                            numvis+=1
    return numest,numprof,numadm,numvis

def txt2(EDIFICIO):
    numaut=0
    numele=0
    nummoto=0
    numdis=0
    for a in EDIFICIO.keys():
        for b in range(len(EDIFICIO[a])):
            for c in range(10):
                if EDIFICIO[a][b][c]!=1 and EDIFICIO[a][b][c]!=2 and EDIFICIO[a][b][c]!=3 and EDIFICIO[a][b][c]!=4:
                        if EDIFICIO[a][b][c][4]==1:
                            numaut+=1
                        elif EDIFICIO[a][b][c][4]==2:
                            numele+=1
                        elif EDIFICIO[a][b][c][4]==3:
                            nummoto+=1
                        elif EDIFICIO[a][b][c][4]==4:
                            numdis+=1
    return numaut,numele,nummoto,numdis

def txt3(EDIFICIO):
    contpor=0
    contpiso1=0
    contpiso2=0
    contpiso3=0
    contpiso4=0
    contpiso5=0
    contpiso6=0
    for a in EDIFICIO.keys():
        for b in range(len(EDIFICIO[a])):
            for c in range(10):
                if EDIFICIO[a][b][c]!=1 and EDIFICIO[a][b][c]!=2 and EDIFICIO[a][b][c]!=3 and EDIFICIO[a][b][c]!=4:
                    contpor+=1
                    
    for a in EDIFICIO.keys():
        for b in range(len(EDIFICIO[a])):
            for c in range(10):
                if EDIFICIO[a][b][c]!=1 and EDIFICIO[a][b][c]!=2 and EDIFICIO[a][b][c]!=3 and EDIFICIO[a][b][c]!=4:
                    if a=='Piso1':
                         contpiso1+=1
                    elif a=='Piso2':
                         contpiso2+=1
                    elif a=='Piso3':
                         contpiso3+=1
                    elif a=='Piso4':
                         contpiso4+=1
                    elif a=='Piso5':
                         contpiso5+=1
                    elif a=='Piso6':
                         contpiso6+=1
                         
    return contpor,contpiso1,contpiso2,contpiso3,contpiso4,contpiso5,contpiso6
    
                            









APAGADO=''
while APAGADO!=-1:                                                                          #El programa con un while para cuando se desee parar, lo unico que hice aqui es organizar las funciones para que el programa empeice a correr
    EDIFICIO=transformicepisos(EDIFICIO)
    USUARIOS=tranformiceusuarios (USUARIOS)
    accion=eval(input('Ingrese la accion que quiera realizar:\n 1.Registrar auto\n 2.Ingresar un auto\n 3.Retirar un auto\n '))
    if accion==1:
        USUARIOS=validacionregistro(USUARIOS)
        print(USUARIOS)



        
    elif accion==2:
        USUARIOS,placaingreso=ingreso(USUARIOS)
        EDIFICIO,disponibles1,disponibles2,disponibles3,disponibles4,disponibles5,disponibles6,minilista=ingreso2(EDIFICIO,placaingreso,USUARIOS)
        print('El numero de puestos disponibles en el piso 1 es:', disponibles1)
        print('El numero de puestos disponibles en el piso 2 es:', disponibles2)
        print('El numero de puestos disponibles en el piso 3 es:', disponibles3)
        print('El numero de puestos disponibles en el piso 4 es:', disponibles4)
        print('El numero de puestos disponibles en el piso 5 es:', disponibles5)
        print('El numero de puestos disponibles en el piso 6 es:', disponibles6)
        pisoelegido=representacion(EDIFICIO,minilista)
        print('\n')
        EDIFICIO,fila,columna=ocupa(EDIFICIO,minilista,pisoelegido)
        print('\n')
        representacion2(fila,columna,minilista,EDIFICIO,pisoelegido)



    elif accion==3:
        validacionretiro(EDIFICIO)


        
    else:
        print('Esa accion no existe')
        
    Cargaredificio=EDIFICIO
    Cargarusuarios=USUARIOS
    with open ('BACKUPEDIFICIO.json','w') as file:
        json.dump(Cargaredificio,file)
    with open ('BACKUPUSURIOS.json','w') as file:
        json.dump(Cargarusuarios,file)


    numest,numprof,numadm,numvis=txt1(EDIFICIO)
    REPORTE1=open("Cantidad de vehículos estacionados según el tipo de usuario.txt","w")
    REPORTE1.write('Numero de vehiculos estacionados de estudiantes:'+str(numest)+'\n')
    REPORTE1.write('Numero de vehiculos estacionados de profesores:'+str(numprof)+'\n')
    REPORTE1.write('Numero de vehiculos estacionados de administrativos:'+str(numadm)+'\n')
    REPORTE1.write('Numero de vehiculos estacionados de visitantes:'+str(numvis)+'\n')
    REPORTE1.close()

    numaut,numele,nummoto,numdis=txt2(EDIFICIO)
    REPORTE2=open("Cantidad de vehículos estacionados según el tipo de vehículo.txt","w")
    REPORTE2.write('Numero de automóviles:'+str(numaut)+'\n')
    REPORTE2.write('Numero de automóvil eléctricos:'+str(numele)+'\n')
    REPORTE2.write('Numero de motocicletas:'+str(nummoto)+'\n')
    REPORTE2.write('Numero de discapacitados:'+str(numdis)+'\n')
    REPORTE2.close()

    contpor,contpiso1,contpiso2,contpiso3,contpiso4,contpiso5,contpiso6=txt3(EDIFICIO)
    porto=(contpor*100)/550
    por1=(contpiso1*100)/100
    por2=(contpiso2*100)/100
    por3=(contpiso3*100)/100
    por4=(contpiso4*100)/100
    por5=(contpiso5*100)/100
    por6=(contpiso6*100)/50
    REPORTE3=open("Porcentajes.txt","w")
    REPORTE3.write('Porcentaje ocupación global:'+str(porto)+'\n')
    REPORTE3.write('Porcentaje ocupación piso 1:'+str(por1)+'%\n')
    REPORTE3.write('Porcentaje ocupación piso 2:'+str(por2)+'%\n')
    REPORTE3.write('Porcentaje ocupación piso 3:'+str(por3)+'%\n')
    REPORTE3.write('Porcentaje ocupación piso 4:'+str(por4)+'%\n')
    REPORTE3.write('Porcentaje ocupación piso 5:'+str(por5)+'%\n')
    REPORTE3.write('Porcentaje ocupación piso 6:'+str(por6)+'%\n')
    REPORTE3.close()



    
    APAGADO=int(input('Para apagar el programa ingrese -1, si desea continuar ingrese cualquier tecla diferente a -1. '))


