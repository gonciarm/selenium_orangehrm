import configparser

config = configparser.RawConfigParser()
config.read('..\\Configurations\\config.ini')

class ReadConfig():

    @staticmethod
    def getUrl():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def getChromeDriverPath():
        path = config.get('common info', 'chromeDriverPath')
        return path

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password