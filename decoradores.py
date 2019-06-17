def saludo(tipoSaludo, *args):
    print(type(args))
    listaDeAmigos = ''
    for amigo in args:
        listaDeAmigos = listaDeAmigos + ' ' + amigo
    print(listaDeAmigos)
 
print('EJEMPLO CON *ARGS:')
saludo('Hola', 'Juan', 'Pedro', 'Rubén')
 
def verArgsConNombre(**kwargs):
    print(type(kwargs))
    for nombre, valor in kwargs.items():
        print(nombre + ': ' + valor)
 
print('EJEMPLO CON **KWARGS')
verArgsConNombre(edad='42', profesion='arquitecto', nacionalidad='argentino')


    