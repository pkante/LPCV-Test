import socket
import os

# Create TCP Internet socket and connect to local host
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

# Gets file
file = open("LPCVC-Test/test_img.png", "rb")
file_size = os.path.getsize("LPCVC-Test/test_img.png")

#Transmits file
client.send("recieved_image.png".encode())
client.send(str(file_size).encode())

#Send data and ending tag
data = file.read()
client.sendall(data)
client.send(b"<PranavServer>")


file.close()
client.close()
