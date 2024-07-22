# Пункты задачи:
#
# 1. Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    _recipient = recipient.lower()
    _sender = sender.lower()

    # 2. Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
    # то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    valid = True
    if not _recipient.__contains__("@"):
        valid = False
    if not _recipient.endswith(".com") and not _recipient.endswith(".ru") and not _recipient.endswith(".net"):
        valid = False
    if not _sender.__contains__("@"):
        valid = False
    if not _sender.endswith(".com") and not _sender.endswith(".ru") and not _sender.endswith(".net"):
        valid = False
    if not valid:
        print(f"Невозможно отправить письмо с адреса <{_sender}> на адрес <{_recipient}")
        return

    # 3. Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    if _sender == _recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # 4. Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
    # "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    # 5. В противном случае вывести сообщение:
    # "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
    if _sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса <{_sender}> на адрес <{_recipient}>.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{_sender}> на адрес <{_recipient}>.")

    # 6. Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
    # 7. За один вызов функции выводится только одно и перечисленных уведомлений!
    # Проверки перечислены по мере выполнения.


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
