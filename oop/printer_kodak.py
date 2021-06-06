from printer import Printer


class PrinterKodak(Printer):
    def write(self, text : str):
        print(text)


