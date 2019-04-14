'''
# Created by:
# Selina Chua
# selina.a.chua@gmail.com
#
# This file contains the class declaration for a hospital service.
# Each policy contains a hospital service (aside from general only types).
# This class contains all the information required about the 
# policy's hospital cover.
'''

class HospService():
    def __init__(self, covered, not_covered, limited_cover, wait, other, co_pay):
        self.covered = covered 
        self.not_covered = not_covered 
        self.limited_cover = limited_cover
        self.wait = wait
        self.other = other
        self.co_pay = co_pay

    def __str__(self):
        string = "COVERED: \n"
        for s in self.covered:
            string += f"{s}\n"
        string += "NOT COVERED:\n"
        for s in self.not_covered:
            string += f"{s}\n"
        string += "LIMITED:\n"
        for s in self.limited_cover:
            string += f"{s}\n"
        string += "WAITING PERIOD:\n"
        string += self.wait
        string += "OTHER FEATURES:\n"
        string += self.other + '\n'
        string += f"COPAYMENT: {self.co_pay}"
        return string