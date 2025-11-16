print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")


cups = int(input("Write how many cups of coffee you will need:\n"))

water = 200 * cups
milk = 50 * cups
beans = 15 * cups

print(f"\nFor {cups} cups of coffee you will need:")
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{beans} g of coffee beans")

water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups_needed = int(input("Write how many cups of coffee you will need:\n"))

water_cups = water 
milk_cups = milk 
beans_cups = beans 

max_cups = min(water_cups, milk_cups, beans_cups)

if max_cups == cups_needed:
    print("Yes, I can make that amount of coffee")
elif max_cups > cups_needed:
    extra = max_cups - cups_needed
    print(f"Yes, I can make that amount of coffee (and even {extra} more than that)")
else:
    print(f"No, I can make only {max_cups} cups of coffee")


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "main"  
        self.running = True

    def print_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money\n")

    def process(self, s: str):
        if self.state == "main":
            
            if s == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                self.state = "buy"
            elif s == "fill":
                print("Write how many ml of water do you want to add:")
                self.state = "fill_water"
            elif s == "take":
                print(f"I gave you {self.money}\n")
                self.money = 0
            elif s == "remaining":
                self.print_state()
            elif s == "exit":
                self.running = False
            else:
                
                pass

        elif self.state == "buy":
            if s == "back":
                self.state = "main"
            else:
                self.make_coffee(s)
                self.state = "main"

        elif self.state == "fill_water":
            self.water += int(s)
            print("Write how many ml of milk do you want to add:")
            self.state = "fill_milk"

        elif self.state == "fill_milk":
            self.milk += int(s)
            print("Write how many grams of coffee beans do you want to add:")
            self.state = "fill_beans"

        elif self.state == "fill_beans":
            self.beans += int(s)
            print("Write how many disposable cups of coffee do you want to add:")
            self.state = "fill_cups"

        elif self.state == "fill_cups":
            self.cups += int(s)
            print()
            self.state = "main"

    def make_coffee(self, choice: str):
        if choice == "1":      # espresso
            need_water, need_milk, need_beans, price = 250, 0, 16, 4
        elif choice == "2":    # latte
            need_water, need_milk, need_beans, price = 350, 75, 20, 7
        elif choice == "3":    # cappuccino
            need_water, need_milk, need_beans, price = 200, 100, 12, 6
        else:
            return

        
        if self.water < need_water:
            print("Sorry, not enough water!")
            return
        if self.milk < need_milk:
            print("Sorry, not enough milk!")
            return
        if self.beans < need_beans:
            print("Sorry, not enough coffee beans!")
            return
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return

        print("I have enough resources, making you a coffee!")
        self.water -= need_water
        self.milk -= need_milk
        self.beans -= need_beans
        self.cups -= 1
        self.money += price
        print()


def main():
    machine = CoffeeMachine()

    while machine.running:
        print("Write action (buy, fill, take, remaining, exit):")
        user_input = input()
        machine.process(user_input)


if __name__ == "__main__":
    main()