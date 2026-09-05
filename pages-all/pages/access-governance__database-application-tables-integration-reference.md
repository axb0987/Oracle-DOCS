# Database Application Tables Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/database-application-tables-integration-reference.htm
- Fetched: 2026-09-05 03:13 CDT

# Database Application Tables Integration Reference

## Database Application Tables Components Certified for Integration with Oracle Access Governance

The Database Application Tables components that you can integrate with are listed below.

### Certified Components

Certified Components
Component Type Component
Oracle Specific Requirements
System The target system can be database tables from any one of the following RDBMSs:
- Oracle Autonomous AI Database
- Oracle AI Database 23ai, 19c, 18c or 12c as a single database, pluggable database (PDB), or Oracle RAC implementation
- Oracle AI Database 10g and 11g as either a single database or Oracle RAC implementation
JDK JDK 1.6 or later
Microsoft SQL Server Specific Requirements
System Microsoft SQL Server 2016, 2017
JDBC Drivers For Microsoft SQL Server 2014: sqljdbc4 version 4.0
Microsoft MySQL Specific Requirements
System MySQL 5.x, MySQL 8.x
JDBC Drivers mysql-connector-java-5.1.12-bin
General Requirements
Format in which user data is stored in the system

You can use a Database Application Tables connector only if user data is stored in the target system in any one of the following formats:

- All user data is in a single table or view.
- User data is spread across one parent table and one or more child tables. This target system can be configured only as a managed system, and not as an authoritative source.
- All user data is in a single updatable view (that is based on one or more tables).
- User data is spread across one updatable view (that is based on one or more tables) and one or more child views (that are based on one or more tables). This type of system can be configured only as a managed system, and not as an authoritative source with this connector. In other words, an authoritative source cannot store child data.
Other requirements of the system

The system must meet the following requirement:

- If parent and child tables are not joined by a foreign key (for example, if you are using views), then the names of the foreign key columns in both tables must be the same.
- The primary key for any tables used in the target system should be provided by a single column for identity, account, entitlement, and lookup tables. Composite primary keys are only supported for tables linking entitlement and identity/account tables.

## Supported Configuration Modes for Database Application Tables Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on the requirement for on-boarding identity data, and provisioning accounts.

### Supported Modes

Database Application Tables Orchestrated System supports the following modes:
- Authoritative Source
You can use Database Application Tables as an authoritative (trusted) source of identity information for Oracle Access Governance where:
- All user data is in a single table or view OR
- All user data is in a single editable view (that is based on one or more tables)
- Managed System
You can manage Database Application Tables permissions where:
- All user data is in a single table or view OR
- All user data is in a single editable view (that is based on one or more tables) OR
- User data is spread across one parent table and one or more child tables. OR
- User data is spread across one editable view (that is based on one or more tables) and one or more child views (that are based on one or more tables). You can run full or partial data load. For more information, see[Configure Partial Data Load Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-partial-data-load-settings).

## Configure a Minimum Privileged Service User

### Configure A Minimum Privileged Service User For Database Application Tables (Oracle)

To enable a secure connection between Oracle Access Governance and the Database Application Tables (Oracle) database, you can create a service user with the minimum privileges required to configure the integration.

#### Permissions Required for Authoritative Source Mode

If you configure your Database Application Tables (Oracle) orchestrated system in authoritative mode, you need to grant read permissions to your service user on the table containing your identities, so that they can be loaded into Oracle Access Governance. The minimum set of permissions required in this case is`SELECT`permission on the table containing identity or person information.
An example might be:
```

```
where:
- `MYDBAT_PERSON`: Is the table in your Database Application Tables (Oracle) database containing identity information.
- `SERVICEUSER`: Is the service account user.

#### Permissions Required for Managed System Mode

If you configure your Database Application Tables (Oracle) orchestrated system in managed system mode, you need to grant read and write permissions for account tables and permissions tables, to allow for reconciliation, create, update, and delete of accounts and account permissions. The minimum set of permissions required in this case is`SELECT`,`INSERT`,`UPDATE`, and`DELETE`permissions on the account and account permission tables.
An example might be:
```

```

```

```

```

```

```

```

```

```
where
- `MYDBAT_PERSON`: Is the table in your Database Application Tables (Oracle) database containing account information.
- `MYDBAT_ROLES`: Is the table in your Database Application Tables (Oracle) database containing role information.
- `MYDBAT_GROUPS`: Is the table in your Database Application Tables (Oracle) database containing group information.
- `MYDBAT_PERSON_ROLE`: Is the table in your Database Application Tables (Oracle) database containing people role information.
- `MYDBAT_PERSON_GROUP`: Is the table in your Database Application Tables (Oracle) database containing group role information.
- `SERVICEUSER`: Is the service account user.

#### Permissions Required for Custom Scripts

To develop custom scripts for operations on the Database Application Tables (Oracle) integration as described in[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm), you will need to add permissions to any stored procedures or other database objects referenced in the custom scripts. If you create the stored procedures using the service user then you should not require any permissions. If stored procedures or other database objects are created in another user, then you should grant permissions as appropriate.
An example might be:
```

```
where:
- `MYDBAT_CUSTOMDEV`: Is the user you used to create the stored procedure.
- `GET_USERROLE`is the stored procedure name.
- `SERVICEUSER`: Is the service account user.

### Configure A Minimum Privileged Service User For Database Application Tables (MSSQL)

To enable a secure connection between Oracle Access Governance and the Database Application Tables (MSSQL) database, you can create a service user with the minimum privileges required to configure the integration.

#### Permissions Required for Authoritative Source Mode

If you configure your Database Application Tables (MSSQL) orchestrated system in authoritative mode, you need to grant read permissions to your service user on the table containing your identities, so that they can be loaded into Oracle Access Governance. The minimum set of permissions required in this case is`SELECT`permission on the table containing identity or person information.
An example might be:
```

```
where:
- `MYDBAT_PERSON`: Is the table in your Database Application Tables (MSSQL) database containing identity information.
- `SERVICEUSER`: Is the service account user.

#### Permissions Required for Managed System Mode

If you configure your Database Application Tables (MSSQL) orchestrated system in managed system mode, you need to grant read and write permissions for account tables and permissions tables, to allow for reconciliation, create, update, and delete of accounts and account permissions. The minimum set of permissions required in this case is`SELECT`,`INSERT`,`UPDATE`, and`DELETE`permissions on the account and account permission tables.
An example might be:
```

```

```

```

```

```

```

```

```

```
where
- `MYDBAT_PERSON`: Is the table in your Database Application Tables (MSSQL) database containing account information.
- `MYDBAT_ROLES`: Is the table in your Database Application Tables (MSSQL) database containing role information.
- `MYDBAT_GROUPS`: Is the table in your Database Application Tables (MSSQL) database containing group information.
- `MYDBAT_PERSON_ROLE`: Is the table in your Database Application Tables (MSSQL) database containing people role information.
- `MYDBAT_PERSON_GROUP`: Is the table in your Database Application Tables (MSSQL) database containing group role information.
- `SERVICEUSER`: Is the service account user.

#### Permissions Required for Custom Scripts

If you want to develop custom scripts for operations on the Database Application Tables (MSSQL) integration as described in[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm), you will need to add permissions to any stored procedures or other database objects referenced in your custom scripts. If you create the stored procedures using the service user then you should not require any permissions. If stored procedures or other database objects are created in another user, then you should grant permissions as appropriate.
An example might be:
```

```
where:
- `OBJECT::dbo`: Is the Microsoft MSSQL database object.
- `GET_USERROLE`is the stored procedure name.
- `SERVICEUSER`: Is the service account user.

### Configure A Minimum Privileged Service User For Database Application Tables (MySQL)

To enable a secure connection between Oracle Access Governance and the Database Application Tables (MySQL) database, you can create a service user with the minimum privileges required to configure the integration.

#### Permissions Required for Authoritative Source Mode

If you configure your Database Application Tables (MySQL) orchestrated system in authoritative mode, you need to grant read permissions to your service user on the table containing your identities, so that they can be loaded into Oracle Access Governance. The minimum set of permissions required in this case is`SELECT`permission on the table containing identity or person information.
An example might be:
```

```
where:
- `MYDBAT_PERSON`: Is the table in your Database Application Tables (MySQL) database containing identity information.
- `SERVICEUSER`: Is the service account user.

#### Permissions Required for Managed System Mode

If you configure your Database Application Tables (MySQL) orchestrated system in managed system mode, you need to grant read and write permissions for account tables and permissions tables, to allow for reconciliation, create, update, and delete of accounts and account permissions. The minimum set of permissions required in this case is`SELECT`,`INSERT`,`UPDATE`, and`DELETE`permissions on the account and account permission tables.
An example might be:
```

```

```

```

```

```

```

```

```

```
where
- `MYDBAT_PERSON`: Is the table in your Database Application Tables (MySQL) database containing account information.
- `MYDBAT_ROLES`: Is the table in your Database Application Tables (MySQL) database containing role information.
- `MYDBAT_GROUPS`: Is the table in your Database Application Tables (MySQL) database containing group information.
- `MYDBAT_PERSON_ROLE`: Is the table in your Database Application Tables (MySQL) database containing people role information.
- `MYDBAT_PERSON_GROUP`: Is the table in your Database Application Tables (MySQL) database containing group role information.
- `SERVICEUSER`: Is the service account user.

#### Permissions Required for Custom Scripts

If you want to develop custom scripts for operations on the Database Application Tables (MySQL) integration as described in[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm), you will need to add permissions to any stored procedures or other database objects referenced in your custom scripts. If you create the stored procedures using the service user then you should not require any permissions. If stored procedures or other database objects are created in another user, then you should grant permissions as appropriate.
An example might be:
```

```
where:
- `MYSQLDB`: Is the MySQL database in which you created the stored procedure.
- `GET_USERROLE`Is the stored procedure name.
- `SERVICEUSER`: Is the service account user.

## Supported Operations When Provisioning To Database Application Tables

When you provision an account from Oracle Access Governance to Database Application Tables certain operations are supported.

The Database Application Tables Orchestrated System supports the following account operations when provisioning a user:
- Create account
- Enable account
- Disable account
- Revoke account
- Assign permission
- Remove permission

## Supported Data Types

The data types supported for reconciliation and provisioning operations are listed in the following section:

### For Oracle AI Database

The data types supported for reconciliation and provisioning operations for an Oracle AI Database orchestrated system are as listed below:

- VARCHAR2
- CHAR
- NUMBER
- NUMERIC
- INTEGER
- INT
- SMALLINT
- DOUBLE
- FLOAT
- DECIMAL
- DEC
- REAL
- DATE
- TIMESTAMP

### For Microsoft SQL Server

The data types supported for reconciliation and provisioning operations for a Microsoft SQL Server database orchestrated system are as listed below:

- CHAR
- VARCHAR
- SMALLINT
- INT
- BIGINT
- DECIMAL
- NUMERIC
- NVARCHAR
- FLOAT
- REAL
- SMALLDATETIME
- DATETIME

### For MySQL

The data types supported for reconciliation and provisioning operations for an MySQL database orchestrated system are as listed below:

- BOOL
- SMALLINT
- MEDIUMINT
- INT
- BIGINT
- FLOAT
- DOUBLE
- DECIMAL
- CHAR
- VARCHAR
- TINYTEXT
- DATE
- DATETIME
- TIMESTAMP

## Default Supported Attributes

As Database Application Tables integration requires schema discovery, and the discovered schema is not fixed, there are no specific default supported attributes as such. You can modify your`schema.json`to add core and custom attributes as required. As a minimum you should include the`uid`and`name`attributes required for an Oracle Access Governance identity as defined in[Core Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/schema-json-file-reference.htm#db-tables-schema-json-coreidattributes).

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each Orchestrated System.

The default matching rule for Database Application Tables orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Authoritative Source

Identity matching checks if incoming identities match an existing identity or are new

Screen value :

`Employee user name = Employee user name`

Attribute name :

`Identity.userName = Identity.userName`
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.name = Identity.userName`

## Database Application Table Guidelines

When using database access tables with Oracle Access Governance you should consider the following guidelines in the design and structure of your tables.

### General Guidelines
Any database access tables should conform to the following guidelines:
- The Name and Key columns for any entity must be configured as NOT NULL.
- For a specific entity, the same database column can be configured as the Name and the Key . You can also use different columns for these if required.
- Any core attribute included in the ACCOUNT entity should comply with the following rules:
- The column data type should be compatible with the Oracle Access Governance-side data type.
- Any attribute that is configured as`"nature":["REQUIRED"]`in the schema JSON file should correspond to a NOT NULL database field.
- ENTITLEMENT and LOOKUP tables must have a primary key constraint on key columns.
- If related columns on ENTITLEMENT and LOOKUP tables match then there is no need to define a foreign key relationship between your ACCOUNT/TARGETACCOUNT tables and the ENTITLEMENT and LOOKUP tables. See the following section for more details.

### Table Relationships
User tables which map to ACCOUNT/TARGETACCOUNT entities may have a relationship with ENTITLEMENT and LOOKUP tables. When the Database Application Tables connector performs schema discovery, it will initially look for foreign keys (FK) defined as constraints in your database tables which define the relationship between your user table and your ENTITLEMENT or LOOKUP tables. This would look something like the example that follows for the relationship between a user table and a lookup table for the user's country:
```

```

If no foreign key is defined then the Database Application Tables connector will attempt to match on the column names. If the column names match then the relationship is matched. For example:
```

```

However, if there is no foreign key relationship defined between the tables, and the column names do not match, then an error will be thrown. This would happen, for example, if you define the columns as below:
```

```

The same principles as explained above for the relationship between a user and a lookup would apply when defining tables for the relationship between a user and entitlements.

## Associate Identity Attribute with Account Attribute

You can associate an identity attribute with an account attribute by editing the account attribute settings.

- Sign in to the Oracle Access Governance console and navigate to Service Administration → Orchestrated Systems .
- Select Manage Integration for the DBAT orchestrated system where you want to associate an identity attribute with an account attribute.
- Select Manage from the Account attributes tile.
- For the account attribute you want to map, select Edit associated identity attribute from the action menu.
- Select the identity attribute you want to associate with your account attribute and click Save . The value will now show in the Associated identity attribute columns for your account attribute.

## DBAT Affiliation Support for Custom Multivalued Identity Attributes

DBAT orchestrated systems provide support for affiliation data through the implementation of Custom (Complex) Multivalued Attributes.

Affiliation is enabled by adding a custom table for the affiliation required, and linking it to the account table. For example, you might have an account table, Users similar to this:

Account (e.g. USERS) → PK (USER_ID)
USER_ID USER_NAME FIRST_NAME LAST_NAME EMAIL STATUS
1 USR001 User One userone@email.com ACTIVE
2 USR002 User Two usertwo@email.com ACTIVE

Next, you need to create a custom table for the affiliation you want to represent. For example, you might want to have an affiliation which allows you to assign multiple job titles to an identity. To do this, create a table Jobs similar to this:

Affiliation (e.g. JOBS) → Composite PK (USER_ID, JOBCODE)
JOBCODE USER_ID JOBNAME DESCRIPTION
JB001 1 A Job This is a job
1 Another Job This is another job
2 A New Job This is a new job

The Account table is directly linked to the Affiliation table by the composite primary key (USER_ID, JOBCODE).

Finally, you need to add the affiliation to the schema.json fill as shown in the following snippet.

```

```

Include this table name along with other affiliation tables in the Integration settings. For more information, see[Affiliations](https://docs.oracle.com/en-us/iaas/Content/access-governance/multi-affiliations.htm)
