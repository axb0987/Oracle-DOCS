# Create Required IAM Groups and Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm
- Fetched: 2026-09-05 02:59 CDT

# Create Required IAM Groups and Policies

Learn how to set up groups and policies to enable Roving Edge administration and functionality.
- [Creating a Policy for Ordering Roving Edge Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#ordering-devices-console)
- [Allowing Access to Roving Edge Infrastructure Resources in OCI](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#allow-access-resources)
- [Allowing Your Roving Edge Infrastructure Devices Object Storage Access](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#allow-device-object-storage-access)
- [Allowing Roving Edge Infrastructure Devices to be Self-Provisioned](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#allowing-roving-edge-infrastructure-devices-to-be-provisioned)
- [Enabling Disconnected Upgrade Bundle Delivery (Optional)](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#enabling-disconnected-upgrade)
- [Enabling Certificate Management (Optional)](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#enable-certificate-management)
- [Policy Examples](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#policy-examples)

## Creating a Policy for Ordering Roving Edge Devices

You can create a policy that allows you to order and manage your Roving Edge Infrastructure devices using the Oracle Cloud Console. This task uses the Create Policy template in the Oracle Cloud Console.
- 

Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .
- 

Select Create Policy . The Create Policy dialog box appears.
- 

Complete the required fields as described in[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm).
- 

Use the Policy Builder and select Let Users Create and Manage Roving Edge Devices under Common Policy templates .
- 

For self-provisioning, add the following policy to the template:

```

```

- 

Follow the instructions displayed in the Policy Builder to configure your policy groups.
- 

Select Create . Your changes go into effect typically within 10 seconds.

## Allowing Access to Roving Edge Infrastructure Resources in OCI

Use the following syntax to allow your user groups access to Roving Edge Infrastructure resources in your tenancy:
```

```

```

```

where`< admin_user_group >`is a group created to manage Roving Edge Infrastructure administrators.

You can also narrow this access to compartments. For example, if you wanted to allow a group of users to manage all Roving Edge Infrastructure resources in the compartment "finance" in Oracle Cloud Infrastructure, use the following:
```

```

```

```

## Allowing Your Roving Edge Infrastructure Devices Object Storage Access

This section describes the steps required to allow your Roving Edge Infrastructure device to perform data synchronization while the device is in your possession.

Each Roving Edge Infrastructure device node functions as a resource in Oracle Cloud Infrastructure, requiring permission to read/write buckets in your compartments within your tenancy for data sync tasks.

Use a dynamic group to represent all the Roving Edge node resources in your tenancy. See[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm)for more information on how to create dynamic groups.
Note  
  
All dynamic group names must exactly match what is specified in the policy statements. Dynamic group names and policy statements are case-sensitive.
Note  
  

If your dynamic group belongs to a non-default identity domain such as[Oracle Identity Cloud Service](https://docs.oracle.com/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm), and the dynamic group is created in that domain, you must prefix the dynamic group name with the domain name in all policy statements for dynamic groups. For example:
```

```

Create a dynamic-group called`roving-edge-devices`with the matching rules below:
```

```

Grant this dynamic-group a policy to read and write to buckets, for example:
```

```

Grant dynamic group access to the Object Storage namespace
```

```

Set a policy to grant the Roving Edge Infrastructure service read access to your buckets. This read access policy allows the generation of a manifest file containing the information about the objects you want synced to your Roving Edge Infrastructure devices.
```

```

Note  
  

You can narrow your access to a compartment. Ensure you give read access to all the compartments associated with all your workload buckets. For example, if you had two buckets, one in compartment "finance" and the other in compartment "accounts," you must set this policy for both the compartments.

## Allowing Roving Edge Infrastructure Devices to be Self-Provisioned

Using the previously created dynamic group`roving-edge-devices`in[dynamic-group for Object Storage access](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#allow-device-object-storage-access), grant the dynamic-group manage permissions to enable device self-provisioning on-site.
```

```

## Allowing Recovery Key Backups

Create a policy for the administration user group to access the Roving Edge Infrastructure resources to set up secrets, grant admin access to create vault, key, secret, secret-version.

This recommended policy enables administrators to back up the recovery key when a device is self-provisioned as described in[Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device).

```

```

For more information about more granular access control, see[Overview of Vaults, Key Management, and Secret Management](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).

## Enabling Disconnected Upgrade Bundle Delivery (Optional)

To enable disconnected upgrade bundles to be delivered to your tenancy, follow these instructions.

Grant the requester object create and overwrite permissions to the destination bucket:
```

```

Grant the Object Storage service in the region to manage the buckets in your tenancy:
```

```

You can also create narrower permissions using the following example:
```

```

See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for a list of region identifiers.

## Enabling Certificate Management (Optional)

This section describes the steps required to allow your administrators to create certificate authorities and allow your Roving Edge Infrastructure device to access certificate management resources in the Oracle Cloud Infrastructure Cloud.

Create a policy for the security administrators to create vault and master key:
```

```

Create a policy for the security administrators to use the certificate authority:
```

```

Create a dynamic group called`certificate-authority-dynamic-group`with the matching rules:
```

```

Create a policy for the certificate authority to use keys:
```

```

Create a policy for Roving Edge Infrastructure devices to use the certificate authority and manage certificates:
```

```

Create a policy for Roving Edge Infrastructure nodes to fetch and update its certificate configurations:
```

```

Note  
  
If you created the self-provisioning policy described in[Allowing Roving Edge Infrastructure Devices to be Self-Provisioned](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#allowing-roving-edge-infrastructure-devices-to-be-provisioned), don't create this policy. The self-provsioning policy satisfies this requirement.

## Policy Examples

The group`rover-admins`is defined to be the administrator for Roving Edge Infrastructure resources:
```

```

Allow Roving Edge Infrastructure to attach workloads:
```

```

Allow Roving Edge Infrastructure access to Object Storage:
```

```

Allow the dynamic group of Roving Edge nodes to be self-provisioned and manage its certificate configurations:
```

```

Allow`rover-admins`to setup and back up the Device Recovery Key:
```

```

(Optional) Enable disconnected upgrade bundle delivery:
```

```

(Optional) Enable certificate management:
```

```

What's next?

If you're requesting a device, see one of the following sections based on the type of device:
- [Creating and Submitting a Node for Compute, GPU, and Storage Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Node2/create_node2.htm#top)
- [Creating a Roving Edge Ultra Node](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Ultra/create_ultra.htm#top)
