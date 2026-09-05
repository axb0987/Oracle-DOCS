# Details for File Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_file_storage.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for File Storage

Logging details for File Storage logs.

For more information, see[File Storage Logging](https://docs.oracle.com/iaas/Content/File/Concepts/logging.htm).

## Resources
- mount targets

## Log Categories

API value (ID): Console (Display Name) Description
`filestorageservice.mounttarget.nfs.logging`NFS Logs Mount target NFS logs.

## Availability

File Storage logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Contents of a File Storage Mount Target NFS Log

File Storage logs capture detailed information about requests related to troubleshooting and monitoring. Each log entry contains information such as the time the request was received, error type, and extra details related to the specific error. Details appear as values in the`data`field. This value is a JSON-formatted data with the following fields.

Property Description
`level`The level of the log event.
`message`A summary of the log event.
`numberOfOccurances`The number of times that this event has occurred.

## An Example Mount Target NFS Log
```

```
