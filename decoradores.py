
def upper(func):
    """*args: conjunto arbitrario de argumentos posicionales ('Hola', 'Juan', 'Pedro', 'Rubén')"""
    """*kwargs: conjunto arbitrario de argumentos con keyword (edad='42', profesion='arquitecto', nacionalidad='argentino')"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        return result.upper()
    return wrapper
        
@upper
def my_name(name):
    return 'Hola, {}'.format(name)

if __name__ == '__main__':
    print(my_name('droal'))
    