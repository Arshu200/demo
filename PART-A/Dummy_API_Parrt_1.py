import requests
from pymongo import MongoClient

# Define your API credentials
app_id = "6513d85d7214df66eaf75898"
api_url_users = "https://dummyapi.io/data/v1/user"
api_url_posts = "https://dummyapi.io/data/v1/user/{user_id}/post"

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/Tailnode")
db = client["dummyapi"]

# Fetch Users Data and Store in MongoDB
def fetch_and_store_users():
    headers = {"app-id": app_id}
    response = requests.get(api_url_users, headers=headers)

    if response.status_code == 200:
        users_data = response.json()["data"]

        # Create or access the "users" collection in MongoDB
        users_collection = db["users"]

        # Insert user data into the collection
        users_collection.insert_many(users_data)
        print("Users data stored in MongoDB")
    else:
        print("Failed to fetch users data from the API")

# Fetch User Posts Data and Store in MongoDB
def fetch_and_store_user_posts():
    # Access the "users" collection
    users_collection = db["users"]
    users = users_collection.find()

    headers = {"app-id": app_id}

    for user in users:
        user_id = user["id"]
        response = requests.get(api_url_posts.format(user_id=user_id), headers=headers)

        if response.status_code == 200:
            posts_data = response.json()["data"]

            # Create or access the "posts" collection in MongoDB
            posts_collection = db["posts"]

            # Insert posts data into the collection, associating with the user
            for post in posts_data:
                post["user_id"] = user_id
            posts_collection.insert_many(posts_data)
            print(f"Posts data for user {user_id} stored in MongoDB")
        else:
            print(f"Failed to fetch posts data for user {user_id} from the API")

if __name__ == "__main__":
    fetch_and_store_users()
    fetch_and_store_user_posts()
