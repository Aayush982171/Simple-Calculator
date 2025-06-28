# CALCULATOR

print("""
╔════════════════════════════════════════════════════════╗
║                    🔢 CALCULATOR 🔢                   ║
║════════════════════════════════════════════════════════║
║            Created by : Aayush Singh 💻               ║
║                   From : Nepal 🇳🇵                     ║
╚════════════════════════════════════════════════════════╝
""")

print("""
1. Add ➕
2. Subtract ➖
3. Multiply ✖
4. Divide ➗
""")

num1 = int(input("Enter number (1/2/3/4): "))
num2 = int(input("Enter first number: "))
num3 = int(input("Enter second number: "))

if num1 == 1:
    print("The result of", num2, "+", num3, "=", num2 + num3)
    
elif num1 == 2:
    print("The result of", num2, "-", num3, "=", num2 - num3)
    
elif num1 == 3:
    print("The result of", num2, "*", num3, "=", num2 * num3)
    
elif num1 == 4:
    if num3 == 0:
        print("❌ Error: Cannot divide by zero")
    else:
        print("The result of", num2, "/", num3, "=", num2 / num3)
else:
    print("⚠ Invalid option! Please select from 1 to 4.")
