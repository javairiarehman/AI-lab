#!/usr/bin/env python
# coding: utf-8

# In[129]:


class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
    def push(self, val):
        new_node = Node(val)
         
        if self.head is None:
            self.head=new_node
            return
                
        last =self.head
        while last.next is not None:
            last=last.next
                
        last.next=new_node    
        
        
    def pop(self):
        if self.head is None:
            raise Exception ("cannot pop.No value.")
            
        if self.head.next is None:
            print("case 1")
            val=self.head.val
            self.head=None
            
            
            
        print("case 2") 
        temp=self.head
        while temp.next is not None:
            prev=temp
            temp=temp.next
            
      
    
    def insert(self,index,val):
            new_node=Node(val)
            
            if index==0:
                print("case 1")
                new_node.next=self.head
                self.head=new_node
                return
            
            
            print("case 2")
            temp=self.head
            counter=0
            while temp is not None and counter < index:
                prev=temp
                temp=temp.next
                counter+=1
            
            
            
            prev.next=new_node
            new_node.next=temp

   

        


# In[130]:


def __str__(self):
    ret_str='['
    temp=self.head
    while temp is not None:
        ret_str +=str(temp.val)+','
        temp=temp.next
        
    ret_str=ret_str.rstrip(',')
    ret_str +=']'
    return ret_str


# In[102]:


LinkList.__str__=__str__


# In[103]:


l1=LinkList()


# In[104]:


l1.push(1)


# In[105]:


print(l1)


# In[132]:


def deleteNode(self, key):
        
       
       temp = self.head

      
       if (temp is not None):
           if (temp.data == key):
           self.head = temp.next
           temp = None
           return

    
       while(temp is not None):
           if temp.data == key:
               break
           prev = temp
           temp = temp.next

      
      if(temp == None):
           return

      
      prev.next = temp.next

      temp = None


# In[ ]:




