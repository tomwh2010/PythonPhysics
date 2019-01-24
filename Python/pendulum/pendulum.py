import random

class RandomPendulum:
    def __init__(self):
        self.radius0=random.randint(50,150)
        self.radius1=random.randint(50,150)
        self.radius2=random.randint(50,150)
        self.radius3=random.randint(50,150)
        self.radius4=random.randint(50,150)

        self.startangle0=random.randint(0,359)
        self.startangle1=random.randint(0,359)
        self.startangle2=random.randint(0,359)
        self.startangle3=random.randint(0,359)
        self.startangle4=random.randint(0,359)

        self.startvelocity0=random.uniform(-0.1, 0.1)
        self.startvelocity1=random.uniform(-0.1, 0.1)
        self.startvelocity2=random.uniform(-0.1, 0.1)
        self.startvelocity3=random.uniform(-0.1, 0.1)
        self.startvelocity4=random.uniform(-0.1, 0.1)

        self.influence00=random.uniform(-0.1, 0.1)
        self.influence01=random.uniform(-0.1, 0.1)
        self.influence02=random.uniform(-0.1, 0.1)
        self.influence03=random.uniform(-0.1, 0.1)
        self.influence04=random.uniform(-0.1, 0.1)
        self.influence10=random.uniform(-0.1, 0.1)
        self.influence11=random.uniform(-0.1, 0.1)
        self.influence12=random.uniform(-0.1, 0.1)
        self.influence13=random.uniform(-0.1, 0.1)
        self.influence14=random.uniform(-0.1, 0.1)

        def printvalues():
            print(self.radius0, self.radius1, self.radius2, self.radius3, self.radius4)
            print(self.startvelocity0, self.startvelocity1, self.startvelocity2, self.startvelocity3, self.startvelocity4)
            print(self.startangle0, self.startangle1, self.startangle2, self.startangle3, self.startangle4)
            print(self.influence00, self.influence01, self.influence02, self.influence03, self.self.influence04)
            print(self.influence10, self.self.influence11, self.self.influence12, self.self.influence13, self.self.influence14)


class HuhPendulum1(RandomPendulum):
    def __init__(self):
        super().__init__()
        self.startangle0=1
        self.startangle1=1
        self.startangle2=1
        self.startangle3=1
        self.startangle4=1

        self.startvelocity0=0
        self.startvelocity1=0
        self.startvelocity2=0
        self.startvelocity3=0
        self.startvelocity4=0

        self.influence00=0
        self.influence01=0
        self.influence02=0
        self.influence03=0
        self.influence04=0
        self.influence10=0
        self.influence11=0
        self.influence12=0
        self.influence13=0
        self.influence14=0


class SpiralPendulum1(RandomPendulum):
    def __init__(self):
        super().__init__()
        self.startangle0=0
        self.startangle1=0
        self.startangle2=0
        self.startangle3=0
        self.startangle4=0

        self.startvelocity0=0.1
        self.startvelocity1=0.1
        self.startvelocity2=0.1
        self.startvelocity3=0.1
        self.startvelocity4=0.1

        self.influence00=0
        self.influence01=0
        self.influence02=0
        self.influence03=0
        self.influence04=0
        self.influence10=0
        self.influence11=0
        self.influence12=0
        self.influence13=0
        self.influence14=0


class SimplePendulum(RandomPendulum):
    def __init__(self):
        super().__init__()
        self.radius0=75
        self.radius1=75
        self.radius2=75
        self.radius3=75
        self.radius4=75

        self.startangle0=0
        self.startangle1=0
        self.startangle2=0
        self.startangle3=0
        self.startangle4=0

        self.startvelocity0=0.1
        self.startvelocity1=0
        self.startvelocity2=0
        self.startvelocity3=0
        self.startvelocity4=0

        self.influence00=0
        self.influence01=0
        self.influence02=0
        self.influence03=0
        self.influence04=0
        self.influence10=0
        self.influence11=0
        self.influence12=0
        self.influence13=0
        self.influence14=0
