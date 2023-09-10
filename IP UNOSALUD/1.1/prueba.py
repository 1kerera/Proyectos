import socket
import tkinter as tk

def obtener_ip_y_hostname():
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    return f"Hostname: {hostname}\nDirección IP: {direccion_ip}"

def mostrar_info():
    info_label.config(text=obtener_ip_y_hostname())

# Crear una ventana
ventana = tk.Tk()
ventana.title("IP y Hostname")

# Crear una etiqueta para mostrar la información
info_label = tk.Label(ventana, text="", padx=10, pady=10)
info_label.pack()

# Botón para actualizar la información
actualizar_button = tk.Button(ventana, text="Actualizar", command=mostrar_info)
actualizar_button.pack()

# Mostrar la información inicial
mostrar_info()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
