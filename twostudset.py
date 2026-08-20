morning = {"Amit", "Rahul", "Sneha", "Priya", "Neha"}
afternoon = {"Sneha", "Priya", "Rohit", "Karan", "Neha"}

both = morning.intersection(afternoon)
only_morning = morning.difference(afternoon)
only_afternoon = afternoon.difference(morning)
at_least_one = morning.union(afternoon)

print("Students present in both sessions:", both)
print("Students present only in morning:", only_morning)
print("Students present only in afternoon:", only_afternoon)
print("Students present in at least one session:", at_least_one)