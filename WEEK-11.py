#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from numpy import log2 as log
eps = np.finfo(float).eps


# eps’ here is the smallest representable number. At times we get log(0) or 0 in the denominator, to avoid that we are going to use this.

# USING ID3

# In[37]:


df = pd.read_csv('weather.csv')
df=df.drop(columns=['Day'])
print(df)


# 1. claculate entropy o the whole dataset

# In[38]:


def find_entropy(df):
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    entropy_node = 0  #Initialize Entropy
    values = df[Class].unique()  #Unique objects - 'Yes', 'No'
    for value in values:
        fraction = df[Class].value_counts()[value]/len(df.Decision)  
        entropy_node += -fraction*np.log2(fraction)
    print(f"Entropy_Node-> {entropy_node}")
    return(entropy_node)


# 2 .Now define a function {ent} to calculate entropy of each attribute :

# In[39]:


def ent(df,attribute):
    target_variables = df.Decision.unique()  #This gives all 'Yes' and 'No'
    variables = df[attribute].unique()    #This gives different features in that attribute (like 'Sweet')


    entropy_attribute = 0
    for variable in variables:
        entropy_each_feature = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute]==variable][df.Decision ==target_variable]) #numerator
            den = len(df[attribute][df[attribute]==variable])  #denominator
            fraction = num/(den+eps)  #pi
            entropy_each_feature += -fraction*log(fraction+eps) #This calculates entropy for one feature like 'Sweet'
        fraction2 = den/len(df)
        entropy_attribute += -fraction2*entropy_each_feature   #Sums up all the entropy ETaste

    return(abs(entropy_attribute))


# find_entropy_attribute

# In[40]:


def find_entropy_attribute(df,attribute):
  Class = df.keys()[-1]   #To make the code generic, changing target variable class name
  target_variables = df[Class].unique()  #This gives all 'Yes' and 'No'
  variables = df[attribute].unique()    #This gives different features in that attribute (like 'Hot','Cold' in Temperature)
  entropy2 = 0
  for variable in variables:
      entropy = 0
      for target_variable in target_variables:
          num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
          den = len(df[attribute][df[attribute]==variable])
          fraction = num/(den+eps)
          entropy += -fraction*log(fraction+eps)
      fraction2 = den/len(df)
      entropy2 += -fraction2*entropy
  return abs(entropy2)


# find_winner

# In[41]:


def find_winner(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:#Entropy_att.append(find_entropy_attribute(df,key))
        IG.append(find_entropy(df)-find_entropy_attribute(df,key))
    return df.keys()[:-1][np.argmax(IG)]


# get_subtable

# In[42]:


def get_subtable(df, node,value):
  return df[df[node] == value].reset_index(drop=True)


# Build a Tree

# In[43]:


def buildTree(df,tree=None): 
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    
    #Here we build our decision tree

    #Get attribute with maximum information gain
    node = find_winner(df)
    
    #Get distinct value of that attribute e.g Salary is node and Low,Med and High are values
    attValue = np.unique(df[node])
    
    #Create an empty dictionary to create tree    
    if tree is None:                    
        tree={}
        tree[node] = {}
    
   #We make loop to construct a tree by calling this function recursively. 
    #In this we check if the subset is pure and stops if it is pure. 

    for value in attValue:
        
        subtable = get_subtable(df,node,value)
        clValue,counts = np.unique(subtable[Class],return_counts=True)                        
        
        if len(counts)==1:#Checking purity of subset
            tree[node][value] = clValue[0]                                                    
        else:        
            tree[node][value] = buildTree(subtable) #Calling the function recursively 
                   
    return tree
  


# Final Output

# In[44]:


import pprint
T= buildTree(df)
pprint.pprint(T)


# USING CART ALGORITHM 

# In[51]:


df = pd.read_csv('weather.csv')
df=df.drop(columns=['Day'])
df


# In[52]:


data=pd.read_csv('weather.csv')
data=data.drop(columns=['Day'])
attributes = data.columns[1:-1]  
target_attribute = 'Decision'
class Node:
    def __init__(self, attribute=None, value=None, result=None):
        self.attribute = attribute
        self.value = value
        self.result = result
        self.children = {}
def gini_impurity(data, target_attribute):
    value_counts = data[target_attribute].value_counts()
    total = len(data)
    impurity = 1
    for value_count in value_counts:
        probability = value_count / total
        impurity -= probability ** 2
    return impurity

def gini_impurity_gain(data, attribute, target_attribute):
    impurity_before = gini_impurity(data, target_attribute)
    values, counts = np.unique(data[attribute], return_counts=True)
    impurity_after = 0
    for value, count in zip(values, counts):
        subset = data[data[attribute] == value]
        impurity_after += (count / len(data)) * gini_impurity(subset, target_attribute)
    return impurity_before - impurity_after

def cart(data, attributes, target_attribute):
    if len(np.unique(data[target_attribute])) == 1:
        return Node(result=data[target_attribute].iloc[0])

    if len(attributes) == 0:
        most_common = data[target_attribute].value_counts().idxmax()
        return Node(result=most_common)

    best_attribute = max(attributes, key=lambda a: gini_impurity_gain(data, a, target_attribute))
    tree = Node(attribute=best_attribute)

    values = np.unique(data[best_attribute])
    for value in values:
        subset = data[data[best_attribute] == value]
        if len(subset) == 0:
            most_common = data[target_attribute].value_counts().idxmax()
            tree.children[value] = Node(result=most_common)
        else:
            remaining_attributes = [a for a in attributes if a != best_attribute]
            tree.children[value] = cart(subset, remaining_attributes, target_attribute)

    return tree

tree = cart(data, attributes, target_attribute)

new_sample = pd.Series({'Outlook': 'Sunny', 'Temp': 69, 'Humidity': 80, 'Wind': 'Strong'})

def classify(tree, sample):
    if tree.result is not None:
        return tree.result
    attribute_value = sample[tree.attribute]
    if attribute_value in tree.children:
        return classify(tree.children[attribute_value], sample)

result = classify(tree, new_sample)
print("Predicted decision:", result)


# In[ ]:




