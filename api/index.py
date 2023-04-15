from flask import Flask,request,render_template
import urllib
import json

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/aml', methods=['GET','POST'])
def aml():
    data =  {
    "Inputs": {
        "input1": [       
        {
            "Total number of nearby rooms": request.values['p1'],
            "Distance from nearest competitor": request.values['p2'],
            "Peripheral office space": request.values['p3'],
            "University enrollment": request.values['p4'],
            "Household income": request.values['p5'],
            "distance from city center": request.values['p6'],
            "operating profit": 35.5
        }
        ]
    },
    "GlobalParameters": {}
    }

    body = str.encode(json.dumps(data))

    url = 'http://83acf92f-59b6-4931-9fab-bbd13a52c939.southeastasia.azurecontainer.io/score    '
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = 'MLLYjITrseeLOQxc1WutVs35J2HXaOlF'

    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")


    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    htmlstr="<html><body>"

    try:
        response = urllib.request.urlopen(req)

        result = json.loads(response.read())
        htmlstr=htmlstr+"依據您輸入的參數，經過數據分析模型，預測利潤為:"
        htmlstr=htmlstr+str(result['Results']['WebServiceOutput0'][0]['Scored Labels'])
        # print(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        # print(json.load(error.read().decode("utf8", 'ignore')))

    htmlstr=htmlstr+"</body></html>"

    # return "hello"
    return htmlstr

@app.route('/about')
def about():
    return 'About'