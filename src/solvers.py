import numpy as np

def gauss_elimination(A, B):
    """
    sistema de ecuaciones lineales usando el método de eliminación de Gauss.
    """
    try:
        n = len(A)
        A = np.array(A, float)
        B = np.array(B, float)
        steps = []  # Lista para guardar los pasos

        # Eliminación 
        for k in range(n - 1):
            if A[k, k] == 0:
                raise ValueError(f"El sistema no tiene solución única: pivote nulo en la fila {k + 1}.")

            steps.append({
                "paso": f"Inicio del paso {k + 1}",
                "descripcion": f"Eliminación para hacer ceros debajo del pivote en la columna {k + 1}.",
                "A": A.tolist(),
                "B": B.tolist()
            })

            for i in range(k + 1, n):
                factor = A[i, k] / A[k, k]
                A[i, k:] -= factor * A[k, k:]
                B[i] -= factor * B[k]

                # Guardar el estado después de modificar la fila i
                steps.append({
                    "paso": f"Modificación de la fila {i + 1}",
                    "descripcion": f"Se eliminó el coeficiente en la columna {k + 1} de la fila {i + 1} usando un factor de {factor:.2f}.",
                    "A": A.tolist(),
                    "B": B.tolist()
                })

        # Sustitución
        X = np.zeros(n)
        for i in range(n - 1, -1, -1):
            if A[i, i] == 0:
                raise ValueError(f"El sistema no tiene solución única: pivote nulo en la fila {i + 1}.")

            # Cálculo de la incógnita x[i]
            sumatoria = np.dot(A[i, i + 1:], X[i + 1:])
            X[i] = (B[i] - sumatoria) / A[i, i]

            # Calculo de x[i] 
            detalles_calculo = f"x[{i + 1}] = ({B[i]} - (" \
                               + " + ".join([f"{A[i, j]:.2f} * {X[j]:.2f}" for j in range(i + 1, n)]) \
                               + f")) / {A[i, i]} = ({B[i]:.2f} - ({sumatoria:.2f})) / {A[i, i]:.2f} = {X[i]:.2f}"

            steps.append({
                "paso": f"Cálculo de la variable x[{i + 1}]",
                "descripcion": "Cálculo de la incógnita.",
                "detalles_calculo": detalles_calculo
            })

        # Resultado 
        steps.append({
    "paso": "Solución final",
    "descripcion": "Se ha obtenido la solución del sistema de ecuaciones.",
    "A": A.tolist(),  # Matriz A final
    "B": B.tolist(),  # Vector B final
    "X": X.tolist()   # Solución final
        })

        return steps

    except Exception as e:
        raise ValueError(f"Error en la eliminación de Gauss: {str(e)}")







def gauss_jordan(A, B):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Jordan
    """
    try:
        n = len(A)
        A = np.array(A, float)
        B = np.array(B, float)
        steps = []  # Lista para guardar los pasos

        for i in range(n):
            if A[i, i] == 0:
                raise ValueError("El sistema no tiene solución única (pivote nulo).")

            steps.append({
                "paso": f"Paso {i + 1}",
                "descripcion": f"Transformando la fila {i + 1} para hacer el pivote 1.",
                "A": A.copy(),
                "B": B.copy()
            })

            # Ajustar la fila actual
            factor = A[i, i]
            A[i] = A[i] / factor
            B[i] = B[i] / factor

            # Guardar 
            steps.append({
                "paso": f"Paso {i + 1}",
                "descripcion": f"Fila {i + 1} transformada (pivote = 1).",
                "A": A.copy(),
                "B": B.copy()
            })

            # Hacer ceros en la columna i para todas las demás filas
            for j in range(n):
                if j != i:
                    factor = A[j, i]
                    A[j] -= factor * A[i]
                    B[j] -= factor * B[i]
                    steps.append({
                        "paso": f"Paso {i + 1}",
                        "descripcion": f"Eliminando el elemento en la fila {j + 1}, columna {i + 1}.",
                        "A": A.copy(),
                        "B": B.copy()
                    })

        # solución final
        steps.append({
            "paso": "Solución final",
            "descripcion": "El sistema ha sido resuelto. Aquí está la solución.",
            "A": A.copy(),
            "B": B.tolist()
        })

        return steps

    except Exception as e:
        raise ValueError(f"Error en Gauss-Jordan: {str(e)}")