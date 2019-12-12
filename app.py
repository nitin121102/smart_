import urllib.request, json 
import pandas as pd

from flask import Flask, render_template, request
app = Flask(__name__)



def data():
    url= urllib.request.urlopen("https://s3.amazonaws.com/open-to-cors/assignment.json")
    da = json.loads(url.read().decode())
    p= da['products']
    r= []
    for i in p:
        r.append([p[i]['title'],int(p[i]['popularity']), p[i]['price'], p[i]['subcategory']])
    
    df= pd.DataFrame(r,columns=['title', 'pop.','price', 'sub'])
    
    return df

	
@app.route('/')
def result():
    re=data()
    return render_template("index.html",result= [re.to_html()])
  
if __name__ == '__main__':
    app.run(port=8080, debug=True)
    