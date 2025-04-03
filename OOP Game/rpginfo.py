class RPGInfo:
    author = "Oscar"
    def __init__(self, game_title):
        self.title = game_title
    def welcome(self):
        print(f"Welcome to {self.title}")
    def info():
        print("Made using the OOP RPG Course")
    @classmethod
    def credits(cls):
        print("Thanks for playing")
        print(f"Created by {cls.author}")