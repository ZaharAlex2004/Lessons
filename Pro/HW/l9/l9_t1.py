import re


def email_valid(email: str) -> None:
    """
    Проверка email.
    :param email:
    :return:
    """
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    if re.match(pattern, email) is not None:
        print("Validation complete")
    else:
        print("Validation failed")


email_valid('example@domain.com')
email_valid('example@domain.co')
email_valid('ex.ample@domain.com')
email_valid('example@domain.c')
email_valid('example@domain.toolongtld')
email_valid('exampledomain.сom')
