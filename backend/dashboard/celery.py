from celery import Celery
from celery.schedules import crontab
import torch
from transformers import BertForSequenceClassification, BertTokenizer

# Путь к сохраненной модели
model_path = "../model_dl/fine-tune-bert_tonality.pth"

# Загрузка модели
model = BertForSequenceClassification.from_pretrained(
    'DeepPavlov/rubert-base-cased-sentence', 
    num_labels=4  
)
model.load_state_dict(torch.load(model_path))
# Токенизация текста
tokenizer = BertTokenizer.from_pretrained('DeepPavlov/rubert-base-cased-sentence')

# Создание экземпляра Celery
celery = Celery('tasks', broker='redis://localhost:6379/0')

# Определение задачи для проверки мусора
@celery.task
def check_garbage(text):
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits).item()
    return is_garbage

# Определение задачи для определения категории
@celery.task
def determine_category(text):
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits).item()
    return category

# Определение задачи для определения тональности
@celery.task
def determine_tonality(text):
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits).item()
    return tonality

@celery.task
def process_text(text):
    is_garbage = check_garbage.delay(text).get()
    category = determine_category.delay(text).get()
    tonality = determine_tonality.delay(text).get()

# Настройка периодического выполнения задачи
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Запуск задачи process_text каждый день в полночь
    sender.add_periodic_task(
        crontab(hour=0, minute=0),
        process_text.s(parse_text)
    )