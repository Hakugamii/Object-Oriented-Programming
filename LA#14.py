class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

objectTom = Tom("tom", "23", "Spiderman 3")
objectAndrew = Andrew("andrew", "23", "Spiderman 2")
objectTobey = Tobey("tobey", "23", "Spiderman 1")

print(f"Name: {objectTom.name.upper()}\nMovie: {objectTom.movieTitle}\nName: {objectAndrew.name.upper()}\nMovie: {objectAndrew.movieTitle}\nName: {objectTobey.name.upper()}\nMovie: {objectTobey.movieTitle}")