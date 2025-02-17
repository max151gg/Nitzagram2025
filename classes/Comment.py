import constants
from helpers import from_text_to_array
class Comment:
    Text: str

    def __init__(self,Text):
        self.Text = from_text_to_array(Text)


    def display(self):
        s = ""
        Text_seperated = []
        for i in range(0,len(self.Text)):
            s += self.Text[i]

            if i % 24 == 0 or i == len(self.Text) - 1:
                Text_seperated.append(s)
                s = ""
        not_sure = 24
        for comment in Text_seperated:
            text_font = Font.re

