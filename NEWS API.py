import requests

# API key for the NewsAPI
api_key = '00c0fbc912a044d4ab2b07f56a643b87'

# Topics for which you want to fetch news
topics = ['technology', 'sports', 'business']

# Iterate over the topics and fetch news for each
for topic in topics:
    # URL to fetch news for a specific topic
    url = f'https://newsapi.org/v2/top-headlines?apiKey={api_key}&category={topic}&pageSize=5'
    
    # Make the GET request
    response = requests.get(url)
    
    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        data = response.json()  # Get the response data in JSON format
        
        # Extract and print the news articles
        articles = data['articles']
        print(f'----- {topic.capitalize()} News -----')
        for article in articles:
            title = article['title']
            description = article['description']
            print(f'Title: {title}')
            print(f'Description: {description}')
            print('---')
    else:
        # Request failed
        print('Request failed with status code:', response.status_code)
