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
        elif (breakfast_main > 1 or breakfast_side > 1):
            breakfast_order = "Unable to process order: Main and Side can only be served once"
        elif (breakfast_drink == 0):
            breakfast_order = breakfast[1] +", "+  breakfast[2] +", Water"
        elif (breakfast_drink == 1):
            breakfast_order = breakfast[1] + ", "+ breakfast[2] +", "+ breakfast[3]
        elif (breakfast_drink > 1):
            breakfast_order = breakfast[1] +", "+  breakfast[2] +", "+ breakfast[3] + "(" + str(breakfast_drink) + ")"
        return breakfast_order

class Lunch(Resource):
    def get(self, order):
        lunch_order = ""
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
        if (lunch_side > 1 and lunch_drink == 1):
            lunch_order = lunch[1] + ", "+ lunch[2] + "(" + str(lunch_side) + ")"+ lunch[3]   
        if (lunch_main == 1 and lunch_side == 1 and lunch_drink == 1):
            lunch_order = lunch[1] + ", " + lunch[2] + ", " + lunch[3]
        if (lunch_drink > 1):
            lunch_order = "Unable to process: Drink cannot be ordered more than once"
        return lunch_order

class Dinner(Resource):
    def get(self, order):
        dinner_list = order.split(",")
        dinner_order = ""
        dinner_list = order.split(",")
        dinner_main = dinner_list.count("1")
        dinner_side = dinner_list.count("2")
        dinner_drink = dinner_list.count("3")
        dinner_dessert = dinner_list.count("4")
        for i in range (0, len(dinner_list)):
                dinner_list[i] = int(dinner_list[i])
        if (dinner_dessert == 0):
            dinner_order = " Unable to process: Dessert is missing" 
        if (dinner_main == 0 or dinner_side == 0):
            dinner_order = "Unable to process order: Since Main or Side is missing"
        if (dinner_dessert == 0):
            dinner_order = "Unable to process: Dessert is missing"
        if (dinner_main == 1 and dinner_side == 1 and dinner_drink == 1 and dinner_dessert ==1):
            dinner_order = dinner[1] + ", " + dinner[2] + ", " + dinner[3] + ", Water, " + dinner[4]
        if (dinner_drink > 1 and dinner_dessert == 1):
            dinner_order = dinner[1] + ", " + dinner[2] + ", " + dinner[3] + "("+ str(dinner_drink)+ "), Water, " + dinner[4]
        if (dinner_drink == 1 and dinner_dessert > 1):
            dinner_order = dinner[1] + ", " + dinner[2] + ", " + dinner[3] + ", Water, " + dinner[4] + "(" + str(dinner_dessert) + ")"
        if (dinner_drink > 1 and dinner_dessert > 1):
            dinner_order = dinner[1] + ", " + dinner[2] + ", " + dinner[3] + "("+ str(dinner_drink)+ "), Water, " + dinner[4] + "(" + str(dinner_dessert) + ")"
        return dinner_order

class MissingBreakfastOrder(Resource):
    def get(self):
        return "Unable to process: Main is missing, side is missing"

class MissingLunchOrder(Resource):
    def get(self):
        return "Unable to process: Main is missing, side is missing"

class MissingDinnerOrder(Resource):
    def get(self):
        return "Unable to process: Main is missing, side is missing"


api.add_resource(Breakfast, "/Breakfast "+ "<string:order>")
api.add_resource(Lunch, "/Lunch " + "<string:order>")
api.add_resource(Dinner, "/Dinner " + "<string:order>")
api.add_resource(MissingBreakfastOrder, "/Breakfast")
api.add_resource(MissingLunchOrder, "/Lunch")
api.add_resource(MissingDinnerOrder, "/Dinner")

if __name__=="__main__":
    app.run(debug = True)