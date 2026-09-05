# In-transit Encryption-enabled Mount Targets Stop Responding to OS Commands
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/intransit-encryption-commands-unresponsive.htm
- Fetched: 2026-09-05 02:06 CDT

# In-transit Encryption-enabled Mount Targets Stop Responding to OS Commands

Commands issued to a file system using in-transit encryption receive no response.

Cause: More than 4096 client connections to the in-transit encryption-enabled mount target.

Solution: Reduce the number of SSL clients (both instances and processes) concurrently connecting to the mount target to less than 4096.

This behavior is because of a known and documented limitation of the number of SSL connections the mount target allows. For more information, see[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/intransitencryption.htm#Limitations_and_Considerations)
