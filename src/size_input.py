import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import requests
from matrix_input import create_matrix_window  # Importa la función para abrir la ventana de matriz

def create_size_window():
    size_window = tk.Tk()
    size_window.title("Tamaño del Sistema de Ecuaciones")
    
    # Dimensiones de la ventana
    window_width = 1000
    window_height = 600
    screen_width = size_window.winfo_screenwidth()
    screen_height = size_window.winfo_screenheight()
    x_cord = int((screen_width / 2) - (window_width / 2))
    y_cord = int((screen_height / 2) - (window_height / 2))
    size_window.geometry(f"{window_width}x{window_height}+{x_cord}+{y_cord}")
    size_window.resizable(False, False)
    size_window.config(bg="#ADD8E6")

    # Dividir en dos marcos
    left_frame = tk.Frame(size_window, bg="#ADD8E6", width=window_width // 2, height=window_height)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    right_frame = tk.Frame(size_window, bg="#ADD8E6", width=window_width // 2, height=window_height)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)

    # Crear un nuevo frame dentro de left_frame para centrar el contenido
    center_frame = tk.Frame(left_frame, bg="#ADD8E6")
    center_frame.pack(side=tk.TOP, fill=tk.Y, expand=True)

    # Lado izquierdo: Entrada y botones
    tk.Label(
        center_frame, 
        text="Ingrese el número de incógnitas del sistema de ecuaciones:", 
        font=("Comic Sans MS", 12, "bold"), 
        bg="#ADD8E6", 
        fg="#003B5C"
    ).grid(row=0, column=0, pady=20, padx=20)

    # Definir example_text solo una vez y luego usarlo en el widget Label
    example_text = (
        "Ejemplo:\n"
        "Si tiene:\n"
        "  x₁ + x₂ + x₃ = 0\n"
        "  x₄ + x₅ + x₆ = 0\n"
        "  x₇ + x₈ + x₉ = 0\n"
        "Este es un sistema de ecuaciones 3x3, por lo tanto tiene 3 incógnitas."
    )

    # Ejemplo explicativo
    example_frame = tk.Frame(center_frame, bg="#ADD8E6")
    example_frame.grid(row=4, column=0, pady=20, padx=20)
    
    tk.Label(
        example_frame, 
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

    entry_size = tk.Entry(
        center_frame, 
        font=("Comic Sans MS", 12), 
        bd=3, 
        relief="sunken", 
        bg="#E0FFFF", 
        fg="#003B5C", 
        justify="center"
    )
    entry_size.grid(row=1, column=0, pady=10, padx=20)

    # Mensaje de error con estilo
    # Mensaje de error con estilo
    error_label = tk.Label(
    center_frame, 
    text="", 
    font=("Comic Sans MS", 11), 
    bg="#ADD8E6",  # Fondo que se asemeja al color de la ventana
    fg="#FF0000",  # Texto rojo
    justify="center",
    relief="flat",  # Sin borde de ranura
    padx=10,
    pady=5
)
    error_label.grid(row=2, column=0, pady=10, padx=20)


    def next_window():
        size = entry_size.get()
        if size.isdigit():
            size = int(size)
            if size > 1:
                size_window.destroy()  # Cierra la ventana de tamaño
                create_matrix_window(size)  # Llama a la ventana de matriz con el tamaño seleccionado
            else:
                error_label.config(text="El número debe ser mayor a 1.")
        else:
            error_label.config(text="Por favor ingrese un número válido.")

    confirm_button = tk.Button(
        center_frame, 
        text="Confirmar", 
        font=("Comic Sans MS", 14, "bold"), 
        bg="#66B3FF", 
        fg="#FFF", 
        command=next_window, 
        relief="raised", 
        bd=5, 
        padx=20, 
        pady=10
    )
    confirm_button.grid(row=3, column=0, pady=30, padx=20)

    # Lado derecho: Imagen decorativa
    try:
        image_url = "https://img.freepik.com/premium-vector/calculator-logo_10250-2601.jpg"
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        image = Image.open(image_data)

        # Redimensionar la imagen para que se ajuste al marco
        image = image.resize((window_width // 2, window_height), Image.Resampling.LANCZOS)
        calculator_image = ImageTk.PhotoImage(image)

        tk.Label(right_frame, image=calculator_image, bg="#ADD8E6").pack(fill=tk.BOTH, expand=False)
        size_window.calculator_image = calculator_image  # Mantener referencia

    except requests.exceptions.RequestException:
        tk.Label(
            right_frame,
            text="No se pudo cargar la imagen.",
            font=("Comic Sans MS", 12),
            fg="red",
            bg="#ADD8E6"
        ).pack(pady=50)

    size_window.mainloop()
