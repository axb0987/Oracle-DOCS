# Testing DNS Using dig
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm
- Fetched: 2026-09-05 01:59 CDT

# Testing DNS Using dig

Use BIND'S Domain Information Groper (dig) command line tool to test against the delegation where the domain is hosted. Immediately see whether changes took place without accounting for the cache or TTL (Time to Live) that you have configured.
Note  
  
Windows users can download the tool from BIND's[website](https://www.isc.org/downloads/). Use Terminal to access dig on Linux and Macintosh systems.

## Using dig

Before using BIND's dig tool, you must access or install dig on the system you use. After you have access to dig, you can use dig to test DNS.

[To access dig (Mac)](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm#)

- From the`Applications`folder, open the`Utilities`folder, and then select Terminal .
- When the terminal is open, type a[dig command](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm#use-dig)using a hostname you want to look up.

[To install dig (Windows)](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm#)

- 

Go to[ISC's website](https://www.isc.org/downloads/)and download the most current, stable version of BIND.
Note  
  
BIND supports both 32 and 64 bit Windows systems. Confirm which version of Windows you're using and download the correct version of BIND. View Microsoft's[documentation](http://windows.microsoft.com/windows/which-operating-system)to find which version of Windows you're using.
- Extract the downloaded file and install BIND in the following directory:`C:\Program Files\ISC BIND 9`. Select the Tools Only checkbox.
- After BIND is installed, open the Control Panel from the Windows menu, and then open System properties .
- On the Advanced tab, select Environment Variables .
- Under System Variables , select Path , and then select Edit .
- At the end of the path in the Edit System Variable window, add`C:\Program Files\ISC BIND 9\bin`, and then select OK .
- In the Edit Variables window, select OK . In the System properties window, select OK .

#### To open the Command Prompt

For Windows versions 8 to10:
- Select the Windows menu icon.
- In the Search field, type`CMD`.
- Select Command Prompt .

For Windows version 7:
- On the Start menu select Run .
- Enter`CMD`, and then select OK .

[To use dig to test DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm#)

- Open a terminal (Mac and Linux) or command prompt (Windows).
- Type`dig <any hostname>`, and then press Enter .

The following information is returned:

[
- Question section : The query made to the nameserver. In this example, we asked for the first available A record for the hostname,`oracle.com`.
- Answer section : The first available answer for the query made to the DNS. In this example, we received the A record containing the IP address 137.254.16.101.
- Authority section : The authoritative nameservers from which the answer to the query was received. These nameservers house the zones for a domain.
- Additional section : More information the resolver might need but not the answer to the query.

## dig Commands

Command Description Example
`dig [hostname]`Returns any A records found within the queried hostname's zone.`dig oracle.com`
`dig [hostname] [record type]`Returns the records of that type found within the queried hostname's zone.`dig oracle.com MX`
`dig [hostname] +short`Provides a brief answer, often an IP address.`dig oracle.com +short`
`dig @[nameserver address] [hostname]`Queries the nameserver directly instead of the resolver configured in a local system.`dig @dnsmaster6.oracle.com`
`dig [hostname] +trace`Adding`+trace`instructs dig to resolve the query from the root nameserver downwards and to report the results from each query step.`dig oracle.com +trace`
`dig -x [IP address]`Reverse lookup for IP addresses.`dig -x 108.59.161.1`
