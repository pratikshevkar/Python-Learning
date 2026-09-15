c1 = input("enter c1")
c2 = input("enter c2")
if c1 == c2:
    print("draw")
elif (c1 == "rock" and c2 == "scissor") or (c1 == "paper" and c2 == "rock") or (c1 == "scissor" and c2 == "paper"):
    print("c1 win")
elif (c1 == "rock" and c2 == "paper") or (c1 == "paper" and c2 == "scissor") or (c1 == "scissor" and c2 == "rock"):
    print("c2 win")
else:
    print("invalid input")