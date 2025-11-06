class fake_print:
    def __init__(self, print):
        self.print = print

    def __str__(self):
        return f"{self.print}
    
