def leerUsuarioClave(mensaje):
    return input(mensaje)

def validarUsuarioClave(usuario,clave):
    nombreUsuario="Jego"
    claveUsuario="123abc"
    if nombreUsuario==usuario and claveUsuario==clave:
        return "Bienvenido/a...."
    elif nombreUsuario==usuario and not claveUsuario==clave:
        return "Clave INCORRECTA"
    elif not nombreUsuario==usuario and claveUsuario==clave:
        return "Usuario INCORRECTO"
    else:
        return "Usuario y clave INCORRECTAS"

#PP
usuario=leerUsuarioClave("Usuario: ")
clave=leerUsuarioClave("Contraseña: ")
print(validarUsuarioClave(usuario,clave))

# TAREA (para practicar) > controlar 3 intentos

# Usario: OK    Clave: OK
# Usario: OK    Clave: Error
# Usario: Error Clave: OK
# Usario: Error Clave: Error
