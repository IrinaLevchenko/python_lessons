import os
import datetime


class Logger:
    day = 0
    month = 0
    year = 0
    hour = 0
    minute = 0
    second = 0
    path = None
    current_file = None

    def __init__(self, path='.'):
        Logger.fill_date()
        Logger.path = path
        if path != '.':
            if not os.path.exists(path):
                os.makedirs(f'./{path}')
            Logger.path = f'./{path}'
        Logger.create_new_log_file()

    @classmethod
    def create_new_log_file(cls):
        Logger.current_file = f'log_{Logger.day}.{Logger.month}.{Logger.year}.log'
        if not os.path.exists(Logger.full_file_path()):
            with open(Logger.full_file_path(), 'w'):
                pass

    @staticmethod
    def today():
        current_date = datetime.datetime.now()
        return {'day': current_date.day,
                'month': current_date.month,
                'year': current_date.year,
                'hour': current_date.hour,
                'minute': current_date.minute,
                'second': current_date.second}
    
    @classmethod
    def fill_date(cls, second=None):
        current_date = cls.today()
        cls.day = current_date.get('day')
        cls.month = current_date.get('month')
        cls.year = current_date.get('year')
        cls.hour = current_date.get('hour')
        cls.minute = current_date.get('minute')
        cls.second = current_date.get('second')

    @classmethod
    def full_file_path(cls):
        return cls.path + '/' + cls.current_file

    @classmethod
    def check_day(cls):
        if cls.day != cls.today().get('day'):
            return True

    def write_log(self, event):
        if Logger.check_day():
            Logger.fill_date()
            Logger.create_new_log_file()
        with open(self.full_file_path(), 'a', encoding='UTF-8') as f:
            self.fill_date()
            f.write(f'[{Logger.hour}:{Logger.minute}:{Logger.second}] {event} \n')


l = Logger('logs')
l.write_log('Some danger event')
l.write_log('Everything ok')

print()

