import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import size_input  # Función para abrir la ventana input_size

# Función para abrir la ventana input_size
def open_size_window(current_window):
    current_window.destroy()  # Cierra la ventana actual
    size_input.create_size_window()  # Llama a la función definida en size_input.py

# Crear la ventana de bienvenida
def create_welcome_window():
    welcome_window = tk.Tk()
    welcome_window.title("Bienvenida a la Calculadora de Ecuaciones")

    # Configurar tamaño fijo
    window_width = 1000
    window_height = 600
    screen_width = welcome_window.winfo_screenwidth()
    screen_height = welcome_window.winfo_screenheight()
    x_cord = int((screen_width / 2) - (window_width / 2))
    y_cord = int((screen_height / 2) - (window_height / 2))
    welcome_window.geometry(f"{window_width}x{window_height}+{x_cord}+{y_cord}")
    welcome_window.resizable(False, False)
    welcome_window.config(bg="#ADD8E6")

    # Crear marco principal
    frame = tk.Frame(welcome_window, bg="#f5f5f5")
    frame.pack(fill=tk.BOTH, expand=False)

    # Lado izquierdo
    left_frame = tk.Frame(frame, bg="#ffffff", width=window_width // 2, height=window_height)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    # Lado derecho
    right_frame = tk.Frame(frame, bg="#ffffff", width=window_width // 2, height=window_height)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)

    # Logo y título en el lado izquierdo
    try:
        logo_url = "https://i.pinimg.com/736x/f4/a5/02/f4a5023b5bff23f40a8364e09b5acd31.jpg"
        response = requests.get(logo_url)
        response.raise_for_status()
        logo_image_data = BytesIO(response.content)
        logo_image = Image.open(logo_image_data)

        # Redimensionar logo
        logo_image = logo_image.resize((150, 150), Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(logo_image)

        tk.Label(left_frame, image=logo, bg="#ffffff").pack(pady=10)
        welcome_window.logo = logo  # Referencia

    except requests.exceptions.RequestException:
        tk.Label(
            left_frame,
            text="No se pudo cargar el logo.",
            font=("Helvetica", 12),
            fg="red",
            bg="#ffffff"
        ).pack(pady=10)

    # Texto de bienvenida
    tk.Label(
        left_frame,
        text="¡Bienvenido a la Calculadora \nde Ecuaciones!",
        font=("Helvetica", 24, "bold"),
        fg="#2c3e50",  # Texto gris oscuro
        bg="#ffffff"
    ).pack(pady=30, padx=20)

    # Botones personalizados
    def create_custom_button(parent, text, command):
        button = tk.Button(
            parent,
            text=text,
            font=("Helvetica", 14, "bold"),
            bg="#66b3ff",  # Azul suave
            fg="#ffffff",  # Texto blanco
            activebackground="#00509e",  # Azul más oscuro al hacer clic
            activeforeground="#ffffff",  # Texto blanco en clic
            relief="flat",
            bd=0,
            highlightthickness=0,
            padx=15,
            pady=5,
            command=command
        )
        button.bind("<Enter>", lambda e: button.configure(bg="#00509e"))  # Hover azul oscuro
        button.bind("<Leave>", lambda e: button.configure(bg="#66b3ff"))  # Regreso al azul suave
        button.pack(pady=10, ipadx=5, ipady=5)
        return button

    # Botón "Comenzar" llama a la función open_size_window
    create_custom_button(left_frame, "Comenzar", lambda: open_size_window(welcome_window))
    # Botón "Salir" cierra la aplicación
    create_custom_button(left_frame, "Salir", welcome_window.destroy)

    # Imagen en el lado derecho
    try:
        calculator_image_url = "https://img.freepik.com/premium-vector/calculator-logo_10250-2601.jpg"
        response = requests.get(calculator_image_url)
        response.raise_for_status()
        calculator_image_data = BytesIO(response.content)
        calculator_image = Image.open(calculator_image_data)

        # Redimensionar imagen
        calculator_image = calculator_image.resize((window_width // 2, window_height), Image.Resampling.LANCZOS)
        calculator_logo = ImageTk.PhotoImage(calculator_image)

        tk.Label(right_frame, image=calculator_logo, bg="#ffffff").pack(fill=tk.BOTH, expand=False)
        welcome_window.calculator_logo = calculator_logo  # Referencia

    except requests.exceptions.RequestException:
        tk.Label(
            right_frame,
            text="No se pudo cargar la imagen de la calculadora.",
            font=("Helvetica", 12),
            fg="red",
            bg="#ffffff"
        ).pack(pady=50)

    welcome_window.mainloop()


def main():
    create_welcome_window()
