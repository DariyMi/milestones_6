eq = input()
eq = " = ".join(eq.split("="))
eq = " + ".join(eq.split("+"))
eq = "".join(eq.split("("))
eq = "".join(eq.split(")"))

a = int(eq.replace("x^2 + ", " ").replace("x + ", " ").split()[0])
b = int(eq.replace("x^2 + ", " ").replace("x + ", " ").split()[1])
c = int(eq.replace("x^2 + ", " ").replace("x + ", " ").split()[2])

x1 = int((-b+(b**2 - 4*a*c)**(1/2))/(2*a))
x2 = int((-b-(b**2 - 4*a*c)**(1/2))/(2*a))

# написала int, бо в прикладах цілі числа мали вийти в результаті
# Але взагалом там можуть бути і дробові відповіді. Тоді без int
# x1 = (-b+(b**2 - 4*a*c)**(1/2))/(2*a)
# x2 = (-b-(b**2 - 4*a*c)**(1/2))/(2*a)

print(x1, x2)
