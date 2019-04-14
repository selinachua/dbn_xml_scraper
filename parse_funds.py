'''
# Created by:
# Selina Chua
# selina.a.chua@gmail.com
#
# This file scrapes information on all the funds from 
# the funds xml file. This file is assumed to exist in 
# the ./privatehealth-04-apr-2019 directory, and is assumed
# to be named FUND_FILE_NAME. If this changes, it can be 
# modified in the constants.py folder.
'''

import sys
from bs4 import BeautifulSoup
from constants import *

class Fund():
    def __init__(self, code, name, preferred_provider_services, amb_emer, amb_call_out_fees, amb_other, restrictions):
        self.code = code
        self.name = name 
        self.preferred_provider_services = preferred_provider_services
        self.amb_emer = amb_emer
        self.amb_call_out_fees = amb_call_out_fees
        self.amb_other = amb_other
        self.restrictions = restrictions

    def __str__(self):
        string = (
            f"CODE: {self.code}\n"
            f"NAME: {self.name}\n"
            f"PREFERRED PROVIDER SERVICES: {self.preferred_provider_services}\n"
            f"AMBULANCE EMERGENCY: {self.amb_emer}\n"
            f"AMBULANCE CALL OUT FEES: {self.amb_call_out_fees}\n"
            f"AMBULANCE OTHER FEATURES: {self.amb_other}\n"
            f"RESTRICTIONS: {self.restrictions}\n"
        )
        return string

def find_text(soup, tag):
    found = soup.find_all(tag)
    if not found:
        return "Not found"
    return found[0].get_text().strip()


def get_fund_info(fund):
    '''
    This functions finds the information for a fund.
    '''
    code = find_text(fund, 'fundcode').strip()
    name = find_text(fund, 'fundname').strip()

    # Get preferred providers in the form (state, service)
    providers = []
    preferred_providers = fund.find_all('preferredprovider')
    for p in preferred_providers:
        if p['covered'] == 'Covered':
            providers.append((p['state'], find_text(p, 'freetext').strip()))
    
    # Get ambulance information.
    ambulance = fund.find_all('ambulance')[0]
    amb_call_out_fees = ambulance['calloutfees']
    try:
        amb_emer_wait = find_text(ambulance, 'waitingperiodemergency') + ambulance.find_all('waitingperiodemergency')[0]['unit'].strip()
    except:
        amb_emer_wait = "Not found"
    amb_emer_limit = find_text(ambulance, 'ambulanceservicelimitemergency')
    amb_emer_str = f"Wait: {amb_emer_wait}\nLimit: ${amb_emer_limit}\n"
    amb_other = []
    amb_details = ambulance.find_all('detail')
    for detail in amb_details:
        amb_other.append((detail['state'], detail.get_text().strip()))

    restrictions = find_text(fund, 'restrictionparagraph')
    if restrictions == "Not found":
        restrictions = "No restrictions"

    fund_info = Fund(code, name, providers, amb_emer_str, amb_call_out_fees, amb_other, restrictions)

    return fund_info


def parse_funds_file():
    '''
    This function goes through the fund file and collects information.
    Returns fund_dict, which contains the infromation.
    fund_dict = {
        code: Fund object 
    }
    '''
    # Find fund file and make soup.
    fund_file = open(f"{sys.path[0]}/privatehealth-04-apr-2019/{FUND_FILE_NAME}")
    fund_soup = BeautifulSoup(fund_file, "lxml")
    # Set up fund dictionary to store all information.
    fund_dict = {}
    # Finds all funds.
    all_funds = fund_soup.find_all("fund")
    for fund in all_funds:
        code = find_text(fund, 'fundcode')
        fund_dict[code] = get_fund_info(fund)
    
    return fund_dict

if __name__ == "__main__":
    parse_funds_file()