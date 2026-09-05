# Starting a Provisioning Bridge on a Generic Machine
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/start-provisioning-bridge-generic-machine.htm
- Fetched: 2026-09-05 02:27 CDT

# Starting a Provisioning Bridge on a Generic Machine

Start a provisioning bridges in an IAM identity domain on a generic machine.
A generic machine has Java 8 installed on it and supports bash shell. For this type of machine, you can start the Provisioning Bridge in two modes:
- `normal:`The bridge starts in a Terminal window.
- `background:`The bridge starts as a process in the background in a Terminal window.

Important  
  
You can't start multiple provisioning bridges with the same configuration information. If you want to start another provisioning bridge, then use the provisioning bridges list page to create a new bridge, and use the newly generated client ID and secret for the identity domain to start the bridge.

- Start the generic machine where you installed the client for the bridge.

Important  
  
Ensure that you have administrative rights for this machine. Also, check that this machine communicates with the client network that the bridge uses to access the apps that you want to monitor.
- In a Terminal window, navigate to the folder you created that contains the files for the bridge. You created this folder in[Create a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/create-provisioning-bridge.htm).
- 3. At the prompt, enter one of the following commands, depending on the mode you want to use:`./startup.sh normal`.
- `./startup.sh normal`
- `./startup.sh background`
- At the prompt, enter the password for Oracle Wallet that you created when you created the bridge.
The Provisioning Bridge attempts to connect to the identity domain server.
- If you're using`normal`mode, verify that you see the status message`The Provisioning Bridge is started`, which indicates that a connection is established between the bridge and the identity domain server.

Important  
  
Ensure that you keep this Terminal window open. If you close it, then you stop the Provisioning Bridge.
- If you're using background mode, verify that you see the status message`The Provisioning Bridge is started. [Process_ID] is the process ID that's used to start this bridge`. A connection is established between the bridge and the identity domain server

Note  
  
If you want to stop the bridge, then use the process ID to stop the process. You can also use this ID to check if the process is running properly, or if there are any errors associated with the process.
- On the Provisioning bridges list page, select the provisioning bridge you want to work with. If you need help finding the list page or the recipe, see[Listing Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/list-provisioning-bridges.htm).
- Verify that the bridge has a status of Started .
- Select the name of the bridge, and then select Connectors .
-
