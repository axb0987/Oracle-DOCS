# Configure Integration with Oracle Transport and Global Trade Management (OTM/GTM)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-configure-integration-otmgtm.htm
- Fetched: 2026-09-05 03:15 CDT

# Configure Integration with Oracle Transport and Global Trade Management (OTM/GTM)

You can establish a connection between Oracle Access Governance and Oracle Transport and Global Trade Management (OTM/GTM) application as a Managed System. To configure, use Orchestrated Systems in the Oracle Access Governance Console.

## Prerequisites

Before you install and configure the Oracle Transport and Global Trade Management (OTM/GTM) orchestrated system. You should consider the following prerequisites and tasks.
- You must create a confidential application in Oracle Cloud Infrastructure.
- You must create a new user account in Oracle Transport and Global Trade Management (OTM/GTM) and assign a User Administrator role for external integrations.

### OAuth 2.0: Create an Integrated Confidential Type Application

To create an integrated application of Confidential type in OCI IAM, you must have the Identity Domain Administrator role.

Assign client ID as the nickname for Oracle Transport and Global Trade Management (OTM/GTM) integration user account.

Complete the mentioned prerequisites to obtain integration parameters.[OAuth 2 for OTM/GTM](https://docs.oracle.com/en/cloud/saas/transportation/25c/otmit/oauth-2.html).

- Navigate to Identity &amp; Security , and click Domains .
- Select Domains .
- Select the Integrated applications tab.
- Select Add application .
- Select Confidential Application tile, and then select Launch workflow .
- In the Details page, enter the following:
- Enter name and description for the confidential application.
- In the Authentication and authorization section, enable Enforce grants as authorization .
- Click Submit .
Edit OAuth configurations
- Select the OAuth configuration tab.
- Select Edit OAuth configuration .
Resource Server Configurations
- Select Configure this application as a resource server now
- In the Primary audience field, enter the Oracle Transport and Global Trade Management (OTM/GTM) URL.
- Add the application scope
Client configuration
- Select Configure this application as a client now .
- Select the following grant types:
- Client Credentials
- JWT assertion
- Authorization token
- Enter the Redirect URL, such as`https://otmgtm-example-instance.oraclecloud.com/sso/openid_connect_redirect.jsp`
- Select network perimeter to restrict login attempts to specific IPs or ranges, else select Anywhere .
- Under Client configuration &gt; Token Issuance policy select Add resources .
- Click Add scope , select the drop-down against the Confidential application we created and select the available scope under this application and click Add .
- Click Save Changes .
- Click Submit .
- Activate the application, click the Actions icon and then select Activate . The status should change from Inactive to Active .
Note Client ID and Client Secret for integration settings and also when configuring the application user Nickname.

### Create User Account For External Integrations

Create a user and assign User Administrator role to the service user.

- Go to the Oracle Transport and Global Trade Management (OTM/GTM) Console.
- Select Configuration and Administration .
- From the User Management list, select User Manager .
- Select New .
- Enter User Name avoiding the special characters. For more details, see[Special Characters](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-gtm-integration-reference.htm#oracle-otm-special-characters).
- Assign Client ID as the Nickname . For example,`S92C5BDC1234`.
- Select Domain Name . You cannot update the domain name once assigned.
- Enter password and verify the password.
- In the User Role ID, assign the following:
- For the Least Privilege access, select`USER-ADMINISTRATION`. To know about provisioning restrictions, see[Limitations](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-gtm-integration-reference.htm#oracle-otm-known-issues).
- In the Account Policy ID list, select BASIC POLICY .
- In the Access Control list, select External Integration .
- Select Finished .

## Configure

You can establish a connection between Oracle Transport and Global Trade Management (OTM/GTM) and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of your orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select Oracle Transport and Global Trade Management (OTM/GTM) .
- Click Next .

### Add details

Add details such as name, description, and configuration mode.
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- For this orchestrated system, Oracle Access Governance can manage permissions
- Click Next .

### Add Owners

Add primary and additional owners to your orchestrated system to allow them to manage resources.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account settings

Manage account settings when setting up your orchestrated system including notification settings, and default actions when an identity moves or leaves your organization.
- Select to allow Oracle Access Governance to create new accounts when a permission is requested, if the account does not already exist. By default, the account is be created if it doesn't exist, when a permission is requested. If the option is cleared, then permissions can only be provisioned where the account already exists in the orchestrated system. If permission is requested where no user exists then the provisioning operation is failed.
- 
Select where and who to send notification emails when an account is created. The default setting is User . You can select one, both, or none of these options. If you select no options then notifications is not sent when an account is created.
- User
- User manager
- When an identity leaves your enterprise you must remove access to their accounts. You can select what to do with the account when this happens. Select one of the following options:
- Delete
- Disable
- No action
Note  
  
These options are displayed only if supported in the orchestrated system type being configured. For example, if Delete isn't supported, then Disable and No action options are displayed.
- When all permissions for an account are removed, for example when moving from one department to another, you might need to adjust what accounts the identity has access to. You can select what to do with the account when this happens. Select one of the following options:
- Delete
- Disable
- No action
Note  
  
These options are displayed only if supported in the orchestrated system type being configured. For example, if Delete isn't supported, then Disable and No action options are displayed.
- If you want Oracle Access Governance to manage accounts created directly in the orchestrated system you can select the Manage accounts that are not created by Access Governance option. This reconciles accounts in the managed system and allows to manage them from Oracle Access Governance.

### Integration settings

Enter details of the connection to your Oracle Transport and Global Trade Management (OTM/GTM) system.
- On the Integration settings step of the workflow, enter the details required to allow Oracle Access Governance to connect to your Oracle Transport and Global Trade Management (OTM/GTM) system.

Integration settings
Parameter Name Description

Base URL Primary URL address which includes host and port of your Oracle Transport and Global Trade Management (OTM/GTM) service instance. For example:
```

```

Authentication server URL Enter the OCI IAM Domain URL followed by`oauth2/v1/token`. To find your Domain URL, see[Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm). For example:
```

```

Client ID Client ID of the OCI IAM confidential application.

Client secret Client secret of the OCI IAM confidential application .
What is the scope? Enter applicable scopes allowed to the confidential application. For example:
```

```

Do you want to set a custom admin role on user termination or an admin role removal? Assigns the defined role instead of the DEFAULT role, when:
- Entitlements are deleted if 'Delete the permissions for disabled accounts' is enabled. See
- When a role is removed After removal, check the activity log. Update Account followed by Remove account or permission events are triggered. In the View details link under Assignment data , Oracle Access Governance assigns the defined fallback role.
- Click Add to create the orchestrated system.

### Finish Up

Finish up configuration of the orchestrated system by providing details of whether to perform further customization, or activate and run a data load.

The final step of the workflow is Finish Up .
You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
-
