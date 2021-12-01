class User:
    def __init__(self, name, genres, console, key_words):
        self.name = name 
        self.genre = genre
        self.console = console
        self.key_words = keywords
        
        # get user input
        attributes = ["List your console(s): ", "Name 1-3 genres: ", "Name 1-3 keywords: "]
        choices = []
        n = input("Name: ")
        for i in attributes:
            choices += input(i)
        me = User(n, choices[0], choices[1], choices[2])
        me.printUser()


    def printUser(self):
        print(self.name, " profile:\n", self.console", "self.genre"," self.key_words)



