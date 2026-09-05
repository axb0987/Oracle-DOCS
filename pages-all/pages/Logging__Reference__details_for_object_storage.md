# Details for Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_object_storage.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Object Storage

Logging details for Object Storage logs.

## Resources
- buckets

## Log Categories

API value (ID): Console (Display Name) Description
write Write Access Events Includes logs for write events.
read Read Access Events Includes logs for read events.

## Availability

Object Storage logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Comments

Choose the log category for the type of information that you want to log. For example, if you enable a write log, the`requestAction`property would contain values of`PUT`,`POST`, or`DELETE`. If you enable a read log,`requestAction`would contain values of`GET`,`LIST`, or`HEAD`.
Note  
  
Service logs for Object Storage are delivered on a best effort basis. In limited situations, a small number of log entries may not be delivered successfully.

## Contents of an Object Storage Log

Property Description
additionalDetails

Includes the following fields when applicable to the particular log:
- versionId: From PutObject and DeleteObject responses
- isDeleteMarker: From the DeleteObjectVersion response
- retentionRuleName
apiType Originating Object Storage API:
- native
- s3-compatible
- swift
authenticationType Request authentication type:
- user
- service
- resource
- instance
bucketCreator OCID of the bucket creator
bucketId OCID of the bucket
bucketName Name of the bucket
clientIpAddress IP address of the requesting client
compartmentId OCID of the compartment
compartmentName Name of the compartment
credentials Request security credentials
endTime Request end timestamp
errorCode If present, a short error code meant for programmatic parsing that defines the error
eTag Entity tag (ETag) for the resource
isPar Boolean describing whether this is a pre-authenticated request:
- true
- false
message Human-readable string describing the request
namespace Object Storage namespace used for the request
objectName Name of the object
opcRequestId Client request ID for tracing
principalId OCID of the requestor
principalName Name of the requestor
region Region identifier
requestAction HTTP method of the request (DELETE/GET/HEAD/POST/PUT)
requestResourcePath Resource path of the request
startTime Request start timestamp
statusCode Response status code
tenantId OCID of the tenant
tenantName OCID of the tenant
userAgent User Agent that sent the request to Object Storage

## An Example Object Storage Log
```

```

## Object Storage Log Object Name

Objects that store Object Storage data use the following naming format:
```

```

For example:
```

```

## Using the Command Line Interface (CLI)

See[Object Storage Example](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/../Task/object_storage_eg.htm)
