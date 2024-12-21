class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        pass
    def post(self):
        pass

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self):
        pass

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self):
        pass