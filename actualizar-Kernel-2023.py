import os

# Mensaje de bienvenida
print("-----                                                         \n")
print("Bienvenido al script de actualización de Kernel para Kali Linux.")
print("-----               Ing. Franck Tscherig     V1.3           \n")
print("Este script te ayudará a actualizar tu kernel.(Ctrl+ Z para Suspender)\n")

# Mostrar la versión actual del kernel
current_kernel = os.popen('uname -r').read()
print(f"La versión actual del kernel en tu sistema es: {current_kernel}\n")
print("-----                                                         \n")

# Mensaje sobre paquetes de kernel disponibles
print("A continuación, se muestran los paquetes de kernel disponibles y compatibles con tu sistema:\n")

# Listar los paquetes de kernel disponibles
available_kernels = os.popen('apt search linux-image | grep -E "linux-image-[0-9]+"').read().split('\n')
for i, kernel in enumerate(available_kernels):
    if kernel:
        print(f"{i + 1}. {kernel}")
print("-----                                                         \n")
# Selección del paquete de kernel
while True:
    try:
        selected_option = int(input("\nSelecciona el número del paquete de kernel que deseas instalar: "))
        if 1 <= selected_option <= len(available_kernels):
            break
        else:
            print("Opción no válida. Debes seleccionar un número válido.")
    except ValueError:
        print("Opción no válida. Debes ingresar un número.")

selected_kernel = available_kernels[selected_option - 1].split('/')[0].strip()
print(f"Has seleccionado el paquete: {selected_kernel}\n")
print("-----                                                         \n")
# Confirmación de instalación del paquete de kernel
while True:
    confirmation = input(f"Se configurará el siguiente comando: sudo apt install {selected_kernel}\n¿Es correcto? (Sí/No): ").lower()
    if confirmation == 'si' or confirmation == 'sí':
        break
    elif confirmation == 'no':
        while True:
            try:
                selected_option = int(input("\nSelecciona el número de otro paquete de kernel que deseas instalar: "))
                if 1 <= selected_option <= len(available_kernels):
                    selected_kernel = available_kernels[selected_option - 1].split('/')[0].strip()
                    print(f"Has seleccionado el paquete: {selected_kernel}\n")
                    break
                else:
                    print("Opción no válida. Debes seleccionar un número válido.")
            except ValueError:
                print("Opción no válida. Debes ingresar un número.")
print("-----                                                         \n")
# Actualización del sistema
print("\nAntes de actualizar el kernel, es importante asegurarse de que todo el sistema esté actualizado.")
update_confirmation = input("¿Deseas actualizar el sistema? (Sí/No): ").lower()
if update_confirmation == 'si' or update_confirmation == 'sí':
    os.system('sudo apt update')
    print("\nSe ha actualizado el sistema.\n")
print("-----                                                         \n")
# Instalación del nuevo kernel
print(f"Ahora procederemos a instalar el paquete de kernel: {selected_kernel}")
os.system(f'sudo apt install {selected_kernel}')
print(f"Se ha completado la instalación del nuevo kernel: {selected_kernel}\n")
print("-----                                                         \n")
# Comparación entre el kernel antiguo y el nuevo
new_kernel = os.popen('uname -r').read()
print(f"El kernel antiguo era: {current_kernel}")
print(f"El kernel nuevo es: {new_kernel}")
print("-----                                                         \n")
# Limpieza de paquetes
print("\nSe están limpiando los paquetes innecesarios...")
os.system('sudo apt autoremove')
print("-----                                                         \n")
# Indicación de reinicio
print("\nEs necesario reiniciar el sistema para aplicar los cambios.")
reboot_confirmation = input("¿Deseas reiniciar ahora? (Sí/No): ").lower()
if reboot_confirmation == 'si' or reboot_confirmation == 'sí':
    os.system('sudo reboot')
