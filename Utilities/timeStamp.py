from datetime import datetime

now = datetime.now()  # current date and time

class TimeStamp():

    @staticmethod
    def dateTime():
        timeStamp = now.strftime('_%d-%m-%Y_%H-%M-%S')
        return timeStamp
