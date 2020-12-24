from bot import create_bot

def main():
    TOKEN = '1299551318:AAH9bGbI3W68qElo7MY3KwCmPaDwAXRkQE0'
    updater = create_bot(TOKEN)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()