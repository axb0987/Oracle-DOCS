# Exporting Using the REST API
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm
- Fetched: 2026-09-05 02:17 CDT

# Exporting Using the REST API

This section provides example requests and responses when you want to export users, groups, and AppRoles from your environment into another identity domain using the identity domains REST API.

The following sections walk you through the steps:
- 

[Schedule the Export Job](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting__ScheduleTheExportJob-3FFF2CA7)
- 

[View Job Details](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting__ViewJobDetails-40007695)
- 

[View the Job Report](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting__ViewJobReport-40010B63)
- 

[Download the File](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Exporting.htm#Exporting__DownloadTheFile-400160A5)
Note  
  
To safely handle the export of the CSV file from an identity domain, any cell values that start with the following characters are escaped. This ensures that if a cell value starts with one of these blocklisted values, it's escaped in the CSV, which avoids CSV injection. For example, during export if the value is`@test`, the actual value will be`'@test'`.
- At:`@`
- Plus:`+`
- Minus:`-`
- Equals to:`=`
- Pipe:`|`
- Percentage:`%`

## Schedule the Export Job
Note  
  

To access the complete list of allowed CSV column names and their descriptions, use the following request:
```

```

See[Transferring Data](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../datatransfer/overview.htm)for more information on bulk loading using the identity domain Console.

To export users, groups, or AppRoles, send a POST request to the`/job/v1/JobSchedules`endpoint and use the payload provided in the example request. In the JSON example request body below, for resource specific`jobType`exports, the value for`jobType`can be`UserExport,``GroupExport`, or`AppRoleExport`, depending on the type of data that you're trying to export.

There's also a generic export option available where the value for`jobType`is`Export`, and then the attribute`resourceType`is added and the values can be`User,``Group`, or`AppRole`, depending on the type of data that you're trying to export.
Note  
  
Export AppRole memberships to only a single application. Exporting across multiple applications exports the membership of various AppRoles across all applications.

The examples below show both the resource specific`jobType`export and the generic export options.

Example Request for Resource-Specific jobType Export
```

```

Example Response for Resource-Specific jobType Export
Note  
  
Make note of the`id`value (bold in the example response). This is the value for the`jobScheduleid`that you specify in the next section.
```

```

Example Request for Generic Export
```

```

Example Response for Generic Export
Note  
  
Make note of the`id`value (bold in the example response). This is the value for the`jobScheduleid`that you specify in the next section.
```

```

## View Job Details

To view details from the export job, send a GET request to the`/job/v1/JobHistories`endpoint using the`jobScheduleid`as the identifier.

Example Request
```

```

Example Response
Note  
  
Make note of the`id`value (bold in the example response). This is the value for the job`historyId`that you specify in the next section.
```

```

## View the Job Report

To view the job report for the export job, send a GET request to the`/job/v1/JobReports`endpoint using the job`historyId`as the identifier.

Example Request
```

```

Example Response
Note  
  
Make note of the`name`value (bold in the example response). This is the value for the`fileName`that you specify in the next section.
```

```

## Download the File

To download the file from the server, send a GET request to the`/storage/v1/Files`endpoint using the`fileName`as the identifier.
```

```
