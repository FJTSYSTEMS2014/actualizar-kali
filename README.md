# actualizar-kali
Actualizar Kernel de Kali Linux

Actualizar Kernel de Kali Linux en base a la documentacion oficial https://www.kali.org/docs/general-use/updating-kali/

Este script (Actualizacion-Oficial-Kali.py) realiza las siguientes acciones:

    Verifica los permisos de sudo.
    Muestra la versión actual del kernel.
    Verifica y, si es necesario, agrega la línea del repositorio de Kali en /etc/apt/sources.list.
    Pregunta al usuario si desea actualizar el sistema.
    Si el usuario lo desea, actualiza el sistema y muestra un mensaje de confirmación.
    Pregunta al usuario si desea actualizar el kernel.
    Si el usuario lo desea, actualiza el kernel, muestra el kernel antiguo y el nuevo.
    Limpia paquetes innecesarios.
    Pregunta al usuario si desea reiniciar el sistema y, si lo confirma, realiza el reinicio.

