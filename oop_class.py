class TwitterUser():
    def __init__(self, name, bio): #required at object creation
        self.name = name
        self.bio = bio
        self.tweets = []
        
    def add_tweet(self, text):
        self.tweets.append(text)
        
    def delete_tweet(self):
        self.tweets.pop()
        
ash = TwitterUser('Ash', 'Software Developer in NYC')
ash.add_tweet('Today was the longest day of the summer.')

paul = TwitterUser('Paul', 'PhD student at Columbia University')
paul.add_tweet('Cambridge looks great during fall!')

print(ash.name)
print(ash.bio)
print(ash.tweets[0])
print(paul.name)
print(paul.bio)
print(paul.tweets[0])


serena = TwitterUser('Serena', 'Student at Columbia')
serena.add_tweet('Mister Softee is back!')
serena.add_tweet('Why is the sky blue?')

print(serena.tweets)

serena.delete_tweet()

print(serena.tweets)

