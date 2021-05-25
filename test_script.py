import requests

localHost = "http://127.0.0.1:5000/"

# Test Cases for Breakfast
breakfast_test1 = "Breakfast 1,2,3"
breakfast_test2 = "Breakfast 2,3,1"
breakfast_test3 = "Breakfast 1,2,3,3,3"
breakfast_test4 = "Breakfast 1"
breakfast_test5 = "Breakfast"

# Test Cases for lunch
lunch_test1 = "Lunch 1,2,3"
lunch_test2 = "Lunch 1,2"
lunch_test3 = "Lunch 1,1,2,3"
lunch_test4 = "Lunch 1,2,2"
lunch_test5 = "Lunch"

# Test Cases for Dinner
dinner_test1 = "Dinner 1,2,3,4"
dinner_test2 = "Dinner 1,2,3"
dinner_test3 = "Dinner 4"
dinner_test4 = "Dinner 1,2,2"
dinner_test5 = "Dinner 1,2,3,3,4,4"

response = requests.get(localHost + breakfast_test1)

print (response.text)