PASSWORD = '123456'

def password_required(func):
    def wrapper():
        password = input('Ingrese contraseña:')
        
        if password == PASSWORD:
            return func()
        else:
            print('La contraseña es incorrecta!')
            
    return wrapper

@password_required
def needs_pasword():
    print('La contraseña es correcta!')


if __name__ == '__main__':
    needs_pasword()
    

    