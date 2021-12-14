# Library_parser

Парсит сайт tululu.org получая основную информацию о книгах жанра научной фантасти со страниц в определенном диапозоне и рендерит создает сервер с страницами с карточками книг



## Варианты установки:


- Скачать архив с кодом ( "Зеленая кнопка Code" -> "Download ZIP" ) и распоковать его

- Скачать репозиторий:

  - cd <Директория установки >

  - git clone https://github.com/LuFent/Library.git

## Как пользваться (предпологается что python уже скачан):

- cd <Директория>

- ```pip install -r requirements.txt```

- ```python parse.py --start_page <...> --end_page <...>```

  --start_page - Номер страницы с книгами с которой начнется парсинг

  --end_page - Номер страницы с книгами на которой закончится парсинг.
  &nbsp;

  если параметры не указывать то они примут значение 1 и 5 соответсвенно

  Например, при параметрах:

  ```python parse.py --start_page 1 --end_page 6```
  Скрипт скачает все книги с 1ой по 6ую страницу.

- ```python run.py``` - команда запустит сервер


Пример готового сайта можно посмотреть по ссылке

 https://lufent.github.io/Library_gh_pages_website/pages/index1.html
