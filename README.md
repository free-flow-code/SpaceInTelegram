# Космический Телеграм

Программа автоматически скачивает фотографии космоса
с сайтов SpaceX и NASA. И публикует их в Telegram-канал.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для работы понадобится API-ключ с [сайта NASA](https://api.nasa.gov/)
И токен телеграм-бота. Взять можно [здесь.](https://telegram.me/BotFather)
Затем в директории с программой создайте `.env` файл следующего
содержания:
```
NASA_API_KEY="you_key"
TG_TOKEN="you_token"
POSTING_DELAY="14400"
```
Программа состоит из нескольких скриптов:

###`fetch_spacex_images.py`
Загружает фотографии с сайта SpaceX.
В качестве аргумента при запуске скрипта нужно указать id запуска.
Если id запуска не указан, загружает фото с последнего запуска.
```
python fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```

###`fetch_apod_images.py`
Загружает фото Astronomy Picture of the Day [(APOD)](https://api.nasa.gov/#apod)
```
python fetch_apod_images.py
```
###`fetch_epic_images.py`
Загружает фото Earth Polychromatic Imaging Camera [(EPIC)](https://api.nasa.gov/#epic)

```
python fetch_epic_images.py
```

###`telegram_bot.py`
Публикует фото из директории `./image` в telegram-канал.
В качестве аргумента при запуске скрипта нужно передать имя файла
с изображением. Если оно не указано, публикует случайное фото:
```
python telegram_bot.py AndromedaGalex_900.jpg
```

###`deferred_posting.py`
Публикует все фотографии из директории `./image` каждые 4 часа.
Если все фото из директории опубликованы – он начинает публиковать их заново, перемешав фото в случайном порядке.
Частоту публикации можно контролировать с помощью переменной среды (`.env` файл):
```
POSTING_DELAY="14400"
```
или передать в качестве аргумента командной строки. Время задержки между публикациями должно быть указано в секундах:
```
python deferred_posting.py 14400
```
###`file_processing.py`
Файл с вспомогательными функциями, необходимыми для работы вышеперечисленных скриптов.

Все загруженные фото хранятся в директории `./image`
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).