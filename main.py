from bot import create_bot

def main():
    TOKEN = 'your_token'
    updater = create_bot(TOKEN)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
