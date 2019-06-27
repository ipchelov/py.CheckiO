VOWELS = "aeiou"


class Chat:
    def __init__(self):
        self.human = None
        self.robot = None
        self.sender = []
        self.message = []

    def connect_human(self, human):
        self.human = human
        human.chat = self

    def connect_robot(self, robot):
        self.robot = robot
        robot.chat = self

    def show_human_dialogue(self):
        result=''
        result+= f"{self.sender[0]} said: {self.message[0]}\n"
        for i in range(1, len(self.sender)):
            result+=f"{self.sender[i]} said: {self.message[i]}\n"

        return result[:-1]

    def show_robot_dialogue(self):
        result = ''
        def translated_to_rob(self, message):
            result = ''
            for i in message:
                if i in VOWELS:
                    result += '0'
                else:
                    result += '1'

            return result

        translated = translated_to_rob(self, self.message[0])

        result += f"{self.sender[0]} said: {translated}\n"

        for i in range(1, len(self.sender)):
            translated = translated_to_rob(self, self.message[i])
            result += f"{self.sender[i]} said: {translated}\n"

        return result[:-1]


class Human:
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, message):
        self.chat.sender.append(self.name)
        self.chat.message.append(message)



class Robot:
    def __init__(self, id):
        self.id = id
        self.chat = None

    def send(self, message):
        self.chat.sender.append(self.id)
        self.chat.message.append(message)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?\nR2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011\nR2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")
