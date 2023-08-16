customer = {
    "name": "Rafael Gubert",
    "age": 19,
    "is_verified" : True
}
customer["name"] = "Gustavo Gubert"
print(customer.get("birthdate", "Nov 9 1999"))