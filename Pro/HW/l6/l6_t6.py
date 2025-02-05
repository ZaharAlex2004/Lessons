class MessageSender:
    """
    Класс MessageSender.
    """
    def send_message(self, message: str) -> str:
        """
        Приём сообщений.
        :param message:
        :return:
        """
        pass


# Існуючі класи для відправки повідомлень
class SMSService:
    """
    Класс SMSService.
    """
    def send_sms(self, phone_number: int, message: str) -> None:
        """
        Приём SMS.
        :param phone_number:
        :param message:
        :return:
        """
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    """
    Класс EmailService.
    """
    def send_email(self, email_address: str, message: str) -> None:
        """
        Приём Email.
        :param email_address:
        :param message:
        :return:
        """
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    """
    Класс PushService.
    """
    def send_push(self, device_id: int, message: str) -> None:
        """
        Приём Push.
        :param device_id:
        :param message:
        :return:
        """
        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


class SMSAdapter(MessageSender):
    """
    Класс SMSAdapter.
    """
    def __init__(self, sms_service: "SMSService", phone_number: int) -> None:
        """
        Инициализация.
        :param sms_service:
        :param phone_number:
        """
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        """
        Приём SMS.
        :param message:
        :return:
        """
        try:
            self.sms_service.send_sms(self.phone_number, message)
        except Exception as e:
            print(f"SMS error: {e}")


class EmailAdapter(MessageSender):
    """
    Класс EmailAdapter.
    """
    def __init__(self, email_service: "EmailService", email_address: str) -> None:
        """
        Инициализация.
        :param email_service:
        :param email_address:
        """
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str) -> None:
        """
        Приём Email.
        :param message:
        :return:
        """
        try:
            self.email_service.send_email(self.email_address, message)
        except Exception as e:
            print(f"Email error: {e}")


class PushAdapter(MessageSender):
    """
    Класс PushAdapter.
    """
    def __init__(self, push_service: "PushService", device_id) -> None:
        """
        Инициализация.
        :param push_service:
        :param device_id:
        """
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        """
        Приём Push.
        :param message:
        :return:
        """
        try:
            self.push_service.send_push(self.device_id, message)
        except Exception as e:
            print(f"Push-mail error: {e}")


class MessageSenderSystem:
    """
    Класс MessageSenderSystem.
    """
    def __init__(self, senders: list) -> None:
        """
        Инициализация.
        :param senders:
        """
        self.senders = senders

    def send_all_messages(self, message: str) -> None:
        """
        Приём всех сообщений.
        :param message:
        :return:
        """
        for sender in self.senders:
            sender.send_message(message)


# Використання
sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

sms_adapter = SMSAdapter(sms_service, int(input('Введіть SMS-повідомленя для відправки: ')))
email_adapter = EmailAdapter(email_service, str(input('Введіть Email для відправки:')))
push_adapter = PushAdapter(push_service, str(input('Введіть Push-повідомленя для відправки: ')))

# Відправка повідомлень через різні сервіси за допомогою адаптерів
message = input('Введіть повідомленя: ')

#sms_adapter.send_message(message)
#email_adapter.send_message(message)
#push_adapter.send_message(message)

senders = [sms_adapter, email_adapter, push_adapter]
sender_system = MessageSenderSystem(senders)
sender_system.send_all_messages(message)
