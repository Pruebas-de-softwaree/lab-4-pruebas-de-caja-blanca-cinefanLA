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

"""
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

if __name__ == "__main__":
    # ---- DECISION COVERAGE test ----
    
    # DC-01: grades == None → True
    students = [
        {'name': 'N', 'grades': None}
    ]
    result = process_grades(students)
    print("\nFinal processing result (DC-01):")
    print(result)

    # DC-02: average > 70 → True
    students = [
        {'name': 'Ana', 'grades': [80, 90, 85]}
    ]
    result = process_grades(students)
    print("\nFinal processing result (DC-02):")
    print(result)

    # DC-03: frontera 70 (debería aprobar, pero sale "in recovery")
    students = [
        {'name': 'Luis', 'grades': [70, 70, 70]}
    ]
    result = process_grades(students)
    print("\nFinal processing result (DC-03):")
    print(result)

    # DC-04: average < 50 → else
    students = [
        {'name': 'Marta', 'grades': [40, 45, 50]}
    ]
    result = process_grades(students)
    print("\nFinal processing result (DC-04):")
    print(result)

    # DC-05: counter > 0 (1 válido + 1 sin notas)
    students = [
        {'name': 'A', 'grades': [60, 60, 60]},
        {'name': 'B', 'grades': None}
    ]
    result = process_grades(students)
    print("\nFinal processing result (DC-05):")
    print(result)


"""
Prueba: Decision Coverage (DC-01 a DC-05)

Entradas y Resultados Esperados vs Obtenidos:

DC-01:
  Entrada: [{'name': 'N', 'grades': None}]
  Esperado: Mensaje "Student N has no grades", resultado {'passed': [], 'failed': [], 'overall_average': 0.0}
  Obtenido: Igual (cumple).

DC-02:
  Entrada: Ana con [80, 90, 85]
  Esperado: {'passed': ['Ana'], 'failed': [], 'overall_average': 85.0}
  Obtenido: {'passed': ['Ana'], 'failed': [], 'overall_average': 0.0}
  Observación: promedio general falla (counter comentado).

DC-03:
  Entrada: Luis con [70, 70, 70]
  Esperado: ≥70 aprobado → {'passed': ['Luis'], 'failed': [], 'overall_average': 70.0}
  Obtenido: imprime "Luis is in recovery", {'passed': [], 'failed': [], 'overall_average': 0.0}
  Observación: condición mal implementada (>70 en lugar de ≥70).

DC-04:
  Entrada: Marta con [40, 45, 50]
  Esperado: {'passed': [], 'failed': ['Marta'], 'overall_average': 45.0}
  Obtenido: {'passed': [], 'failed': ['Marta'], 'overall_average': 0.0}
  Observación: promedio general falla otra vez.

DC-05:
  Entrada: A con [60, 60, 60], B con None
  Esperado: {'passed': [], 'failed': [], 'overall_average': 60.0}
  Obtenido: {'passed': [], 'failed': [], 'overall_average': 0.0}
  Observación: promedio general mal calculado.

"""
