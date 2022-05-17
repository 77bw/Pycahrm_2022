class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Pdf(Document):
    def show(self):

        return 'Show pdf contents!'


class Word(Document):
    def show(self):

        return 'Show word contents!'


pdf_obj = Pdf("嫩模联系方式.pdf")
word_obj = Word("nurse联系方式.doc")


objs = [pdf_obj,word_obj]
for o in objs:
    print(o.show())

