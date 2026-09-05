# Set Up Users
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm
- Fetched: 2026-09-05 03:16 CDT

# Set Up Users

You can set up user accounts for everyone you expect to use Oracle Access Governance before or after you create your Oracle Access Governance instance.

## About Setting Up Users and Groups

Set up user accounts for everyone you expect to use Oracle Access Governance.

The way you manage users for Oracle Access Governance (and Oracle Cloud Infrastructure) depends on whether identity domains are available in your cloud account.

- Oracle Cloud Infrastructure Identity and Access Management (IAM) Identity Domains : Some Oracle Cloud regions have been updated to use identity domains. If you have a new cloud account in one of these regions, you use identity domains to manage the users who perform tasks in both Oracle Access Governance and Oracle Cloud Infrastructure.
- Oracle Identity Cloud Service : If you have an existing cloud account or you deploy Oracle Access Governance in a region that does not currently offer identity domains, you use a federated Oracle Identity Cloud Service to manage the users who perform tasks in Oracle Access Governance. In addition, you use Oracle Cloud Infrastructure Identity and Access Management to manage the users who create and manage your Oracle Access Governance deployments using the Oracle Cloud Infrastructure Console.

It is easy to determine whether or not your cloud account offers identity domains. In Oracle Cloud Infrastructure Console, navigate to Identity &amp; Security . Under Identity , check for Domains .

- If you see Domains , you use identity domains to manage users and groups for Oracle Cloud Infrastructure and your Oracle Access Governance deployments. See[Use Identity Domains to Onboard Users and Groups for Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm#set-up-users-with-iam-domains).
- If Domains is not listed, you use a federated Oracle Identity Cloud Service to manage Oracle Access Governance users and IAM to manage Oracle Cloud Infrastructure users. See[Use Oracle Identity Cloud Service to Onboard Users and Groups for Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm#set-up-users-without-iam-domains).

The following table outlines the differences between the two configurations.

Cloud Accounts That Use Identity Domains Cloud Accounts That Don't Use Identity Domains
Users and groups are configured in IAM.

Users and groups are configured in both IAM and Oracle Identity Cloud Service, and are linked through federation.
Provides a single, unified console for managing users, groups, dynamic groups, and applications in domains . Oracle Cloud Infrastructure Identity and Access Management must be federated with Oracle Identity Cloud Service.
Provides Single Sign-On to more applications using a single set of credentials and a unified authentication process. Requires separate federated credentials for Oracle Identity Cloud Service.
The Federation page doesn't list any entries for Oracle Identity Cloud Service. The Federation page lists oracleidenitycloudservice , the primordial Oracle Identity Cloud Service automatically federated in your cloud account.

## Use Identity Domains to Onboard Users and Groups for Oracle Access Governance

If your Oracle Access Governance instance uses identity domains for identity management, you use Oracle Identity Governance provisioning, an external Identity Provider (IDP), or a self-registration profile to onboard user accounts for everyone you expect to use Oracle Access Governance. These users will be assigned to a group, which, when you have completed onboarding, you map to Oracle Access Governance application roles )

As an Oracle Cloud Infrastructure Cloud Administrator , you can use one of the following approaches to enable access for users to the Oracle Access Governance application.

Approach 1: Set Federated Authentication from an External Identity Provider (IDP)

- Setup federation with an external IDP:
- Set up a federated login between an Identity Domain and external IDP. Users can sign in and access Oracle Access Governance resources and features by using existing logins and passwords managed by the IDP.
- Refer to[Managing Identity Providers](https://docs.oracle.com/iaas/Content/Identity/identityproviders/manage-identity-providers.htm)in the Oracle Cloud Infrastructure documentation for further details.
- Enable SAML Just-In-Time provisioning.
- This process automates user account creation when a user first tries to sign in to Oracle Cloud Infrastructure where the user does not yet exist in the Identity Domain.
- Refer to[About SAML Just-In-Time Provisioning](https://docs.oracle.com/iaas/Content/Identity/identityproviders/manage-identity-providers.htm#understand-saml-just-time-provisioning)in the Oracle Cloud Infrastructure documentation for further details.

Approach 2: Configure Oracle Identity Governance Provisioning with Oracle Cloud Infrastructure Identity and Access Management Using the Oracle Identity Cloud Service Application

- Configure the Oracle Identity Cloud Service Application.
- Download the connector installation package and copy the contents to the OIG_HOME/server/ConnectorDefaultDirectory directory. Refer to[Downloading the Connector Installation Package](https://docs.oracle.com/en/middleware/idm/identity-governance-connectors/12.2.1.3/cgidc/deploying-oracle-identity-cloud-service-connector.html#GUID-99BD300F-87AA-44D6-9CAE-9D6CA0D19DAD)for further details.
- Log in to the Oracle Cloud Infrastructure Console and create an application with the type Confidential . Refer to[Creating an Application By Using the Connector](https://docs.oracle.com/en/middleware/idm/identity-governance-connectors/12.2.1.3/cgidc/deploying-oracle-identity-cloud-service-connector.html#GUID-172043FF-EF15-4808-B0E7-A5600848BE04)for further details.
- Copy the Client ID and Client Secret from the created Application. This will be used in customAuthHeaders in ITResource.
- Configure SSL to secure communication between Oracle Identity Governance and the target system, in this case, Oracle Access Governance. Refer to[Configuring SSL for the Connector](https://docs.oracle.com/en/middleware/idm/identity-governance-connectors/12.2.1.3/cgidc/performing-postconfiguration-tasks-idcs-connector.html#GUID-ADA498BB-B713-48BE-BCAB-5CC44761C540)for further details.
- Create Groups: Login to the Oracle Cloud Infrastructure Console and create groups for any Oracle Identity Governance groups you want to map to Oracle Access Governance roles.
- Create an IDCS application in Oracle Identity Governance. Refer to[Creating an Application By Using the Connector](https://docs.oracle.com/en/middleware/idm/identity-governance-connectors/12.2.1.3/cgidc/deploying-oracle-identity-cloud-service-connector.html#GUID-172043FF-EF15-4808-B0E7-A5600848BE04)for further details.
- Run the Group Lookup Recon Job.
- Provision the IDCS application for those users with a membership of Access Governance groups.

Approach 3: Self Registration Profiles

Create self-registration profiles to enable users to create their accounts in Oracle Cloud Infrastructure Identity and Access Management. Refer to[Creating Self-Registration Profiles](https://docs.oracle.com/iaas/Content/Identity/selfregistrationprofiles/overview.htm)for further details.

## Use Oracle Identity Cloud Service to Onboard Users and Groups for Oracle Access Governance

If your Oracle Access Governance instance uses Oracle Identity Cloud Service for identity management, you use Oracle Identity Governance provisioning, an external Identity Provider (IDP), or a self-registration profile to onboard user accounts for everyone you expect to use Oracle Access Governance. These users will be assigned to a group, which, when you have completed onboarding, you map to Oracle Access Governance application roles .

As an Oracle Cloud Infrastructure Cloud Administrator , you can use one of the following approaches to enable access for users to the Oracle Access Governance application.

Approach 1: Set Federated Authentication from an External Identity Provider (IDP)

- Setup federation with an external IDP:
- Set up a federated login between an Identity Domain and external IDP. Users can sign in and access Oracle Access Governance resources and features by using existing logins and passwords managed by the IDP.
- Refer to[Federating with Identity Providers](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm)in the Oracle Cloud Infrastructure documentation for further details.
- Enable SAML Just-In-Time provisioning.
- This process automates user account creation when a user first tries to sign in to Oracle Cloud Infrastructure where the user does not yet exist in the Identity Domain.
- Refer to[User Provisioning for Federated Users](https://docs.oracle.com/iaas/Content/Identity/Tasks/usingscim.htm#User_Provisioning_for_Federated_Users)in the Oracle Cloud Infrastructure documentation for further details.

Approach 2: Configure Oracle Identity Governance Provisioning with Oracle Cloud Infrastructure Identity and Access Management Using the Oracle Identity Cloud Service Application

- Configure the Oracle Identity Cloud Service Application.
- Download the connector installation package and copy the contents to the OIG_HOME/server/ConnectorDefaultDirectory directory. Refer to[Downloading the Connector Installation Package](https://docs.oracle.com/en/middleware/idm/identity-governance-connectors/12.2.1.3/cgidc/deploying-oracle-identity-cloud-service-connector.html#GUID-99BD300F-87AA-44D6-9CAE-9D6CA0D19DAD)for further details.
- Log in to the Oracle Cloud Infrastructure Console and create an application with the type Confidential . Refer to[Creating an Application By Using the Connector](https://docs.oracle.com/en/middleware/idm/identity-governance-connectors/12.2.1.3/cgidc/deploying-oracle-identity-cloud-service-connector.html#GUID-172043FF-EF15-4808-B0E7-A5600848BE04)for further details.
- Copy the Client ID and Client Secret from the created Application. This will be used in customAuthHeaders in ITResource.
- Configure SSL to secure communication between Oracle Identity Governance and the target system, in this case, Oracle Access Governance. Refer to[Configuring SSL for the Connector](https://docs.oracle.com/en/middleware/idm/identity-governance-connectors/12.2.1.3/cgidc/performing-postconfiguration-tasks-idcs-connector.html#GUID-ADA498BB-B713-48BE-BCAB-5CC44761C540)for further details.
- Create Groups: Login to the Oracle Cloud Infrastructure Console and create groups for any Oracle Identity Governance groups you want to map to Oracle Access Governance roles.
- Create an IDCS application in Oracle Identity Governance. Refer to[Creating an Application By Using the Connector](https://docs.oracle.com/en/middleware/idm/identity-governance-connectors/12.2.1.3/cgidc/deploying-oracle-identity-cloud-service-connector.html#GUID-172043FF-EF15-4808-B0E7-A5600848BE04)for further details.
- Run the Group Lookup Recon Job.
- Provision the IDCS application for those users with a membership of Access Governance groups.

Approach 3: Self Registration Profiles

Create self-registration profiles to enable users to create their accounts in Oracle Cloud Infrastructure Identity and Access Management. Refer to[Creating Self-Registration Profiles](https://docs.oracle.com/iaas/Content/Identity/selfregistrationprofiles/overview.htm)for further details.

## Assign Access Governance Application Roles to Users and Groups

Once users are on-boarded, all active Workforce users can log in and access the Oracle Access Governance Console. To determine what privileges they have within Oracle Access Governance, assign them the relevant predefined application roles as described in[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm#predefined-application-roles-reference).
Assigning Oracle Access Governance depends on whether identity domains are available in your cloud account.
- If Domains is listed, then use the[For Identity Domain Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm#assign-application-roles)method.
- If Domains is not listed, and you use the federated Oracle Identity Cloud Service (IDCS) method to manage users, then use the[For Non Identity Domain Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm#assign-application-roles)method.

For Identity Domain Users

Here's how you can assign Oracle Access Governance application roles to Users and Groups:
- Open your web browser and navigate to[https://cloud.oracle.com](https://cloud.oracle.com).
- Enter the name of your Cloud Account Administrator in the Cloud Account Name field and click Next .
- On the Cloud Infrastructure sign-in page, enter your sign-in credentials under Oracle Cloud Infrastructure Direct Sign-In . Click Sign In .
- Click the icon in the top, left corner to display the navigation menu.
- Click Identity &amp; Security in the navigation menu.
- Select Domains within the Identity list.
- On the left pane, in the Compartment list, select the relevant compartment for Oracle Access Governance.
- In the available domain list, select the domain link related to Oracle Access Governance. Your selected domain page is displayed.
- From the left pane, select the Oracle Cloud Services tab.
- Select the Oracle Access Governance cloud service.
- On the left pane, in the Resources section, select Application roles .
- In the Application roles section, select the icon corresponding to the application role that you want to assign.
- Select the Manage link corresponding to the Assigned users category. The Manage user assignments window is displayed.
Note  
  
To assign application roles to user groups, select the Manage link corresponding to the Assigned groups category.
- Select the Show available users link.
- In the available list of users, select the check box corresponding to the user name, and then click Assign .

The application role is assigned to the selected user or group. You can verify the same by viewing the names in the Available users or Available groups list.

For Non Identity Domain Users

Here's how you can assign Oracle Access Governance application roles to Users and Groups for Non Identity Domain-based users:
- Sign in to the Oracle Identity Cloud Service console with the user assigned as the Service Administrator team role.
- Click the icon in the top, left corner to display the navigation menu.
- Click Oracle Cloud Services and then select your Oracle Access Governance service instance.
- Click the Application Roles tab. All the available application roles in Oracle Access Governance are displayed.
-
