# actualizar-kali
Actualizar Kernel de Kali Linux en base a la documentacion oficial
[https://www.kali.org/docs/general-use/updating-kali/](URL)

Este script (Actualizacion-Oficial-Kali.py) realiza las siguientes acciones:

1. Verifica los permisos de sudo.
2. Muestra la versión actual del kernel.
3. Verifica y, si es necesario, agrega la línea del repositorio de Kali en /etc/apt/sources.list.
4. Pregunta al usuario si desea actualizar el sistema.
5. Si el usuario lo desea, actualiza el sistema y muestra un mensaje de confirmación.
6. Pregunta al usuario si desea actualizar el kernel.
7. Si el usuario lo desea, actualiza el kernel, muestra el kernel antiguo y el nuevo.
8. Limpia paquetes innecesarios.
9. Pregunta al usuario si desea reiniciar el sistema y, si lo confirma, realiza el reinicio.
