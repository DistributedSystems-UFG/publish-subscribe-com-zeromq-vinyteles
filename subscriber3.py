import zmq
from constPS import * #-

context = zmq.Context()
s1 = context.socket(zmq.SUB)          # create a subscriber socket
p1 = "tcp://"+ HOST1 + ":" + PORT     # how and where to communicate
s1.connect(p1)                        # connect to the server

s2 = context.socket(zmq.SUB)          # create a subscriber socket
p2 = "tcp://"+ HOST2 + ":" + PORT        # how and where to communicate
s2.connect(p2)                         # connect to the server

s1.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages
s2.setsockopt_string(zmq.SUBSCRIBE, "DICE")

for i in range(5):  # Five iterations
	ans1 = s1.recv()   # receive a message
	print (bytes.decode(ans1))
	ans2 = s2.recv()
	print (bytes.decode(ans2))
