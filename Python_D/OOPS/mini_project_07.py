class Movie:
    '''This class developed by Kali'''
    def __init__(self,title, hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

m = Movie("Bahubali","Prabhas","Anushka")
print(m)
print(m.__class__)
print(m.__doc__)
print(m.__init__)

list_of_movies =[]

while True:
    title = input("Enter Movie Name")
    hero = input("Enter Movie Hero")
    heroine = input("Enter Movie Heroine")

    m = Movie(title,hero,heroine)
    list_of_movies.append(m)
    print("Movies added succesfully")
    option = input("Do you wanted to one more movie")
    print(list_of_movies)
    if option.lower() == 'no':
        break
