# Schema JSON File Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/schema-json-file-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# Schema JSON File Reference

On creation of a Database Application Tables orchestrated system, the agent creates a`schema.json`in the agent directory (`<agent-volume>/data/schema`) which maps identity data between the integrated database tables and Oracle Access Governance. This file can be accepted as-is, or changed by you to configure what entities and attributes are mapped to Oracle Access Governance for consideration in campaigns and reviews.

## Schema Discovery Flow

The schema discovery flow for Database Application Tables is as follows:

- Day0 : When you create the Database Application Tables orchestrated system, the initial`schema.json`file is created, based on the integration settings you enter. The schema file is created with details of tables and columns containing user data for Account, Entitlement, and Lookup entities. Relationship information is loaded from the configuration you supply, together with any constraints set in the database (Primary and Foreign keys). The intermediate schema JSON file will contain mapping for the following attributes by default, if they are defined. To map additional attributes you should edit the`schema.json`file:
- UID :`__UID__`
- Name :`__NAME__`
- Status :`__ENABLE__`
- Password :`__PASSWORD__`
- DayN : DayN activities take place at any point after you have generated the intermediate schema JSON file. The default file created by the agent can be used for testing, but does not support full data load since it only brings UID and name attributes. For full data load you should edit the file to determine which entities and attributes get passed to Oracle Access Governance. For full details on the structure and options available when editing the`schema.json`, refer to[Schema JSON File Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/schema-json-file-reference.htm).
Note  
  
Post-Day0 you cannot rerun schema discovery against the source database and generate a new schema file. The schema JSON file located with your agent is the source of truth for DayN activities, and any updates must be made in the file. DayN activities may include the following:
- Run dataload with the limited schema . You can run a test dataload with the limited schema generated on Day0. This will only include, where available, the attributes uid, name, status, and password.
- Modify schema file : You can modify the`schema.json`file to update Account, Entitlement, and Lookup details if required. Some reasons why you might do this are:
- You want to onboard attributes additional to the default uid, name, status, and password ones. To do this, set the`name`property for any attributes you want to be included.
- If there is a change in the source database then this should be reflected in the schema file. For example, if you add a new column into the ACCOUNT table, that would need to be added to the schema file as an attribute.
- You should perform a schema discovery operation which will fetch the latest custom attribute information. For details on how to perform this task, see[Fetch Latest Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#fetch-attributes).
- To apply outbound transformation, you must update it from the Oracle Access Governance Console. Any transformation rule applied within`Schema.json`would not be considered. To apply transformation rule, see[Apply Outbound Transformations for Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-outbound-transformations-for-identity-attributes). However, if you change the attribute or delete an attribute in`Schema.json`, the transformation rules, related to that particular account attribute, gets deleted during Schema Discovery operation.
- Run data load and provisioning operations : Using the discovered schema, load user data into Oracle Access Governance from the integrated database, and allow Oracle Access Governance to provision accounts and permissions in the integrated database.

## Intermediate Schema JSON For Managed System

The intermediate`schema.json`file is generated using all information available from the configuration you supply during orchestrated system creation. This serves as a template to which you can make any changes that affect the user data you can onboard. The structure of the intermediate`schema.json`file is as follows:
```

```

Note  
  
The`uiProperties`attribute is only in scope for TARGETACCOUNT entity types. It should not be used for ACCOUNT, ENTITLEMENT, or LOOKUP entity types.

The schema can contain entities from the following types:
- ACCOUNT : The ACCOUNT entity type maps to the Oracle Access Governance Identity entity. Attributes from the ACCOUNT entity type are used to populate an Identity within Oracle Access Governance.
- TARGETACCOUNT : The TARGETACCOUNT entity type maps Oracle Access Governance Account entity. When you provision an account in your database application, attributes from the ACCOUNT Oracle Access Governance entity type will be used to populate the TARGETACOUNT database entity.
- ENTITLEMENT : ENTITLEMENT maps to Oracle Access Governance Permission .
- LOOKUP : LOOKUP maps to Lookup information in Oracle Access Governance.
When the intermediate schema JSON is generated, it populates both ACCOUNT and TARGETACCOUNT for each user in the database tables. This happens regardless of whatever mode you configure the orchestrated system, authoritative source and/or managed system. However, when the dataload is run, then the following rules apply regarding which of these entities are actually created in Oracle Access Governance.
- Mode selected is Authoritative Source only:
- ACCOUNT and TARGETACCOUNT are generated in the schema JSON.
- Only an Identity is created in Oracle Access Governance, based on the values of ACCOUNT.
- TARGETACCOUNT can be ignored.
- Mode selected is Managed System only:
- ACCOUNT and TARGETACCOUNT are generated in the schema JSON.
- Only an Account is created in Oracle Access Governance, based on the values of TARGETACCOUNT.
- ACCOUNT can be ignored.
- Mode selected is Authoritative Source and Managed System .
- ACCOUNT and TARGETACCOUNT are generated in the schema JSON.
- Identity is created in Oracle Access Governance, based on the values of ACCOUNT.
- Account is created in Oracle Access Governance, based on the values of TARGETACCOUNT.
Note  
  
Any entitlements that are granted directly in the database tables, that are then loaded into Oracle Access Governance cannot be managed by Oracle Access Governance when the orchestrated system is configured in managed systems mode. Only entitlements that originate in a provisioning request from Oracle Access Governance can be managed by Oracle Access Governance.

## Core Identity Attributes

When you run Database Application Tables in authoritative source mode, you can onboard user data from your integrated database into Oracle Access Governance, which is used to create an Oracle Access Governance Identity.

Note  
  
For source of identities, schema discovery supports adding and updating identity attributes. However, after an identity attribute has been onboarded into Oracle Access Governance, removing the corresponding attribute from the`schema.json`file and rerunning schema discovery doesn't remove the existing identity attribute from Oracle Access Governance.
The following identity core attributes that can be assigned to an Oracle Access Governance. The element,`"nature": ["REQUIRED"]`indicates that an attribute must be NOT NULL in the source database. The attribute must be included in the schema discovery, you can then make a choice whether to include it into the schema you want to integrate.
```

```

Note  
  
Use either`managerUid`or`managerLogin`as the core identity attribute. The system returns a validation error if both attributes are included in the identity schema.

## User Status

When you run Database Application Tables in authoritative source mode, you can onboard user data from your integrated database into Oracle Access Governance, which is used to create an Oracle Access Governance Identity.

When you configure the orchestrated system you are prompted for the database column holding the status of a user record. This column determines whether the user is enabled or disabled in Oracle Access Governance. This information is always captured during full data load, irrespective of the configured mode (authoritative source or managed system).
You also configure the following boolean values for enabled/disabled status:
- User account enabled status value : This value will default to ACTIVE or can be defined as any text value from the database which maps to a status of enabled in Oracle Access Governance. Some examples include Y , Yes , true and so on.
- User account disabled status value : This value will default to INACTIVE or can be defined as any text value from the database which maps to a status of disabled in Oracle Access Governance. Some examples include N , No , false and so on.
Mapping from the database value to Oracle Access Governance enabled/disabled status uses the following logic:
- If the user has a status which equals the User account disabled status value value then the user will be marked as disabled in Oracle Access Governance.
- If the user has any other value then it is assumed that the user is enabled and the user is marked as such in Oracle Access Governance.

## Updating the Intermediate Schema JSON File

You can update the intermediate schema JSON file to include attributes in the Oracle Access Governance schema.

To include or exclude Oracle Access Governance schema attributes, consider the following example entity, which shows an example of an ACCOUNT entity:

```

```

### Including Attributes in your Schema
Note the`name`and`targetName`parameters for the attributes listed in the example. You will see that in all cases the`targetName`parameter is populated. This is because this parameter maps to the column name in your Oracle database which contains the user information you are integrating. So, for example, we have`FIRSTNAME`,`LASTNAME`,`DESCRIPTION`, and so on. The`name`parameter is, however, not always populated. This is because the`name`parameter correlates to the attribute in the schema on the Oracle Access Governance side. If`name`is populated, then that parameter is included in the Oracle Access Governance schema, for example:
```

```
If`name`is not populated, then that parameter is not included in the Oracle Access Governance schema. In the example above the parameter`DESCRIPTION`is not included:
```

```

### Including Lookup Tables

To include lookup tables to your schema, you use the same method as above, by setting the`name`parameter in your schema JSON file. Setting the`name`parameter will include any lookup data and will map it to the relevant Oracle Access Governance attribute. Additionally, if you include a lookup table, the values will be displayed in a list-of-values when creating a new access bundle.
```

```

Additionally, you should create a field in your main ACCOUNT table which holds the value from your lookup. In this example you might have an attribute something like`account.homeCountry`which holds this value. This attribute should have a foreign key relationship with your ACCOUNT table. An example might be:
```

```

### Mapping to Core and Custom Attributes
You can determine if a parameter is mapped to a core attribute or a custom attribute. If you use the core attribute name in the`name`then the corresponding`targetName`value is mapped to the core attribute. If`name`is not the name of a core attribute, then the`targetName`value is mapped to a custom attribute. For example the following would map the database column`FIRSTNAME`to the core attribute`firstName`.
```

```
while the following would map`FIRSTNAME`to a custom attribute called`foreName`
```

```
