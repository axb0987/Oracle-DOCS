# Mapped Drive isn't Available for All Users
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/mapping-for-multiple-windows-users.htm
- Fetched: 2026-09-05 02:06 CDT

# Mapped Drive isn't Available for All Users

Learn how to troubleshoot an issue where a File Storage file system mapped to a Windows drive isn't available for all users.

Symptom : After[mounting a file system from a Windows instance](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingwindowsos.htm)as the`opc`user, the mapped drive isn't available to other logged in users.

Cause : This is expected behavior with a mapped network drive mounted locally to a Windows machine.

Solution :

For domain users , create a logon group policy object that runs the mount command when domain users log in to the Windows machine attached to the domain. For more details about configuring a logon group policy in Windows, see[Using Startup, Shutdown, Logon, and Logoff Scripts in Group Policy](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn789196(v=ws.11)).

For Windows machine local users , you can have the same mount command logon script as a local policy object at the Windows machine level. Or, you can use following option as well:
- Log in to the Windows instance as the`opc`user.
- 

Create a batch file called`FSSmount.BAT`with contents such as:

```

```

- Copy the batch file to`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`.
-
