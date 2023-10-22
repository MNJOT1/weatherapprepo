from flask import Flask, jsonify, render_template, request
import requests
app=Flask(__name__)

# cloud give us blank system we have to install library there.
# so add these all in requirement.txt
# in one single shot it will install 
# here requirement .txt comes into picture
# always try to keep latest version search in pip in python,
# gunicorn for cloud

# after you make a html page download it in local and open it, it will run on browser and show you the UI AND UX
# more help you can take from html and css job, that's it.
# after this we host it on cloud.
# html and css is just copy paste
# without even knowing the python code, they hit API and get the code
# this is what we are doing in real life, we are hitting always API, this is real thing
# even in this lab we are doing same . VS CODE API
# url- 
# API key= '07e4bca57b7c121d3c7793e3c3c2309a'
# params={'q':"delhi",'appid':apikey, 'units':'metric'}


# now to make this code more production base, try to use expection handling, logging
# user investiagtion, more beautify then css
@app.route("/") # hit link and port number, thats' it.
def show_page():
    return render_template('index.html')


# so after this it is indirectly to the weather app
@app.route("/weatherapp",methods=['POST', 'GET'])
def get_weatherdata():
    url='https://api.openweathermap.org/data/2.5/weather'
    # how you will get this data will get the form we are filling

    # one thing more you can do that is that fix the appid and units, permanenlty
    # then user can can only enter city.
    parmas={
        'q':request.form.get("city"), # we are getting this data from form
        'appid':request.form.get('appid'),# we are getting this data from form
        'units':request.form.get('units') # we are getting this data from form
        
        }
    
    # same code what was done in python
    response = requests.get(url,params=parmas)
    data=response.json()
    # print me only city on server console
    print("city") 
    # now return data to user

    return f" data :{data}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5004) # 5000 by default