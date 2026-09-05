# Manage Integrations with Orchestrated System
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-integrations-with-orchestrated-system.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Integrations with Orchestrated System

Using Orchestrated System of Oracle Access Governance, you can perform integrations with other systems by adding an orchestrated system, change the connection settings, validate and load the data in Oracle Access Governance.

## Add an Orchestrated System

You can integrate various systems, such as database, directory, applications, and cloud provider. The first step to integrate with the system of your choice is to add an Orchestrated system.

To add an Orchestrated system:
- In the Oracle Access Governance Console, from the navigation menu, select Service Administration → Orchestrated Systems
- Select Add an orchestrated system to add a new Orchestrated system, or select an existing orchestrated system from the list to manage existing orchestrated systems.
Note  
  
The integration details depend on the type of Orchestrated system. Refer to the[Supported Integrations in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/supported-integrations-in-oracle-access-governance.htm)article for the appropriate documentation for the required Orchestrated system.

## Manage an Orchestrated System

The Orchestrated Systems page of the Oracle Access Governance Console allows you to easily manage your orchestrated systems. You can view a list of the Orchestrated Systems configured in your service instance, including name, type, configuration mode, and status . You can also initiate a data load, update configuration settings, and enable/disable individual orchestrated systems.
To manage your orchestrated systems, navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- On the Orchestrated Systems page, you are able to view the orchestrated systems that you have configured in your Oracle Access Governance instance. The list of orchestrated systems displays the following details:
- Name : The name of the orchestrated system.
- Type : The type of orchestrated system, for example, Flat File , Database User Management (Oracle) , or Microsoft Active Directory . A complete list of orchestrated system types supported by Oracle Access Governance can be found in[Supported Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/supported-integrations-in-oracle-access-governance.htm#supported-systems).
- Configuration mode : The configuration mode that the orchestrated system is setup with.
- Last updated : Last date the orchestrated system configuration was updated.
- Upcoming data load : Date and time of any upcoming scheduled data load.
- Status : Current status of the orchestrated system. Values include:
- Active
- Disabled
- Waiting for initial connection After you have reviewed the orchestrated systems in the Oracle Access Governance instance, select a specific orchestrated system and drill down into further information or update various configuration elements.
Select one of the following to view configuration of a specific orchestrated system:
- The orchestrated system link in the Name column.
- Manage connection from the navigation menu. This displays the configuration page for the selected orchestrated system.

## Manage Orchestrated System Resources

Decide which resources are ingested from governance orchestrated systems, allowing full control of the source used to load data into Oracle Access Governance. This functionality is specific to Oracle Identity Governance.

To manage resources:
- In the Oracle Access Governance Console, access the navigation menu by selecting the icon. Select Service Administration → Orchestrated Systems .
- In the Orchestrated Systems page, click on the icon for the governance orchestrated system you want to update, and select Manage resources from the drop down list.
- On the Resources page, you can see a list of Connected resources and Disconnected resources .
- To disable a connected resource:
- Select the Disconnect icon, , for the resource you want to disable.
- A confirmation dialog displays, asking you if you are sure you want to disconnect the resource from the governance orchestrated system.
Note  
  
All information related to the resource will be removed, and you cannot reconnect the resource after it's disconnected.
- To remove the resource, select Disconnect . If not, select No, keep connected . If the resource is disconnected, it displays in the Disconnected resources section.

## Initiate Data Load

You can initiate data load from orchestrated systems on-demand, using the Oracle Access Governance Console.

To initiate a data load from an orchestrated system, perform the following tasks.

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select one of the following to view the configuration of a specific orchestrated system:
- The orchestrated system link in the Name column.
- Manage integration from the navigation menu. This displays the configuration page for the selected orchestrated system.
- Select the Load data now button which will initiate a data load. You can track the status in the Activity Log .

## View Activity Log

Use the activity log to monitor the status of the orchestrated system.

To view the activity log:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select View activity log from the navigation menu to view the configuration of a specific orchestrated system. This displays the Activity log page for the selected orchestrated system, which displays log details for the selected orchestrated system.
The activity log includes information on activities including the following:
- Data load : Initiates when the data is either run on-demand by the Administrator, or when data is automatically synced according to the system settings for the orchestrated system.
- Full data load : Initiates when data is synchronized for the first time after a new integration is established.
- Validate : Initiates when a new integration is established or when you update the connection settings.
- Revoke : Initiates when an access reviewer revokes one or more user privileges in the access review tasks. This activity occurs to support closed-loop access remediation.
- Schema discovery : Initiates when a new integration is established, or when you select the[Fetch attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#fetch-attributes)button in the Identity Attributes page.
- Provisioning : Includes Create Account, Update Account, Add Child Data, Remove Child Data operations.
Select View details for an activity to view operation information.
- Data load operations : Displays data load, full data load, and terminated identities data load details. The detail includes the processed record count for each data type in the orchestrated system, such as the number of accounts, identities, applications, permissions, and permission types loaded.
- Provisioning operations : Displays activity details and the associated user, account, and assignment data for the provisioning operation, when applicable.

## Disable an Orchestrated System

You can disable an orchestrated system to stop operations between Oracle Access Governance and the orchestrated system.

To disable an orchestrated system, perform the following tasks.

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select one of the following to view the configuration of a specific orchestrated system:
- The orchestrated system link in the Name column.
- Manage connection from the navigation menu. This displays the configuration page for the selected orchestrated system.
- Select the Disable button which would disable the selected orchestrated system.

## Delete an Orchestrated System

You can delete an orchestrated system only with the Draft status. Use Disable for other statuses.

To delete an orchestrated system, perform the following tasks.

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select one of the following to delete the orchestrated system:
- Select Delete from the Actions icon to delete the orchestrated system in the Draft state.
- Select Manage integration from the Actions icon, and then in the Actions list, select Delete .
-
