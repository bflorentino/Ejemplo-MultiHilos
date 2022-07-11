from threading import Thread

# Calcular sueldo de una persona con deducciones de la ley aplicando multihilos
def calcularSueldoNeto(salario, nombre):
    
    salarioDeducido_AFP_ARS = salario - (salario*0.028) - (salario*0.0304)
    salarioAnual = salarioDeducido_AFP_ARS * 12
    salarioNeto = 0
    
    # Caso en que el salario anual del empleado sea igual o menor a 416,220.00
    if salarioAnual  <= 416220.00:
        salarioNeto = salarioDeducido_AFP_ARS
    
    elif salarioAnual > 416220.00 and salarioAnual <= 624329.00:
        excedenteSueldo = (salarioAnual / 12) - (416220.01/12)
        ISR = excedenteSueldo * 0.15
        salarioNeto = round(salarioDeducido_AFP_ARS - ISR, 2)
    
        # Caso en que el salario anual del empleado sea entre 624329.01 y 867123.00.00
    elif salarioAnual > 624329.00 and salarioAnual <= 867123.00:
        excedenteSueldo = (salarioAnual / 12) - (624329.01/12)
        ISR = (excedenteSueldo * 0.20) + (31216/12)
        salarioNeto = round(salarioDeducido_AFP_ARS -  ISR, 2)

    # Caso en que el salario anual del empleado sea mayor o igual a 867123.01
    elif salarioAnual >  867123.00:
        excedenteSueldo = (salarioAnual / 12) - (867123.01/12)
        ISR = (excedenteSueldo * 0.25) + (79776 / 12)
        salarioNeto = round(salarioDeducido_AFP_ARS - ISR, 2)

    print(f"El salario neto del empleado {nombre} es {salarioNeto}")


# Lista de tuplas de empleados adjunto con sus salarios
empleados = []
empleados.extend([(100000, "Bryan"), 
                (50000, "José"), 
                (75000, "Anyeida"), 
                (32000, "Magda"), 
                (540000, "Santiago")])

# Creacion de hilos
hilos = []
for empleado in empleados:
    hilos.append(Thread(target = calcularSueldoNeto, args=(empleado[0], empleado[1])))

# Aqui los hilos empiezan a correr
for hilo in hilos:
    hilo.start()

# Aqui esperamos a que los hilos terminen de ejecutarse
for hilo in hilos:
    hilo.join()