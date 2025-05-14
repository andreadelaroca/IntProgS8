# registrar la asistencia de estudiantes a clases 
# en varias secciones durante una semana

secciones = 3 #numero de secciones
estudiantes_por_seccion = 6 #estudiantes por seccion
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"] #dias de la semana

asistencias_totales = 0 #contador total de asistencias

for seccion in range(1, secciones + 1): #bucle para cada seccion
    print(f"\nSección: {seccion}")
    asistencias_seccion = 0 #contador de asistencias por seccion
    
    for estudiante in range(1, estudiantes_por_seccion + 1): #bucle para cada estudiante
        asistencias_estudiante = 0 #contador de asistencias por estudiante
        
        for dia in dias: #bucle para cada dia
            asistencia = input(f"¿El estudiante {estudiante} asistió el día {dia}? (S/N):").strip().upper()
            if asistencia == "S":
                asistencias_estudiante += 1
                asistencias_seccion += 1
                asistencias_totales += 1
            else:
                print(f"El estudiante {estudiante} no asistió el día {dia}.")
        print(f"El estudiante {estudiante} tuvo {asistencias_estudiante} asistencias esta semana.")
    print(f"\nTotal de asistencias en la sección {seccion}: {asistencias_seccion}")
print(f"\nTotal general de asistencias: ", asistencias_totales)
