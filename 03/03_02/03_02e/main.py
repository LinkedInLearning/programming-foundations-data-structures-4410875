# Key: State
# Value: Capital

states_to_capitals = {
    "Texas" : "Austin",
    "New York" : "Albany"
}

print(states_to_capitals["New York"])

for key, value in states_to_capitals.items():
    print(key + " | " + value)
    