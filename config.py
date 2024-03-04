from dotenv import dotenv_values

BOT_TOKEN = dotenv_values()["KEY"]

SITE_URL = "https://ukr-mova.in.ua/"
SITE_API_EXAMPLES = "https://ukr-mova.in.ua/api-new?route=examples"
SITE_API_CATEGORIES = "https://ukr-mova.in.ua/api-new?route=categories"

MONGO_CLIENT = "mongodb://localhost:27017/"
MONGO_DATABASE = "urkChatBot"
