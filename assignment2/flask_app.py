#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template
import requests
    
app = Flask(__name__)

@app.route("/")
def home():
    user = {"name":"day_photography"}
    headers = {'Authorization': 'Bearer keyfIJmVVuHtf9e2u',}
    params = (('view', 'Grid view'),)

    r = requests.get('https://api.airtable.com/v0/appbpFRGfIh1CPxat/Hong%20Kong%20Photography%20Spots?api_key=keyfIJmVVuHtf9e2u', headers=headers, params=params)
    dict = r.json()
    dataset = []
    for i in dict["records"]:
        dict = i['fields']
        dataset.append(dict)
    return render_template('siyu2.html',album_user=user, dataset=dataset)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9010, app)
# if __name__ == '__main__':
   # app.run(debug = True)


# In[ ]: