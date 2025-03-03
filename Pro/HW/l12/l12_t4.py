import http.server
import socketserver
import threading
import logging
import time


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('server.log')
    ]
)


class MyHandler(http.server.SimpleHTTPRequestHandler):
    """
    Класс MyHandler для обработки GET-запросов.
    """

    def do_GET(self):
        """
        Ответ на GET запрос
        :return:
        """
        logging.info(f"Получен GET запрос от {self.client_address}")
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Site is working!')
        except Exception as e:
            logging.error(f"Ошибка при обработке запроса: {e}")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Internal Server Error')


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    Многозадачный сервер, который обрабатывает запросы в отдельных потоках.
    """
    pass


def run_server():
    """
    Функция для запуска сервера
    :return:
    """
    host, port = 'localhost', 8080
    server_address = (host, port)
    httpd = ThreadedTCPServer(server_address, MyHandler)
    logging.info(f"Сервер запущен на http://{host}:{port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Сервер остановлен пользователем.")
        httpd.server_close()
    except Exception as e:
        logging.error(f"Ошибка при работе сервера: {e}")
        httpd.server_close()


if __name__ == '__main__':
    # Запуск сервера в отдельном потоке
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Главный процесс завершен. Сервер остановлен.")
