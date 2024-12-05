import tkinter as tk
from tkinter import messagebox

import solvers

def format_matrix(matrix):
    """
    Formatea una matriz (lista de listas) para mostrarla en la interfaz de manera legible.
    """
    return "\n".join(["\t".join([f"{value:.2f}" for value in row]) for row in matrix])

def create_matrix_window(n):
    from method_selection import create_method_window
    """
    Ventana para ingresar la matriz A y el vector B con soporte de desplazamiento.
    """
    matrix_window = tk.Tk()
    matrix_window.title(f"Ingresar Matriz ({n} incógnitas)")

    # Configuración de tamaño y diseño de la ventana
    window_width = 800
    window_height = 600
    screen_width = matrix_window.winfo_screenwidth()
    screen_height = matrix_window.winfo_screenheight()
    x_cord = int((screen_width / 2) - (window_width / 2))
    y_cord = int((screen_height / 2) - (window_height / 2))
    matrix_window.geometry(f"{window_width}x{window_height}+{x_cord}+{y_cord}")
    matrix_window.resizable(True, True)

    # Marco principal con scrollbar
    main_frame = tk.Frame(matrix_window)
    main_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(main_frame, bg="#ADD8E6")
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#ADD8E6")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Contenido de la ventana
    tk.Label(
        scrollable_frame,
        text="Ingrese los coeficientes de la Matriz A y el vector B:",
        font=("Comic Sans MS", 14, "bold"),
        bg="#ADD8E6",
        fg="#003B5C"
    ).pack(pady=10)

    # Ejemplo explicativo
    example_text = (
        "Ejemplo:\n"
        "Si tiene el sistema de ecuaciones:\n"
        "  2x₁ + 3x₂ + x₃ = 10\n"
        "  4x₁ + 1x₂ + 2x₃ = 8\n"
        "  3x₁ + 5x₂ + 6x₃ = 15\n\n"
        "Debe ingresar la matriz A como:\n"
        "  [2, 3, 1]\n"
        "  [4, 1, 2]\n"
        "  [3, 5, 6]\n\n"
        "Y el vector B como:\n"
        "  [10, 8, 15]"
    )
    tk.Label(
        scrollable_frame,
        text=example_text,
        font=("Comic Sans MS", 10),
        bg="#E0FFFF",
        fg="#003B5C",
        justify="center",
        relief="groove",
        bd=5,
        padx=10,
        pady=10
    ).pack()

    # Campos de entrada para la matriz A
    matrix_frame = tk.Frame(scrollable_frame, bg="#ADD8E6")
    matrix_frame.pack(pady=20)
    matrix_entries_a = []
    for i in range(n):
        row_entries = []
        for j in range(n):
            entry = tk.Entry(
                matrix_frame,
                width=5,
                font=("Comic Sans MS", 12),
                bd=3,
                relief="sunken",
                bg="#E0FFFF",
                fg="#003B5C",
                justify="center"
            )
            entry.grid(row=i, column=j, padx=10, pady=10)
            row_entries.append(entry)
        matrix_entries_a.append(row_entries)

    # Vector B
    tk.Label(
        scrollable_frame,
        text="Vector B:",
        font=("Comic Sans MS", 12, "bold"),
        bg="#ADD8E6",
        fg="#003B5C"
    ).pack(pady=10)
    vector_frame = tk.Frame(scrollable_frame, bg="#ADD8E6")
    vector_frame.pack()
    matrix_entries_b = []
    for i in range(n):
        entry = tk.Entry(
            vector_frame,
            width=5,
            font=("Comic Sans MS", 12),
            bd=3,
            relief="sunken",
            bg="#E0FFFF",
            fg="#003B5C",
            justify="center"
        )
        entry.grid(row=i, column=0, padx=10, pady=5)
        matrix_entries_b.append(entry)

    # Mensaje de error
    error_label = tk.Label(
        scrollable_frame,
        text="",
        font=("Comic Sans MS", 12),
        fg="red",
        bg="#ADD8E6"
    )
    error_label.pack(pady=5)

    # Botón Confirmar
    def next_window():
        try:
            if any(entry.get() == "" for row in matrix_entries_a for entry in row) or \
               any(entry.get() == "" for entry in matrix_entries_b):
                error_label.config(text="Por favor complete todos los campos.")
                return

            A = [[float(entry.get()) for entry in row] for row in matrix_entries_a]
            B = [float(entry.get()) for entry in matrix_entries_b]

            matrix_window.destroy()
            create_method_window(A, B)
        except ValueError:
            error_label.config(text="Por favor ingrese valores numéricos válidos.")

    tk.Button(
        scrollable_frame,
        text="Confirmar",
        font=("Comic Sans MS", 14, "bold"),
        bg="#66B3FF",
        fg="#FFF",
        command=next_window,
        relief="raised",
        bd=5,
        padx=10,
        pady=5
    ).pack(pady=20)

    matrix_window.mainloop()
