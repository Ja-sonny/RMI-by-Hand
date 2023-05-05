import socket
import marshal

host, port = 'localhost', 10314

def add(lhs, rhs):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = marshal.dumps(('add', (lhs, rhs)))
    s.connect((host, port))
    s.sendall(data)
    
    data = s.recv(1024)
    result = marshal.loads(data)
    s.close()
    return result

def divide(lhs, rhs):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = marshal.dumps(('divide', (lhs, rhs)))
    s.connect((host, port))
    s.sendall(data)

    data = s.recv(1024)
    result = marshal.loads(data)
    if result == 'Exception':
        raise Exception('ArithmeticException')
    
    s.close()
    return result

def echo(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = marshal.dumps(('echo', (msg)))
    s.connect((host, port))
    s.sendall(data)

    data = s.recv(1024)
    result = marshal.loads(data)
    s.close()
    return result

# --------------------------------------------
# The following exercises the remote calls
# and should not need modification

print("Starting Client...")
if (add(2, 4) == 6):
    print(".")
else:
    print("X")

try:
    divide(1, 0)
    print("X")
except Exception:
    print(".")


if echo("Hello") == "You said Hello!":
    print(".")
else:
    print("X")

print(" Finished")
