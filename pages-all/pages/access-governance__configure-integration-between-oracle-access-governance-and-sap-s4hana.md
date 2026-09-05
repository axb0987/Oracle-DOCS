# Configure Integration Between Oracle Access Governance and SAP S/4HANA
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-s4hana.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Integration Between Oracle Access Governance and SAP S/4HANA

You can establish a connection between Oracle Access Governance and SAP S/4HANA SaaS application as a Managed System. To configure, use Orchestrated Systems in the Oracle Access Governance Console.

## Prerequisites

Before you install and configure the SAP S/4HANA Orchestrated System, you should consider the following prerequisites and tasks.

### Setup to Authenticate for Data Exchange - Create a Communication User

Create a communication user to authenticate for reconciliation and provisioning in Oracle Access Governance. Use the same communication user to perform integration operations in Oracle Access Governance.

You need the Administrator role to use the Communication Management applications.

Create a Communication User in SAP S/4HANA
- Sign in to SAP S/4HANA Cloud application with administrator credentials.
- From the Communication Management catalog, choose the Communication Systems application.
- Click New to create a new communication user.
The Create Communication User page is displayed.
- Enter User Name, Description, and Password.
- Click Propose Password to get a system-generated password. Save the credentials for authentications for your communication user.
- Click Create .

### Create Communication System

Perform the following steps to create a communication system and assign a communication user to the communication system

- Sign in to SAP S/4HANA Cloud application with administrator credentials.
- From the Communication Management catalog, choose the Communication Systems .
- Click New to create a new communication system.
- Enter System ID and System Name, and then click Create .
- Under Technical Data , enter the Host Name of your SAP S/4HANA Cloud tenant in the following format:`<tenant ID>.s4hana.ondemand.com`
- Click User for Inbound Communication tab, then click the add (+) icon.
- Assign the communication user you created, and select the authentication method as User ID and Password .
- Click Save .

### Create a Communication Arrangement

Create a communication arrangement by setting up endpoint URLs to call the SOAP service.
Inbound service allows you to configure settings for sending data from Oracle Access Governance to SAP S/4HANA.

Create a New Communication Arrangement
- Log in to SAP S/4HANA Cloud application with administrator credentials.
- From the Communication Management catalog, choose the Communication Arrangements .
- Click New to create a new communication arrangement.
- Select communication scenarios, as follows
- SAP_COM_0093 Identity Management Integration
- SAP_COM_0193 Identity Provisioning Integration
- Enter an arrangement name, and click Create .
- Select Communication Arrangement in the list. The inbound communication user is automatically assigned.
- Under Inbound Services , the endpoint URLs to call the SOAP service in the following format

Option Description
Business User - Read`https://<S4HANA tenant ID>-api.s4hana.ondemand.com/sap/bc/srt/scs_ext/sap/querybusinessuserin`

For more details, see[Business User - Read](https://api.sap.com/api/QUERYBUSINESSUSERIN/overview)  

Business User - Update`https://<S4HANA tenant ID>-api.s4hana.ondemand.com/sap/bc/srt/scs_ext/sap/managebusinessuserin`

For more details, see[Business User](https://api.sap.com/api/MANAGEBUSINESSUSERIN/overview)  

- Click Save .
WSDLs can be downloaded from this arrangement once saved.
- Expand the Integration Manager option and select End Point Configuration .
- To create a new endpoint, click Create New .
An End Point Configuration - Create End Point page opens.
- In the Name field, enter a name for the end point.
- Select the type as Inbound .
- Navigate to the HTTP Authentication section , to use HTTP Basic Authentication.
- Enter the user ID in the Sign In field.
- Enter password in the Password field.
You need to provide this information to configure orchestrated system in the Oracle Access Governance Console.
- Click Save .

## Configure

You can establish a connection between SAP S/4HANA and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

Identity orchestrations are set up from the Oracle Access Governance Console. Go to the Orchestrated Systems page to integrate SAP S/4HANA with Oracle Access Governance.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select System

On the Select system step of the workflow, you can specify the type of system that you want to integrate.

You can search for the required system by name using the Search field.
- Select SAP S/4HANA.
- Click Next .

### Enter Details

In the Enter Details step, give a meaningful name to your orchestrated system, add a supporting description, and determine if you can use this system as an authoritative source or for managing permissions. For SAP S/4HANA, you can use Oracle Access Governance to manage permissions for identity accounts.
On the Enter Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
Note  
  
A message is displayed on the page indicating that Oracle Access Governance can manage permissions for this system, enabling provisioning of accounts.
- Click Next .

### Add Owners

In this step, add primary and additional owners for your orchestrated system.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account Settings

On the Account settings step of the workflow, enter details of how you would like to manage accounts with Oracle Access Governance when configured as a managed system
- Select where to send notification emails when an account is created. The default setting is User . You can select one, both, or none of these options. If you select no options then notifications will not be sent when an account is created.
- User
- User manager

For this orchestrated system, the identity accounts can only be disabled and not be deleted. So, the choices to select for mover and leaver case will be grayed out.

### Integration Settings

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to SAP S/4HANA.

Fill the configuration information as explained in the following table, and then click Add .

Integration Details
Field Description Example Reference
What is the base URL to connect to? Enter the base URL for your SAP application. Your base URL is in the format`https>://<hostname.s4hana.cloud.sap>:<port>`https://my-sap-system.s4hana.cloud.sap
What is the username to use for loading data? Enter the communication username that you created in the prerequisite. John_Rim[Setup to Authenticate for Data Exchange - Create a Communication User](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-s4hana.htm#sap-s4hana-prereq-communication-user)
What is the password? Enter password for your communication system user for authentication. 123ABC12345@cxx[Setup to Authenticate for Data Exchange - Create a Communication User](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-s4hana.htm#sap-s4hana-prereq-communication-user)
Confirm password Confirm the password. 123ABC12345@cxx

### Finish Up

Review and configure your configuration setup. You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load.
Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
