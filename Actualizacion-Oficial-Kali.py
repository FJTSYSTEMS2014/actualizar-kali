import os

os.system('clear')

# Mensaje de bienvenida
print("----------------------------------------------------------\n")
print("---         Ing. Franck Tscherig v1.1            \n")

print("Bienvenido al script de actualización de Kali Linux.")
print("Este script te ayudará a actualizar el kernel y el sistema.")
print("Programado en base a la documentacion oficial ")
print("https://www.kali.org/docs/general-use/updating-kali/")

print("                                                          ---\n")
print("----------------------------------------------------------\n")

# Verificación de permisos de sudo
if os.geteuid() != 0:
    print("--- Asegúrate de ejecutar este script con permisos de sudo")
    print("    para que pueda realizar las actualizaciones necesarias")
    exit(1)

# Verificación de la versión actual del kernel
kernel_version = os.uname().release
print(f"Versión actual del kernel: {kernel_version}")
print("---                                                          \n")

# Verificación y actualización del archivo /etc/apt/sources.list
sources_list_path = "/etc/apt/sources.list"
kali_source_line = "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware"

if os.path.exists(sources_list_path):
    with open(sources_list_path, "r") as sources_file:
        sources_list_content = sources_file.read()
        if kali_source_line not in sources_list_content:
            print("El repositorio de Kali no está correctamente configurado.")
            confirmacion = input("¿Deseas agregar la línea al archivo sources.list? (y/n): ")
            if confirmacion.lower() == "y":
                with open(sources_list_path, "a") as sources_file:
                    sources_file.write("\n" + kali_source_line)
                    print("Línea agregada al archivo sources.list.")
            else:
                print("No se realizarán cambios en el archivo sources.list.")
        else:
            print(f"Contenido actual del archivo {sources_list_path}:\n")
            print(sources_list_content)
            
            print("---                                                          \n")

# Actualización del sistema
actualizar_sistema = input("¿Deseas comenzar con la actualización del sistema? (y/n): ")
if actualizar_sistema.lower() == "y":
    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")
    print("Actualización del sistema realizada.")
    print("---                                                          \n")

# Actualización del kernel
actualizar_kernel = input("¿Deseas comenzar con la actualización del kernel? (y/n): ")
if actualizar_kernel.lower() == "y":
    os.system("sudo apt full-upgrade -y")
    print("Actualización del kernel realizada.")
    new_kernel_version = os.uname().release
    print(f"Kernel antiguo: {kernel_version}")
    print(f"Nuevo kernel: {new_kernel_version}")
    print("---                                                          \n")

# Limpieza de paquetes innecesarios

remover_paquetes = input("¿Deseas comenzar con la limpieza de paquetes innecesarios del sistema? (y/n): ")
if remover_paquetes.lower() == "y":
   
    os.system("sudo apt autoremove -y")
    print("Limpieza de paquetes innecesarios del sistema realizada.")
    print("---                                                          \n")
# Reinicio del sistema
reiniciar_sistema = input("¿Deseas reiniciar el sistema ahora? (y/n): ")
if reiniciar_sistema.lower() == "y":
    print("Reiniciando...")
    print("---                                                          \n")
    os.system("sudo reboot")
else:
    print("No se reiniciará el sistema. ¡Adiós!")
    print("---                                                          \n")
