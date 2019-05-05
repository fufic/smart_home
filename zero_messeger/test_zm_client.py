import zero_messeger as zm
client = zm.Sender()

while True:
    message =input("Type message: ")
    client.send(message.encode())
    