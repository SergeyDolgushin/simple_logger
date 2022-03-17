import os
from datetime import datetime 

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

def write_log_to_file(text_str, file_name = 'log.txt', path = os.getcwd()):
    '''Записываем результирующую строку в файл'''
    path_to_file = os.path.join(path, file_name)
    with open(path_to_file, 'a') as text:
        return text.write(text_str)

def make_trace(checked_function):

    def new_function(*args, **kwargs):
        start_time = datetime.now().time()
        result = checked_function(*args, **kwargs)
        delimiter_str = '*' * 30
        text_str = f'вызвана функция {checked_function.__name__}, дата: {datetime.now().date()}, время: {start_time}\nс аргументами {args}\nПолучили {result}\n{delimiter_str}\n'
        write_log_to_file(text_str, file_name = 'log.txt', path = os.getcwd())
        return result

    return new_function

def make_trace_with_param(file_name = 'log.txt', path = os.getcwd()):

    def make_trace2(checked_function):

        def new_function(*args, **kwargs):
            start_time = datetime.now().time()
            result = checked_function(*args, **kwargs)
            delimiter_str = '*' * 30
            text_str = f'вызвана функция {checked_function.__name__}, дата: {datetime.now().date()}, время: {start_time}\nс аргументами {args}\nПолучили {result}\n{delimiter_str}\n'
            write_log_to_file(text_str, file_name, path)
            return result

        return new_function

    return make_trace2

@make_trace_with_param('log1.txt')
def deepListsGenerator (obj):
    for item in obj:
        if isinstance(item, list):
            yield from deepListsGenerator(item)
        else:    
            yield item

if __name__ == '__main__':

    for item in deepListsGenerator(nested_list):
        print(item)