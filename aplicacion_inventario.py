import sys

clients = ['pedro','pablo','juan']


def new_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('The client already is in the client\'s list!')
        

def update_client(client_to_udate, new_name):
    global clients
    
    if client_to_udate in clients:
        ind = clients.index(client_to_udate)
        clients[ind] = new_name
    else:
        print('The client isn\'t in the list !')


def delete_client(client_to_delete):
    global clients
    
    if client_to_delete in clients:
        clients.remove(client_to_delete)
    else:
        print('The client isn\'t in the list !')
        
def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue
        else:
            return True
            

def show_clients():
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))
    

def _print_welcome():
    print('Welcome to app')
    print('*' * 50)
    print('What would you to like do ?')
    print('[C] Create client')
    print('[D] Delete client')
    print('[U] Update client')
    print('[S] Search client')
    
    
def _get_client_name_input():
    user_input = None
    
    while not user_input:
        user_input = input('What is the client name?')
        if user_input == 'exit':
            user_input = None
            break
    if not user_input:
        sys.exit()
    
    return user_input
    
    
if __name__ == '__main__':
    _print_welcome()
    
    command = input()
    command = command.upper()
    
    if command == 'C':
        client_name = _get_client_name_input()
        new_client(client_name)
        show_clients()
    elif command == "D":
        client_name = _get_client_name_input()
        delete_client(client_name)
        show_clients()
    elif command == 'U':
        client_name = _get_client_name_input()
        new_client = input('What is the new name?')
        update_client(client_name, new_client)
        show_clients()
    elif command == 'S':
        client_name = _get_client_name_input()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {}, is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command!')