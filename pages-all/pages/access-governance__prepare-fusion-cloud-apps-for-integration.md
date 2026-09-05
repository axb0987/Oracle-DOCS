# Prepare Oracle Fusion Cloud Applications for Integration
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm
- Fetched: 2026-09-05 03:16 CDT

# Prepare Oracle Fusion Cloud Applications for Integration

Before you install and configure an Oracle Fusion Cloud Applications orchestrated system, complete the following prerequisites and tasks.

## Certification

You must certify the Oracle Fusion Cloud Applications system to access Oracle Access Governance. See[Certified Components](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm)for information about supported versions.

## Enable HCM Atom Feeds for Partial Data Load

To enable incremental data load change for your orchestrated system, enable`User Requests HCM Atom Feed`in Oracle Fusion Cloud Applications. This option is valid only when the orchestrated system is configured as HCM or Both.

- Enable User Requests HCM Atom Feed . See[Manage HCM Atom Feeds](https://docs.oracle.com/en/cloud/saas/field-service/fagsf/t-manage-hcm-atom-feeds.html). The following atom feed collections are used by Oracle Access Governance
- `newhire`
- `empupdate`
- `empassignment`
- `termination`
- `cancelworkrelship`
- `workrelshipupdate`
For more information, see[Employee Feeds](https://docs.oracle.com/en/cloud/saas/human-resources/24d/farws/Employee_Atom_Feeds.html).
- Configure Partial Data Load settings from the Oracle Access Governance Console. See[Configure Partial Data Load Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-partial-data-load-settings).

Note  
  
When email-related changes occur, the incremental/partial data load can only ingest work email creation, update, and deletion events. Other changes, such as Primary Email updates or From Date modifications aren't ingested incrementally. Perform a full data load instead. See[Employee Atom Feed](https://docs.oracle.com/en/cloud/saas/human-resources/farws/Employee_Atom_Feeds.html).

## Create FA HCM Data Roles and Security Profiles

Before configuring the orchestrated system you must set up either an HCM or ERP service account and grant permissions required to integrate with Oracle Access Governance.

To view a list of Default Roles or permissions, see[Grant Default Roles or Permissions](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-grantfaroles).
Required Roles:
- IT Security Manager Job role (`ORA_FND_IT_SECURITY_MANAGER_JOB`)
- Human Capital Management Integration Specialist (`ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_INTEGRATION_SPECIALIST_JOB)`
- Sign in to Oracle Fusion Cloud Applications.
- Go to My Enterprise &gt; Setup and Maintenance .
- Select the Tasks icon on the right side of the page.
- Select Search and select Manage Data Role and Security Profiles .
- Search for`Human Capital Management Integration Specialist`job role that doesn't have a security profile.
- Select +Create :
- Enter a data role name. For example,`<ServiceAccountName>-DataRole`.
- Select`Human Capital Management Integration Specialist`job role to inherit.
- Select OK .
- Select Next .
- On the Security Context page, select View All in the list across security profile configurations.
- Select Next to review and Submit .
- Search for the data role that you created. Verify that the Security Profile Assigned column is selected.
- Select Done .

You must create a service account and assign this data role to the service account.

## Create a Service Account and Grant Default Roles

Use the service account when you configure the connection in the orchestrated system. You can configure this service account by using default Oracle Fusion Cloud Applications roles and permissions, or using a custom role.

### Create a Service Account in Oracle Fusion Cloud Applications

You must have the IT Security Manager Job role (`ORA_FND_IT_SECURITY_MANAGER_JOB`).

- Sign in to Oracle Fusion Cloud Applications.
- From the Navigator , go to Tools &gt; Security Console .
- Select Users &gt; Add User Account .
- Enter the required user information.
- Select Save and Close . Ensure the status is Active .
- Select the user, and then select Edit .

### Add Roles to Service Account
- Select the Add Role button.
- For HCM, assign the default roles one at a time to the account. See[Grant Default Roles or Permissions](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-grantfaroles).
- For ERP, assign the default roles one at a time to the account. See[Grant Default Roles or Permissions](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-grantfaroles).
Note  
  
If you configure both HCM and ERP, you must assign all default roles for both application types.
Note  
  
You must add the required Look up Types for the Access Request Security Administrator. See[Add Lookup Types](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-serviceuser).
- Assign the data role that you created in the previous task. See[Create FA HCM Data Roles and Security Profiles](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-managedataroles).
- Select Save and Close .
- Search for the account and verify that the required roles are assigned.
- Sign in to verify the creation of the new service account.

### Grant Permissions Using a Custom Role - Least Privilege Principle

Use privileges instead of the default Oracle Fusion Cloud Applications roles and permissions to set up a custom role for the service user. This configuration follows the principle of least privilege because it grants only the fine-grained privileges required by the service user. Create the custom role as follows:
- Create an Oracle Fusion Cloud Applications role of category Common - Job Roles .
- Add the privileges to the function security policies. See the list:[Grant Privileges](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-grantfaprivilges-customuser).
- Add the aggregated privileges as roles in the role hierarchy. See the list:[Grant Privileges](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-grantfaprivilges-customuser)[Grant Aggregated Privileges](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-grantfaprivilges-customuser).
- Grant Data Security Policies for the appropriate dataset to the custom role. If you don't grant the correct data security policies, some data might not be returned. The API calls return a 200 OK response, but the count is 0 when the data security policies are omitted.
- Assign the custom role to the Service Account. See[Add Role to Service Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-serviceuser).

## Run Refresh Access Control Data Job

You must run the Access Control Data Job after configuring the service account. By default, this job runs every hour, or you can run it manually.

To run the job:
- Navigate to Tools → Scheduled Processes .
- Search for Refresh Access Control Data .
- Select Schedule New Process .
- Select Refresh Access Control Data as the job name and enter a meaningful description.
- Select Full Refresh or Incremental Refresh , as required to run the job.
- Select OK .
- Select Submit . Copy the process ID number.
- Run User and Roles Synchronization Process to retrieve the latest users and role definitions. For more information, see[Run User and Roles Synchronization Process](https://docs.oracle.com/en/cloud/saas/field-service/fagsf/t-run-user-and-roles-synchronization-process.html).

## Add Lookup Types for Access Request Security Administrator

Grant the following lookup type permission to the Access Request Security Administrator role type.

- Sign in to Oracle Fusion Cloud Applications.
- Go to My Enterprise &gt; Setup and Maintenance .
- Select Tasks icon on the right side of the page.
- Select Search and select Manage Standard Lookups .
- Add the new lookup type`FUN_DS_OPTIN_OPTIONS`by using the lookup code`FUN_DS_GET_BOOKCODE`.
- In the Module list, select Application Core .
- In the REST Access Secured list, select Authenticated .
- Select Save and Close .

## Configure Business Unit for Procurement Agent (PO Agent) in Oracle Fusion Cloud Applications

Before creating or managing a Procurement Agent (PO Agent), the selected Business Unit must be configured as a Procurement Business Unit in Oracle Fusion Cloud Applications.

Verify the business unit configuration:
- Sign in to the Oracle Fusion Cloud Applications application.
- Go to My Enterprise → Setup and Maintenance .
- Under Functional Areas , select Organization Structures .
- Open the task Assign Business Unit Business Function .
- Select the relevant business unit.
- Select the Procurement checkbox under Business Unit Functions .
- Save the changes.
- After you save the changes, run a Full Data Load from the Orchestrated System page to refresh Business Unit data in Oracle Access Governance.

Result : Access Bundle displays all available business units. When managing select Business Units configured with the Procurement business unit function when managing Procurement Agents. Selecting a business unit that isn't configured for procurement causes an Add Permission operation failed error.

## AOR Template-Based Provisioning

To enable provisioning of Area of Responsibility (AOR) assignments using AOR templates, the user account must be linked to a person.
Required Roles and Privileges
- Human Capital Management Application Administrator

`(ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_APPLICATION_ADMINISTRATOR_JOB)`
- Areas of Responsibility (AOR) using REST services`PER_REST_SERVICE_ACCESS_AREAS_OF_RESPONSIBILITY_PRIV`

### Create AoR Template in Oracle Fusion HCM
You can create an Area of Responsibility (AOR) template for responsibilities that need to be assigned often.
- Sign in to Oracle Fusion Cloud Applications.
- Go to My Client Groups .
- Search Area of Responsibility Templates .
- In the Area of Responsibility Templates page, select + Add .
- In the What info do you want to manage? field, select Assign to People .
- Select Continue .
- Enter basic information to create a template.
- Select Continue .
- Attach scope attributes such as Legal Employer, Business Unit, and Department.
- Select Submit .

This template is ingested as a permission in Oracle Access Governance during the data load and lookup activity. See[AOR Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-oracle-fusion-cl.htm#oracle-fusion-integrationsettings__aor-integration).

## Configure OCI OAuth and OCI Vault for Fusion Cloud Integration

Use OAuth to authenticate and authorize Oracle Fusion Cloud Applications with Oracle Access Governance.

### OAuth Prerequisites
The following prerequisites must be met to authorize Oracle Fusion Cloud Applications using OAuth.
- Create a[Service Account and grant permissions](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-serviceuser)required to integrate with Oracle Access Governance.
- Ensure configuration is performed in the same Identity domain that hosts Oracle Fusion Cloud Applications.

### Access Certificates and Keys

Use a certificate issued by a trusted Certificate Authority (CA) in the PEM format for secure authentication and compatibility, or use OCI Certificate Service to generate and manage certificates.
- Use a trusted certificate authority in the PEM format.
- To retrieve the public certificate, ensure that the Identity Domain is configured to issue and sign tokens.
- In the Identity &amp; Security , select Domains .
- From the Settings tab, enable Access signing certificate .

### Import Certificate as the Trusted Partner Certificate to the FA instance's OCI IAM Domain
- Navigate to Identity &amp; Security , and select Domains .
- Find and select compartment for the Oracle Fusion Cloud Applications services instance, and then select the domain.
- Select the Security tab.
- Go to the Trusted partner certificates section and then select Import certificate .
- Enter the alias name that you used when you generated the keystore certificate.
- Import the`.cer`file.
- Select Import .

Result : Verify that the correct details are displayed, including the SHA-1 Thumbprint, SHA-256 Thumbprint, Certificate Start Date, and Certificate End Date.

### Create an Integrated Confidential Type Application
- Navigate to Identity &amp; Security , and select Domains .
- Select the required domain.
- Select the Integrated applications tab.
- Select Add application .
- Select Confidential Application tile, and then select Launch workflow .
- In the Details page, enter the following:
- Enter a name and description for the confidential application.
- Select Submit .

### Edit OAuth configurations
- Select the OAuth configuration tab.
- Select Edit OAuth configuration .
- Client Configuration : Select Configure this application as a client now .
- Enable Grant Types : Select Client Credentials , JWT assertion and Refresh token grant types.
- Select Trusted as the Client type option.
- Import the certificate used earlier.
- Select On behalf of as the Allowed operations .
- Select network perimeter to restrict sign-in attempts to specific IPs or ranges. Otherwise, select Anywhere .
- Under the Token Issuance Policy , select All .
- Scope Configuration:
- Enable Add Resources toggle
- Select Add Scopes
- Select the Oracle Fusion Cloud Applications application references.
Note  
  
If scopes aren't listed, verify from the Oracle Cloud Services tab, if Oracle Fusion Cloud Applications instance is registered in this domain.
- Select Submit .
- Activate the application: select the Actions icon and then select Activate . The status must change from Inactive to Active .

### Fetch Confidential OAuth Application Details for Authorization
- Open the Confidential OAuth integrated application that you created.
- Select the OAuth configuration tab.
- Under the General Information section, copy and save Client ID and Client Secret .
- Under the Resources section, copy and save the application scope.

## Create an OCI Vault to Store Credentials

Oracle Access Governance uses OCI Vault and Secret Management service to store sensitive values such as passwords, client secrets, and private keys.

Create an Oracle Cloud Infrastructure (OCI) vault, an encryption key, and secrets for Basic Authentication or OAuth credentials where the Oracle Access Governance instance is configured.
Ensure you have the required access:
- Permission to create vaults, keys, and secrets in the target compartment.
- Permission to use keys to encrypt secrets.

- [Create a vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm).
- Create an encryption key when the vault is in active state. See[Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm).
- From the navigation menu , select Identity &amp; Security , then Secret Management .
- Select Create secret .
- Select the compartment in which to create the secret.
- Enter a meaningful secret name. For example,`agcs-fa-oauth`.
- Select the Vault compartment and Vault name.
- Select the Encryption key compartment.
- In the Encryption key field, select the key that you created.
- Select Manual secret generation .
- In the secret contents:

- If you use Basic Auth, enter:
```

```

- For OAuth, perform the[OAuth prerequisites,](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-oauth-prereqs)and enter the details:
```

```

Parameters Details
- adminUser : Service account username used for integration. See[Service Account and grant permissions](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-serviceuser)
- domainURL : Copy only the domain URL.`https://idcs-<tenant>.example.com`. See[Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm).
- Client Id and Client Secret : Retrieve the details from the OAuth application. See[Fetch Confidential OAuth Application Details for Authorization](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-oauth-prereqs__fetch-Oauth-details).
- privateKey : Private key corresponding to the certificate used in Trusted Partner Certificate setup.
- alias : Same alias used during certificate import .
- scope : See[Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm). As displayed in the OAuth application. For example,
```

```

- Select Create secret .
- Enter the tenancy OCID and secret OCID in the[Integration settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-oracle-fusion-cl.htm#oracle-fusion-integrationsettings). This generates the required IAM policy on the Console. To find secret details, see[Viewing Secret Details](https://docs.oracle.com/iaas/Content/secret-management/Tasks/view-secret-details.htm).
-
