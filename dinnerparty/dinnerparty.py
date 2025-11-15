import random

num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = {}

    for _ in range(num_friends):
        name = input()
        friends[name] = 0

    total_amount = int(input("\nEnter the total amount:\n"))

    
    share = round(total_amount / num_friends, 2)
    for name in friends:
        friends[name] = share

    answer = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if answer == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"\n{lucky} is the lucky one!")

        
        new_share = round(total_amount / (num_friends - 1), 2)
        for name in friends:
            friends[name] = new_share
        friends[lucky] = 0

        print()
        print(friends)
    else:
        print("\nNo one is going to be lucky")
        print()
        print(friends)