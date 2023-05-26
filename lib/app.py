# content of test_sample.py

# class Vehicle:
#     def __init__ (self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     def drive (self):
#         print ("I am driving a ", self.brand, " ", self.color, " vehicle")
        
# car = vehicle ("Toyota", "Black")
    
# car.drive()

# class Car (Vehicle):
#     def __init__(self, brand, color, make, number_of_wheels):
#         super().__init__(brand, color)
#         self.number_of_wheels = number_of_wheels
#         self.make = make
            
#     def drive (self):
#         print ("I am driving a ", self.brand, " ", self.color, " ", self.make, " ", self.number_of_wheels, " vehicle")

# car = Car ("Toyota", "Blue", "Audi", 4)
# car.drive()        


print("hello world! Pass this test, please.")


#print("hello town!")
#print("hello planet")

#import random 

#print (random. randrange(1, 10))


#height = (2, 5, 7, 10, 8, 4, 3, 9)

#def function_height(height):

   #max_height = max(height)
   #min_height = min(height)
   #next_height = next(height)
   #print(max_height)
   #print(min_height)
    #print(next_height)

#function_height(height)


#def findNumbers():
    #num = [0, 3, 5, 9, 6, 7, 4]
    #num.sort()
    #print(num[-1])
    #print(num[0])
    #print(num[-2])
#findNumbers()

# books = {
#     'F. Scott Fitzgerald': ['The Great Gatsby'],
#     'Harper Lee': ['To Kill a Mockingbird'],
# }


# while True:
#     title = input("Enter the book title (or 'q' to quit): ")
#     if title == 'q':
#         break

#     author = input("Enter the author's name: ")

#     if author in books:
#         books[author].append(title)
#     else:
#         books[author] = [title]

# print("Books by Authors:")
# for author, titles in books.items():
#     print(f"{author}: {', '.join(titles)}")

# author = input("Enter the author's name to edit their book list: ")
# if author in books:
#     print(f"Current books by {author}: {', '.join(books[author])}")
#     action = input("Enter the action (add, remove, update): ")
#     if action == "add":
#         title = input("Enter the new book title: ")
#         books[author].append(title)
#     elif action == "remove":
#         title = input("Enter the book title to remove: ")
#         if title in books[author]:
#             books[author].remove(title)
#             print(f"Removed '{title}' from {author}'s book list.")
#         else:
#             print("Book not found in the author's list.")
#     elif action == "update":
#         old_title = input("Enter the old book title: ")
#         new_title = input("Enter the new book title: ")
#         if old_title in books[author]:
#             index = books[author].index(old_title)
#             books[author][index] = new_title
#             print(f"Updated '{old_title}' to '{new_title}' in {author}'s book list.")
#         else:
#             print("Book not found in the author's list.")
#     else:
#         print("Invalid action.")
# else:
#     print("Author not found.")




