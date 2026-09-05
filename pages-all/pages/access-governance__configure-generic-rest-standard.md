# Configure Integration with Generic REST (Standard UI-driven)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Integration with Generic REST (Standard UI-driven)

Establish a connection between target applications and Oracle Access Governance using REST APIs as a managed system. Use the Generic REST(Standard UI-driven) orchestrated system in the Oracle Access Governance Console.

## Before you Begin - Prerequisites

Before configuring Generic REST(Standard UI-driven), ensure that the required OCI resources, authentication credentials, flat file storage (optional), and target REST API details are available.

### Create a bucket in the OCI Object Storage service for Flat File Data Load

Perform this step only when you use flat files for full data loads during[Integration settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#oracle-grest-integrationsettings).

To load data using flat file into Oracle Access Governance you need to place the data files in a bucket created using the OCI Object Storage service. This bucket can be created in any compartment of the OCI tenancy. For details regarding OCI Object Storage, see[Managing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm).

Enter the bucket details specified in the[Use Flat File for Full Data Load](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#oracle-grest-integrationsettings__flat-file-data-load)and copy the exact policies in the root compartment of the tenancy as displayed on the Console. See[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm)for details on how to apply the policies.

### Create OCI Vault and Secret

Perform this step only when you use OCI Vault during the Integration settings. Use the OCI Vault service to store target credentials for authentication. Oracle Access Governance retrieves the credentials at runtime using the configured secret OCID.
This method is recommended for secure credential management. Alternatively, you can use the User entered option to store credentials directly in Oracle Access Governance. You must have:
- Permission to create vaults, keys, and secrets in the target compartment.
- Permission to use keys to encrypt secrets.
- Sign in to the Oracle Cloud Infrastructure Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security → Key Management &amp; Secret Management .
- [Create a vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm).
- Create an encryption key when the vault is in active state. See[Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm).
- From the navigation menu , select Identity &amp; Security , then Secret Management .
- Select Create secret .
- Select the compartment to create the secret.
- Enter meaningful secret name. For example,`agcs-grest`.
- Select the Vault compartment and Vault name.
- Select the Encryption key compartment.
- In the Encryption key field, select the key that you created.
- Select Manual secret generation .
- In the secret contents:
- Basic Authentication:
```

```

- For storing API key:
```

```
You can append`Bearer`if you application accepts a Bearer API key token.
- Select Create secret .
- Enter the OCI vault details in the Integration settings. This generates the required IAM policy on the Console. To find secret details, see[Viewing Secret Details](https://docs.oracle.com/iaas/Content/secret-management/Tasks/view-secret-details.htm).
- Copy the exact statements in the root compartment of the tenancy where you have created the vault.

## Configure

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of the orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select Generic REST (Standard UI-driven) .
- Select Next .

### Add details

Add details such as name, description. You can only manage permissions for Generic REST (Standard UI-driven) orchestrated system.
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- Select Next .

### Add Owners

Add primary and additional owners to your orchestrated system to allow them to manage resources.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account settings

Outline details of how to manage account settings when setting up the orchestrated system, such as managing existing accounts.
- Manage accounts that aren't created by Access Governance : Select to manage accounts that are created directly in the orchestrated system. With this, you can reconcile existing accounts and manage them from Oracle Access Governance.
- Select Next .

### Integration settings

Enter connection details in the Generic REST system.
- 

On the Integration settings step of the workflow, enter the details to connect to the Generic REST system.

Integration settings
Parameter Name Mandatory? Description
Authentication Type Yes Select the authentication method to authenticate to the target system. Select:
- Bearer : Bearer Token authentication uses an access token to authorize requests
- Basic : Uses username and password to authenticate REST API requests.
- API key : Uses API key to authenticate REST API requests. Append Bearer before entering the API key if the application accepts Bearer.
Access credentials source Yes Specify how credentials are provided.
- OCI Vault (recommended): Uses a secret stored in OCI Vault. See[Create OCI Vault and Secret](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#oci-vault).
- User entered : Enter credentials manually and stored in Oracle Access Governance
OCI tenancy OCID hosting the vault secret Enter the OCID of the tenancy that contains the vault secret. This field is required when OCI Vault is selected.
Secret OCID for access credentials Enter the OCID of the secret that stores the authentication credentials. This field is required when OCI Vault is selected.
Username Enter username to authenticate. This field is required when User entered is selected.
Password Enter password to authenticate. This field is required when User entered is selected.
API Key Enter API Key.
```

```
To resolve the value at runtime, use`<<CREDENTIALS>>`in the API settings. See[Create Account API Request Response](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference-standard.htm#rest-schema-outline).
Use flat files for full data loads Select to use flat file for the full data instead of configuring listing APIs. If not selected, you must configure REST APIs to ensure data load is performed using APIs. See[Use Flat File for Full Data Load](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#oracle-grest-integrationsettings__flat-file-data-load).

[Use Flat File for Full Data Load](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#)

Field Description
What is the OCI tenancy of the object storage bucket? Add the tenancy OCID for the Object Storage bucket containing the flat files you want to import.
What is the namespace for the bucket? Enter the bucket namespace of the tenancy
Bucket Name Enter the name of the bucket where the flat file is stored in OCI Object Storage
What is the OCI tenancy's home region code? Enter the home region code of the tenancy. For example,`us-ashburn-1`. See[The Home Region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#The), and[How do I find my tenancy home region?](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How).
Encoding Encoding info. Default is`UTF-8`
Field Delimiter Enter the field delimiter character used in the Flat File. Default is`,`.
Sub Field Delimiter Enter the sub field delimiter character. Default is`#`.
Multi Value Delimiter Enter the multivalue delimiter character used in the Flat File. Default is`;`.
Text Qualifier Enter the character used in the Flat File to act as a text qualifier. Default is`"`.
Date Format Enter the Java data format in which date type fields are included in the Flat File, for example`dd/MM/yyyy`. If no date format is specified, the date field would be assumed to be of data type Long .
Copy the exact policies in the root compartment as displayed on the Console. See[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm)for details on how to apply the policies.
Note  
  
The required policies vary depending on where the Object Storage and the Oracle Access Governance instance are hosted (for example, in the same tenancy compared to different tenancies).
- Select Test Integration to verify the connection.
- Select Add . The orchestrated system would be saved in the Draft mode.

#### Finish Up

Finish up configuration of the orchestrated system by providing details of whether to perform further customization, or activate and run a data load.

The final step of the workflow is Finish Up .

Select I'm done . The orchestrated system is saved in the Draft mode.

After the orchestrated system is created, Oracle Access Governance displays the Next steps section on the Console to perform remaining configuration tasks required before activation.

## Post Configuration

After creating the Generic REST orchestrated system, define permissions, lookups, account attributes, and configure REST APIs to complete the account lifecycle setup.

### Create Permissions for the Generic REST System

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the navigation menu . to view the configuration of a specific orchestrated system. This displays the configuration page for the selected orchestrated system.
- From the Data settings section of the page, select Manage on the Permissions tile.
- Enter name and display name.
- Select Create .
- Add attributes for permissions.

Note  
  
You can't delete a permission if it's referenced in account attributes or configured REST APIs for the orchestrated system.
Each permission includes uid and name attributes. You can define more attributes based on the permission structure.
- Based on the configuration, use one of the following for data load for permissions:
- REST API-based data load : Configure Search API using the REST API settings. To fetch permissions from the target system, use Request JSON:
```

```

Response JSON
```

```
See[Group Search API](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference-standard.htm#search-account-APi).
- Flat file-based data load : If you have configured flat file integration during setup, upload data using CSV file in the`inbox`folder. The CSV column names must match the permission schema attribute names.

After activation of the orchestrated system, you can download the schema from the`sample`folder of the bucket. Add the CSV data and place these in the`inbox`for data load. For details, see[Flat File Bucket Folder Structure](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-postconfig)For CSV example:
```

```

### Manage Lookups

Use lookups to define reference data used for account attribute mapping, such as countries or languages.
Based on the orchestrated system configuration, lookup data can be loaded using one of the following methods:
- 

Flat file-based data load : Lookup data is loaded only using flat files.
- REST API-based data load
If REST API-based integration is configured, you can load lookups data using:
- REST APIs for dynamic lookup synchronization
- Static file upload for lookup values

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the navigation menu . to view the configuration of a specific orchestrated system. This displays the configuration page for the selected orchestrated system.
- From the Data settings section of the page, select Manage on the Lookups tile.
- Select Create Lookup .
- Enter name and display name.
- Select Create .
- Based on the configuration, lookup data can be loaded using one of the following methods:
- REST APIs for dynamic lookup. See[Country Lookup API](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference-standard.htm#lookup-api).
- Flat file (CSV-based lookup values). After activation of the orchestrated system, you can download the schema from the`sample`folder of the bucket. Add the CSV data and place these in the`inbox`for data load. For details, see[Flat File Bucket Folder Structure](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-postconfig)
- For static file lookup, upload the sample CSV
Sample CSV for Static Lookup
```

```

Note  
  
You can't delete a lookup if it's referenced in account attributes or REST API configurations.
Use the lookups defined at the orchestrated-system level for account attributes.

### Define Account Attributes

Define account attributes to support outbound transformation or account provisioning operations. You can also use these account attributes to define the account profile required for provisioning.

You can define account attributes using one of the following methods:
- Manually create attributes using the Console. See[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes). Use the lookups defined at the orchestrated-system level to populate reference values for an account attribute.
- Import a schema by uploading a JSON file. When you use the Import schema option, the uploaded schema replaces any existing account attributes.

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the navigation menu . to view the configuration of a specific orchestrated system. This displays the configuration page for the selected orchestrated system.
- From the Account settings section of the page, select Manage on the Account attributes tile.
- Select Import schema .
- Upload a JSON file that defines the account structure. For example:

```

```

- Review the attributes and save.

### Configure Authentication - For Bearer Token

The following steps show how to configure a Bearer Token API in the Oracle Access Governance Console. A Bearer Token API is required only when Bearer Token authentication is selected. The exact steps might vary based on the REST API implementation.

Oracle Access Governance retrieves credentials from OCI Vault, generates an access token using the configured Bearer Token API, and uses that token to invoke account, permission, and lookup APIs at runtime.

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the navigation menu . to view the configuration of a specific orchestrated system. This displays the configuration page for the selected orchestrated system.
- From the Data settings section of the page, select Manage on the REST APIs tile.
- Select Bearer token API.
- Enter the details either in the JSON format or use the Console to enter the request and response details.
- Use Console, enter the details, such as:
- 
- Name : Get Token API
- Method : POST
- URL :`<token-endpoint>`
- Configure Headers
- Content-Type:`application/x-www-form-urlencoded`
- Authorization:`<<CREDENTIALS>>`. Credentials are resolved at runtime using OCI Vault or user-entered credentials.
- Select Request body type
- None : REST API doesn't require a request body
- JSON : Send the request body in JSON format.
- Form : Send the request body as form parameters.
- Configure body. For example:

```

```

```

```

- Configure response. For example:

```

```

- Select Save .

### Configure REST APIs for Entities

After defining permissions, account attributes, and lookups, configure REST APIs for these entities to support provisioning, reconciliation, and data load operations based on the selected configuration.
Use runtime expressions in the request and response. See[REST API Runtime Expressions](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#runtime-expressions)and[examples](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference-standard.htm#generic-rest-reference-standard).

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the navigation menu . to view the configuration of a specific orchestrated system. This displays the configuration page for the selected orchestrated system.
- From the Data settings section of the page, select Manage on the REST API tile.
- Select the required API category (for example, Bearer token or Test connection ).
- Select an API (for example, Get ) or select Create API .
- Enter the details either in the JSON format or use the Console.
- In the Console, enter the following details based on the API:
- Name : Enter a name for the API (for example, Get Token API )
- Method : Select the HTTP method (GET, POST, PUT, PATCH, DELETE)
- URL : Enter the endpoint URL
- Enter Headers, Parameters, Body, Response, Request, Subrequests.
- Enter response validation. See[Response Validation](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference-standard.htm#response-validation).
- Select Save .

## REST API Runtime Expressions

Use runtime expressions to dynamically retrieve values during REST API execution.

Syntax Desciption Example
`<<CREDENTIALS>>`Resolves authentication credentials configured in Integration Settings at runtime. Credentials can be retrieved from OCI Vault or User entered configuration. Used in REST API headers for authentication.
```

```

`<EL>...</EL>`Expression Language (EL) to retrieve attribute values at runtime. Used in request payloads, headers, parameters, or URLs when values must be populated dynamically from attributes.
```

```

Note  
  
The`name`attribute must be present in the account attribute schema.
`<JP>...</JP>`JSON Path (JP) expression to extract values from REST API responses. Used in response mappings to retrieve values returned by target REST APIs.
```

```

`UQ:`Value must be inserted into the payload without quotation marks. Used for literal values such as boolean and numbers
```

```

### Activate Orchestrated System

On the Manage orchestrated system page, select Activate .

Activate the orchestrated system after completing all tasks listed in the Next Steps section. If Flat File for Full Data Load is configured, access the Flat File folder structure under the configured Object Storage bucket and upload the input CSV files for Permissions, Lookups and Target Account after activation, as needed.

## Configure Outbound Transformations for Generic REST (Standard UI Driven)

Use outbound transformations to map Oracle Access Governance identity attributes to target system account attributes during provisioning operations.

Outbound transformations dynamically populate values used in REST API request payloads for operations such as Create Account or Update Account.

For configuring outbound transformation, see[Apply Outbound Transformations for Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-outbound-transformations-for-identity-attributes).
Examples
```

```

For all utility methods, see[Transformation Utilities for Outbound Data Transformation](https://docs.oracle.com/en-us/iaas/Content/access-governance/transformation-for-inbound-and-outbound-rules.htm#transformationutilitiesforoutbounddatatransformation)and[Examples for Outbound Data Transformation](https://docs.oracle.com/en-us/iaas/Content/access-governance/transformation-for-inbound-and-outbound-rules.htm#sample-mapping-rules-for-outbound-data-transformations).

## Migrate User Credentials to OCI Vault

You can migrate previously stored credentials in Oracle Access Governance to use an OCI Vault secret.
- Follow the process of creating the OCI Vault secret. See[Create OCI Vault and Secret](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#oci-vault).
- Select Test integration to validate integration.
-
