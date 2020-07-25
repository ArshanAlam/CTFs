message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: p""".format(input())


end = message[-16:]
print(message)
print(len(end), end)
print(len(end), "_"*16)
print(len(message))
