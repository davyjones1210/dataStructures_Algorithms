
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print("User created!")
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]


# user1 = User("test1", "wakang", "wakangtaka@gmail.com")
# print(type(user1))
#
# user3 = User('jane', 'Jane Doe', 'jane@doe.com')
# user3.introduce_yourself('David')

database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')
print(user)

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))
user = database.find('siddhant')
print(user)

database.insert(biraj)
print(database.list_all())