# Tuple
#
#  - Mathematical name for ordered set of data
#  - Ordered is a requirement for python sequence
#  - In python tuples are another sequence types along with strings, lists and ranges
#  - Tuples differ from list because tuples are immutable that means they cannot be changed after
#     they are created. Just like strings.
#  - The main difference between a tuple and list if that Tuples are immutable
#  - Because they dont have the overhead of the methods needed to change them, tuples use
#      less memory than lists. Thats one reason why you might want to use tuples
#  - If yu program is dealing with millions of these things, you can save memory by using a tuple
#  - Helps in protecting the integrity of your data as we cannot change the data once assigned.
#  - Using a List method we can convert a Tuple to a list

t = ("a", "b", "c")
print(t)

welcome = "Welcome to the nightmare", "Alice cooper", 1975
bad = "Bad company", "Bad company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

title, artist, year = metallica
print(title)
print(artist)
print(year)

print()
table = ("Cofee table", 200, 100, 75, 34.50)

name, length, width, height, price = table
print(length * width)

albums = [("Welcome to the nightmare", "Alice cooper", 1975),
         ("Bad company", "Bad company", 1974),
         ("Nightflight", "Budgie", 1981),
         ("More Mayhem", "Emilda May", 2011),
         ("Ride the Lightning", "Metallica", 1984)]
print(len(albums))

for album in albums:
    print("Album: {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))

print("\n \n")
#Approach 2
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))