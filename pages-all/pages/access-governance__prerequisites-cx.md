# Prerequisites for Oracle CX (Sales) Integration
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/prerequisites-cx.htm
- Fetched: 2026-09-05 03:16 CDT

# Prerequisites for Oracle CX (Sales) Integration

Before integrating and configuring an orchestrated system, complete the following prerequisites..

## Step 1: Create Data Roles and Security Profiles

Before configuring the orchestrated system, create a service account and grant the permissions required to integrate with Oracle Access Governance.
Required Roles:
- IT Security Manager Job role (`ORA_FND_IT_SECURITY_MANAGER_JOB`)
- Human Capital Management Integration Specialist (`ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_INTEGRATION_SPECIALIST_JOB)`
- Sign in to Oracle Fusion Cloud Applications.
- Go to My Enterprise &gt; Setup and Maintenance .
- Select Tasks icon at the right-side of the page.
- Select Search and select Manage Data Role and Security Profiles .
- Search for`Human Capital Management Integration Specialist`job role that doesn't have any security profiles.
- Select +Create
- Enter data role name. For example,`<ServiceAccountName>-DataRole`.
- Select`Human Capital Management Integration Specialist`job to inherit.
- Select OK .
- Select Next .
- On the Security Context page, select View All in the list across security profile configurations.
- Select Next to review and Submit .
- Search for the data role that you created. Notice that now the Security Profile Assigned column is now selected.
- Select Done .

Next, create a service account and assign this data role to the service account.

## Step 2. Create a Service Account and Grant Default Roles

Use the service account when configuring the connection in the orchestrated system. You can set this service account using default Oracle Fusion Cloud Applications roles and permissions, or using a custom role.

### Step 2.1 Create a Service Account in Oracle Fusion Cloud Applications

You must have the IT Security Manager Job role (`ORA_FND_IT_SECURITY_MANAGER_JOB`).

- Sign in to Oracle Fusion Cloud Applications.
- From the Navigator , go to Tools &gt; Security Console .
- Select Users &gt; Add User Account .
- Enter the required fields for User information.
- Select Save and Close . Ensure the status is Active .
- Select the user and select Edit .

### Step 2.2 Add Roles to Service Account
- Select the Add Role button.
- Assign the default roles one at a time to the account.
- Integration Specialist (`ORA_FND_INTEGRATION_SPECIALIST_JOB`)
- Application Implementation Consultant (`ORA_ASM_APPLICATION_IMPLEMENTATION_CONSULTANT_JOB`)
- Sales Administrator (`ORA_ZBS_SALES_ADMINISTRATOR_JOB`)
- Assign the Data Role created in Step 1. See[Step 1: Create Data Roles and Security Profiles](https://docs.oracle.com/en-us/iaas/Content/access-governance/prerequisites-cx.htm#oracle-cx-managedataroles).
- Select Save and Close .
- Search account and verify roles needed are assigned.
- Sign in to verify the creation of the new service account.

### Step 2.3 Grant Permissions Using a Custom Role - Least Privilege Principle

Use privileges instead of the default Oracle Fusion Cloud Applications roles and permissions to set up a custom role for the service account. This conforms to the principle of least privilege by only configuring the fine-grained privileges required by the service account. To create the custom role:
- Create an Oracle Fusion Cloud Applications role of category Common - Job Roles .
- Add the privileges into the function security policies train stop. Refer the list:[Grant Privileges](https://docs.oracle.com/en-us/iaas/Content/access-governance/prerequisites-cx.htm#oracle-cx-serviceuser__cx-priviliges).
- Grant Data Security Policies for the correct dataset to the custom role. If you don't grant the correct data security policies, some data might not be returned. The API calls would not fail (200 OK), but the count would be 0 if the data security policies are omitted.
- Assign the Data Role (`ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_INTEGRATION_SPECIALIST_JOB`) created in Step 1. See[Step 1: Create Data Roles and Security Profiles](https://docs.oracle.com/en-us/iaas/Content/access-governance/prerequisites-cx.htm#oracle-cx-managedataroles).

### Step 2.4 Grant Privileges to a Custom User

Create a custom role instead of using the default roles to ensure the least privilege by granting only the necessary fine-grained permissions. Assign the data role`ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_INTEGRATION_SPECIALIST_JOB`along with the privileges.

Note  
  
You must grant the required data security policies and associate them with the relevant roles to enable access to the appropriate dataset (for example,`/workers`). If the correct data security policies aren't configured, API calls would not fail (200 OK), but the response would contain no data (count would be 0). For further details, see[Data Security Policies](https://docs.oracle.com/en/cloud/saas/applications-common/24b/facsa/data-security.html#Data-Security-Policies).

EndPoint/Functionality Privileges In Function Security Policies
`/userAccounts`

Privilege Name: Use REST Service - User Accounts

Privilege Code:`PER_REST_SERVICE_ACCESS_USER_ACCOUNTS_PRIV`
`/workers`

Privilege Name: Use REST Service - Workers

Privilege Code:`PER_REST_SERVICE_ACCESS_WORKERS_PRIV`
`/userAccounts`LOVs

Use REST Service - Users and Roles LOVs`PER_REST_SERVICE_ACCESS_USERS_AND_ROLES_LOVS_PRIV`

### Step 2.5 Run Refresh Access Control Data Job
You must run the Access Control Data Job after configuring the service account. This job runs every hour, by default or you might select it to run manually. To run the job:
- Navigate to Tools → Scheduled Processes .
- Search Refresh Access Control Data .
- Select Schedule New Process .
- Select Refresh Access Control Data as job name and enter meaningful description.
- Select Full Refresh or Incremental Refresh , as required to run the job.
- Select OK .
- Select Submit . Copy the process ID number.
- Run User and Roles Synchronization Process to retrieve latest users and role definitions. For more information, see[Run User and Roles Synchronization Process](https://docs.oracle.com/en/cloud/saas/field-service/fagsf/t-run-user-and-roles-synchronization-process.html).

## Authenticate and Authorize with OCI IAM

Use OCI IAM to authenticate and authorize Oracle CX (Sales) with Oracle Access Governance.

### Prerequisites
The following prerequisites must be met to authorize Oracle CX (Sales) using OAuth.
- Create a[Service Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/prerequisites-cx.htm#oracle-cx-serviceuser)and grant permissions required to integrate with Oracle Access Governance.
- Ensure configuration is performed in the same Identity domain where Oracle Fusion Cloud Applications applications are hosted.

### Access Certificates and Keys

Use a certificate issued by a trusted Certificate Authority (CA) in the PEM format for secure authentication and compatibility, or leverage OCI Certificate Service to generate and manage certificates efficiently.
- Use a trusted certificate authority in the PEM format.
- To retrieve public certificate, ensure that the Identity Domain is configured to issue and sign tokens.
- In the Identity &amp; Security , select Domains .
- From the Settings tab, enable Access signing certificate .

### Import Certificate as the Trusted Partner Certificate to the FA instance's OCI IAM Domain
- Navigate to Identity &amp; Security , and select Domains .
- Find and select compartment for the Oracle Fusion Cloud Applications services instance, and then select the domain.
- Select the Security tab.
- Go to the Trusted partner certificates section and then select Import certificate .
- Enter the same alias name that you provided while generating the keystore file certificate alias
- Import the`.cer`file.
- Select Import .

Results : Ensure the correct details are shown along with the SHA-1 Thumbprint, SHA-256 Thumbprint, Certificate Start Date, and Certificate End Date.

### Create an Integrated Confidential Type Application
- Navigate to Identity &amp; Security , and select Domains .
- Select the required domain.
- Select the Integrated applications tab.
- Select Add application .
- Select Confidential Application tile, and then select Launch workflow .
- In the Details page, enter the following:
- Enter name and description for the confidential application.
- Select Submit .

### Edit OAuth configurations
- Select the OAuth configuration tab.
- Select Edit OAuth configuration .
- Client Configuration : Select Configure this application as a client now .
- Enable Grant Types : Select Client Credentials , JWT assertion and Refresh token grant types.
- Select Trusted as the Client type option.
- Import the certificate used earlier.
- Select On behalf of as the Allowed operations .
- Select network perimeter to restrict sign-in attempts to specific IPs or ranges, else select Anywhere .
- Under the Token Issuance Policy , select All .
- Scope Configuration
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

Perform this step only when you use OCI Vault during the Integration settings. Oracle Access Governance uses OCI Vault and Secret Management service to store sensitive values such as passwords, client secrets, and private keys.

Create an Oracle Cloud Infrastructure (OCI) vault, an encryption key, and secrets for Basic Authentication credentials where the Oracle Access Governance instance is configured.
This method is recommended for secure credential management. Ensure you have the required access:
- Permission to create vaults, keys, and secrets in the target compartment.
- Permission to use keys to encrypt secrets.

- Sign in to the Oracle Cloud Infrastructure Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security → Key Management &amp; Secret Management .
- [Create a vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm).
- Create an encryption key when the vault is in active state. See[Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm).
- From the navigation menu , select Identity &amp; Security , then Secret Management .
- Select Create secret .
- Select the compartment to create the secret.
- Enter meaningful secret name. For example,`agcs-cx-vault`.
- Select the vault compartment and vault name.
- Select the encryption key compartment.
- In the Encryption key field, select the key that you created.
- Select Manual secret generation .
- In the secret contents:

- If you need to use Basic Auth, enter:
```

```

- For OAuth, perform the[OAuth prerequisites](https://docs.oracle.com/en-us/iaas/Content/access-governance/prerequisites-cx.htm#cx-oauth-prereqs), and enter the details:
```

```

Parameters Details
- adminUser : Service account username used for integration. See[Step 2. Create a Service Account and Grant Default Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/prerequisites-cx.htm#oracle-cx-serviceuser)
- domainURL : Copy only the domain URL.`https://idcs-<tenant>.example.com`. See[Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm).
- Client Id and Client Secret : Retrieve the details from the OAuth application. See[Fetch Confidential OAuth Application Details for Authorization](https://docs.oracle.com/en-us/iaas/Content/access-governance/prerequisites-cx.htm#cx-oauth-prereqs__fetch-Oauth-details)
- privateKey : Private key corresponding to the certificate used in Trusted Partner Certificate setup.
- alias : Same alias used during certificate import
- scope : See[Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm). As displayed in the OAuth application. For example,
```

```

- Select Create secret .
- Enter the tenancy OCID and secret OCID in the . This generates the required IAM policy on the Console. To find secret details, see[Viewing Secret Details](https://docs.oracle.com/iaas/Content/secret-management/Tasks/view-secret-details.htm).
-
