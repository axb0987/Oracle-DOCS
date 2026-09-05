# Installing the VMware Solution Management Appliance
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-install.htm
- Fetched: 2026-09-05 03:08 CDT

# Installing the VMware Solution Management Appliance

Install the VMware Solution Management Appliance.

Before you can install the Management Appliance, you must have the following:
- 

An SDDC that's operational. See[Creating an SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvssettingupsddc.htm)for instructions.
- 

A service gateway to the SDDC. See[Connecting an SDDC to the Oracle Services Network](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_the_Oracle_Services_Network.htm)for instructions.
- A NAT gateway to the SDDC. For instructions, see[Connecting an SDDC to the Internet](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_the_Internet_Through_a_NAT_Gateway.htm).
After you[create an SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvssettingupsddc.htm)and set up the[services gateway](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_the_Oracle_Services_Network.htm), create the vCenter system users, and then store the credentials of the users as an OCI Vault secret. The Management Appliance requires access to credentials of the following types of users to perform certain operations:
- vSphere administrator : A vSphere user with administrative privileges. This user type is used to register and unregister the vSphere plugin during provisioning and termination of the Management Appliance. It's also used to reregister the vSphere plugin when the Management Appliance is upgraded with a new version. Use the administrator@vsphere.local user created during provisioning of the SDDC.
- OCVS system user : A vSphere user with read-only privileges used to access ESXi host metrics. Use vCenter to create a dedicated user called ocvssystem@vsphere.local .
- NSX administrator user : A user who performs NSX operations when the Management Appliance is adding a new ESXi host. Use the NXS admin user created during provisioning of the SDDC.

The vSphere Administrator and NSX admin users are already created for all SDDCs and you should already have their credentials. OCVS system user should be created manually as it is described below.

Record the OCIDs of the vault secrets because they're used in the next step for security policy setup for the following variables:
- `<administrator_secret_ocid>`
- `<ocvssystem_secret_ocid>`
- `<nsx_admin_secret_ocid>`

## Configure a Service Gateway

Service gateway access is required for the Management Appliance to reach OCI services during operation. It enables the appliance to report its state to OCI, export metrics, read/update SDDC resources, and perform other operations.

You might already have a service gateway. Follow these steps to verify your service gateway is configured correctly:

- Open the Virtual Cloud Network (VCN) associated with your SDDC and go to the Gateways section.
- Scroll down to the Service Gateways section and check whether any service gateways exist.
- If one or more service gateways exist, check the Services column to see if any gateway is set to “All Services in Oracle Services Network.” Note the name of that service gateway.
- If no service gateways exist, or none includes “All &lt;region-id&gt; Services in Oracle Services Network,” create a new one:

- Select Create Service Gateway .
- Enter a name, for example, “Service Gateway 1” or “SGW”.
- Select a compartment. Using the same compartment as the SDDC or VCN is recommended, but this can vary by setup.
- In the Services list, select “All &lt;region-id&gt; Services in Oracle Services Network.”
- Select Create Service Gateway .
- In your VCN, open the Subnets section and find the subnet where your management cluster ESXi hosts reside. It typically has the “Subnet-” prefix, but your naming might differ.
- Open the subnet details and locate the associated route table.
- Open the Route Table details.
- Go to the Route Rules section.
- In the route rules table, verify a rule exists with the following settings:

- Target Type : Service Gateway
- Destination : All Services in Oracle Services Network
- If such a rule doesn't exist, add one:

- Select Add route rules .
- Set Target Type to "Service Gateway."
- Set Destination Service to “All Services in Oracle Services Network.”
- Select the target service gateway you noted in step 3 or created in step 4. You might also need to select the compartment where it resides.
- Enter a description. For example, “Access to all OCI services from ESXi host subnet.”
- Select Add route rules .

## Create vCenter System Users

In this section, you create the ocvssystem@vsphere.local user and then configure it.

- Sign in to vSphere. From the OCI Console,[navigate to the SDDC details page](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-get.htm), and select the vSphere client link. Sign in with the Administrator@vsphere.local user (or any other privileged user).
- Create the user by following these steps:

- Under Administration , go to Users and Groups , and then select Single Sign On .
- Under Users and Groups , select the Users tab.
- Select the vsphere.local domain, and then select Add .
- In the Add User dialog, enter information for Username , Password , and Confirm password . The Description is optional, but we recommend that you specify the purpose of this user.
- Create the user role by following these steps:

Note  
  
If you already have a role you want to use, you can skip this step.
- Under Administration , go to Roles , and then select Access control .
- Select the VSPHERE.LOCAL role provider, and then select New .
- In the New Role panel, provide the Role name . The Description is optional, but we recommend that you specify the purpose of this role.
- In the Permissions table, assign the required privileges based on your vCenter version:
- vCenter Server 7:
- Category: Sessions → Privilege: Validate session
- vCenter Server 8:
- Category: Sessions → Privilege: Validate session
- Category: Host → Group: Statistics → Privilege: Query

You must select Propagate to children for this permission to be correctly propagated to ESXi host resources.
- Create the Global permission (assign the role to the user) by following these steps:

- Under Administration , go to Access Control , and then select Global Permissions .
- Select the VSPHERE.LOCAL permissions provider, and then select Add .
- In the Add Permission | Global Permission Root , select the vsphere.local domain, the user and a role you created.

You must select Propagate to children for this permission to be correctly propagated to ESXi host resources.
- Test the new user. Sign out of vSphere client. Use the new ocvssystem@vsphere.local user to sign in to vSphere. In vCenter Inventory , verify you can select an ESXi host. In the Monitor tab, verify you can view metrics for the ESXi host.
- Sign out of vSphere.

## Create Vault Secrets with User Credentials

When creating a secret, select the Manual secret generation option under Encryption key .

Select Plain-text under Secret type template . See[Managing Vault Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)for instructions.

The secrets must contain the username and password in JSON format:
- `administrator`user secret:
```

```

- `ocvssystem`user secret:
```

```

- `nsx_admin`secret:
```

```

If you gave the ocvssystem user a different name than what is listed here, use the name you created in the`username`field.

Remember the OCIDs of the Vault secrets because they're used in the next step for security policy setup for the following variables:

`<administrator_secret_ocid>`

`<ocvssystem_secret_ocid>`

`<nsx_admin_secret_ocid>`

## Create an IAM Dynamic Group and Policies

- Obtain the following information. Each value is represented in the following steps with a corresponding variable as shown in the table:

Variable Value
`<sddc_compartment_name>`The SDDC compartment name.
`<sddc_compartment_ocid>`The SDDC compartment OCID.
`<administrator_secret_ocid>`The OCID of the administrator user secret.
`<ocvssystem_secret_ocid>`The OCID of the ocvssystem user secret.
`<nsx_administrator_secret_secret_ocid>`The OCID of the nsx_admin user secret.
- Use the following statement to create a dynamic group. Replace`<sddc_compartment_ocid>`with the actual OCID of the compartment that you obtained in the previous steps. See[Creating a Dynamic Group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/To_create_a_dynamic_group.htm)for more information.

```

```

Note the dynamic group name for use in the next step.
- Use the following statements to create permissions for the dynamic group. Replace`<resource_principal_dynamic_group_name>`and`<instance_principal_dynamic_group_name>`with the name of the dynamic group you created in the previous steps. Replace`<sddc_compartment_name>`with the corresponding actual information you obtained in the previous steps. These permissions are used by system user of Management Appliance.

Important  
  

Create the policies in the root compartment (tenancy level compartment).

If your policy subject (user, group, dynamic group) is in a non-default Identity Domain, prefix the subject with the domain name. Subjects in the default domain don't need a prefix. For more information, see[Subjects](https://docs.oracle.com/iaas/Content/Identity/policysyntax/subject.htm)for more information.
```

```

- To set up permissions for the user who creates the management appliance, use the following policies.

If your admin has access rights to all resources in the tenancy you can skip this step.

If you still need to manage these permissions, we assume that you have a group which your admin user belongs to and you have to grant the permissions below to that group. Replace`<user_group_name>`with the name of your user group and replace &lt;sddc_compartment_name&gt; with your compartment name.
```

```

Note  
  
If you place SDDC and Management Appliance to your root compartment (tenancy) you should use "in tenancy" filter for the policies instead of`in "compartment <sddc_compartment_name>`."

## Install the Appliance Using the Console

- Select a compartment, and then select the SDDC.
- Under Resources , select Management appliance .
- Select Create management appliance .
The Create management appliance panel opens.
- Enter the following information:

- Compute instance name : Enter a name for the Compute instance that's created in the tenancy to host the Management Appliance.
- Metric ingestion to OCI : Enables transmission of Management Appliance metrics to the OCI Logging service.
- vSphere admin user vault secret : Enter the OCID of the vault secret you created before for the Administrator user.
- NSX admin user vault secret : Enter the vault secret for a user with full NSX administrative privileges. The Management Appliance uses this user for NXS operations when adding ESXi hosts. When no longer needed, you can turn off access to this user's credentials by disabling or removing the corresponding vault secret. This user is created when you create the SDDC.
When the appliance is created, the following status updates are displayed on the Management Appliance details page:

- State : Active
- State details : Healthy

## Check for the vSphere Plugin

- In the Management Appliance details page, next to State details , select View details .
- View the following status updates to verify connectivity:

- vSphere connectivity : Healthy
- vSphere admin connectivity : Healthy
-
