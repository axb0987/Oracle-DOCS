# Transfer the AD Bridge
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/maintain-microsoft-active-directory-ad-bridge.htm
- Fetched: 2026-09-05 02:24 CDT

# Transfer the AD Bridge

Transfer the bridge between IAM and Microsoft Active Directory to another machine and restart it.

## Transferring the AD Bridge

Note  
  
If you can't remove the client for the AD bridge or the bridge still appears in the Directory Integrations page, then follow the procedure in[Removing an AD Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/remove-microsoft-active-directory-ad-bridge.htm).

- From the original machine, access the Control Panel , and uninstall the client for the AD bridge.
- On the other machine, install the client. See[Create a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/create-microsoft-active-directory-ad-bridge.htm).
- In the IAM Console, expand the Navigation Drawer , select Settings , and then select Directory Integrations .
- Verify that the AD bridge appears in the other machine with an Active status. This bridge can now be used to synchronize with your Microsoft Active Directory enterprise directory structure.

## Restarting the Microsoft Active Directory Bridge

- Select Start .
- In the text box, enter Services , and then press Enter .
The Services window appears. This window contains a utility that's used to manage daemon processes within the Windows OS. These processes include the backend service that's used to establish communication between IAM and Microsoft Active Directory.
- Select Services (Local) , select the Standard tab, scroll down the list of services, right-click Oracle Identity Cloud Service Microsoft Active Directory Bridge Service , and then select Start .
-
