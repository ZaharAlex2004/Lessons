def up():
    """
    Преобразователь в верхний регистр и удаление пробела.
    :return:
    """
    try:
        u = input('Enter the text: ')
        ur = u.upper()
        print(ur.replace(" ", ""))
    except ValueError as e:
        print(e)
