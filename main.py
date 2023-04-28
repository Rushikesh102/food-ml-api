import json

from flask import Flask, request, jsonify
from normal import Normal
from restaurants import Restaurants
app = Flask(__name__)

@app.route('/normal_getNames')
def normal_getNames():
    import pandas as pd
    df = pd.read_csv('indianFood.csv')
    json_data = df['name'].to_json(orient='records')

    return json_data
@app.route('/normal_recommend',methods=['GET'])
def normal_recommend():
    args = request.args
    food = args.get('food')
    flavor_profile = args.get('flavor_profile')
    diet = args.get('diet')
    course = args.get('course')

    obj = Normal()
    res = obj.recommend_food_based_on_plot(food)
    if (diet != ''):
        res = res[res['diet'] == diet]
    if (flavor_profile != ''):
        res = res[res['flavor_profile'] == flavor_profile]
    if (course != ''):
        res = res[res['course'] == course]
    json_data = res.to_json(orient='records')
    # print(res.keys())
    return json_data
@app.route('/fast_food_recommend',methods=['GET'])
def fast_food_recommend():
    args = request.args
    a = args.get('restaurants')
    b = args.get('hunger')
    if (b != ''):
        b = int(b)
    c = args.get('protein')
    obj = Restaurants()
    res = obj.recommend_fast_food(a,b,c)
    # print(res)
    if (a != ''):
        res = res[res['Company'] == a]
        # print("Company")
        # print(res)
    if (b != ''):
        res = res[res['Hunger Level'] == b]
        # print("Hunger")
        # print(res)
    if (c != '' and c=='y'):
        res = res[res['Protein Level'] >= 2]
        # print("Protein y")
        # print(res)
    if (c != '' and c=='n'):
        res = res[res['Protein Level'] >= 0 and res['Protein Level'] <2]
        # print("Protein n")
        # print(res)
    # res['Result']=res['Company']+" "+res['Product']
    json_data = res.to_json(orient='records')
    # json_data=json.dumps(res)
    return json_data


if __name__ == '__main__':
    app.run(debug=True)

