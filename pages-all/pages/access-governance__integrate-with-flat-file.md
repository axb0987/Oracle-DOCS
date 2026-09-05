# Integrate with Flat File
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Flat File

Establish a connection between Flat File and Oracle Access Governance as an authoritative source and as a managed system. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

## Prerequisites

Before you install and configure a Flat File orchestrated system, you must consider the following prerequisites and tasks.

### Certified Components

The system must be the following:

- CSV Flat file created in Oracle Cloud Infrastructure (OCI) Object Storage in the tenancy

### Supported Modes
Flat File orchestrated system supports the following modes:
- Authoritative Source
- Managed System

### Supported Operations
The Flat File orchestrated system supports the following operations:
- Create Account
- Delete Account
- Add Entitlement
- Remove Entitlement

### Create a bucket in the OCI Object Storage service for Flat File Orchestrated System Operations

To load a flat file into Oracle Access Governance you need to place the data files in a bucket created using the OCI Object Storage service. This bucket can be created in any compartment of the OCI tenancy. For details regarding OCI Object Storage, see[Managing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm).

To integrate Oracle Access Governance with Flat File, following the instructions specified in[Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-configure__flat-file-integration-details)and copy the exact policies in the root compartment of the tenancy as displayed on the Console. See[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm)for details on how to apply the policies.

## Configure

Configure a connection with Flat File by entering connection details.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard.
- Select Flat File .
- Select Next .

### Enter details
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- Decide if this orchestrated system is an authoritative source, and if Oracle Access Governance can manage permissions by setting the following check boxes.
- This is the authoritative source for my identities

Select one of the following:
- Source of identities and their attributes : System acts as a source identities and associated attributes. New identities are created through this option.
- Source of identity attributes only : System ingests additional identity attributes details and apply to existing identities. This option doesn't ingest or creates new identity records.
- I want to manage permissions for this system The default value in each case is Unselected .
- Select Next .

### Add Owners
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account settings
On the Account settings step of the workflow, enter how you want Oracle Access Governance to manage accounts when the system is configured as a managed system:
- When a permission is requested and the account doesn't already exist, select this option to create new accounts . This option is selected by default. When selected, Oracle Access Governance creates an account if one doesn't exist when a permission is requested. If you clear this option, permissions are provisioned only for existing accounts in the orchestrated system. If no account exists, the provisioning operation fails.
- Select the recipients for notification emails when an account is created. The default recipient is User . If no recipients are selected, notifications aren't sent when accounts are created.
- User
- User manager
- Configure Existing Accounts
Note  
  
You can only set these configurations if allowed by the system administrator. When global account termination settings are enabled, application administrators can't manage account termination settings at the orchestrated-system level.
- Select what to do with accounts when early termination begins : Choose the action to perform when an early termination begins. This happens when you need to revoke identity accesses before official termination date.
- Delete : Deletes all accounts and permissions managed by Oracle Access Governance.
Note  
  
If specific orchestrated system doesn't support the action, no action is taken.
- Disable : Disables all accounts and disables permissions managed by Oracle Access Governance.
- Delete the permissions for disabled accounts : To ensure zero residual access, select this to delete directly assigned permissions and policy-granted permissions during account disablement.
- No action : No action is taken when an identity is flagged for early termination by Oracle Access Governance.
- Select what to do with accounts on the termination date : Select the action to perform during official termination. This happens when you need to revoke identity accesses on the official termination date.
- Delete : Deletes all accounts and permissions managed by Oracle Access Governance.
Note  
  
If specific orchestrated system doesn't support Delete action, then no action is taken.
- Disable : Disables all accounts and disables permissions managed by Oracle Access Governance.
- Delete the permissions for disabled accounts : To ensure zero residual access, select this to delete directly assigned permissions and policy-granted permissions during account disablement.
Note  
  
If specific orchestrated system doesn't support the Disable action, then account is deleted.
- No action : No action is taken on accounts and permissions by Oracle Access Governance.
- When an identity leaves your enterprise you must remove access to their accounts.
Note  
  
You can only set these configurations if allowed by your system administrator. When global account termination settings are enabled, application administrators cannot manage account termination settings at the orchestrated-system level.

Select one of the following actions for the account:
- Delete : Delete all accounts and permissions managed by Oracle Access Governance.
- Disable : Disable all accounts and mark permissions as inactive.
- Delete the permissions for disabled accounts : Delete directly assigned and policy-granted permissions during account disablement to ensure zero residual access.
- No action : Take no action when an identity leaves the organization.
Note  
  
These actions are available only if supported by the orchestrated system type. For example, if Delete is not supported, you will only see the Disable and No action options.
- When all permissions for an account are removed, for example when an identity moves between departments, you may need to decide what to do with the account. Select one of the following actions, if supported by the orchestrated system type:
- Delete
- Disable
- No action
- Manage accounts that aren't created by Access Governance : Select to manage accounts that are created directly in the orchestrated system. With this, you can reconcile existing accounts and manage them from Oracle Access Governance.
- Do not allow users to do password resets : Select to prevent users from resetting the passwords for the orchestrated system. If the orchestrated system doesn't support password change operation, password resets are unavailable, and a message is displayed.
Note  
  
If you don't configure the system as a managed system then this step in the workflow will display but is not enabled. In this case you proceed directly to the Integration settings step of the workflow.
Note  
  
If your orchestrated system requires dynamic schema discovery, as with the Generic REST and Database Application Tables integrations, then only the notification email destination can be set (User, Usermanager) when creating the orchestrated system. You cannot set the disable/delete rules for movers and leavers. To do this you need to create the orchestrated system, and then update the account settings as described in[Configure Orchestrated System Account Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-account-settings).

### Integration settings

On the Integration settings step of the workflow, enter the configuration details required to connect to the Flat File.

Field Description
What is the OCI tenancy of the object storage bucket? Add the tenancy OCID for the Object Storage bucket containing the flat files you want to integrate.
What is the OCI tenancy's home region code? Enter the home region code of the tenancy. . For example,`us-ashburn-1`. Details of region codes can be found in[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)OCI documentation.
What is the namespace for the bucket? Enter the bucket namespace of the tenancy
Enter the name of the bucket where the flat file is stored in OCI Object Storage Enter the name of the bucket where the flat file is stored in OCI Object Storage
Encoding Encoding info. Default is`UTF-8`
Field Delimiter Enter the field delimiter character used in the Flat File. Default is`,`.
Sub Field Delimiter Enter the sub field delimiter character. Default is`#`.
MultiValue Delimiter Enter the multivalue delimiter character used in the Flat File. Default is`;`.
Text Qualifier Enter the character used in the Flat File to act as a text qualifier. Default is`"`.
Date Format Enter the Java data format in which date type fields are included in the Flat File, for example`dd/MM/yyyy`. If no date format is specified, the date field would be assumed to be of data type Long .
- Copy the exact policies in the root compartment as displayed on the Console. See[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm)for details on how to apply the policies.
Note  
  
The required policies vary depending on where the Object Storage and the Oracle Access Governance instance are hosted (for example, in the same tenancy compared to different tenancies).
- After you have applied policies, select Test integration to check the connection. If you have any errors or messages, review the configuration.
- Select Add to create the orchestrated system.

### Finish up

Finally, if you have enabled Virtual Systems, you first need to define and upload the subsystems CSV file and then activate the orchestrated system. Select I'm done .

If virtual systems are disabled, then you can either activate the orchestrated system or save it as draft only.

### Upload the CSV File

If you have enabled virtual systems, then upload a CSV file with ID and Name for the systems. You could add up to 100 virtual systems.

For example:

ID Name
virtual_ad_123 Alpha
virtual_ad_456 Beta
virtual_ad_789 Gamma
- Virtual system name must not contain the following special characters``~!@#$%^&*><"`.
- Special characters aren't allowed for ID or Name.
- Virtual Systems name must be unique across all orchestrated systems.
- IDs must be unique for that orchestrated system.

Select the Update button to add a latest version of the virtual systems.

Existing virtual systems cannot be deleted but can be updated. To manage virtual systems after the creation, see[Manage Virtual Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-virtual-systems).

## Migrate API Key Access to Resource Principal Access

If you have an existing orchestrated systems that use the API Key access method to connect, then you must migrate at the earliest convenience to Resource Principal access method.

To migrate API Key access to Resource Principal access:
- Navigate to the Integration settings page following the instructions specified in[Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-configure__flat-file-integration-details).
- On the Integration settings page, you would see a deprecation warning. Select the Learn more about migrating button.
- Copy the exact policies in the root compartment as displayed on the Console. See[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm)for details on how to apply the policies.
Note  
  

The required policies vary depending on where the Object Storage and the Oracle Access Governance instance are hosted (for example, in the same tenancy compared to different tenancies).
- After you have applied policies, select Test integration to check the connection. If you have any errors or messages, review the configuration. You can't complete the migration until the test is successful.
- If the connection is confirmed then select the Migrate button to start the migration.
- When the migration completes, a confirmation message is displayed.

## Post Configuration

### Check Bucket Folder Structure

After creation of the orchestrated system, the following folder structure should be created in the defined bucket.

```

```

Note  
  
Sub folders such as,`virtual-sys-1`,`virtual-sys-2`, and so on are created only when virtual systems are enabled.
These folders fulfill the following purposes:
- `failed`: Files with any kind of data issue will be moved to this folder under the respective entity folder, in the event of a data load operation failure.
- `inbox`: Contains`IDENTITY`,`PERMISSION`and`TARGETACCOUNT`folders, each of which contains virtual systems folders, referenced by ID. Place the CSV files within the virtual systems folder to include in the data load operation. If you have not selected virtual systems during your configuration, then directly place your data files under the`IDENTITY`,`PERMISSION`and`TARGETACCOUNT`folders.
- `outbox`: Provisioning events for each entity of the orchestrated system.
- `sample`: Contains example CSVs with the expected header. These can be used as a reference for generating data and putting in the inbox for data load. These files should not be altered.
- `schema`: Contains the JSON representation of each entity's schema. This can be referred to for understanding details like:
- `dataType`
- Mandatory attributes
- Whether an attribute is multivalued or not
- If the attribute is complex and has nested attributes (dataType will be CUSTOM)
- Supported`dataTypes`are:
- TEXT
- NUMBER
- DECIMAL_NUMBER
- DATE
- FLAG
- CUSTOM

### Define Custom Attributes

Custom attributes are supported for the`IDENTITY`entity. If you want to include custom attributes in your dataload then you need to add them in the`<ServiceInstanceName>/<OrchestratedSystemName>/schema/IDENTITY.json`file.
Custom attribute names should meet the following requirements:
- start with a character: A-Z or a-z
- contain only characters or numbers: A-Z or a-z or 0-9
- For the DATE type attribute, only long value is supported
- Custom attributes can only be added, they cannot be deleted
- A custom attribute of CUSTOM type cannot be added

After you have added any custom attributes in the`IDENTITY.json`file, you would need to include them in Oracle Access Governance as described in[Fetch Latest Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#fetch-attributes). After this is completed, the sample CSV would be updated with the newly added custom attribute(s). Update the data files in the`inbox`to include the custom attribute(s) in the next data load.

### Run Dataload

Data load is on demand. Always run the data load after you have defined custom attributes or added the relevant CSV data files into the`inbox`folder. Each time you run a data load it is a full data load, there is no incremental load.`UTF-8-BOM`encoding is not supported.

If there is any kind of failure (single record or complete file failure), the data load operation will be marked as failed. The files that have been processed successfully will stay in the`inbox`while the failed files will be moved to the`failed`folder. Fix the data issue and place the files again in the`inbox`folder.

Data integrity issues, such as a permission being assigned to an account that is missing in the CSV, can also cause the data load operation to fail. However, in such cases the CSV files is not moved to the`failed`folder. Files are moved to the`failed`folder only when there are issues reading the data itself, such as missing mandatory data.

## Schema Extension - Adding Custom Account Attributes

You can configure account attributes for your Flat File orchestrated system in addition to the default account attributes supported out-of-the box. Details of account attributes and how they are managed can be found in[Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#account-attributes)and[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes).

### Schema Extension - Simple Attribute Example

To demonstrate how to add a simple account attribute let's look at the example of adding a phone number attribute to your Flat File schema.
Assume that you have a Day 0 configuration of your Flat File orchestrated system which has the following attributes by default:
- commonName
- displayName
- email
- firstName
- lastName
- middleName
- __NAME__
- permissions
- __ENABLE__
- title
- __UID__
A sample TARGETACCOUNT.csv would be:
```

```

A sample TARGETACCOUNT.json would be:
```

```

To add a custom account attribute, phoneNumber , complete the steps detailed in[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes), for example:
- Create a system provided attribute, phoneNumber , and select the options include in inbound and outbound data, and support multiple values.
- Add the new attribute to the TARGETACCOUNT.csv and TARGETACCOUNT.json .
```

```

```

```

- Trigger a full data load from Oracle Access Governance Console. The new custom attribute should be loaded and is visible in the Enterprise Wide Browser.

### Schema Extension - Complex Attribute Example

To demonstrate how to add a complex account attribute let's look at the example of adding an other contact details attribute to your Flat File schema.
Assume that you have a Day 0 configuration of your Flat File orchestrated system which has the following attributes by default:
- commonName
- displayName
- email
- firstName
- lastName
- middleName
- __NAME__
- permissions
- __ENABLE__
- title
- __UID__
A sample TARGETACCOUNT.csv would be:
```

```

A sample TARGETACCOUNT.json would be:
```

```

To add a custom account attribute, otherContactDetails with , complete the steps detailed in[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes), for example:
- Create a system provided attribute, otherContactDetails , with the following child attributes:
- contactDetailsId
- faxNumber
- website and select the options include in inbound and outbound data, and support multiple values.
- Add the new attribute to the TARGETACCOUNT.csv and TARGETACCOUNT.json .
```

```

```

```

- Trigger a full data load from Oracle Access Governance Console. The new custom attribute should be loaded and is visible in the Enterprise Wide Browser.

## Affiliations Support with Identity Schema Extension - Adding Custom Complex Identity Attributes

You can configure identity attributes for your Flat File orchestrated system in addition to the default identity attributes. To know more about Affiliations, see[Handling Identity Personas with Affiliations](https://docs.oracle.com/en-us/iaas/Content/access-governance/multi-affiliations.htm).

On Day 0, for`IDENTITY.csv`, all entities configured from the object storage include the simple attributes. For Day N, you can extend the existing schema and add additional simple attribute.

### Schema Extension - Complex Attribute Example

Include custom attribute, which is an object type attribute containing one or more sub-attributes, you need additional modification to the Identity schema. To demonstrate how to add a complex identity attribute let's look at the example of adding an address attribute to your Flat File schema.

Assume that you have a`Day 0`configuration of your Flat File orchestrated system which has the following attributes by default:
A sample IDENTITY.csv would be:
```

```

In the Schema folder, the sample`IDENTITY.json`contains the following:
```

```

To add custom complex attribute:

- Extend the schema in the IDENTITY.json file.
```

```

- After making the above changes in IDENTITY.json ,
- Run the Schema Discovery Operation. See[Fetch Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#fetch-attributes).
- From the Identity Attributes page, edit the attribute to update the Include in identity details flag. See[Manage Global Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings). The new identity schema is displayed.
- Confirm the IDENTITY.csv CSV headers
```

```

Simple attributes appear as comma‑separated columns in the CSV header. Custom complex attributes use a flat structure: each sub‑attribute is included in the header with its parent attribute, separated by dot (.) notation.

#### Single Value Entry for Complex Custom Attribute
Data input for complex attribute needs to be done in the following way in a CSV.
```

```

- Be sure to include the correct column headers.
- For empty fields (such as`addressTwo`), include a blank value between commas.
Resulting User Data
```

```

#### Multi Valued Entry for Complex Custom Attribute
When dealing with multi-valued entries, use a semicolon (;) to separate multiple values for each sub-attribute. The following CSV shows the correct representation for the multivalued address. Each row in the CSV represents one user with potentially multiple address entries
```

```

- For missing data, leave the value between delimiters blank, for the first address,`addressTwo`is empty)
- Each attribute’s values correspond by position: the first value for each attribute forms the first address, the second value forms the second address, and so on.
Resulting User Data
```

```
