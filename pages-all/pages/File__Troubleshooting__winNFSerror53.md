# Accessing a Mounted File System is Slow or Fails After a Few Seconds
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSerror53.htm
- Fetched: 2026-09-05 02:07 CDT

# Accessing a Mounted File System is Slow or Fails After a Few Seconds

Learn how to troubleshoot delayed UNC access or Error 53 on a file system mounted using Windows NFS.
Important  
  

Before proceeding with troubleshooting, be sure to implement the following prerequisites for connecting to file systems from Windows instances:
- Install the NFS Client. Follow the installation procedure found in[Mounting File Systems From Windows Instances](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingwindowsos.htm).
- Set up security rules to work with File Storage. Follow the procedure found in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm)

Symptom 1 : Accessing a mounted file system with File Explorer or Universal Naming Convention (UNC) path or Command Prompt/Powershell is significantly delayed or fails. The effect is intermittent.

Symptom 2 : Mount fails using Windows NFS connection with "Network Error 53 "Network path not found".

Cause : By default, Windows network providers have higher priority than the client for NFS network provider. Initially, the delay as Windows tries each provider in the default order is significant. Subsequent attempts may be faster because the mount information is cached. After the cache times out, the delay increases again. The native Windows file system client called Distributed File System (DFS) is also given default priority over NFS client, increasing the delay.

Solution : Change the network provider order and disable the DFS client so that the client for NFS Network provider is tried first.

[To change the network provider order on Windows 2012+](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSerror53.htm#)

- Select Windows Search.
- Enter`regedit`in the Search field and press Enter .
- Select Yes to allow changes to your device.
- Select`HKEY_LOCAL_MACHINE`.
- Browse to:`System\CurrentControlSet\Control\NetworkProvider\Order`
- 

Change the`Network Provider`order from default to Nfsnp,RDPNP,LanmanWorkstation:
- Right-click`ProviderOrder`, and select Modify .
- In the Value Data field, enter`Nfsnp,RDPNP,LanmanWorkstation`. If there are any further items that exist in this field on your instance, enter them after`LanmanWorkstation`.
- Select OK .
- Restart the instance.

[To disable the DFS Client on Windows 2012+](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSerror53.htm#)

- Select Windows Search.
- Enter`regedit`in the Search field and press Enter .
- Select Yes to allow changes to your device.
- Select`HKEY_LOCAL_MACHINE`.
- Browse to:`System\CurrentControlSet\Services\Mup.`
- 

Add a new DWORD32 registry entry for`DisableDfs`:
- Select Edit , and select New DWORD (32 bit) Value .
- In the Name field, enter`DisableDfs`.
- Right-click`DisableDFS`, and select Modify .
- In the Value Data field, enter`1`.
- Select OK .
- Restart the instance.

For more information, see:
- [Support for UNC Naming and MUP](https://docs.microsoft.com/windows-hardware/drivers/ifs/support-for-unc-naming-and-mup)
- [Modify the protocol bindings and network provider order](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc732472(v=ws.10)?redirectedfrom=MSDN)
- [MUP and DFS Interactions](https://docs.microsoft.com/windows-hardware/drivers/ifs/mup-and-dfs-interactions)
