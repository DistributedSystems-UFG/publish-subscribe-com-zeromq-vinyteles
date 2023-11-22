import zmq, time, random
from constPS import * #-

def flip_coin():
	number = random.randint(1, 10)

	coin = "heads" if number % 2 else "tails"

	return coin

def roll_dice():
  number = random.randint(1, 6)

  return str(number)

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://0.0.0.0:" + PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
  time.sleep(5)                    # wait every 5 seconds
  msg2 = str.encode("COIN " + flip_coin())
  msg3 = str.encode("DICE " + roll_dice())
  s.send(msg2)
  s.send(msg3)
