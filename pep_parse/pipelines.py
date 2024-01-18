import csv
import datetime as dt
from collections import defaultdict

from .constants import BASE_DIR, DATETIME_FORMAT, RESULTS_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        """Создает словарь для статусов PEP."""
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        """Обрабатывает данные статусов PEP для таблицы."""
        self.statuses[item['status']] += 1
        if not item['status']:
            raise KeyError

        return item

    def close_spider(self, spider):
        """
        Сохраняет данные статусов PEP в таблицу.
        Таблицу сохраняет в CSV-файл
        """
        status_summary = [('Статус', 'Количество')]
        status_summary.extend(self.statuses.items())
        status_summary.append(('Total', sum(self.statuses.values())))
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(status_summary)
