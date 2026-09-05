# Generic REST Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm
- Fetched: 2026-09-05 03:14 CDT

# Generic REST Reference

A Generic REST Orchestrated System is created with a minimal template, which is updated at runtime using OCI Functions to update the Orchestrated System with object classes, lookup types, and outbound transformation data.

## Schema Discovery High-Level Workflow

Schema discovery is the process by which a Generic REST Orchestrated System applies OCI Function templates to enable discovery of the schema, object classes, attributes, and connection details for the configured Authoritative Source or Managed System.

Schema discovery occurs when an Orchestrated System is created in Oracle Access Governance. Simplified workflows for Day0 and DayN scenarios are detailed in the following tables.

### Day0 Workflow

Day0 Workflow
Step # Task/Operation Description
1 Create Orchestrated System

Create Orchestrated System using the Oracle Access Governance Console.

The Orchestrated System is created with details of the OCI Function you have created to return details from the required Authoritative Source or Managed System.
Based on the details entered into the Orchestrated System, the following operation is created.
- Validate
2 Validate operation execution
The Validate operation is executed and, based on the configured schema template, fetches the schema, including the following object classes:
- Identity : fetches core attributes only. Must have the mandatory core objects detailed[here](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm#rest-generic-rest-schema-discovery-mandatory-schema-attributes)
- Non-identity : fetches all attributes. Must have the minimum attributes detailed[here](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm#rest-generic-rest-schema-discovery-mandatory-schema-attributes)

The configure test template is called to validate connectivity with the Managed System.
3 Post Validate operation
On successful execution of the Validate operation, the following operations are created:
- Lookup Data Load
- Full Data Load

### DayN Workflow

DayN Workflow
Step # Task/Operation Description
1 Select Fetch Attributes from the Identity Attributes page of the Oracle Access Governance. See[Fetch Latest Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#fetch-attributes)for further details. A Schema Discovery operation is created in the Orchestrated System
2 Schema Discovery operation execution The Schema Discovery operation is executed and, based on the configured schema template, fetches the schema, including the following object classes:
- Identity : fetches core and custom attributes
- Non-identity : fetches all attributes
3 Refresh the Identity Attributes page The custom attributes list starts showing the new custom attributes for identity object class. If all the above completes successfully, the Orchestrated System is available for scheduler to create subsequent Full Data Load operations.

## Generic REST Schema Discovery Mandatory Schema Attributes

During schema discovery certain mandatory attributes must be returned as part of the schema output.

### Identity Object Class

The mandatory attributes that must be returned as part of the schema output for the Identity object class are:

- uid
- name
- email
- firstName
- middleName
- lastName
- displayName
- employeeType
- title
- empNo
- status
- jobCode
- state
- risk
- location
- department
- managerUid
- managerLogin
- organizationUid
- organizationName
- country
- postalCode
- territory

```

```

### Non-Identity Object Class

The mandatory attributes that must be returned as part of the schema output for the Non-Identity object class are:

- uid
- name

```

```

## Schema Template Outline

In order to support schema discovery you need to create your schema template using the supported outline.

### Schema Outline
The schema outline you should follow when creating your schema template is:
```

```

## Schema Template Output

Output of the schema template is returned as a JSON document.

### Schema Template Output
Your schema template output will look similar to that provided in the reference implementation (`<ReferenceBase>/functions/grc-schema-template/src/main/resources/schema/applications/<YourApplicationName>/TEMPLATE.json`):
```

```

## Request Template Outline

In order to support requests to the required Authoritative Source or Managed System you need to create your request template using the supported outline.

### Request Outline
The request outline you should follow when creating your request template is:
```

```

### Pagination Support
The request outline supports a number of pagination methods to prevent large search results causing excessive network traffix. The following pagination methods are supported:
- OFFSET
- PAGE_INCREMENT
- PAGE_TOKEN
Parameters for these methods are detailed as follows. These should be added to the request outline.

Pagination Support
Pagination Type Prerequisite Configuration
OFFSET The REST API that you are integrating with Oracle Access Governance must support OFFSET pagination when returning a response.

If`paginationType`is set to OFFSET then you should add the following parameter values to the outline:

```

```

PAGE_INCREMENT The REST API that you are integrating with Oracle Access Governance must support PAGE_INCREMENT pagination when returning a response.

If`paginationType`is set to PAGE_INCREMENT then you should add the following parameter values to the outline:

```

```

PAGE_TOKEN The REST API that you are integrating with Oracle Access Governance must support PAGE_TOKEN pagination when returning a response.

If`paginationType`is set to PAGE_TOKEN then you should add the following parameter values to the outline:

```

```

Note  
  
The name for a particular pagination parameter may vary depending on the REST API that you are connecting with. For example, for OFFSET pagination, the parameters could be:
```

```
or
```

```
You should use the name specified by your API, but use the values as discussed in this article.

## Request Template Output

Output of the request template is returned as a JSON document for defined entities and operations.

### Request Template Output

Your request template output will look similar to that provided in the reference implementation (`<ReferenceBase>/functions/grc-schema-template/src/main/resources/request/applications/<YourApplicationName>/<EntityName>/<Operation>_TEMPLATE.json`):

For example, from the reference implementation:

- EntityName: UserAsIdentity
- Operation: GET
```

```

- EntityName: UserAsIdentity
- Operation: SEARCH
```

```

## Response Template Outline

In order to support response format for identity and account data you need to create your response template using the supported outline.

### Response Outline
The response outline you should follow when creating your response template is:
```

```

## Response Template Output

Output of the response template is returned as a JSON document for defined entities and operations.

### Response Template Output

Your response template output will look similar to that provided in the reference implementation (`<ReferenceBase>/functions/grc-response-template/src/main/resources/response/applications/<YourApplicationName>/<EntityName>/<Operation>_TEMPLATE.json`):

For example, from the reference implementation:

- EntityName: UserAsIdentity
- Operation: GET
```

```

- EntityName: UserAsIdentity
- Operation: SEARCH
```

```

## Basic Authorization - Sample Token Creation Code

If you use basic authorization with your Generic REST orchestrated system you will need to create an authorization token. The sample code which follows, gives an example of how to code this function:

### Sample Token Creation Code
If you use basic authorization with your Generic REST orchestrated system you will need to create an authorization token. The sample code which follows, gives an example of how to code this function:
```

```

## OAuth Authorization - Sample Token Creation Code

If you use OAuth authorization with your Generic REST orchestrated system you will need to create an authorization token. The samples which follow, give an example of how to code this function:

### Sample Token Creation Code

For IDCS orchestrated system :
This code is provided with the sample implementation that comes with the Generic REST Connector, and can be found at`<SampleBase>/grc-serverless-function-samples/idm-agcs-serverless-multi-application-sample/grc-commons/src/main/java/com/oracle/idm/agcs/grc/fn/commons/provider/IDCSAuthenticationProvider.java`.
```

```

For AzureAD orchestrated system :
This code is provided with the sample implementation that comes with the Generic REST Connector, and can be found at`<SampleBase>/grc-serverless-function-samples/idm-agcs-serverless-multi-application-sample/grc-commons/src/main/java/com/oracle/idm/agcs/grc/fn/commons/provider/AzureAdAuthenticationProvider.java`.
```

```
