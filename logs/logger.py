class log(object):

    @staticmethod
    def info(message):
        print "\033[94m[I]\033[0m INFO: " + message

    @staticmethod
    def err(message):
        print "\033[91m[X]\033[0m ERROR: " + message

    @staticmethod
    def success(message):
        print "\033[92m[+]\033[0m SUCCESS: " + message

    @staticmethod
    def warn(message):
        print "\033[93m[!]\033[0m WARNING: " + message
