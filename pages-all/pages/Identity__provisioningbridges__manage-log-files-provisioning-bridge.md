# Managing Log Files for a Provisioning Bridge
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/manage-log-files-provisioning-bridge.htm
- Fetched: 2026-09-05 02:27 CDT

# Managing Log Files for a Provisioning Bridge

After you install and start a provisioning bridge, you might want to access the log files for troubleshooting purposes. You can locate these files in the`logs`folder.

The`logs`folder is contained in the directory that you created when you unzipped the file for the provisioning bridge client when you created the provisioning bridge.

You can change the folder path where all log files for the provisioning bridge are stored and the log level for these log files. To do this, you modify the`log4j.properties`file.

The`log4j.properties`file is in the`conf`folder of the directory that you created when you unzipped the file for the provisioning bridge client, and contains properties associated with logging operations that the provisioning bridge performs.

- Navigate to the`conf`folder.
- Using a text editor, open the`log4j.properties`file.
- In the file, locate the following line of code:`property.baseLocation = ./logs/`
- Change the value of the`property.baseLocation`parameter to the folder path where you want all log files for the provisioning bridge to be stored.
- Locate the following line of code:`filter.threshold.level = error`
- Change the value of the`filter.threshold.level`parameter to one of the following log levels:

Log Level Description
`all`Capture all events
`debug`Capture fine-grained informational events that are most useful to debug the provisioning bridge
`error`Capture error events that might still allow the provisioning bridge to continue running
`info`Capture informational events that highlight the progress of the provisioning bridge at a coarse-grained level
- Save and close the`log4j.properties`file.

Note  
  
You must stop the provisioning bridge and restart it for the changes you made to the`log4j.properties`
