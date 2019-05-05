import zmq

class Sender:
    
    def __init__(self, address = 'tcp://*:8080'):
        self.context = zmq.Context.instance()
        self.sock = self.context.socket(zmq.REQ)
        self.sock.bind(address)
        
    def Send(self, message = "Hi"):   
        self.sock.send(message)
        response = self.sock.recv()
        print(response.decode())

class Receiver:
    
    def __init__(self, address = 'tcp://localhost:8080'):
        self.context = zmq.Context.instance()
        self.sock = self.context.socket(zmq.REP)
        self.sock.connect(address) #use address
        print("Server is on!")
    
    def handle_message(self, message):
        print("New user")
        return  message
    
    def Run(self):
        while True:
            message = self.sock.recv()
            response = self.handle_message(message)
            self.sock.send(response)

class Publisher:
    
    def __init__(self, address = 'tcp://*:8080'):
        self.context = zmq.Context.instance()
        self.sock = self.context.socket(zmq.PUB)
        self.sock.bind(address)
        
    def Send(self, message ):   
        self.sock.send(message.encode())
        print(str(message) + " sent")

class Subscriber:
    def __init__(self, address = 'tcp://127.0.0.1:8080'):
        self.context = zmq.Context.instance()
        self.sock = self.context.socket(zmq.SUB)
        self.sock.setsockopt(zmq.SUBSCRIBE, b"");
        self.sock.connect(address)
          
    def GetUpdates(self ):
        while True:
            message = self.sock.recv()
            print(message.decode() + "recieved")

if __name__ == "__main__":
    server = Receiver()
    message = "Test"
    response = server.handle_message(message)
    print(response)
    

    