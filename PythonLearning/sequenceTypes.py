#Sequence Types
    #List
    #Tuple
    #Range

#A sequence is a ordered collection of items
#The word ordered here is important
    #If a sequence wasnt ordered, you couldn't refer to individual
    #items by their index position

#In python anything that you can iterate over is an iterable. That means
#if you can use it in a for loop then its iterable
    #Iterable is an object that contains either __iter__ method or __getitem__ method
    #Indexing must also start from 0

#All sequence types can be iterated over
#That means all sequence types - Strings, Lists, etc are also iterable types
#Not all iterable are sequences
#For example, you can use a dictionary in a for loop, but its not a sequence

#String and List are both immutable, which means they cant be changed
#Lists on the other hand are mutable. You can change the contents of a list

#Immutable Ojects (cant be changed)
    #int
    #float
    #bool
    #str
    #tuple
    #frozenset
    #bytes