# MSTSCEventLogParser
#Description
MSTSCEventLogParser is a Python Script that extracts RDP Connection related information from  Local Session Manager Operational event viewer(evtx) file. 
**Prerequisites**:
* Pre Requisites are mention in requirements.txt file and can be installed using "pip install -r requirements.txt"
* Log file obtained from 
	%SystemRoot%\System32\Winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx"
	"C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx"

## Usage
```shell
python3 rdpparser.py -i LocalSessionManagerOperational.evtx -o output.csv
```

where
* **-i** - Name of the input file (LocalSessionManagerOperational.evtx)
* **-o** - Name of the output file to store the event logs

