from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient("mongodb://localhost:27017/")
db = client["store"]

prod_col = db["products"]
orders = db["orders"]

prod_col.insert_many([{"name": "sausage", "Category": "meat", "price": 120, "stock_quantity": 60},
                      {"name": "apple", "Category": "fruits", "price": 20, "stock_quantity": 70},
                      {"name": "potato", "Category": "vegetables", "price": 50, "stock_quantity": 100}])

orders.insert_many([{"number": 1, "customer": "Peter Loy", "products": [{"name": "apple", "quantity": 2}], "order_date": "2026-04-18"}])

thirty_days_ago = datetime.now() - timedelta(days=30)
order_res = orders.find({"order_date": {"$gte": thirty_days_ago}})
for order in order_res:
    print(order)

prod_col.update_one(
    {"name": "apple"},
    {"$inc": {"stock_quantity": -1}}  # Уменьшаем количество на складе на 1
)

prod_col.delete_many({"stock_quantity": 0})

pipeline = [
    {"$unwind": "$products"},
    {"$group": {"_id": "$products.name", "total_sold": {"$sum": "$products.quantity"}}}
]
result = orders.aggregate(pipeline)
for item in result:
    print(item)

pipeline = [
    {"$match": {"customer": "John Doe"}},
    {"$group": {"_id": "$customer", "total_spent": {"$sum": "$total_amount"}}}
]
result = orders.aggregate(pipeline)
for item in result:
    print(item)

prod_col.create_index([("category", 1)])

