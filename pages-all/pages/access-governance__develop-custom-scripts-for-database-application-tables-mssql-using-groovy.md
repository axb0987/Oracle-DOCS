# Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-mssql-using-groovy.htm
- Fetched: 2026-09-05 03:14 CDT

# Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy

## Custom Scripting for Database Application Tables (MSSQL) Overview

When you provision accounts from Oracle Access Governance using the Database Application Tables integration, operations such as create, update, and delete are implemented using the default supplied code. On occasions where you wish to modify the default supplied operations, you can optionally provide your own custom scripts which implement your own specific provisioning operation requirements. This step is completely optional, you do not have to create custom scripts if the default operations provide you with what you need. You can add custom scripts to any operations supported. If you choose custom scripts, you only need to add them where you require the default operation to be modified, you can have a combination of custom and default scripts for the operations supported, though you can only have one or the other option for each specific operation. For example, the create operation might be implemented with a custom script that adds some functionality specific to your organization, while the delete operation is unchanged and uses default functionality.

Once you have implemented and configured your Database Application Tables to use a custom script then that script will be used when you next perform a provisioning or data load operation.
Note  
  
Any custom script must be implemented using Groovy format. Other scripting formats are not supported.

When you create a Database Application Tables orchestrated system you can identify scripts to be run for a number of provisioning operations on the database application containing account data. These operations are:
- Create
- Update
- Delete
- Dataload
- Add relationship data
- Remove relationship data These scripts should be located on the agent host, in the install directory of the agent, for example,`/app/<custom script>`. You configure the agent with the location of the scripts in the integration settings for your orchestrated system. You should ensure that the operating system user running the agent has read/write permissions for any custom scripts.
When you perform a provisioning task, your script will be run as a replacement to the standard processing associated with the task. The script must handle the default provisioning task such as create or update, and can also have custom tasks above and beyond the default provisioning process, such as:
- Perform custom table updates
- Custom auditing
- Send custom notifications This means that you have two options for provisioning processing using the Database Application Tables integration:
- Use the default logic provided with the Database Application Tables connector
- Use the custom logic implemented in scripts Custom scripts are only used when configured in your orchestrated system. So, if you have specified a create script when creating your orchestrated system, but no script for update, then the custom script will be used for the create provisioning task, while the update task will be implemented using the default connector processing.

You should also note that all custom script types are supported for an orchestrated system configured for managed system mode. The only script type supported for authoritative source mode is the Dataload type, which is supported for both modes.

## Sample Database Schema

The samples provided in the following sections are based on the database tables described in this section.

### MYDBAT_PERSON
```

```

### MYDBAT_GROUPS
```

```

### MYDBAT_ROLES
```

```

### MYDBAT_PERSON_GROUP
```

```

### MYDBAT_PERSON_ROLE
```

```

### MYDBAT_COUNTRY
```

```

Note  
  
Child tables such as`mydbat_roles`,`mydbat_groups`, and`mydbat_country`should have a primary key constraint defined. If no primary key is defined for child tables then your validate operation will fail and you will see an error Key for table &lt;tablename&gt; are not defined .

## Groovy Script Arguments

The following arguments can be used in your Groovy scripts:

Script Arguments
Argument Description
connector The Database Application Tables connector object.
timing

When the Groovy script is called. The timing attribute also explains the type of operation being performed. For example, if it is a search operation, then the object class being searched is also returned.
The following is the format of the timing argument for lookup field synchronization:
```

```
In this format`OBJECT_CLASS`is replaced with the type of object being reconciled.
For example, for a lookup field synchronization scheduled job that contains the object type Role , the value of the timing argument will be as follows:
```

```

attributes All attributes.
trace Logger as a script trace bridge to the application
where String where condition for execute query, or null.
handler resultSetHandler or SyncResultsHandler for the connector objects produced by the execute query, sync operation or null return.
quoting The type of table name quoting to be used in SQL. The default value is an empty string. The value of this argument is obtained from the integration settings.
nativeTimestamps Specifies whether the script retrieves the timestamp data of the columns as java.sql.Timestamp type from the database table. This information is obtained from the integration settings.
allNative Specifies whether the script must retrieve the data type of the columns in a native format from the database table. The value of this argument is obtained from the integration settings. The value of this argument specifies whether the script must throw exceptions when a zero (0x00) error code is encountered.
enableEmptyString Specifies whether support for writing an empty string instead of a NULL value must be enabled. The value of this argument is obtained from the integration settings.
filterString String filter condition for execute query, or null.
filterParams List of filter parameters. Each parameter is present in the COLUMN_NAME:VALUE format. For example, FIRSTNAME:test.
syncattribute Name of the database column configured for incremental reconciliation. This argument is available in the sync script, which is called during an incremental reconciliation run.
synctoken Value of the sync attribute. This argument is available in the sync script.

## Sample Dataload Script

The data load script reads the data from all the tables for all the defined entities. In this scenario, the term data load refers to the full data load and the lookup data load.

This sample script reads user data from the MYDBAT_PERSON table, and the users' relationship data from the MYDABAT_PERSON_ROLE and MYDBAT_PERSON_GROUP tables. Entitlements data is read from the MYDBAT_GROUPS table, and lookup data is read from the MYDBAT_COUNTRY table. It also has support for a basic filter search on MYDBAT_PERSON table. All these data reads are done using stored procedures.

### Dataload Script

```

```

### Stored Procedure: Load Users

```

```

### Stored Procedure: Filtered User Search

```

```
This is a very basic example of filter search with only one filter condition, for example, MYDBAT_PERSON.USERID:21 . This is used specifically for writeBack processing after the create operation

### Stored Procedure: Get Roles

```

```

### Stored Procedure: Get User Roles

```

```

### Stored Procedure: Get Groups

```

```

### Stored Procedure: Get User Groups

```

```

### Stored Procedure: Get Lookups (Country)

```

```

## Sample Create Script

This script is invoked during provisioning of a new account from Oracle Access Governance. Here we are inserting data into the MYDBAT_PERSON table.

### Create Script

```

```

## Sample Add Child Script

This script is invoked during provisioning of entitlements/permissions to users from Oracle Access Governance. Here we are inserting data into the MYDBAT_PERSON_GROUP and MYDBAT_PERSON_ROLE tables.

### Add Child Script

```

```

## Sample Remove Child Script

This script is invoked during deprovisioning of entitlements/permissions from users from Oracle Access Governance. Here we are removing data from MYDBAT_PERSON_GROUP and MYDBAT_PERSON_ROLE tables using stored procedures.

### Remove Child Script

```

```

### Stored Procedure: Remove Child
```

```

## Sample Delete Script

This script is invoked during revocation of an account from Oracle Access Governance. Here we are deleting the data user relationship tables, MYDBAT_PERSON_ROLE and MYDBAT_PERSON_GROUP, as well as data from the MYDBAT_PERSON table

### Delete Script

```

```

### Stored Procedure: Delete
```

```

## Sample Update Script

This script is invoked during provisioning operations when account is updated from Oracle Access Governance. Here we are updating the data in MYDBAT_PERSON table

### Update Script

```

```
