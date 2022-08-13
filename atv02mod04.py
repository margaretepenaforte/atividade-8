class Pessoa:
    def __init__(self):
        self.sla = 0

    def Count(self):
        self.sla += 1

    def Total(self):
        print(self.sla)


sl1 = Pessoa()
sl2 = Pessoa()
sl3 = Pessoa()


sl1.Count()
sl2.Count()
sl3.Count()

sl1.Total()
sl2.Total()
sl3.Total()