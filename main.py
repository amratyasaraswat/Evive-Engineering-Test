from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app)

breakfast = {1: "Eggs", 2: "Toast", 3: "Coffee"}
lunch = {1: "Salad", 2: "Chips", 3: "Soda"}
dinner = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"} 

class Breakfast(Resource):
    def get(self, order):
        breakfast_order = ""
        breakfast_list = order.split(",")
        breakfast_main = breakfast_list.count("1")
        breakfast_side = breakfast_list.count("2")
        breakfast_drink = breakfast_list.count("3")
        for i in range (0, len(breakfast_list)):
            breakfast_list[i] = int(breakfast_list[i])
        if (breakfast_main == 0 or breakfast_side == 0):
            breakfast_order = "Unable to process order: Since Main or Side is missing"
        if (breakfast_main > 1 or breakfast_side > 1):
            breakfast_order = "Unable to process order: Main and Side can only be served once"
        if (breakfast_drink == 0):
            breakfast_order = breakfast[1] +", "+  breakfast[2] +", Water"
        if (breakfast_drink == 1):
            breakfast_order = breakfast[1] + ", "+ breakfast[2] +", "+ breakfast[3]
        if (breakfast_drink > 1):
            breakfast_order = breakfast[1] +", "+  breakfast[2] +", "+ breakfast[3] + "(" + str(breakfast_drink) + ")"
        return breakfast_order

class Lunch(Resource):
    def get(self, order):
        lunch_order = ""
        if (len(order) == 0):
            lunch_order = "Unable to process: Main is missing, Side is missing"
        lunch_list = order.split(",")
        lunch_main = lunch_list.count("1")
        lunch_side = lunch_list.count("2")
        lunch_drink = lunch_list.count("3")
        for i in range (0, len(lunch_list)):
            lunch_list[i] = int(lunch_list[i])
        if (lunch_main == 0 or lunch_side == 0):
            lunch_order = "Unable to process order: Since Main or Side is missing"
        if (lunch_main > 1):
            lunch_order = "Unable to process: Salad cannot be ordered more than once"
        if (lunch_main == 1 and lunch_side == 1 and lunch_drink == 0):
            lunch_order = lunch[1] + ", "+ lunch[2] +", Water"
        if (lunch_side > 1 and lunch_drink == 0):
            lunch_order = lunch[1] + ", "+ lunch[2] + "(" + str(lunch_side) + ")"+", Water"   
        if (lunch_main == 1 and lunch_side == 1 and lunch_drink == 1):
            lunch_order = lunch[1] + ", " + lunch[2] + ", " + lunch[3]
        return lunch_order

class Dinner(Resource):
    def get(self, order):
        dinner_list = order.split(",")
        # print("Dinner item are: " + dinner_list)
        return dinner[1] +" "+  dinner[2] +" "+ dinner[3] +" " + dinner[4]


api.add_resource(Breakfast, "/Breakfast "+ "<string:order>")
api.add_resource(Lunch, "/Lunch " + "<string:order>")
api.add_resource(Dinner, "/Dinner " + "<string:order>")

if __name__=="__main__":
    app.run(debug = True)