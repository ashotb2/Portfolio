import sys

def mail():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', r'bill\_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
    
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    clients_set = set(clients)
    participants_set = set(participants)
    recipients_set = set(recipients)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'potential_clients':
            non_clients = participants_set-clients_set
            print(non_clients)
        elif sys.argv[1] == 'call_center':
            non_recipients = clients_set-recipients_set
            print(non_recipients)
        elif sys.argv[1] == 'loyalty_program':
            non_participants = clients_set - participants_set
            print(non_participants)
        else:
            print('Invalid task')

if __name__ == '__main__':
    mail()
    