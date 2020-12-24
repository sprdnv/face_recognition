import requests
import numpy as np
from PIL import Image
from io import BytesIO
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from models import detection, features, make_predictions

def start_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Привет! Загрузи фото и увидишь, что я могу')

def text_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Уважай мое время, я не общаться сюда пришел')

def photo_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Принято, ожидайте')
    file_id = context.bot.get_file(update.message.photo[0].file_id)
    response = requests.get(file_id['file_path'])
    try:
        face = detection(np.asarray(Image.open(BytesIO(response.content))))
        Image.fromarray(face).save('img.jpg')
        face_emb = features(face)
        predictions = make_predictions(face_emb)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text=predictions)
        context.bot.send_photo(chat_id=update.effective_chat.id, 
                               photo=open('img.jpg', 'rb'))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='Кажется, здесь нет лица... Попробуйте еще раз')

def create_bot(TOKEN):
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start_message)
    text_handler = MessageHandler(Filters.text & (~Filters.command), text_message)
    photo_handler = MessageHandler(Filters.photo, photo_message)
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)
    dispatcher.add_handler(photo_handler)
    
    return updater