from dashboard.models import Region, Source, Resource, ModelDataTest
from tqdm import tqdm
import requests
import pandas as pd
from datetime import datetime
import pytz
import time
from concurrent.futures import ThreadPoolExecutor
import re
import warnings
warnings.filterwarnings('ignore')
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from autocorrect import Speller
import pymorphy3
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification
nltk.download('stopwords')
nltk.download('punkt')

def map_emotion_to_tonality(emotion_class):
    emotion_to_tonality_map = {
        0: 0,
        1: 1,
        2: 2,
        3: 1,
        4: 2,
        5: 2,
    }
    return emotion_to_tonality_map[emotion_class]

# Определите максимальное количество потоков для многопоточности
MAX_THREADS = 5

def get_prediction_tonality(text, model_name = 'dashboard/model_dl/rubert-tiny2-cedr-emotion-detection/'):
    # Загрузка токенизатора и модели
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Кодирование входного текста
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)

    # Получение предсказания модели
    outputs = model(**inputs)
    logits = outputs.logits

    # Выбор наиболее вероятного класса
    predicted_class = logits.argmax().item()
    result = map_emotion_to_tonality(predicted_class)
    return result

def get_prediction(text, model_path = 'dashboard/model_dl/fine-tune_model_category/', weights_path='dashboard/model_dl/fine-tune-bert_category.pth'):
    # Загрузка токенизатора
    tokenizer = BertTokenizer.from_pretrained(model_path + 'tokenizer_config.json')

    # Загрузка сохраненных весов модели PyTorch
    model_state_dict = torch.load(weights_path, map_location='cpu')

    # Создание экземпляра модели Transformers
    model = BertForSequenceClassification.from_pretrained(model_path, state_dict=model_state_dict)

    # Кодирование входного текста
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)

    # Получение предсказания модели
    outputs = model(**inputs)
    logits = outputs.logits

    # Выбор наиболее вероятного класса
    predicted_class = logits.argmax().item()
    return predicted_class

def preprocess_text(text):
    # 1. Преобразование в нижний регистр
    text = text.lower()

    # 2. Удаление пунктуации и специальных символов
    text = re.sub(r'[^A-Za-z0-9А-Яа-я\s]', '', text)

    # 3. Удаление чисел
    text = re.sub(r'\d+', '', text)

    # 4. Удаление коротких слов
    text = ' '.join([word for word in text.split() if len(word) > 1])

    # 5. Удаление стоп-слов
    stop_words = set(stopwords.words('russian'))
    text = ' '.join([word for word in text.split() if word not in stop_words])

    # 6. Токенизация
    tokens = word_tokenize(text)

    # 7. Исправление опечаток в словах
    spell = Speller(lang='ru')
    tokens = [spell(token) for token in tokens]

    # 8. Лемматизация с использованием pymorphy3
    morph = pymorphy3.MorphAnalyzer()
    tokens = [morph.parse(word)[0].normal_form for word in tokens]

    # Объединение токенов в текст
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text

def save_data(data, time, resource, text, comment_text, type_text, category, tonality):
    ModelDataTest.objects.create(
        data=data,
        time=time,
        region=Region.objects.get(name=resource.source.region.name),
        source=resource.source,
        resource=resource,
        text=text,
        comment_text=comment_text,
        type_text=type_text,
        category=category,
        tonality=tonality
    )


def get_group_id(token, version, group_name):
    params = {
        'access_token': token,
        'v': version,
        'group_id': group_name
    }

    response = requests.get('https://api.vk.com/method/groups.getById', params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['error_msg']}")
        return None

    return -data['response'][0]['id']

def get_comments(token, version, owner_id, post_id):
    params = {
        'access_token': token,
        'v': version,
        'owner_id': owner_id,
        'post_id': post_id,
        'count': 100,
        'extended': 1
    }

    response = requests.get('https://api.vk.com/method/wall.getComments', params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['error_msg']}")
        return []

    comments = data['response']['items']
    return comments

def get_comment_likes(token, version, owner_id, comment_id):
    params = {
        'access_token': token,
        'v': version,
        'type': 'comment',
        'owner_id': owner_id,
        'item_id': comment_id,
        'filter': 'likes',
        'extended': 1,
        'count': 0
    }

    response = requests.get('https://api.vk.com/method/likes.getList', params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['error_msg']}")
        return 0

    likes_count = data['response']['count']
    return likes_count

def get_reply_likes(token, version, owner_id, reply_id):
    params = {
        'access_token': token,
        'v': version,
        'type': 'comment',
        'owner_id': owner_id,
        'item_id': reply_id,
        'filter': 'likes',
        'extended': 1,
        'count': 0
    }

    response = requests.get('https://api.vk.com/method/likes.getList', params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['error_msg']}")
        return 0

    likes_count = data['response']['count']
    return likes_count

def get_comment_replies(token, version, owner_id, comment_id):
    params = {
        'access_token': token,
        'v': version,
        'owner_id': owner_id,
        'comment_id': comment_id,
        'count': 100,
        'extended': 1
    }

    response = requests.get('https://api.vk.com/method/wall.getComments', params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['error_msg']}")
        return []

    replies = data['response']['items']
    return replies

def get_vk_wall_posts(token, version, owner_id, end_date, group_name, resource):
    print(f"Starting data collection for group: {group_name}")
    path_category = 'dashboard/model_dl/fine-tune_model_category/'
    path_category_weights = 'dashboard/model_dl/fine-tune-bert_category.pth'
    params = {
        'access_token': token,
        'v': version,
        'owner_id': owner_id,
        'count': 100,
        'extended': 1,
        'fields': 'post_type,comments,likes,reposts,views',
        'filter': 'all'
    }
    last_post_id = None

    posts = []
    moscow_tz = pytz.timezone('Europe/Moscow')
    last_post_date = end_date

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        while True:
            params['offset'] = last_post_id  # Смещение устанавливается на количество уже полученных постов
            response = requests.get('https://api.vk.com/method/wall.get', params=params)
            data = response.json()

            if 'error' in data:
                print(f"Error: {data['error']['error_msg']}")
                break

            items = data['response']['items']

            if not items or last_post_date is None:
                print(f"No more posts in group {group_name}. Stopping data collection for this group.")
                break

            for item in tqdm(items, desc=f"Processing posts in {group_name}"):
                post_text = str(item['text'])
                post_date = datetime.fromtimestamp(item['date'], moscow_tz)
                post_time = post_date.strftime("%H:%M:%S")

                if post_date.date() < last_post_date.date() or (post_date.date() == last_post_date.date() and post_time <= last_post_date.time().strftime("%H:%M:%S")):
                    last_post_date = None  # Установка значения None для остановки сбора
                    print("!!!!!!!!!!!!!!!!!!!!!!СБОР ЗАКОНЧЕН!!!!!!!!!!!!!!!!!!")
                    break

                # Предобработка
                post_preprocess_text = preprocess_text(post_text)
                # Классификация
                predicted_class_category = get_prediction(text=post_preprocess_text, model_path=path_category, weights_path = path_category_weights)
                predicted_class_tonality = get_prediction_tonality(text=post_preprocess_text)
                save_data(
                    data=post_date.strftime("%Y-%m-%d"),
                    time=post_time,
                    resource=resource,
                    text=post_text,
                    comment_text="",
                    type_text='Пост',
                    category=predicted_class_category,
                    tonality=predicted_class_tonality)
                time.sleep(3)

                if item['comments']['count'] > 0:
                    # Используйте многопоточность для получения комментариев и лайков
                    comments_list = list(executor.map(lambda post_id: get_comments(token, version, owner_id, post_id), [item['id']]))
                    for comments in comments_list:
                        for comment in tqdm(comments, desc=f"Processing comments in {group_name}"):
                            comment_text = str(comment['text'])
                            comment_likes = get_comment_likes(token, version, owner_id, comment['id'])
                            comment_date = datetime.fromtimestamp(comment['date'], moscow_tz)
                            comment_time = comment_date.strftime("%H:%M:%S")
                            # Предобработка
                            comment_preprocess_text = preprocess_text(comment['text'])
                            # Классификация
                            predicted_class_category = get_prediction(text=comment_preprocess_text, model_path=path_category, weights_path = path_category_weights)
                            predicted_class_tonality = get_prediction_tonality(text=comment_preprocess_text)
                            save_data(
                                data=comment_date.strftime("%Y-%m-%d"),
                                time=comment_time,
                                resource=resource,
                                text=post_text,
                                comment_text=comment['text'],
                                type_text='Комментарий',
                                category=predicted_class_category,
                                tonality=predicted_class_tonality)
                            time.sleep(3)

                            replies = get_comment_replies(token, version, owner_id, comment['id'])
                            for reply in tqdm(replies, desc=f"Processing replies in {group_name}"):
                                reply_text = str(reply['text'])
                                reply_likes = get_reply_likes(token, version, owner_id, reply['id'])
                                reply_date = datetime.fromtimestamp(reply['date'], moscow_tz)
                                reply_time = reply_date.strftime("%H:%M:%S")
                                # Предобработка
                                reply_preprocess_text = preprocess_text(reply['text'])
                                # Классификация
                                predicted_class_category = get_prediction(text=reply_preprocess_text, model_path=path_category, weights_path = path_category_weights)
                                predicted_class_tonality = get_prediction_tonality(text=reply_preprocess_text)
                                save_data(
                                    data=reply_date.strftime("%Y-%m-%d"),
                                    time=reply_time,
                                    resource=resource,
                                    text=post_text + "\n\nКОММЕНТАРИЙ:\n" + comment_text,
                                    comment_text=reply['text'],
                                    type_text='Ответ на комментарий',
                                    category=predicted_class_category,
                                    tonality=predicted_class_tonality)
                                time.sleep(3)
                last_post_id = item['id']  # Сохраняем идентификатор последнего обработанного поста

        return posts
