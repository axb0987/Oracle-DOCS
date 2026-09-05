# Configuring the Oracle Cloud Infrastructure NTP Service for an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm
- Fetched: 2026-09-05 01:50 CDT

# Configuring the Oracle Cloud Infrastructure NTP Service for an Instance

Oracle Cloud Infrastructure offers a fully managed, secure, and highly available NTP service that you can use to set the date and time of compute and database instances from within a virtual cloud network (VCN). The Oracle Cloud Infrastructure NTP service uses redundant Stratum 1 devices in every availability domain. The Stratum 2 devices are synchronized to dedicated Stratum 1 devices that every host synchronizes against. The service is available in every region.

This topic describes how to configure compute instances to use this NTP service.

You can also choose to configure instances to use a public NTP service or use FastConnect to leverage an on-premises NTP service.
Note  
  
Platform images for Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7.x, Oracle Linux 9.x, Oracle Linux 8.x, Oracle Linux 7.x, Oracle Linux Cloud Developer 8.x, CentOS 7.x released after February 2018, and CentOS Stream 8 include the Chrony service by default. You do not need to configure the Oracle Cloud Infrastructure NTP service for these instances.

[Oracle Linux 7.x released in February 2018 or earlier](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm#)

Use the following steps to configure Oracle Linux 7.x instances to use the Oracle Cloud Infrastructure NTP service.
- Run commands in this section as root with the following command:

```

```

- Install the NTP service with the following command:

```

```

- Change the firewall rules to allow inbound and outbound traffic with the Oracle Cloud Infrastructure NTP server, at 169.254.169.254, on UDP port 123 with the following command:

```

```

At the prompt`mv: overwrite '/etc/firewalld/direct.xml'?`, enter`y`.
- Restart the firewall with the following command:

```

```

- Set the date of your instance with the following command:

```

```

- Configure the instance to use the Oracle Cloud Infrastructure NTP service for iburst. To configure, modify the`/etc/ntp.conf`file as follows:
- In the`server`section comment out the lines specifying the RHEL servers:

```

```

- 

Add an entry for the Oracle Cloud Infrastructure NTP service:

```

```

The modified`server`section should now contain the following:

```

```

- 

Start and enable the NTP service with the following commands:

```

```

You also need disable the chrony NTP client to ensure that the NTP service starts automatically after a reboot, using the following commands:

```

```

- 

Confirm that the NTP service is configured correctly with the following command:

```

```

The output will be similar to the following:

```

```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm#)

Tip  
  
If you encounter a no time data was available error message when setting up the NTP service on Windows Server, review the information in the[Microsoft known issue](https://docs.microsoft.com/troubleshoot/windows-server/identity/error-message-run-w32tm-resync-no-time-data-available)article.
- 

Configure a Windows Server instance to use the Oracle Cloud Infrastructure NTP service by doing one of the following things:
- 

To configure the NTP service by using Windows Powershell, run the following commands in Powershell as Administrator:

```

```

- 

To configure the NTP service by manually editing the registry, do the following:
- Change the server type to NTP:
- From Registry Editor, navigate to:
```

```

- Click Type .
- Change the value to`NTP`and click OK .
- 

Configure the Windows Time service to enable the`Timeserv_Announce_Yes`and`Reliable_Timeserv_Announce_Auto`flags.

To configure, set the`AnnounceFlags`parameter to 5:
- From Registry Editor, navigate to:
```

```

- Click AnnounceFlags .
- Change the value to`5`and click OK .
- Enable the NTP server:
- From Registry Editor, navigate to:
```

```

- Click Enabled .
- Change the value to`1`and click OK .
- Set the time sources:
- From Registry Editor, navigate to:
```

```

- Click NtpServer .
- Change the value to`169.254.169.254,0x9`and click OK .
- Set the poll interval:
- From Registry Editor, navigate to:
```

```

- Click SpecialPollInterval .
- Set the value to the interval that you want the time service to synchronize on. The value is in seconds. To set it for 15 minutes, set the value to`900`, and click OK .
- Set the phase correction limit settings to restrict the time sample boundaries:
- From Registry Editor, navigate to:
```

```

- Click MaxPosPhaseCorrection .
- Set the value to the maximum time offset in the future for time samples. The value is in seconds. To set it for 30 minutes, set the value to`1800`and click OK .
- Click MaxNegPhaseCorrection .
- Set the value to the maximum time offset in the past for time samples. The value is in seconds. To set it for 30 minutes, set the value to`1800`and click OK .
- Restart the time service by running the following command from a command prompt:

```

```

- 

Test the connection to the NTP service by running the following command from a command prompt:

```

```

The output will be similar to the following:
```

```

After the time specified in the poll interval has elapsed,`State`will change from`Pending`to`Active`
