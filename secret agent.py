name = input("Enter your Agent name: ")
Gadget = input("Enter your Gadget: ")

agent number = 7
rating = 9.0
mission count = 5
hight of agent = 6.2
active now = True

print("name:", name, "-> type:", type(name))
print("Gadget:", Gadget, "-> type:", type(Gadget))
print("Agent number:", agent number, "-> type:", type(agent number))
print("Rating:", rating, "-> type:", type(rating))
print("Mission count:", mission count, "-> type:", type(mission count))
print("Height of agent:", height of agent, "-> type:", type(height of agent))
print("Active now:", active now, "-> type:", type(active now))

agent number text = str(agent number)
mission count text = str(mission count)
rating text = str(rating)
status text = str(active now)

print("Agent number text:", agent number text, "-> type:", type(agent number text))
print("Mission count text:", mission count text, "-> type:", type(mission count text))
print("Rating text:", rating text, "-> type:", type(rating text))
print("Status text:", status text, "-> type:", type(status text))

first three letters = name[:3]
last letters = name[-1:]
code name = first three letters + last letters
print("first three letters of name", first three letters)
print("last letters of name", last letters)
print("code name", code name)

reversed gadget = Gadget[::-1]
print("Reversed Gadget:", reversed gadget)

badge line1 = "ANGENT" + code name.upper()
badge line2 = "ID" + agent number text + " | MISSIONS " + mission count text
badge line3 = "RATING " + rating text + " | ACTIVE " + status text
badge line4 = " SECRET GADGET CODE: " + reversed gadget.upper()

print("")
print("========= AGENT BADGE CODE =========")
print(badge line1)
print(badge line2)
print(badge line3)
print(badge line4)
