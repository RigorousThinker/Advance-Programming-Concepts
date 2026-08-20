user1 = {"Amit", "Rahul", "Sneha", "Priya", "Neha"}
user2 = {"Sneha", "Priya", "Rohit", "Karan", "Neha"}

mutual_friends = user1.intersection(user2)
unique_user1 = user1.difference(user2)
unique_user2 = user2.difference(user1)
total_unique = user1.union(user2)

print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique)