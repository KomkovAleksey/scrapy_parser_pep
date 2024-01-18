# 👨‍💻 [Проект scrapy_parser_pep.](https://github.com/KomkovAleksey/scrapy_parser_pep)

## Оглавление

- [Автор](#Автор)
- [Технологии](#технологии)
- [Описание проекта](#Описание-проекта)
- [Запуск проекта](#Запуск-проекта)
- [Примеры команд](#Примеры-команд)



## Технологии:

- Python 3.9.10
- Scrapy 2.5.1

## Описание проекта:

Проект парсинга информации о всех [PEP](https://peps.python.org/)(номер, имя, статус, клоличество PEP c определенным статусом).

### Запуск проекта:
Клонируйте [репозиторий](https://github.com/KomkovAleksey/scrapy_parser_pep) и перейдите в него в командной строке:
```
git clone https://github.com/KomkovAleksey/scrapy_parser_pep

cd scrapy_parser_pep
```
Создайте виртуальное окружение и активируйте его:
```
python -m venv vevn

source venv/Scripts/activate
```
Обновите pip:
```
python -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```
Проект готов к работе!

## Примеры команд
Создает в папке results два файла:

1) pep_ДатаВремя.csv - csv файл со списком всех PEP
2) status_summary_ДатаВремя.csv - csv файл с таблицей из двух колонок «Статус» и «Количество»
```
scrapy crawl pep
```




## Автор

[Алексей Комков](https://github.com/KomkovAleksey)