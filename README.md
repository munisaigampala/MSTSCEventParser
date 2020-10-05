# MSTSCEventLogParser
#Description
MSTSCEventLogParser is a Python Script that extracts RDP Connection related information from  Local Session Manager Operational event viewer(evtx) file. 
**Prerequisites**:
Pre Requisites are mention in requirements.txt file and can be installed using "pip install -r requirements.txt"
Log file obtained from 
* %SystemRoot%\System32\Winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx"
* "C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx"

## Usage
```shell
python3 rdpparser.py -i LocalSessionManagerOperational.evtx -o output.csv
```

where
* **-i** - Name of the input file (LocalSessionManagerOperational.evtx)
* **-o** - Name of the output file to store the event logs


## Information
* Script checks for Event ID 21,22,24 and 25 which represents "Session Connected" ,"Shell Notification Started" ,"Session Disconnected" and "Session Reconnected" respectively.
* Script looks for the above mentioed Event ID if it finds any match then it Filter Non-Local(LOCAL) connections from it.

```shell
if root[0][1].text in ['21','24','25']:
                if root[1][0][2].text != 'LOCAL':
```
* Output can be seen in Command prompt(will be removed in future builds) as well as in newly generated csv file.
![mstsc_parser_output_log](https://user-images.githubusercontent.com/61400637/95047909-82c2cc00-0704-11eb-9ae3-edecbe20aeb0.png)
