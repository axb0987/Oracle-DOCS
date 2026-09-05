# Importing Using the REST API
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm
- Fetched: 2026-09-05 02:17 CDT

# Importing Using the REST API

This section provides example requests and responses when you want to import users, groups, and AppRoles into your environment using the identity domains REST API..

The following sections walk you through the steps:
- 

[Import the CSV File to Storage](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__ImportTheCSVFileToStorage-3F97EBFF)
- 

[Schedule the Job to Import the CSV File into Your Environment](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__CreateTheScheduledJobToImportTheCSV-3F984404)
- 

[Verify That the Job Was Successful](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__VerifyThatTheJobIsSuccessful-3F986154)
- 

[Review the Job Report](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__ReviewTheJobReport-3F987990)
- 

[When There Are Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__WhenThereAreErrors-3FFEAD0C)
- 

[Replacing Existing Values to Complex Multi-Valued Attributes (CMVA)](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm#Importing__replaceCMVAAttributes)
Note  
  
To safely handle the import of the CSV file into an IAM identity domain, if any cell values are escaped to avoid CSV injection, the quotes are removed. For example, during import if the cell value is`'@test'`, the actual value will be`@test`.
- At:`@`
- Plus:`+`
- Minus:`-`
- Equals to:`=`
- Pipe:`|`
- Percentage:`%`

## Import the CSV File to Storage

To import the CSV file to storage, send a POST request to the`/storage/v1/Files`endpoint.
Note  
  
See[Importing and Exporting Users, Groups, and AppRoles](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/BulkImportExport.htm)for more information on the CSV file.

Parameter Description
`fileName`Enter the name that you want the file to have when you save it to storage.
`isPublic`Indicates whether the file is private or public. Currently, only private files are supported. Set this value to`false.`
`contentType`Files are limited to a`contentType`of`text/csv`or`application/directory.`
`file`Enter the name of file that you want to upload.

Example Request
```

```

Example Response
Note  
  
Make note of the`fileName`value (bold in the example response).
```

```

## Schedule the Job to Import the CSV File into Your Environment
Note  
  

To access the complete list of allowed CSV column names and their descriptions, use the following request:
```

```

See[Transferring Data](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../datatransfer/overview.htm)for more information on bulk loading using the identity domain Console.

To create a scheduled job, send a POST request to the`/job/v1/JobSchedules`endpoint. In the JSON example request body below, for resource specific`jobType`imports, the value for`jobType`can be`UserImport,``GroupImport`, or`AppRoleImport`, depending on the type of data that you're trying to import.
There's also a generic import option available where the value for`jobType`is`Import`, and then the attribute`resourceType`is added and the values can be`User,``Group`, or`Grant`(for AppRole), depending on the type of data that you're trying to import.
Note  
  
Use of the`resourceType`of`AppRole`for import isn't supported.

The examples below show both the resource specific`jobType`import and the generic import options.

Example Request for Resource Specific jobType Import
```

```

An additional parameter is required for the`AppRoleImport jobType:`
```

```

Example Response for Resource Specific jobType Import
Note  
  
Make note of the`id`value (bold in the example response). This is the value for the`jobScheduleid`that you specify in the next section.
```

```

Example Request for Generic Import
```

```

An additional parameter is required for the`Grant ResourceType:`
```

```

Example Response for Generic Import
Note  
  
Make note of the`id`value (bold in the example response). This is the value for the`jobScheduleid`that you specify in the next section.
```

```

## Verify That the Job Was Successful

To verify that the import job succeeded, send a GET request to the`/job/v1/JobHistories`endpoint using`jobScheduleid`as the identifier.

Example Request
```

```

Example Response
Note  
  
Make note of the`id`value (bold in the example response). This is the value for the`historyId`that you specify in the next section.
```

```

## Review the Job Report

To review the status of the import job, send a GET request to the`/job/v1/JobReports`endpoint using`historyId`as the identifier. If there are any failures in the import process, it lists those failures in the form of a CSV file in storage.
```

```

## When There Are Errors

If you encounter errors during a bulk-load operation and you can't fix them by modifying the entries in the import file, you can set a diagnostics level to capture operational logs during the bulk-load operation. You can then view those logs to help you to determine the cause of the problem. See[Running the Diagnostic Data Report](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../reports/run-diagnostic.htm)for more information.

If you encounter errors after a bulk-load operation, use the Jobs page to help you resolve the errors.

- 

Access the Jobs page by selecting Jobs in the Identity Cloud Service console.
- 

Select View Details for the failed job.
- 

Select Export Errors, and then download the exported error file.
- 

Open the comma-separated value error file using any .csv file manager, such as Microsoft Excel. The exported file contains all the failed rows, and the failure reason in the Error Message column.
- 

Correct the errors, and then remove the Type and Error Message columns from the file.
- 

Reimport the file.

See the[Viewing Jobs and Job Details](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../jobs/understand_jobs.htm)for more information.

## Replacing Existing Values to Complex Multi-Valued Attributes (CMVA)

When administrators update users by using Import, by default new values will be added to existing multivalued attributes. For example, say that a user has set her work email to alice@myservice.invalid . Email is a multivalued attribute, and when an administrator imports a CSV file with the updated email value (for example administrator@myservice.invalid ), the new email is added to the existing instance of email, and both the values are saved.

You can also update the email values. For example, to update the email value to alice1@myservice.invalid , pass the`replaceExistingMultiValuedValues`attribute when scheduling an Import job.
Sample JSON payload:
```

```

## Viewing a User Import Job Report

This section provides example requests and responses when you want to view a user import job report when you import users into your environment using the identity domains REST API.

### Example Request

To review the user import job, send a GET request to the`/job/v1/UserImportJobReports`endpoint using`historyId`as the identifier.
```

```

### Example Response
```

```

## Viewing Group Import Job Reports

This section provides example requests and responses when you want to view a group import summary job report and a group import detailed job report when you import groups into your environment using the identity domains REST API.

### Example Import Summary Job Request

To review the group import summary job, send a GET request to the`/job/v1/GroupImportSummaryJobReports`endpoint using`historyId`as the identifier.
```

```

### Example Import Summary Job Response
```

```

### Example Import Detailed Job Request

To review the group import detailed job, send a GET request to the`/job/v1/GroupImportDetailedJobReports`endpoint using`historyId`as the identifier.
```

```

### Example Import Detailed Job Response
```

```

## Viewing AppRole Membership Import Job Reports

This section provides example requests and responses when you want to view an AppRole membership import summary job report and an AppRole membership import detailed job report when you import AppRole memberships into your environment using the identity domains REST API.

### Example Import Summary Job Request

To review the AppRole membership import summary job, send a GET request to the`/job/v1/AppRoleMembershipImportSummaryJobReports`endpoint using`historyId`as the identifier.
```

```

### Example Import Summary Job Response
```

```

### Example Import Detailed Job Request

To review the AppRole membership import detailed job, send a GET request to the`/job/v1/AppRoleMembershipImportDetailedJobReports`endpoint using`historyId`as the identifier.
```

```

### Example Import Detailed Job Response
```

```
