import socket
import tkinter as tk

# Función para mostrar la página de Hostname
def mostrar_hostname_page():
    # Oculta la página inicial
    inicio_frame.pack_forget()
    
    # Muestra la página de Hostname
    hostname_frame.pack(fill=tk.BOTH, expand=True)
    
    # Muestra el hostname
    hostname = socket.gethostname()
    hostname_label.config(text=f"{hostname}")

# Función para mostrar la página de Direcciones IP
def mostrar_ips_page():
    # Oculta la página inicial
    inicio_frame.pack_forget()
    
    # Muestra la página de Direcciones IP
    ips_frame.pack(fill=tk.BOTH, expand=True)
    
    # Muestra las direcciones IP
    ips = obtener_ips_ipv4()
    if ips:
        ips_text = "\n".join(ips)
    else:
        ips_text = "No se encontraron direcciones IPv4."
    ips_label.config(text=f"{ips_text}")

# Función para volver a la página inicial
def volver_a_inicio():
    # Oculta las páginas de Hostname y Direcciones IP
    hostname_frame.pack_forget()
    ips_frame.pack_forget()
    
    # Muestra la página inicial
    inicio_frame.pack(fill=tk.BOTH, expand=True)

def obtener_ips_ipv4():
    ips_ipv4 = []
    hostname = socket.gethostname()
    try:
        # Obtener todas las interfaces de red disponibles
        interfaces = socket.getaddrinfo(hostname, None)
        
        # Filtrar y agregar direcciones IPv4 a la lista
        for info in interfaces:
            if info[0] == socket.AF_INET:  # Corrección aquí
                ips_ipv4.append(info[4][0])
        
        return ips_ipv4
    except Exception as e:
        return [str(e)]

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("IP UNOSALUD")

# Calcular las dimensiones de la ventana y su posición central
ventana_width = 250
ventana_height = 250

screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

x = (screen_width - ventana_width) // 2
y = (screen_height - ventana_height) // 2

# Establecer la geometría de la ventana para centrarla
ventana.geometry(f"{ventana_width}x{ventana_height}+{x}+{y}")

# PAGINA INICIO
inicio_frame = tk.Frame(ventana, bg="#4ea4d9")
inicio_frame.pack(fill=tk.BOTH, expand=True)

ips_button = tk.Button(inicio_frame, text="Mostrar IP", command=mostrar_ips_page, bg="#a8d22f")
ips_button.pack(padx=1,pady=1)

hostname_button = tk.Button(inicio_frame, text="Mostrar Hostname", command=mostrar_hostname_page, bg="#a8d22f")
hostname_button.pack(padx=1,pady=1)


# PAGINA HOSTNAME
hostname_frame = tk.Frame(ventana, bg="#4ea4d9")

volver_a_inicio_hostname_button = tk.Button(hostname_frame, text="<--", command=volver_a_inicio, bg="#a8d22f" )
volver_a_inicio_hostname_button.pack(anchor=tk.NW)

# Etiqueta para mostrar el hostname
hostname_label = tk.Label(hostname_frame, text="", bg="#4ea4d9")
hostname_label.pack(fill="both", expand=True)



# PAGINA IP
ips_frame = tk.Frame(ventana, bg="#4ea4d9")
# Botón para volver a la página inicial desde Direcciones IP
volver_a_inicio_ips_button = tk.Button(ips_frame, text="<--", command=volver_a_inicio, bg="#a8d22f")
volver_a_inicio_ips_button.pack(anchor=tk.NW)
# Etiqueta para mostrar las direcciones IP
ips_label = tk.Label(ips_frame, text="", bg="#4ea4d9")
ips_label.pack(fill="both", expand=True)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
