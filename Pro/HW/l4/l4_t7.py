import re


def error_status(input_file: str) -> str:
    """
    Определение статуса ошибок.
    :param input_file:
    :return:
    """
    with open(input_file, 'r') as f:
        for line in f:
            match = re.search(r'HTTP/\d\.\d" (\d{3})', line)
            if match:
                status_code = int(match.group(1))
                if 400 <= status_code < 600:
                    yield line


def save_errors(input_file: str, output_file: str) -> str:
    """
    Сохранение данных.
    :param input_file:
    :param output_file:
    :return:
    """
    with open(output_file, 'w') as out_f:
        for error_line in error_status(input_file):
            out_f.write(error_line)


input_filename = 'debug.log'
output_filename = 'errors.txt'
save_errors(input_filename, output_filename)



