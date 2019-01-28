import random
from pendulum import Pendulum

class RandomPendulum(Pendulum):
    def __init__(self):
        super().__init__()
        self.radius0=random.randint(self.radiustotal//8,self.radiustotal//5)
        self.radius1=random.randint(self.radiustotal//8,self.radiustotal//5)
        self.radius2=random.randint(self.radiustotal//8,self.radiustotal//5)
        self.radius3=random.randint(self.radiustotal//8,self.radiustotal//5)
        self.radius4=random.randint(self.radiustotal//8,self.radiustotal//5)

        self.angle0=random.randint(0,359)
        self.angle1=random.randint(0,359)
        self.angle2=random.randint(0,359)
        self.angle3=random.randint(0,359)
        self.angle4=random.randint(0,359)

        self.velocity0=random.uniform(-0.1, 0.1)
        self.velocity1=random.uniform(-0.1, 0.1)
        self.velocity2=random.uniform(-0.1, 0.1)
        self.velocity3=random.uniform(-0.1, 0.1)
        self.velocity4=random.uniform(-0.1, 0.1)

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

        self.cycle=3


class SimplePendulum(Pendulum):
    def __init__(self):
        super().__init__()
        self.velocity0=.01
        self.velocity1=.01
        self.velocity2=.01
        self.velocity3=.01
        self.velocity4=.01


class SpiralPendulum(Pendulum):
    def __init__(self):
        super().__init__()
        self.velocity0=0.01
        self.velocity1=0.02
        self.velocity2=0.04
        self.velocity3=0.08
        self.velocity4=0.16

if __name__=="__main__":
    pd=RandomPendulum()
    pd.start()
    pd.draw()
