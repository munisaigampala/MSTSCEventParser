#! python3
__author__ = "Muni Sai G"
__credits__ = "Uday Kumar V,Venkatacharyulu M"

import Evtx.Evtx as evtx
import xml.etree.ElementTree as ET
import argparse
from dateutil.parser import parse
import os
def main(inputfile,output):
    print(inputfile,output)
    outputfile=open(output,"w")
    outputfile.write("Date & Time,Event,User name,IP Address,Computer")
    Event_Desc={'21':'Session Connected','22':'Shell Notification Started','24':'Session Disconnected','25':'Session Reconnected'}
    with evtx.Evtx(inputfile) as log:
        for record in log.records():
            root = ET.fromstring(record.xml())
            if root[0][1].text in ['21','24','25']:
                if root[1][0][2].text != 'LOCAL':
                    outputfile.write("\n")
                    dt=parse(root[0][7].attrib['SystemTime']).strftime('%Y-%m-%d %H:%M:%S %Z%z')
                    eventd=Event_Desc[str(root[0][1].text)]
                    outputfile.write(dt+","+eventd+","+root[1][0][0].text+","+root[1][0][2].text+","+root[0][12].text)
                    print('-'*5+"Entry "+'-'*5)
                    print('Date/Time - ',dt)
                    print('Event  - ',eventd)
                    print('User name -  ',root[1][0][0].text)
                    print('IP Address - ',root[1][0][2].text)
                    print('Computer - ',root[0][12].text)
                


  
if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description="Small script to parse Local Session Manager Operational to display RDP Connection Details")
    my_parser.add_argument('-i','--input',help='Prove Name of the input file (LocalSessionManagerOperational.evtx)')
    my_parser.add_argument('-o','--output',help='Prove Name of the out file (Sould end with csv) . Default is out.csv')
    args = vars(my_parser.parse_args())
    if args:
        if not args['input'] :
            print("Please provide input file")
            print(my_parser.print_help())
            exit(0)
        elif args['input'] and not args['output']:
            choice=input("NO Output file given , Output will be store in out.csv Do You want to continue 'y' ? ")
            if choice not in ["y","Y","Yes","YES","yes"]:
                print("Not a valid option, Exiting")
                exit(0)
            else:
                print("Input File = " ,args['input'],"\n","Output File = out.csv","\n")
                main(args['input'],"out.csv")
            
        elif args['input'] and args['output']:
            if os.path.isfile(args['input']):
                print("Input File = " ,args['input'],"\n","Output File = ",args['output'],"\n")
                main(args['input'],args['output'])
            else:
                print("Invalid Input File")
    else:
        print("Please provide the arguments")
        print(my_parser.print_help())
        exit(0)
    