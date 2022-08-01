monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}
print(monthConversions["Mar"])
print(monthConversions["Jan"])
print(monthConversions.get("Mar"))
print(monthConversions.get("Luv","Not a valid key"))