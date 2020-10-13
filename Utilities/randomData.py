import random
import string


class StringGenerator(object):

    def generateString(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str


class NumberGenerator(object):

    def generateNumber(length):
        result_number_list = random.choices([i for i in range(length)], k=5)
        result_number = ''.join(str(number) for number in result_number_list)
        return result_number

