from tkinter import messagebox
from matrix_input import format_matrix
import solvers
import tkinter as tk

def create_method_window(A, B):
    """
    Ventana para seleccionar el método de resolución del sistema.
    """
    method_window = tk.Tk()
    method_window.title("Seleccionar Método de Resolución")
    window_width = 500
    window_height = 200
    screen_width = method_window.winfo_screenwidth()
    screen_height = method_window.winfo_screenheight()
    x_cord = int((screen_width / 2) - (window_width / 2))
    y_cord = int((screen_height / 2) - (window_height / 2))
    method_window.geometry(f"{window_width}x{window_height}+{x_cord}+{y_cord}")
    method_window.resizable(False, False)
    method_window.config(bg="#ADD8E6")

    # Crear un título centrado
    title = tk.Label(method_window, 
        text="Ingrese el método por el cual va a resolver el sistema de ecuaciones:",
        font=("Comic Sans MS", 10, "bold"),
        bg="#ADD8E6",
        fg="#003B5C"
    )
    title.grid(row=0, column=0, columnspan=3, pady=30, padx=20, sticky="nsew")

    # Configurar filas y columnas
    method_window.grid_rowconfigure(1, weight=1)
    method_window.grid_rowconfigure(2, weight=1)
    method_window.grid_columnconfigure(0, weight=1)  # Espacio izquierdo
    method_window.grid_columnconfigure(1, weight=1)  # Centrado
    method_window.grid_columnconfigure(2, weight=1)  # Espacio derecho

    def solve_gauss():
        try:
            steps = solvers.gauss_elimination(A, B)
            show_steps("Método de Gauss", steps)
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al resolver con Gauss: {str(e)}")

    def solve_gauss_jordan():
        try:
            steps = solvers.gauss_jordan(A, B)
            show_steps("Método de Gauss-Jordan", steps)
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al resolver con Gauss-Jordan: {str(e)}")

    # Botones centrados
    tk.Button(method_window, text="Método de Gauss", font=("Comic Sans MS", 10), bg="#66B3FF", fg="#FFF", 
              command=solve_gauss, relief="raised", bd=3, width=15, height=3).grid(row=1, column=1, pady=5, sticky="nsew")
    tk.Button(method_window, text="Método de Gauss-Jordan", font=("Comic Sans MS", 10), bg="#66B3FF", fg="#FFF", 
              command=solve_gauss_jordan, relief="raised", bd=3, width=15, height=3).grid(row=2, column=1, pady=5, sticky="nsew")

    method_window.mainloop()



def show_steps(method, steps):
    """
    Muestra el paso a paso de la solución en una ventana nueva con desplazamiento.
    """
    steps_window = tk.Toplevel()
    steps_window.title(f"Paso a Paso - {method}")
    steps_window.config(bg="#ADD8E6")

    canvas = tk.Canvas(steps_window, bg="#ADD8E6")
    scrollbar = tk.Scrollbar(steps_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Contenedor para los pasos
    frame = tk.Frame(canvas, bg="#ADD8E6")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    for step in steps:
        step_frame = tk.Frame(frame, bg="#ADD8E6", bd=3, relief="groove", padx=15, pady=15)
        step_frame.pack(pady=20, fill="both", expand=True)

        # Título del paso
        tk.Label(step_frame, text=step["paso"], font=("Comic Sans MS", 14, "bold"), bg="#ADD8E6", fg="#003B5C").pack(pady=5)

        # Descripción del paso
        tk.Label(step_frame, text=step["descripcion"], font=("Comic Sans MS", 12), bg="#ADD8E6", fg="#4A4A4A").pack(pady=5)

        # Mostrar los detalles del cálculo si están presentes
        if "detalles_calculo" in step:
            tk.Label(step_frame, text=step["detalles_calculo"], font=("Comic Sans MS", 12), bg="#E0FFFF", relief="sunken", padx=10, pady=10, fg="#003B5C").pack(pady=5)

        # Mostrar matrices A y B si están presentes
        if "A" in step:
            tk.Label(step_frame, text="Matriz A:", font=("Comic Sans MS", 12, "bold"), bg="#ADD8E6", fg="#003B5C").pack(pady=5)
            tk.Label(step_frame, text=format_matrix(step["A"]), font=("Comic Sans MS", 12), bg="#E0FFFF", relief="sunken", padx=10, pady=10).pack(pady=5)

        if "B" in step:
            tk.Label(step_frame, text="Matriz B:", font=("Comic Sans MS", 12, "bold"), bg="#ADD8E6", fg="#003B5C").pack(pady=5)
            tk.Label(step_frame, text=format_matrix([step["B"]]) if isinstance(step["B"], list) else step["B"], font=("Comic Sans MS", 12), bg="#E0FFFF", relief="sunken", padx=10, pady=10).pack(pady=5)

        # Mostrar solución final si está presente
        if "X" in step:
            tk.Label(step_frame, text="Solución final (Vector X):", font=("Comic Sans MS", 12, "bold"), bg="#ADD8E6", fg="#003B5C").pack(pady=5)
            tk.Label(step_frame, text=step["X"], font=("Comic Sans MS", 12), bg="#E0FFFF", relief="sunken", padx=10, pady=10).pack(pady=5)

    # Ajustar el área de desplazamiento
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Botón para cerrar la ventana
    tk.Button(frame, text="Cerrar", font=("Comic Sans MS", 12, "bold"), bg="#66B3FF", fg="#FFF", command=steps_window.destroy, relief="raised", bd=5, padx=10, pady=5).pack(pady=20)

    steps_window.mainloop()
