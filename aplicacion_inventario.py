import sys

clients = [
    {
        'name': 'Pedro',
        'company': 'Google',
        'email': 'pedro@google.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Twitter',
        'email': 'ricardo@teitter.com',
        'position': 'Data engineer'
    },
    {
        'name': 'Jose',
        'company': 'Apple',
        'email': 'jose@apple.com',
        'position': 'Marketing chief'
    }
    ]


def new_client(client):
    global clients
    
    if client not in clients:
        clients.append(client)
    else:
        print('The client already is in the client\'s list!')
        

def update_client(uid_cliente, new_client):
    global clients
    if (uid_cliente <= len(clients) - 1) & (uid_cliente > 0):
        clients[uid_cliente] = new_client 
    else:
        print('>>>>>>The uid is out of range!')


def delete_client(uid_cliente):
    global clients
    if idx, client in enumerate(clients):
        if idx == uid_cliente:
            del clients[idx]
            break

def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True
            

def show_clients():
    print('uid | name | company | email | position')
    print('----|------|---------|-------|---------')
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))
    

def _print_welcome():
    print('Welcome to app')
    print('*' * 50)
    print('What would you to like do ?')
    print('[C] Create client')
    print('[D] Delete client')
    print('[U] Update client')
    print('[S] Search client')
    print('[L] List of clients')
    
def _get_client_field(field_name, message= 'What is the client {}?'):
    field_input = None
    while not field_input:
        field_input = input(message.format(field_name))
    return field_input
    
def _get_client_input():
    client = {
            'name'      : _get_client_field('name'),
            'company'   : _get_client_field('company'),
            'email'     : _get_client_field('email'),
            'position'  : _get_client_field('position')
        }
    return client
    
    
if __name__ == '__main__':
    _print_welcome()
    
    command = input()
    command = command.upper()
    
    if command == 'L':
        show_clients()
    
    elif command == 'C':
        client = _get_client_input()
        new_client(client)
        show_clients()
        
    elif command == "D":
        uid_client = int(_get_client_field('uid'))
        delete_client(uid_client)
        show_clients()
        
    elif command == 'U':
        uid_client = int(_get_client_field('uid'))
        new_client = _get_client_input()
        update_client(uid_client, new_client)
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