#for loops = execute a block of code a fixed number of times.
#you can iterate over a range, string, sequence,etc.

#example 1 
#counts from 1 - 10
# for x in range (1, 11):
#     print(x)

#example 2 
#count backwards
# for x in reversed (range (1,11)):
#     print(x)

#example 3
# for x in reversed (range (1,11,2)):(it will count down by 2)
#     print(x)

#example 4
#takes the numbers and lines them up
# credit_cards = "1234-5678-9012-3456"
# for x in credit_cards:
#     print (x)

#example 5
#add continue to skip over the number 
# for x in range(1,21):
#     if x == 13:
#         continue
#     if x == 15:
#         continue
#     if x == 20:
#         continue
#     else:
#         print(x)

#example 6
#break will break the program aka it will end it on the number you put
# for x in range(1,21):
#     if x == 13:
#         break
#     else: 
#         print(x)

# #example 7
# horror_characters = ["freddy", "jason","micheal","pennywise","chucky"]
# #iterate through the list and print each character
# for character in horror_characters:
#     if character == "micheal":
#         character = "dracula" #swapped the list 
#     print(character)

#create  akist of famous horror movies or your favorite horror movies
#iterate through the list and if a certain movie is found is your least favoite movie, break out the loop
#print out the rest of the movies
#next replace one of the movies with a movie that you like

# horror_movies = ["saw", "halloween", "friday the 13th", "smile", "it"]
# for movies in horror_movies:
#     if movies == "smile":
#          break
#     else: 
#          print(movies)

horror_movies = ["saw", "halloween", "friday the 13th", "smile", "it"]
for movies in horror_movies:
     if movies == "smile":
         movies = "child's play"
     print(movies)



