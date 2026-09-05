# Sample Implementation of a Custom SCIM Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/scim/sample-implementation-custom-scim-gateway.htm
- Fetched: 2026-09-05 02:28 CDT

# Sample Implementation of a Custom SCIM Gateway

Oracle provides a sample application that conforms to SCIM specifications, and which you can use to develop a custom SCIM gateway to integrate it with your custom application.

You can download the sample implementation`idcs-scim-gateway-app`from[https://github.com/oracle-samples/idm-samples/tree/master/idcs-scim-gateway-app](https://github.com/oracle-samples/idm-samples/tree/master/idcs-scim-gateway-app).

This custom gateway exposes HTTP endpoints to enable operations such as creating, searching for, updating, and deleting users. The custom gateway stores information about the users locally in the`db.json`file. This file has the`JSON`format.

[

Item Description

GET http(s)://&lt;scimgatehost:port&gt;/scimgate/Users

GET http(s)://&lt;scimgatehost:port&gt;/scimgate/Users/&lt;id&gt;

POST http(s)://&lt;scimgatehost:port&gt;/scimgate/Users

PUT http(s)://&lt;scimgatehost:port&gt;/scimgate/Users/&lt;id&gt;

DELETE http(s)://&lt;scimgatehost:port&gt;/scimgate/Users/&lt;id&gt;

The sample application uses express and body-parser packages. The`server.js`file implements a route for users' endpoints:

```

```

The`routes/users.js`file defines the SCIM REST API endpoints, and maps each endpoint to the corresponding JavaScript function:

```

```

The`user.controller.js`file implements JavaScript functions to create, read, update, and delete users in the local user store, represented by the`userdb.json`file:

```

```

The`userdb.json`file contains an array of users, and the structure of each user entry follows the SCIM specification standard, using a subset of the user attributes:
```

```

To authorize the client to make HTTP requests, the sample SCIM gateway application uses two environment variables that you must set before running the application:`ADMINUSER`and`ADMINPASS`. These variables represent the administrator's user name and password for your API authentication service. You provide values for these variables by setting up the`run.sh`shell script for UNIX or Mac environments, or the`run.bat`batch script for Windows environments.

IAM sends these administrative credentials in the form of an authorization header for all requests to authenticate the administrator's credentials, and then accesses the custom SCIM gateway using the`basic`grant type.

You can modify the sample application's source code and implement other types of authentication methods to match your requirements.

You can also change the sample application's source code so that instead of contacting the local user store (represented by the`userdb.json`
