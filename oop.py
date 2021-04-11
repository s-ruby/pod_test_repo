#procedeural programming

ash = {
    'name': 'Ash',
    'bio': 'Software Developer in NYC',
    'tweets': []
}

def add_tweet(user, text):
        user['tweets'].append(text)
        

add_tweet(ash, 'Today was the longest day of the summer.')


serena = {
    'name': 'Serena',
    'bio': 'Student in NYC',
    'tweets': []
}

add_tweet(serena, "Mister Softees is back!")

print(serena["tweets"])