import string
from faker import Faker
import secrets


class FakeUser:

    def createFakeUser(self, numOfUsers:int):
        fake = Faker(locale='en_US')
        fakeUsers = [
            {'email': fake.email(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'city': fake.city(),
            'country': fake.country(),
            'id':''.join(secrets.choice(string.digits) for i in range(9))}
        for x in range(numOfUsers)]
        print(fakeUsers)


if __name__ == '__main__':
   fu=FakeUser()
   fu.createFakeUser(10)