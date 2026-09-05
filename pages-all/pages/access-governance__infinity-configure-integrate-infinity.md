# Configure Integration with Oracle Infinity
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/infinity-configure-integrate-infinity.htm
- Fetched: 2026-09-05 03:14 CDT

# Configure Integration with Oracle Infinity

You can establish a connection between Oracle Access Governance and Oracle Infinity application as a Managed System. To configure, use Orchestrated Systems in the Oracle Access Governance Console.

## Configure

You can establish a connection between Oracle Infinity and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of your orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select Oracle Infinity .
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

Enter details of the connection to your Oracle Infinity system.
- On the Integration settings step of the workflow, enter the details required to allow Oracle Access Governance to connect to your Oracle Infinity system and then click Add .

Integration settings
Parameter Name Description
OCI Orchestrated System Select the dependent OCI orchestrated system name in the list. Your OCI orchestrated system must be Active.
```

```

Domain name Enter the Identity domain name where you have the Oracle Infinity application instance running. For example,`Default`.
Oracle Infinity Oracle cloud service name Enter the service name for the Oracle Infinity application running on the Oracle cloud services.
```

```

- Select Add to create the orchestrated system.

### Finish Up

Finish up configuration of your orchestrated system by providing details of whether to perform further customization, or activate and run a data load.

The final step of the workflow is Finish Up .
You're provided a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

### Post Configuration
