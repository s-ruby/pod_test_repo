ash = {
    'name': 'Ash',
    'bio': 'Software Developer in NYC',
    'tweets': []
}

def add_tweet(user, text):
        user['tweets'].append(text)
        

add_tweet(ash, 'Today was the longest day of the summer.')

        

print(ash['name'])
print(ash['bio'])
print(ash['tweets'][0])

serena = {
    'name': 'Serena',
    'bio': 'Student in NYC',
    'tweets': []
}

add_tweet(serena, 'Mister Softee is back!')

print(serena['tweets'][0])