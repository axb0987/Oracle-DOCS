# Starting a Provisioning Bridge on a Windows Machine
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/start-provisioning-bridge-windows-machine.htm
- Fetched: 2026-09-05 02:27 CDT

# Starting a Provisioning Bridge on a Windows Machine

Start a provisioning bridges in an IAM identity domain on a Windows machine.

Important  
  
You can't start multiple provisioning bridges with the same configuration information. If you want to start another provisioning bridge, then use the provisioning bridges list page to create a new bridge, and use the newly generated client ID and secret for the identity domain to start the bridge.

- Start the Windows machine where you installed the client for the provisioning bridge.

Important  
  
Ensure that you have administrative rights for this machine. Also, check that this machine communicates with the client network that the provisioning bridge uses to access the apps that you want to monitor.
- Open Windows Explorer, and then navigate to the folder you created that contains the files for the provisioning bridge. You created this folder in[Create a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/create-provisioning-bridge.htm).
- Double-click the`startup.bat`file.
- At the command window prompt, enter the password for Oracle Wallet that you created when you created the bridge.
The provisioning bridge attempts to connect to the identity domain server.
- Verify that you see the status message`The Provisioning Bridge is started.`which indicates that a connection is established between the provisioning bridge and the identity domain server.

Important  
  
Ensure that you keep this command window open. If you close it, then you stop the Provisioning Bridge.
- On the Provisioning bridges list page, select the provisioning bridge you want to work with. If you need help finding the list page or the recipe, see[Listing Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/list-provisioning-bridges.htm).
- Verify that the bridge has a status of Started .
- Select the name of the bridge, and then select Connectors .
-
