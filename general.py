'''
# Created by:
# Selina Chua
# selina.a.chua@gmail.com
#
# This file contains the class declaration for a general service.
# It contains the information required for any general service.
'''

class GeneralService():
    def __init__(self, name, cover, wait, limits, max_ben):
        self.name = name 
        self.cover = cover
        self.wait = wait
        self.limits = limits 
        self.max_ben = max_ben 

    def __str__(self):
        string = (
            f"--- {self.name} ---\n"
            f"Covered = {self.cover}\n"
            f"Waiting Period = {self.wait}\n"
            f"Limits = {self.limits}\n"
            f"Max Benefits = {self.max_ben}\n"
        )
        return string