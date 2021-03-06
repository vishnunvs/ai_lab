import numpy as np
import math

class Environment:
	"""environment has states give perception as to check if the agent tries to leave the grid"""

	def __init__(self,L,d):
		self.L = L#size of the grid
		self.d=d#dimension
		self.states = np.arange((self.L+1) ** 2).reshape(self.L+1,self.L +1)
		self.goal_state = self.states[L][L]

		pass

	def percept(self,x):
		"""returns boolean False if agent is about to go out of bounds or if it is out of bounds
		and True if the agent is in the bounds """
		return False if(x<self.states[0] or x>self.states[self.L]) else True
		pass
	def is_goal_reached(self,x):
		""" returns true if the goal is reached by the agent"""
		return x==self.goal_state

class Agent:
	"""docstring for Agent"""
	def __init__(self, init_state):
		self.init_state = init_state#tuple
		self.current_pos = init_state#is also a tuple
		self.agent_path=[self.init_state]
		self.random=[]
		self.no_of_steps=0

	def create_random_action(self):
		return np.random.randint(4,size=1)
	# now we have to define actions taken by the agent 
	def move_left(self):
		self.current_pos -= 1
		if(env.percept(self.current_pos)):
			self.agent_path.append(self.current_pos)
			self.no_of_steps+=1
		else:
			self.current_pos+=1
		# print "moved Left"

	def move_right(self):
		self.current_pos += 1
		if(env.percept(self.current_pos)):
			self.agent_path.append(self.current_pos)
			self.no_of_steps+=1
		else:
			self.current_pos-=1
		# print "moved Right"
	def move_up(self):
		self.current_pos += 1
		if(env.percept(self.current_pos)):
			self.agent_path.append(self.current_pos)
			self.no_of_steps+=1
		else:
			self.current_pos-=1
		# print "moved Right"
	def move_down(self):
		self.current_pos += 1
		if(env.percept(self.current_pos)):
			self.agent_path.append(self.current_pos)
			self.no_of_steps+=1
		else:
			self.current_pos-=1
		# print "moved Right"

	def move(self,env):
		r = self.create_random_action()
		r = int(r)
		# self.random.append[r]
		if(r==0):
			# print "about to move_left" 
			self.move_left()
		if(r==1):
			# print "about to move_right"
			self.move_right()
		if(r==2):
			# print "about to move_up" 
			self.move_up()
		if(r==3):
			# print "about to move_down"
			self.move_down()

env=Environment(4,1)
agent=Agent((int(math.ceil(env.L/float(2))),int(math.ceil(env.L/float(2)))))

print agent.init_state,"is the init_state of the agent"
print env.goal_state,"is the goal state for the agent"
print env.states,"are all the states "

while not env.is_goal_reached(agent.current_pos):
	agent.move(env)
print "path taken by the agent is:",agent.agent_path
print "no_of_steps : ",agent.no_of_steps

print np.arange((env.L+1) ** 2).reshape(env.L+1,env.L +1)
# i*1+j*5 gives me the value of np[i,j]
