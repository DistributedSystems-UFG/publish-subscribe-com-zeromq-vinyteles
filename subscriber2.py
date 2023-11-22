import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST2 + ":" + PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "COIN")  # subscribe to TIME messages
s.setsockopt_string(zmq.SUBSCRIBE, "DICE")

for i in range(5):  # Five iterations
	ans = s.recv()   # receive a message
	print (bytes.decode(ans))
