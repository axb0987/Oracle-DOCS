# Policy Configuration for Cluster Creation and Deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm
- Fetched: 2026-09-05 01:53 CDT

# Policy Configuration for Cluster Creation and Deployment

Find out about the IAM policies to create before using Kubernetes Engine (OKE).

When a tenancy is created, an Administrators group is automatically created for the tenancy in OCI Identity and Access Management (IAM). Users that are members of the Administrators group can perform any operation on resources in the tenancy. If all the users that will be working with Kubernetes Engine are already members of the Administrators group, there's no need to create other policies.

However, if you want to enable users that are not members of the Administrators group to use Kubernetes Engine, you must create policies to enable the groups to which those users do belong to perform operations on resources in the tenancy or in individual compartments. Some policies are required, some are optional. See[Create Required Policy for Groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#policyforgroupsrequired)and[Create One or More Additional Policies for Groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#policyforgroups).

You also have to create additional policies if you want to:
- Create and use clusters with virtual nodes and virtual node pools. See[Create Policy to Set Up and Use Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic-Create_Policies_for_Virtual-Nodes).
- Encrypt data in boot volumes and block volumes using your own master encryption keys from the[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)service. See[Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic_Create_Policies_for_User_Managed_Encryption).

If you want groups of users in one tenancy to access cluster-related resources in other tenancies, you have to create special cross-tenancy policy statements that explicitly state the resources that can be accessed and shared. See[Accessing Cluster-Related Resources Across Tenancies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaccessingokeresourcesacrosstenancies.htm).

As well as the above policies managed by IAM, you can also use the Kubernetes RBAC Authorizer to enforce additional fine-grained access control for users on specific clusters using Kubernetes RBAC roles and clusterroles (see[About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm). These Kubernetes RBAC rules control what authenticated users and service accounts can do within the cluster, such as deploying workloads or accessing secrets, using the Kubernetes API.

Note that an OCI IAM policy that refers to a network source (such as`allow any-user to use clusters in tenancy where request.networkSource.name='corpnet'`) cannot be used to access the Kubernetes API (for example, when using kubectl). For more information about network sources, see[Introduction to Network Sources](https://docs.oracle.com/iaas/Content/Identity/networksources/Introduction_to_Network_Sources.htm).

## Create Required Policy for Groups

To create, update, and delete clusters and node pools, users that are not members of the Administrators group must have permissions to work with cluster-related resources. To give users the necessary access, you must create a policy with a number of required policy statements for the groups to which those users do belong:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select the tenancy's root compartment or an individual compartment containing cluster-related resources from the Compartment filter.
- Select Create Policy .
- 

Enter the following:
- Name: A name for the policy (for example,`acme-dev-team-oke-required-policy`) that is unique within the compartment. If you are creating the policy in the tenancy's root compartment, the name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A friendly description. You can change this later if you want to.
- 

Statement: The following required policy statements to enable users to use Kubernetes Engine to create, update, and delete clusters and node pools:

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

The following required policy statement to enable users to perform any operation on cluster-related resources (this 'catch-all' policy effectively makes all users administrators insofar as cluster-related resources are concerned):

```

```

In the above policy statements, replace`<location>`with either`tenancy`(if you are creating the policy in the tenancy's root compartment) or`compartment <compartment-name>`(if you are creating the policy in an individual compartment).
Note  
  
Note that depending on the type of cluster, some required policy statements might not be necessary:
- To work with "VCN-native" clusters (where the Kubernetes API endpoint is fully integrated with your VCN), the`use private-ips`is always required. However, the`use public-ips`policy statement is only necessary if the clusters' public IP address option is selected. For more information about VCN-native clusters, see[Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#processes).
- To work with clusters where the public Kubernetes API endpoint is in an Oracle-managed tenancy, the`use vnics`,`use private-ips`, and`use public-ips`policy statements are unnecessary.

Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format`group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format`group id <group-ocid>`.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

## Create One or More Additional Policies for Groups

To enable users that are not members of the Administrators group to use Kubernetes Engine, create additional policies to enable the groups to which those users do belong to perform operations on cluster-related resources as follows:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select the tenancy's root compartment or an individual compartment containing cluster-related resources from the Compartment filter.
- Select Create Policy .
- 

Enter the following:
- Name: A name for the policy (for example,`acme-dev-team-oke-additional-policy`) that is unique within the compartment. If you are creating the policy in the tenancy's root compartment, the name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A friendly description. You can change this later if you want to.
- 

Statement: A suitable policy statement to allow existing groups to perform operations on cluster-related resources. In the example policy statements below, replace`<location>`with either`tenancy`(if you are creating the policy in the tenancy's root compartment) or`compartment <compartment-name>`(if you are creating the policy in an individual compartment):
- 

To enable users in the acme-dev-team group to automatically create and configure associated new network resources when creating new clusters in the 'Quick Create' workflow, policies must also grant the group:
- 

VCN_READ and VCN_CREATE permissions. Enter a policy statement like:

```

```

- 

SUBNET_READ and SUBNET_CREATE permissions. Enter a policy statement like:

```

```

- 

INTERNET_GATEWAY_CREATE permission. Enter a policy statement like:

```

```

- 

NAT_GATEWAY_CREATE permission. Enter a policy statement like:

```

```

- 

ROUTE_TABLE_UPDATE permission. Enter a policy statement like:

```

```

- 

SECURITY_LIST_CREATE permission. Enter a policy statement like:

```

```

- 

To enable users in the acme-dev-team-cluster-viewers group to simply list the clusters, enter a policy statement like:

```

```

- 

To enable users in the acme-dev-team-pool-admins group to list, create, update, and delete node pools, enter a policy statement like:

```

```

- 

To enable users in the acme-dev-team-auditors group to see details of operations performed on clusters, enter a policy statement like:

```

```

- 

To enable users in the acme-dev-team-sgw group to create a service gateway to enable worker nodes to access other resources in the same region without exposing data to the public internet, enter a policy statement like:

```

```

- 

To enable users in the acme-dev-team group to access clusters using Cloud Shell, enter a policy statement like:

```

```

Note that to access clusters using Cloud Shell, you'll also need to set up the kubeconfig file appropriately (see[Setting Up Cloud Shell Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengdownloadkubeconfigfile.htm#cloudshelldownload)). For more information about Cloud Shell, see[Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/devcloudshellintro.htm).
- To enable users in the acme-dev-team group to select master encryption keys and vaults in the Vault service when creating and modifying clusters using the Console:

```

```

```

```

- To enable users in the acme-dev-team group to use capacity reservations:

```

```

For more information, see[Using Capacity Reservations to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengmakingcapacityreservations.htm)
- To enable users in the acme-dev-team group to use metrics (for example, to observe the condition of nodes in a Kubernetes cluster):

```

```

For more information, see[Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Reference/contengmetrics.htm).
Note  
  

Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format`group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format`group id <group-ocid>`.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

## Create Policy for Larger Clusters

When creating larger clusters, you must allow the Kubernetes Engine service to manage IP address resources used by the cluster endpoint. For clusters above 5,000 nodes, Kubernetes Engine might provision additional IP addresses in the cluster endpoint subnet. See[Endpoint Subnet Capacity](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic-Create_Policies_for_Larger-Clusters__section-larger-cluster-polices-endpoint-subnet-capacity).

Add the following service policy statements, as applicable:
- Required for IPv4 clusters:

```

```

- 

Required for IPv4 clusters that use a public cluster endpoint subnet:

```

```

- 

Required for clusters that use dual-stack networking.

```

```

For a more restrictive policy, scope the policy statements to the cluster compartment rather than granting access across the tenancy, in the format:

```

```

```

```

```

```

If the policy must be attached at the tenancy/root level, use a supported compartment condition, in the format:

```

```

```

```

```

```

### Endpoint Subnet Capacity

For clusters above 5,000 nodes, Kubernetes Engine might provision additional IP addresses in the cluster endpoint subnet. Plan for at least five additional endpoint address slots for Kubernetes Engine in that subnet, plus any addresses required by your own resources. The underlying IP resources depend on the cluster networking configuration:
- For IPv4 private endpoints, each additional endpoint address requires an available private IPv4 address;
- For IPv4 public endpoints, each additional endpoint address requires an available private IPv4 address and public IPv4 address;
- For dual-stack endpoints, each additional endpoint address requires available IPv4 and IPv6 addresses.

## Create Policy to Set Up and Use Virtual Nodes

Administrator users do not require additional permissions to create and use clusters with virtual nodes and virtual node pools.

To enable non-administrator users to use virtual nodes, you must set up an additional policy to give such users the required permissions. For more information about the policy statements to enter, see[Required IAM Policies for Using Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengvirtualnodes-Required_IAM_Policies.htm).

## Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems

To specify a particular user-managed master encryption key from the[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)service to encrypt data in boot volumes, block volumes, and/or file systems, you have to create a policy to allow access to that master encryption key. For more information about specifying user-managed encryption keys:
- for boot volumes, see[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)and[Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengmodifyingnodepool.htm)as appropriate.
- for block volumes, see[Encrypting Data At Rest and Data In Transit with the Block Volume Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_Encrypting_data)
- for file systems, see[Encrypting Data At Rest and Data In Transit with the File Storage Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_new_FSS-Encrypting_data.dita)

Note that before you can create the policy, you have to know the master encryption key's OCID (see[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm)).

To create a policy to allow access to a user-managed master encryption key:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select the tenancy's root compartment or an individual compartment containing cluster-related resources from the Compartment filter.
- Select Create Policy , follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example,`acme-oke-keys-policy`).
- 

For boot volumes: To use a master encryption key from the Vault service to encrypt data in boot volumes, enter the following policy statements to grant access to the master encryption key:

```

```

```

```

```

```

```

```

where:
- `<group-name>`is a group to which you belong. Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format`group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format`group id <group-ocid>`.
- `<compartment-name>`is the name of the compartment containing the master encryption key.
- `<key-OCID>`is the OCID of the master encryption key in Vault.

For example:
```

```

Note  
  

After August 15, 2024, create the`Allow any-user...`policy statement as shown, namely:
```

```

Note that before August 15, 2024, you had to define the following`Allow service oke...`policy statement:
```

```

If such an`Allow service oke...`policy statement already exists, keep this existing policy statement, and create the new`Allow any-user...`policy statement in addition to the existing policy statement.
- 

For block volumes: To use a master encryption key from the Vault service to encrypt data in block volumes, enter policy statements to grant access to the master encryption key in the format:

```

```

```

```

where:
- `<compartment-name>`is the name of the compartment containing the master encryption key.
- `<key-OCID>`is the OCID of the master encryption key in Vault.

For example:

```

```

- 

For file systems: To use a master encryption key from the Vault service to encrypt data in file systems, enter policy statements to grant access to the master encryption key in the format:

```

```

```

```

where:
- 

`<dynamic-group-name>`is the name of the[dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm)of file systems in the compartment.

An example rule for the dynamic group follows:

```

```

Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format`dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format`dynamic-group id <dynamic-group-ocid>`.
- `<compartment-name>`is the name of the compartment containing the master encryption key.
- `<key_OCID>`is the OCID of the master encryption key in Vault.

For example:

```

```

-
