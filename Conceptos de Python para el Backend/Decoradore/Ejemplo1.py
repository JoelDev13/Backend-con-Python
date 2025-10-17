def decorador (func):
    def wrapper(*args, **kwargs):
        print("ante de ejecutar la funcion")
        resultado =func(*args, **kwargs)
        print("depues de ejecutar la funcion")

    return wrapper

@decorador
def saludo():
    print("hola mi bro")

saludo()

