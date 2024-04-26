from dotenv import dotenv_values

BOT_TOKEN = dotenv_values()["KEY"]
MONGODB_USERNAME = dotenv_values()["MONGODB_USERNAME"]
MONGODB_PASSWORD = dotenv_values()["MONGODB_PASSWORD"]


SITE_URL = "https://ukr-mova.in.ua/"
SITE_API_EXAMPLES = "https://ukr-mova.in.ua/api-new?route=examples"
SITE_API_CATEGORIES = "https://ukr-mova.in.ua/api-new?route=categories"

MONGO_CLIENT = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@mongodb:27017/"
MONGO_DATABASE = "urkChatBot"

AUTH_INCLUDED = False
LOG_INCLUDED = True
