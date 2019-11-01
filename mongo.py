import pymongo


class Connection:

    def __init__(self, ):
        self.client = pymongo.MongoClient("mongodb://24.136.37.135:27017/?replicaSet=replicaSet")
        self.db = self.client['chat-app']
        self.messages = self.db['messages']
        self.users = self.db['users']

    def get_message(self, max_limit=50):
        results = self.messages.find({}, limit=max_limit)  # Get the messages
        results = results.sort('date', pymongo.ASCENDING)
        return results

    def add_message(self, author, content):
        message = {
            'user': author,
            'content': content
        }
        self.messages.insert_one(message)
