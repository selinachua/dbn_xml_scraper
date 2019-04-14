'''
# Created by:
# Selina Chua
# selina.a.chua@gmail.com
#
# This file contains the class declaration for a policy.
# This class contains all required information about a policy, 
# which is then used to populate the excel file.
# OldPolicy is instantiated for schema 2.0 policies.
# NewPolicy is instantiated for schema 3.0 policies.
'''

from abc import ABC

class Policy(ABC):
    def __init__(self, schema, pol_name, fund_name, pdf_link, status, \
                    excess, mo_prem, state, adults, dpndnts, avail, \
                    pol_type, corp, medicare, issue_date, avail_for, \
                    prov_arr, hosp_cover, gen_services, other):
        self.schema = schema
        self.pol_name = pol_name
        self.fund_name = fund_name
        self.pdf_link = pdf_link
        self.status = status
        self.excess = excess
        self.mo_prem = mo_prem
        self.state = state 
        self.adults = adults 
        self.dpndnts = dpndnts
        self.avail = avail 
        self.pol_type = pol_type
        self.corp = corp
        self.medicare = medicare 
        self.issue_date = issue_date 
        self.avail_for = avail_for 
        self.prov_arr = prov_arr 
        self.hosp_cover = hosp_cover
        self.gen_services = gen_services 
        self.other = other
        
    
class OldPolicy(Policy):
    '''
    Policy class for schema 2 files. These are the old PDFs.
    '''
    def __init__(self, schema, pol_name, fund_name, pdf_link, status, \
                    excess, mo_prem, state, adults, dpndnts, avail, \
                    pol_type, corp, medicare, issue_date, avail_for, \
                    prov_arr, hosp_cover, gen_services, other):
        super().__init__(schema, pol_name, fund_name, pdf_link, status, \
                    excess, mo_prem, state, adults, dpndnts, avail, \
                    pol_type, corp, medicare, issue_date, avail_for, \
                    prov_arr, hosp_cover, gen_services, other)

    def __str__(self):
        string = (
            f"--- {self.pol_name} ---\n"
            f"Fund Name: {self.fund_name}\n"
            f"PDF Link: {self.pdf_link}\n"
            f"Status: {self.status}\n"
            f"Excess: {self.excess}\n"
            f"Monthly Premium: {self.mo_prem}\n"
            f"State : {self.state}\n"
            f"Adults : {self.adults}\n"
            f"Dependants : {self.dpndnts}\n"
            f"Availability : {self.avail}\n"
            f"Policy Type : {self.pol_type}\n"
            f"Corporate : {self.corp}\n"
            f"Medicare Levy Exempt : {self.medicare}\n"
            f"Issue Date : {self.issue_date}\n"
            f"Available for : {self.avail_for}\n"
            f"Provider Arrangements: {self.prov_arr}\n"
            f"Hospital Cover : {self.hosp_cover}\n"
            f"Other services: {self.other}\n"
        )
        string += "--- GENERAL SERVICES ---\n"
        for gen_s in self.gen_services:
            string += gen_s + '\n'
            string += self.gen_services[gen_s].__str__()
        return string
        

class NewPolicy(Policy):
    '''
    Policy class for schema 3 files. These are the new PDFs.
    '''
    def __init__(self, schema, pol_name, fund_name, pdf_link, status, \
                    excess, mo_prem, state, adults, dpndnts, avail, \
                    pol_type, corp, medicare, issue_date, avail_for, \
                    prov_arr, hosp_cover, gen_services, other, youth_disc, \
                    travel_accom_ben, pol_id, accident_cover, amb_emer, \
                    amb_callout_fees, amb_other):
        super().__init__(schema, pol_name, fund_name, pdf_link, status, \
                    excess, mo_prem, state, adults, dpndnts, avail, \
                    pol_type, corp, medicare, issue_date, avail_for, \
                    prov_arr, hosp_cover, gen_services, other)
        self.youth_disc = youth_disc
        self.travel_accom_ben = travel_accom_ben
        self.pol_id = pol_id 
        self.accident_cover = accident_cover
        self.amb_emer = amb_emer
        self.amb_callout_fees = amb_callout_fees
        self.amb_other = amb_other

    def __str__(self):
        string = (
            f"--- {self.pol_name} ---\n"
            f"Fund Name: {self.fund_name}\n"
            f"PDF Link: {self.pdf_link}\n"
            f"Status: {self.status}\n"
            f"Excess: {self.excess}\n"
            f"Monthly Premium: {self.mo_prem}\n"
            f"State : {self.state}\n"
            f"Adults : {self.adults}\n"
            f"Dependants : {self.dpndnts}\n"
            f"Availability : {self.avail}\n"
            f"Policy Type : {self.pol_type}\n"
            f"Corporate : {self.corp}\n"
            f"Medicare Levy Exempt : {self.medicare}\n"
            f"Issue Date : {self.issue_date}\n"
            f"Available for : {self.avail_for}\n"
            f"Provider Arrangements: {self.prov_arr}\n"
            f"Hospital Cover : {self.hosp_cover}\n"
            f"Ambulance Emergency: {self.amb_emer}\n"
            f"Ambulance Call out Fees: {self.amb_callout_fees}\n"
            f"Ambulance Other: {self.amb_other}\n"
            f"Other services: {self.other}\n"
        )
        string += "--- GENERAL SERVICES ---\n"
        for gen_s in self.gen_services:
            string += gen_s + '\n'
            string += self.gen_services[gen_s].__str__()
        return string



