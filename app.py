#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install flask


# In[2]:


from flask import Flask, request, render_template


# In[3]:


app = Flask(__name__) #__name__ => to make sure it is yourself


# In[4]:


import joblib


# In[5]:


# dir(app)
#route by default look for .html. @app - declarator - indicate must run this function first before running the codes below
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST": #this happens after pressing button submit
        income = request.form.get("income") #add after testing
        age = request.form.get("age") #add after testing
        loan = request.form.get("loan") #add after testing
        income = float(income) #add after testing
        age = float(age) #add after testing
        loan = float(loan) #add after testing
        print(income, age, loan) #add after testing
        model1 = joblib.load("CART") #add after testing
        pred1 = model1.predict([[income, age, loan]]) #add after testing
        model2 = joblib.load("RF") #add after testing
        pred2 = model2.predict([[income, age, loan]]) #add after testing
        model3 = joblib.load("GB") #add after testing
        pred3 = model3.predict([[income, age, loan]]) #add after testing
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3)) #change from "1" to pred1, pred2, pred3
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2")) #this happens before pressing button submit
                


# In[ ]:


if __name__=="__main__":
    app.run() #change from app.run() to app.run(host='0.0.0.0',port=80) if 5000 cannot work


# In[ ]:




