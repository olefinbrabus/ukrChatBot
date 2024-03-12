from dotenv import dotenv_values

BOT_TOKEN = dotenv_values()["KEY"]
MONGODB_USERNAME = dotenv_values()["MONGODB_USERNAME"]
MONGODB_PASSWORD = dotenv_values()["MONGODB_PASSWORD"]


SITE_URL = "https://ukr-mova.in.ua/"
SITE_API_EXAMPLES = "https://ukr-mova.in.ua/api-new?route=examples"
SITE_API_CATEGORIES = "https://ukr-mova.in.ua/api-new?route=categories"

MONGO_CLIENT = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@localhost:27017/"
MONGO_DATABASE = "urkChatBot"

if __name__ == "__main__":
    print(MONGO_CLIENT)