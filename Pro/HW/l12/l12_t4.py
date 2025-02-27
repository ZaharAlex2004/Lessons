import http.server
import socketserver
import threading


class MyHandler(http.server.SimpleHTTPRequestHandler):
    """
    Класс MyHandler
    """
    def do_GET(self):
        """
        Ответ на GET запрос
        :return:
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Site is working!')


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def run_server():
    """
    Функция для запуска сервера
    :return:
    """
    host, port = 'localhost', 8080
    server_address = (host, port)
    httpd = ThreadedTCPServer(server_address, MyHandler)
    print(f"Сервер запущен на http://{host}:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Сервер остановлен.")
