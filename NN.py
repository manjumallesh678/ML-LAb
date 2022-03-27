import numpy as np
x=np.array(([2,9],[1,5],[3,6]),dtype=float)
y=np.array(([92],[86],[89]),dtype=float)
x = x/np.amax(x,axis=0)
y = y/100
class NeuralNetwork(object):
    
    def __init__(self):
        self.inputsize = 2
        self.hiddensize = 3
        self.outputsize = 1
        
        self.w1 = np.random.randn(self.inputsize,self.hiddensize)
        self.w2 = np.random.randn(self.hiddensize,self.outputsize)
        
    def sigmod(self,s,derive=False):
        if derive == False:
            return 1/(1+np.exp(-s))
        else:
            return s * (1-s)
    
    def feedforward(self,x):
        
        self.z = np.dot(x,self.w1)
        self.z2 = self.sigmod(self.z)
        
        self.z3 = np.dot(self.z2,self.w2)
        output = self.sigmod(self.z3)
        return output
    def backpropagation(self,x,y,output):
        self.outputError = y - output
        self.outputdelta = self.outputError*self.sigmod(output,derive=True)
        
        self.z2Error = self.outputdelta.dot(self.w2.T)
        self.z2delta = self.z2Error*self.sigmod(self.z2,derive=True)
        
        self.w1+=x.T.dot(self.z2delta)
        self.w2+=self.z2.T.dot(self.outputdelta)
        
    def train(self,x,y):
        output = self.feedforward(x)
        self.backpropagation(x,y,output)
    
NN = NeuralNetwork()
for i in range(10000):
    NN.train(x,y)
print(NN.feedforward(x))
NN.feedforward([0.66,0.888]) 
