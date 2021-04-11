class TwitterUser():
    def __init__(self, name, bio): #required at object creation
        self.name = name
        self.bio = bio
        self.tweets = []
        
    def add_tweet(self, text):
        self.tweets.append(text)
        
    def delete_tweet(self):
        self.tweets.pop()
        
        
#self is not used outside class template 
        
ash = TwitterUser('Ash', 'Software Developer in NYC')
ash.add_tweet('Today was the longest day of the summer.')
print(ash.tweets[0])


serena = TwitterUser('Serena', 'Student in NYC')
serena.add_tweet("Mister Softeees is back!")
print(serena.tweets)

serena.add_tweet("I want pizza")
print(serena.tweets)

serena.delete_tweet()
print(serena.tweets)


print(type(serena) == TwitterUser)