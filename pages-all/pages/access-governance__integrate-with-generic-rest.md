# Integrate with Generic REST (Expert mode)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-generic-rest.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Generic REST (Expert mode)

The Generic REST Orchestrated System provides a solution to integrate Oracle Access Governance with REST-based identity-aware systems. A REST-based identity-aware system is any system that exposes its REST APIs or interfaces for identity management.

## Generic REST Orchestrated System Overview

The Generic REST Orchestrated System provides features including the following:
- Full/incremental data load for Authoritative Sources or Managed Systems
- Real-time provisioning
- Cloud native serverless function integration to define REST-based identity-aware system schema, request, response, and test templates

The Generic REST Orchestrated System differs from others in that definitions for schema, request, and response aren't fixed. Other Orchestrated Systems have schema, request, response, and test templates pre-loaded for the Authoritative Source or Managed System to which they apply. You can apply Generic REST Orchestrated Systems to any REST-based identity-aware system, the schema, request, response, and test templates are loaded at runtime, rather than when the Orchestrated System is created.
For each Authoritative Source or Managed System, you will need to create the following templates:
- grc-schema-template : This template defines the schema for the Authoritative Source or Managed System you want to integrate.
- grc-request-template : This template defines the request format (headers, url, request parameters, request body) required to invoke the Authoritative Source or Managed System API to request identity data.
- grc-response-template : This template defines the response format for identity and account data.
- grc-test-template : This template defines an API to test the connectivity between Oracle Access Governance and the Authoritative Source or Managed System.
When an operation is invoked the following parameters are passed to OCI Functions.
- Orchestrated system name
- Entity name (identity or account)
- Operation name

The OCI Function is called and returns a JSON file with the templates relevant to the Orchestrated System.

## Prerequisites

Before you install and configure a Generic REST Orchestrated System, you should consider the following prerequisites and tasks.

### Certified Components

The Managed System can be any one of the following:

- Any identity-aware system that supports REST services

### Supported Modes

Generic REST Orchestrated System supports the following configuration modes:
- Authoritative Source
- Managed System

## Use Cases Supported by the Generic REST Orchestrated System

A Generic REST Orchestrated System can be used to on-board identity data into Oracle Access Governance from a REST service, and then efficiently manage identities in an integrated cycle with the rest of the identity-aware systems in your enterprise.
As a business use case example, consider a leading logistics company that has 20+ cloud applications. Most of these cloud applications are now inefficient because data in these applications are manually entered and are managed using spreadsheets or custom-coded process flows. Therefore, this company wants to integrate its cloud applications with Oracle Access Governance to streamline its operations, increase its organizational efficiency, and at the same time, lower its operational costs. There are two approaches for integrating these cloud applications with Oracle Access Governance. One approach would be to deploy a point-to-point connector for each of these applications. The drawbacks of this approach are as follows:
- 

Increased time and effort to identify and deploy a point-to-point connector for each application.
- 

Increased administration and maintenance overheads for managing connectors for each application.
- 

Unavailability of point-to-point connectors for all applications. In such a scenario, one needs to develop custom connectors which increases time and effort to develop, deploy and test the custom connector.

An alternative to this approach is to use the Generic REST Orchestrated System to integrate all the cloud applications with Oracle Access Governance. The Generic REST Orchestrated System provides the ability to manage accounts across all cloud applications without spending additional resources and time on building custom connectors for each cloud application.

The Generic REST Orchestrated System helps enterprises leverage Oracle Access Governance to integrate with Managed Systems for identity governance. These Managed Systems include any application that exposes REST APIs such as SaaS, PaaS, home-grown applications and so on.

The following are some example scenarios in which the Generic REST Orchestrated System is used:
- 

User Management

The Generic REST Orchestrated System allows you to manage individuals who can access resources by defining them as identities in Oracle Access Governance and assigning them to identity collections and roles. Identities are created from any authoritative Orchestrated System such as Generic REST, on data load.
- 

Access Control

The Generic REST Orchestrated System manages access control via identity collections, roles, access bundles, and policies. Depending on the orchestrated system being used, you can manage access using Oracle Access Governance self service features, specifically[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm). For example, you can use the Generic REST Orchestrated System to automatically assign or revoke access to a system based on predefined access policies in Oracle Access Governance. As new users are added to a specific role, they automatically gain corresponding access in the systems covered by the access policy.

## Setup OCI Serverless Function to Connect with REST-based Identity Aware System

The Generic REST Orchestrated System requires support from OCI Serverless Functions in order to connect to REST-based identity aware systems.

To setup OCI Functions for use with the Generic Rest Orchestrated System refer to[Setup OCI Serverless Function to Connect with REST-based Identity Aware System](https://docs.oracle.com/en-us/iaas/Content/access-governance/setup-oci-serverless-function-to-connect-with-rest-based-identity-aware-syst.htm).

## Configure

You can establish an integration between REST-based identity-aware systems and Oracle Access Governance by entering details of the OCI Functions and templates to integrate the REST-based system. To achieve this, use the Orchestrated System functionality available in the Oracle Access Governance Console.

Establish an integration between REST-based identity-aware systems and Oracle Access Governance by entering details of the OCI Functions and templates to integrate the REST-based system. Use the Orchestrated System functionality in the Oracle Access Governance Console.

Oracle Access Governance uses resource principal to access and invoke the OCI functions. If you have an existing orchestrated system and need to migrate, see[Migrate API Key Access to Resource Principal Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-generic-rest.htm#migrate-api-key-access-to-resource-principal-access).

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard. You can search for the required system by name using the Search field. Select the Generic REST Connector tile. When you select this tile, a dialog page is shown outlining the steps to configure the Orchestrated System. This includes a link to a sample implementation of the OCI Functions required to connect to REST-based identity aware systems. If you have not done so, you should download the idm-agcs-generic-rest-reference-implementation.zip file and develop your own OCI Functions based on this example. For further details on the sample implementation see[Setup Sample Implementation](https://docs.oracle.com/en-us/iaas/Content/access-governance/setup-oci-serverless-function-to-connect-with-rest-based-identity-aware-syst.htm#rest-serverless-deploy). For further details on how to develop the OCI Functions required see[Setup OCI Serverless Function to Connect with REST-based Identity Aware System](https://docs.oracle.com/en-us/iaas/Content/access-governance/setup-oci-serverless-function-to-connect-with-rest-based-identity-aware-syst.htm)and[Generic Rest Schema Discovery](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm).

After selected, a value of Generic REST Connector is displayed on the on the right side under What I've selected . Select Next .

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

### Add owners
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

### Configure

On the Configure step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to the system using the Generic REST Connector.
- What is the OCI tenancy OCID of the OCI function? : Enter the OCID (Oracle Cloud Identifier) for your OCI function. See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five). For example,`ocid1.oc1..aabdgsegsccawmw2o6qraopae7egmlochlopclhnwxq6pctu6oocgn`.
- What is the OCI function's region code? : Enter the home region for the target OCI tenancy, using the region identifier. For example, for US East (Ashburn), the region identifier is`us-ashburn-1`. See[The Home Region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#The), and[How do I find my tenancy home region?](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How).
- What is the OCI function's compartment Id? : Enter the compartment ID for the function you want to integrate.
- What is the OCI function's application name? : Enter the application name of the function you want to integrate.
- Function Version : Enter the function version of the function you want to integrate.
- Duration for request template cache TTL (in minutes) : Duration for which the request template will be cached. If time is set as 0, no caching will be done. When the cache expires the OCI function will be invoked to get the new template. The cache time should be less than the token expiry time to avoid dropped connections due to expired token.
- Duration for response template cache (in minutes) : Duration for which the response template will be cached. If time is set as 0, no caching will be done. When the cache expires the OCI function will be invoked to get the new template. The cache time should be less than the token expiry time to avoid dropped connections due to expired token.
- Duration for test template cache (in minutes) : Duration for which the test template will be cached. If time is set as 0, no caching will be done. When the cache expires the OCI function will be invoked to get the new template. The cache time should be less than the token expiry time to avoid dropped connections due to expired token.
- Duration for schema template (in minutes) : Duration for which the schema template will be cached. If time is set as 0, no caching will be done. When the cache expires the OCI function will be invoked to get the new template. The cache time should be less than the token expiry time to avoid dropped connections due to expired token.
- Read Response Timeout (in seconds) : Enter an integer value that specifies the number of seconds within which response must be received from the
- Connect Timeout (in seconds) : An integer value that specifies the number of seconds after which an attempt to establish the connection between the and times out.
- Select Add .
- Required OCI Policies? : Copy the exact statements in the root compartment of the relevant tenancy. See[Managing Policies](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm)to apply the policies to the tenancy.

### Finish up
On the final step, Finish up , you get a choice whether to further configure your Orchestrated System before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Migrate API Key Access to Resource Principal Access

If you have an existing orchestrated systems that use the API Key access method to connect, then you should migrate at your earliest convenience to Resource Principal access method.

To migrate API Key access to Resource Principal access:
- Navigate to the Integration settings page following the instructions given in Configure Orchestrated System Integration Settings.
- On the Integration settings page, you will see a deprecation warning. Select the Learn more about migrating button.
- Copy the exact policies in the root compartment as displayed on your Console. See[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm)for details on how to apply the policies.
Note  
  

The required policies vary depending on where your OCI Functions and your Oracle Access Governance instance are hosted (for example, in the same tenancy versus different tenancies).
- Once you have applied policies, select Test integration to check the connection. If you have any errors or messages, review your configuration. You will not be able to complete the migration until the test is successful.
- If your connection is confirmed then click on the Migrate button to start the migration.
- When the migration completes, a confirmation message is displayed
Note  
  

Once you have completed migration to the Resource Principal method you cannot reverse the procedure and reinstate API Keys method on your orchestrated system.

## Post Configuration

Once you have configured your Generic REST Orchestrated System, you can navigate to the Orchestrated System page and check operations in the activity log. Some of the operations that you may see include:
- Schema Discovery : The Generic REST Orchestrated System is schema-less at design and deployment time. As part of the orchestration lifecycle, schema discovery must take place to update the Orchestrated System with details of the schema and object classes for the required Authoritative Source or Managed System. For details regarding Schema Discovery see[Generic Rest Schema Discovery](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm).
- Validate : This operation performs the following tasks:
- Invokes the test template, which in turn invokes the endpoint specified in the template and checks connectivity with the Managed System.
- Invokes the schema template and retrieves all the schema information for the Managed System including entities and attributes.
- Lookup Data Load : If any lookups are defined, the data corresponding to the lookups is loaded.
-
