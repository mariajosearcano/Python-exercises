import os 
import time 
#
# Gestión de clientes mediante archivos, 
# permite Adicion, actualización, bus queda, eliminación y listado de clientes
# 
nombreArchivo = '/Users/Redes Cableadas/Desktop/clientes.dat' 
nombreEmpresa = 'EMPRESA XYZ'

def cls():
    try: 
        if os.name.upper()=='NT':
            os.system('cls') 
        else: 
            os.system('clear') 
    except Exception: 
        pass 
    
def esperar(tiempo=3,msg=None):
    try: 
        if msg!=None: 
            msg = f'{msg}. Por favor espere {tiempo} segundos para continuar' 
            print(msg) 
            time.sleep(tiempo) 
    except Exception: 
        pass 


def shocli(): 
    try: 
        sal = '\nError al listar los datos' 
        cls() 
        with open(nombreArchivo,'r') as f: 
            print('{0:^123}\n'.format(nombreEmpresa)) 
            print('{0:^123}\n'.format('Reporte de clientes')) 
            print('{0:<10} {1:>11} {2:<50} {3:>12} {4:<40}'.format('Tip. Ide.','Num. Ide.','Apellidos y Nombres','Teléfono','Dirección')) 
            for linea in f: 
                datos = linea.replace('\n','').split(',')
                
                print(f'{datos[0]:^10} {datos[1]:>11} {datos[2]:<50} {datos[3]:>12} {datos[4]:<40}') 
            sal = '\nListado finalizado' 
    except Exception: 
        pass 
    return sal 

def addcli(): 
    try: 
        cls() 
        sal = '\nNo se pudieron guardar los datos' 
        with open(nombreArchivo,'a') as f: 
            tid=input("Por favor digite el tipo de Identificación : ") 
            nid=input("Por favor digite el número de identificación : ") 
            nom=input("Por favor digite el nombre : ") 
            tel=input("Por favor digite el número de teléfono : ") 
            dcn=input("Por favor digite la dirección : ") 
            print(f'{tid},{nid},{nom},{tel},{dcn}',file=f) 
            sal = '\nDatos guardados exitosamente' 
    except Exception: 
        pass 
    return sal 
    
def seacli(): 
    try: 
        cls() 
        sw = False 
        sal = '\nNo se encontró un registro que coincida con la información buscada.' 
        with open(nombreArchivo,'r') as f: 
            bus = input("Digite el valor a buscar : ") 
            tip = input("Buscará por N)ombre, I)dentificación o T)eléfono : ").lower() 
            for pos,linea in enumerate(f): 
                datos = linea.replace('\n','').split(',') 
                if (tip=="n" and datos[2].upper()==bus.upper()) or (tip=="i" and datos[1]==bus) or (tip=="t" and datos[3]==bus): 
                    sw=True 
                    break 
        if sw: 
           sal = f'\nSe encontró el registro buscado en la línea {pos} del archivo.' 
    except Exception: 
        pass
    return sal 

def fincli(bus): 
    try: 
        sw = False 
        pos = -10 
        with open(nombreArchivo,'r') as f: 
            for pos,linea in enumerate(f): 
                datos = linea.replace('\n','').split(',') 
                if datos[1]==bus: 
                    sw=True 
                    break 
    except Exception: 
        pass 
    return (sw,pos) 
 # 
 # Se implementa borrado físico.
 # 

def delcli(): 
    try: 
        sal = '\nError al eliminar los datos.' 
        bus = input("Digite el número de documento : ") 
        (sw,enc) = fincli(bus) 
        if not sw: 
            sal = "\nNo se encontró ningun registro que coincida con el criterio de búsqueda" 
        else: 
            with open(nombreArchivo,'r') as f: 
                datos = f.readlines() 
                linea = datos[enc].replace('\n','').split(',') 
                print('*** DATOS DEL CLIENTE A ELIMINAR ***') 
                print(f"\tTipo de Identificación : {linea[0]}") 
                print(f"\tNúmero de identificación : {linea[1]}") 
                print(f"\tNombre : {linea[2]}") 
                print(f"\tNúmero de teléfono : {linea[3]}") 
                print(f"\tDirección : {linea[4]}") 
                op = input('Confirma la eliminación del cliente [S/N] (NOTA: Este proceso es irreversible) : ').lower() 
                if op=='s': 
                    datos.pop(enc) 
                    with open(nombreArchivo,'w') as f: 
                        f.writelines(datos) 
                        sal = '\nDatos eliminados exitosamente.' 
                else: 
                       sal = '\nOperación cancelada'

    except Exception: 
        pass 
        return sal 

def updcli(): 
    try: 
        sal = '\nError al actualizar los datos.' 
        bus = input("Digite el número de documento : ") 
        (sw,enc) = fincli(bus) 
        if not sw: 
            sal = "\nNo se encontró ningun registro que coincida con el criterio de búsqueda" 
        else: 
            tid=input("Por favor digite el tipo de Identificación : ") 
            nid=input("Por favor digite el número de identificación : ") 
            nom=input("Por favor digite el nombre : ") 
            tel=input("Por favor digite el número de teléfono : ") 
            dcn=input("Por favor digite la dirección : ") 
            with open(nombreArchivo,'r') as f: 
                datos = f.readlines() 
                datos[enc] = f'{tid},{nid},{nom},{tel},{dcn}\n' 
                with open(nombreArchivo,'w') as f: 
                    f.writelines(datos) 
                    sal = '\nDatos guardados exitosamente.' 
    except Exception: 
        pass 
        return sal 
def main(): 
    op = "1" 
    while op!="S": 
        os.system("cls") 
        print("\tOPCIONES DISPONIBLES\n") 
        print("\t1. Adicionar Cliente") 
        print("\t2. Buscar Cliente") 
        print("\t3. Borrar Cliente") 
        print("\t4. Actualizar Cliente") 
        print("\t5. Listar Clientes") 
        print("\tS. Salir") 
        op = input("\n\tSeleccione su opción : ").upper() 
        if op=="1": 
            esperar(msg=addcli()) 
        elif op=="2": 
            esperar(msg=seacli()) 
        elif op=="3":
            esperar(msg=delcli()) 
        elif op=="4": 
            esperar(msg=updcli()) 
        elif op=="5": 
            esperar(4,shocli()) 
        elif op!="S": 
            esperar(2,"\n\tSeleccione una opción valida") 
        else: 
            print("\tHasta la vista ...") 
main()

