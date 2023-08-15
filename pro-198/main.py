supermarket_data = {
    "customers": [
        {
            "name": "John",
            "age": 30,
            "membership": "gold",
            "purchases": [
                {"item": "apple", "quantity": 5},
                {"item": "banana", "quantity": 3},
                {"item": "milk", "quantity": 2},
            ]
        },
        {
            "name": "Alice",
            "age": 25,
            "membership": "silver",
            "purchases": [
                {"item": "bread", "quantity": 1},
                {"item": "chicken", "quantity": 2},
                {"item": "lettuce", "quantity": 1},
            ]
        }
    ],
    "inventory": {
        "apple": 0.75,
        "banana": 0.50,
        "orange": 0.60,
        "grapes": 2.00,
        "bread": 2.50,
        "milk": 1.50,
        "eggs": 1.75,
        "chicken": 5.00,
        "lettuce": 1.20,
        "tomato": 0.75
    }
}
for customer in supermarket_data["customers"]:
    print(f"Customer: {customer['name']}")
    print(f"Age: {customer['age']}")
    print(f"Membership: {customer['membership']}")
    print("Purchases:")
   
    print("\n")
