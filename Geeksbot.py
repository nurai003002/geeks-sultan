import asyncio
import logging
from aiogram import Bot, Dispatcher,F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart
from config import token


bot = Bot(token=token)
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='Backend info'),KeyboardButton(text='Frontend info'),KeyboardButton(text='UX-UI info'),KeyboardButton(text='Контакты')]
]
keybord = ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)
@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply(f'''Привет {message.from_user.full_name}, я бот IT academy Geeks,
у вас на клавиатуре появились кнопки,
нажмите на них, чтобы узнать информацию об направлениях или о нас''', reply_markup=keybord)

@dp.message(F.text == 'Backend info')
async def but(message: Message):
    await message.reply('''Бэкэнд с Python в Geeks.IT Академии

Приветствуем в Geeks.IT Академии! Если вы хотите узнать, как создавать серверные приложения с использованием Python, вот основные моменты, которые мы охватываем:

- почему Python?

Python — один из самых популярных языков для бэкэнд-разработки благодаря своей простоте, гибкости и большому количеству библиотек и фреймворков.

- Основные фреймворки и библиотеки:

- Django: Полноценный фреймворк для создания веб-приложений. Предлагает множество встроенных функций, таких как админ-панель и ORM.
- Flask: Легковесный фреймворк для создания гибких и быстрых приложений. Отличается минимализмом и возможностью добавления нужных компонентов по мере необходимости.

-Что вы будете изучать:

1. Основы Python: Синтаксис, работа с файлами, модули и пакеты.
2. Создание API: Использование Flask или Django для создания RESTful API.
3. Работа с базами данных: Использование SQL (с помощью Django ORM или SQLAlchemy для Flask) и взаимодействие с реляционными базами данных.
4. Аутентификация и авторизация: Реализация систем безопасности для защиты данных и управления доступом.
5. Скалируемость и производительность: Оптимизация приложений и работа с кэшированием.

-Практика:

В наших курсах вы будете создавать реальные проекты, которые помогут вам применить знания на практике и подготовят вас к реальным задачам в бэкэнд-разработке.

Готовы стать экспертом в бэкэнде на Python? Присоединяйтесь к Geeks.IT Академии и начните свой путь к успешной карьере в IT! 🚀''')
@dp.message(F.text == 'Frontend info')
async def dt(message: Message):
    await message.reply('''### Фронтэнд с Geeks.IT Академией

Здравствуйте в Geeks.IT Академии! Если вы хотите освоить фронтэнд-разработку, мы подготовили для вас всё необходимое:

-Почему фронтэнд?

Фронтэнд — это то, что пользователи видят и с чем взаимодействуют. Это ключ к созданию привлекательных и удобных веб-интерфейсов.

-Основные технологии и инструменты:

- HTML: Основы разметки страниц. Структура и семантика контента.
- CSS: Стилизация и оформление. Flexbox, Grid и адаптивный дизайн.
- JavaScript: Основы программирования и взаимодействие с пользователем. 
- Фреймворки и библиотеки:
  - React: Популярная библиотека для создания пользовательских интерфейсов. Компонентный подход и управление состоянием.
  - Vue.js: Гибкий фреймворк для создания интерактивных интерфейсов. Простота и расширяемость.
  - Angular: Мощный фреймворк для создания масштабируемых приложений. Встроенные возможности и структурированность.

-Что вы будете изучать:

1. Основы HTML и CSS: Разметка страниц, стилизация и создание адаптивных дизайнов.
2. JavaScript: Основы языка, работа с DOM, асинхронное программирование.
3. Разработка SPA (Single Page Applications): Создание одностраничных приложений с помощью React, Vue.js или Angular.
4. Взаимодействие с API: Получение данных с сервера и обновление интерфейса.
5. Инструменты разработки: Использование Webpack, Babel и других инструментов для сборки и оптимизации кода.

-Практика:

В наших курсах вы будете создавать реальные проекты, от простых веб-страниц до сложных одностраничных приложений, что позволит вам применять полученные знания на практике.

Готовы стать мастером фронтэнда? Присоединяйтесь к Geeks.IT Академии и начните свой путь к созданию потрясающих веб-интерфейсов! 🚀''')
@dp.message(F.text == 'UX-UI info')
async def s(message: Message):
    await message.reply('''### UX/UI Дизайн в Geeks.IT Академии

Добро пожаловать в Geeks.IT Академию! Если вы хотите освоить UX/UI дизайн, мы предлагаем вам комплексное обучение, чтобы создать действительно впечатляющие и удобные пользовательские интерфейсы.

- Почему UX/UI Дизайн?

UX/UI дизайн — это искусство и наука создания интерфейсов, которые не только красивы, но и удобны для пользователя. Хороший дизайн улучшает взаимодействие с продуктом и способствует его успеху.

- Основные аспекты UX/UI дизайна:

- UX (User Experience): Фокус на том, как пользователь взаимодействует с продуктом и как он ощущает этот опыт. 
  - Исследование пользователей: Проведение интервью, опросов и тестирования для понимания потребностей и поведения пользователей.
  - Создание прототипов: Разработка и тестирование интерактивных прототипов, чтобы определить, как пользователи будут взаимодействовать с продуктом.
  - Юзабилити-тестирование: Проверка удобства использования продукта на реальных пользователях и получение обратной связи.

- UI (User Interface): Фокус на визуальном оформлении и элементарных компонентах интерфейса.
  - Дизайн интерфейсов: Создание визуальных элементов, таких как кнопки, иконки и макеты.
  - Системы дизайна: Разработка и использование библиотек компонентов и стилей для обеспечения консистентности интерфейса.
  - Принципы дизайна: Основы композиции, цвета, типографики и иерархии.

- Что вы будете изучать:

1. Основы UX-дизайна: Исследование пользователей, создание персонажей и пользовательских сценариев.
2. Проектирование интерфейсов: Разработка прототипов и макетов с использованием инструментов таких как Figma, Adobe XD или Sketch.
3. Принципы UI-дизайна: Работа с цветом, типографикой и элементами интерфейса.
4. Юзабилити и тестирование: Проведение тестов и сбор обратной связи для улучшения пользовательского опыта.
5. Создание дизайна для разных платформ: Адаптация дизайна для мобильных и веб-приложений.

- Практика:

В наших курсах вы будете работать над реальными проектами, создавая прототипы и макеты, которые помогут вам понять, как применять теоретические знания на практике.

Готовы стать мастером UX/UI дизайна? Присоединяйтесь к Geeks.IT Академии и начните создавать удобные и красивые пользовательские интерфейсы! 🚀''')
@dp.message(F.text == 'Контакты')
async def contacts(message: Message):
    await message.reply('''Наши контакты:
+996225082021''')
@dp.message()
async def starting():
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(starting())
    except KeyboardInterrupt:
        print("Exit")