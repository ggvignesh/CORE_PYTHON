#2. Create a function connect(host, port=3306, protocol='TCP') and call it with various combinations.
def connect(host, port=3306, protocol="TCP"):
    print("Host     :", host)
    print("Port     :", port)
    print("Protocol :", protocol)
    print()

connect("localhost")
connect("localhost", 8080)
connect("localhost", 8080, "UDP")