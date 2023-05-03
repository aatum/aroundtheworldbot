import requests
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = ""
BOT_USERNAME: Final = "@rrroundtheworldbot"

# /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there! I'm a bot that can give you information about countries.")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I have three features. Try sending me a message like 'Tell me about Finland' and I will do my best to provide information about the country you asked for! If you want to know which languages are speaken in different countries, send me a message like 'Countries that speak Spanish'. If continents are a thing you are interested in, try to type a message like 'Countries in Africa'.")

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if text.lower().startswith("tell me about "):
        country_name: str = text[len("tell me about "):]
        response: str = get_country_info(country_name)
        print('Bot:', response)
        await update.message.reply_text(response)

    elif text.lower().startswith("hello"):
        response: str = ("Hey! Type /start or /help to see what this bot is about!")
        print('Bot:', response)
        await update.message.reply_text(response)

    elif text.lower().startswith("bye"):
        response: str = ("Bye! Until next time!")
        print('Bot:', response)
        await update.message.reply_text(response)

    elif text.lower().startswith("tell me about "):
        country_name: str = text[len("tell me about "):]
        response: str = get_country_info(country_name)
        print('Bot:', response)
        await update.message.reply_text(response)

    elif text.lower().startswith("countries that speak "):
        language_name: str = text[len("countries that speak "):]
        response: str = get_countries_by_language(language_name)
        print('Bot:', response)
        await update.message.reply_text(response)

    elif text.lower().startswith("countries in "):
        continent_name: str = text[len("countries in "):]
        response: str = get_countries_by_continent(continent_name)
        print('Bot:', response)
        await update.message.reply_text(response)

    else:
        # Reply with a generic message
        await update.message.reply_text("I'm sorry, I didn't understand. Please try again with a message like Tell me about Finland'.")

# Get information about a country using the RestCountries API
def get_country_info(country_name: str) -> str:
    encoded_country_name = requests.utils.quote(country_name)
    url: str = "https://restcountries.com/v3.1/name/{}?fullText=true".format(encoded_country_name)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        # Extract information from the API response and format it as a string
        population = data["population"]
        if population > 1_000_000:
            population_str = f"{population // 1_000_000:,} million"
        elif population > 0:
            population_str = f"{population // 1_000:,} thousand"
        else:
            population_str = "Unknown"        
        return f"Name: {data['name']['common']}\nCapital: {data['capital'][0]}\nRegion: {data['region']}\nPopulation: {population_str}"
    else:
        return "Sorry, I couldn't find information about that country. Check your message for possible typos."

def get_countries_by_language(language: str) -> str:
    url = f"https://restcountries.com/v3.1/lang/{language.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        countries = response.json()
        country_list = [country["name"]["common"] for country in countries]
        country_str = ', '.join(sorted(country_list))
        return f"The following countries have {language.capitalize()} as an official language: {country_str}."
    else:
        return "Sorry, I couldn't find information about countries with that language."
    
def get_countries_by_continent(continent: str) -> str:
    url = f"https://restcountries.com/v3.1/region/{continent.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        countries = response.json()
        country_names = [country["name"]["common"] for country in countries]
        return f"The countries in {continent.capitalize()} are: {', '.join(sorted(country_names))}."
    elif continent.lower() == "antarctica":
        return "There are no countries in Antarctica."
    else:
        return f"Unable to retrieve countries in {continent.capitalize()}."

    
# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

# Run the program
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print("Starting...")
    # Run the bot
    app.run_polling(poll_interval=5)