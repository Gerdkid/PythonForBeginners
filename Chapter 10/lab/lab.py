class LogMessage:
    def __init__(self, fileName):
        self.fileName = fileName

    def read(self):
        file = open(self.fileName, 'r')
        for line in file:
            print(line, end="")

    def write(self, message):
        file = open(self.fileName, 'a')
        file.write(message)

myLog = LogMessage('hello.txt')
myLog.write('Testing..' + '\n')
myLog.read()
