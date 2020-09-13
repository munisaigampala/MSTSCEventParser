# MSTSCEventLogParser
MSTSCEventLogParser is a Python Script that extracts RDP Connection related information from  Local Session Manager Operational event viewer(evtx) file. 
Pre Requisites are mention in requirements.txt file and can be installed using "pip install -r requirements.txt"

Simple example:
python3 rdpparser.py -i LocalSessionManagerOperational.evtx -o output.csv

