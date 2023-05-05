import sys
import socket
import marshal

# Do not modify the add() function
def add(lhs, rhs):
    return lhs + rhs

# Do not modify the divide() function
def divide(lhs, rhs):
    if rhs == 0:
        raise Exception()
    return lhs / rhs

# Do not modify the echo() function
def echo(msg):
    return "You said " + str(msg) + "!"

# Begin your server implementation here
def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 10314))
    serversocket.listen()

    print('Server listening on port 10314')

    while True:
        c, addr = serversocket.accept()
        data = c.recv(1024)
        method, params = marshal.loads(data)
        if method == 'add':
            c.send(marshal.dumps(add(params[0], params[1])))
        elif method == 'divide':
            try:
                c.send(marshal.dumps(divide(params[0], params[1])))
            except Exception:
                c.send(marshal.dumps('Exception'))
        elif method == 'echo':
            c.send(marshal.dumps(echo(params)))
        else:
            c.send(marshal.dumps('Method Not Found, Check Again'))
    
    c.close()


if __name__ == '__main__':
    sys.exit(main())
