#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Queue:
    def __init__(self):
        self.size=5
        self.q=list(range(self.size))
        self.i=0    #rare
        self.o=0    #front
        
        self.is_empty=True
        self.is_full=False


# In[13]:


def _inc(self,idx):
    if idx+1==self.size:
        return 0
    else:
        return idx+1
Queue._inc=_inc


# In[14]:


def enqueue(self,val):
    if self.is_full:
        raise IndexError("queue full.cannot enqueue.")
    
    self.q[self.i]=val
    self.i=self._inc(self.i)
    
    if self.i==self.o:
        self.is_full=True
        
    self.is_empty=False   
Queue.enqueue=enqueue    
    


# In[15]:


def dequeue(self):
    if self.is_empty:
        raise IndexError("Queue empty.cannot dequeue")
        
    ret=self.q[self.o]
    self.o=self._inc(self.o)
    
    if self.i==self.o:
        self.is_empty=True
        
    self.is_full=Fasle
    return ret

Queue.dequeue=dequeue


# In[17]:


def __str__(self):
    return str(self.q)+", in :" +str(self.i) + ",out:" + str(self.o)
Queue.__str__=__str__


# In[ ]:




