# This script is to export choices which is used in choices.py
origin = 'Nursing - CNA, Kid - Debate Team, EKG, EMR, Kid - English Enrichment, IT Auditing, Job Placement, Kid - Math Olympiads, Nursing - MedAssist, Nursing - CMLA, Nursing - MedTrans, Nursing - Nurse , Patient Care Tech, Pharmacy Tech, Kid - PSAT/SAT/SAT II, SAP-BIBO, SAP-CRM, SAP-FICO, SAP-HR, SAP-MM, SummCamp, Sweepstakes'

splited = origin.split(", ") # array

choices = ()
for each in splited:
	choices = choices + ((each.lower(), each),)


print(choices)