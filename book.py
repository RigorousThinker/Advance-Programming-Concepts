available_books = {"Python Basics", "Java Programming", "Data Structures", "Computer Networks"}
requested_books = {"Python Basics", "Data Structures", "Machine Learning", "Java Programming"}

available_requested = available_books.intersection(requested_books)

day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

unique_visitors = day1.union(day2)
returning_visitors = day1.intersection(day2)
only_first_day = day1.difference(day2)
only_second_day = day2.difference(day1)

print("Requested books that are available:", available_requested)
print("Unique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", only_first_day)
print("Visitors only on second day:", only_second_day)