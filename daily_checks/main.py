from daily_checks import DailyCheck


class ConcreteDailyCheck1(DailyCheck):
    def __init__(self, environment, prefix):
        self.name = "concrete daily check"
        super().__init__(environment=environment, prefix=prefix)

    def perform_check(self):
        print(f"I am {self.name}")


myvar = ConcreteDailyCheck1("", "")
myvar.perform_check()
