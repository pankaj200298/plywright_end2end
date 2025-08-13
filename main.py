import time


def random_mail():
    mail = f"pankaj.{time.time()}@gmail.com"
    return str(mail)

print(random_mail())

def generate_random_email():
    return f"pankaj.{int(time.time())}@gmail.com"

print(generate_random_email())