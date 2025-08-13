import time

from  faker  import Faker
import uuid


fake =  Faker()

# def generate_random_mail():
#     mail = f"{fake.first_name().lower()}.{uuid.uuid4().hex[:6]}.@gmail.com"
#     return mail

def generate_random_mail():
    return f"pankaj.{int(time.time())}@gmail.com"


def generate_random_name():
    name = fake.first_name()
    return name

def generate_random_lastname():
    last_name = fake.last_name()
    return last_name

def generate_random_mobile_no():
    mobile_no = fake.msisdn()[0:10]
    return mobile_no


print(generate_random_mobile_no())
print(generate_random_lastname())
print(generate_random_name())
print(generate_random_mail())