
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import cufflinks as cf
cf.set_config_file(offline=True)


# ## Data Preview

# In[2]:


df = pd.read_csv('./data.csv', index_col=0)


# In[3]:


print('Columns:\n{}'.format(df.columns.values))
print('Data Types:\n{}'.format(df.dtypes))
print('Shape:\n{}'.format(df.shape))


# In[4]:


# Drop 'created_at' and 'currency' columns for dimension reduction and also importance
# currency column is proxy for country anyways
df = df.drop(['created_at','currency'], axis=1)
df.head()


# ## Feature Engineering

# In[5]:


unix_time_columns = ['deadline','state_changed_at','launched_at']
for col in unix_time_columns:
    col_name = col+'_dt'
    df[col_name] = pd.to_datetime(df[col],unit='s')


# In[6]:


# feature engineering 1 (duration)
# leave in unix time because only care about the difference
df['expected_duration'] = df['deadline'] - df['launched_at']
df['actual_duration']   = df['state_changed_at'] - df['launched_at']


# In[7]:


# feature engineering 2 (launch times)
df['launch_year']  = df['launched_at_dt'].dt.year
df['launch_month'] = df['launched_at_dt'].dt.month
df['launch_day']   = df['launched_at_dt'].dt.day
df['launch_hour']  = df['launched_at_dt'].dt.hour


# In[8]:


# feature engineering 3 (deadline times)
df['deadline_year']  = df['deadline_dt'].dt.year
df['deadline_month'] = df['deadline_dt'].dt.month
df['deadline_day']   = df['deadline_dt'].dt.day


# In[9]:


for col in unix_time_columns:
    df = df.drop(col, axis=1)
    df = df.drop(col+'_dt', axis=1)


# In[10]:


print('Columns:\n{}'.format(df.columns.values))
print('Data Types:\n{}'.format(df.dtypes))
print('Shape:\n{}'.format(df.shape))
df.head()


# ## Label Encoding

# In[11]:


dummy_cols = ['country',
              'launch_hour','launch_day','launch_month','launch_year',
              'deadline_day','deadline_month','deadline_year']
for col in dummy_cols:
    df = pd.merge(df, pd.get_dummies(df[col], prefix=col), left_index=True, right_index=True)
    df = df.drop(col, axis=1)


# In[12]:


print('Columns:\n{}'.format(df.columns.values))
print('Data Types:\n{}'.format(df.dtypes))
print('Shape:\n{}'.format(df.shape))


# In[13]:


# remove text fields for now
text_cols = ['name','desc','keywords']
df = df.drop(text_cols, axis=1)


# In[14]:


# split into train and test
from sklearn.model_selection import train_test_split

X = df.drop('final_status',axis=1)
y = df['final_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=42)


# ## Decision Trees

# In[15]:


from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import confusion_matrix, classification_report


# In[16]:


tree_gini = DecisionTreeClassifier(max_depth=5, random_state=42)
tree_gini.fit(X_train, y_train)
labels_gini = tree_gini.predict(X_test)


# In[17]:


print(confusion_matrix(labels_gini, y_test))
print(classification_report(labels_gini, y_test))


# In[20]:


import subprocess
def visualize_tree(tree):
    with open("dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")


# In[21]:


visualize_tree(tree_gini)

