def process_grades(students):
    passed = []
    failed = []
    overall_average = 0
    total_grades = 0
    counter = 0

    for student in students:
        name = student['name']
        grades = student['grades']
        
        if grades == None:  
            print(f"Student {name} has no grades")
            continue
        
        average = sum(grades) / len(grades)
        total_grades += average
        # counter += 1

        if average > 70:  
            passed.append(name)
        elif average >= 50:
            print(f"{name} is in recovery")
        else:
            failed.append(name)
    
    if counter > 0:  
        overall_average = total_grades / counter
    
    return {
        'passed': passed,
        'failed': failed,
        'overall_average': round(overall_average, 2)
    }


if __name__ == "__main__":
    students = [
        {'name': 'Ana', 'grades': [80, 90, 85]},
        {'name': 'Luis', 'grades': [70, 70, 70]},
        {'name': 'Jorge', 'grades': []},
        {'name': 'Marta', 'grades': [40, 45, 50]}
    ]

    result = process_grades(students)
    print("\nFinal processing result:")
    print(result)
    
"""

Prueba: SC-01 (Statement Coverage)

Entradas:
  Ana [80, 90, 85]
  Luis [70, 70, 70]
  Jorge []
  Marta [40, 45, 50]

Resultado esperado (según RF):
  {'passed': ['Ana','Luis'], 'failed': ['Marta'], 'overall_average': 66.67}

Resultado obtenido (código actual):
  Consola:
    Luis is in recovery
    Traceback...
    ZeroDivisionError: division by zero

Observaciones:
- Ana fue aprobado correctamente.
- Luis (70) debería aprobar pero fue puesto en "recovery".
- Jorge con lista vacía generó ZeroDivisionError.
- Marta fue identificado como reprobado, pero no se alcanzó a guardar porque el programa se detuvo.
- El promedio general no se calculó porque counter está comentado.

"""