from datetime import datetime as dt
from pathlib import Path
from sys import path
from time import sleep


class Journal:
    default_path = Path(path[0]) / 'journal.log'
    default_datetime_format = '%Y.%m.%d %H:%M:%S'
    
    @classmethod
    def add_entry(cls, text, path=None, datetime_format=None):
        if path is None:
            path = cls.default_path
        
        if datetime_format is None:
            datetime_format = cls.default_datetime_format
        
        text = f'{dt.now():{datetime_format}} — {text}\n'
        
        with open(path, 'a', encoding='utf-8') as fileout:
            fileout.write(text)


Journal.add_entry('первая запись: от класса')

sleep(2)

logger = Journal()
logger.add_entry('вторая запись: от экземпляра')

