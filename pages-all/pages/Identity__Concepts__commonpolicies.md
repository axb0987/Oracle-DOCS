# Common Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm
- Fetched: 2026-09-05 02:14 CDT

# Common Policies

This section includes some common policies you might want to use in your organization.
Note  
  

These policies use example group and compartment names. Make sure to replace them with your own names.

[Let the Help Desk manage users](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create, update, and delete users and their credentials. It does not include the ability to put users in groups.

Where to create the policy: In the tenancy, because users reside in the tenancy.

```

```

[Let auditors inspect your resources](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to list the resources in all compartments. Be aware that:
- The operation to list IAM policies includes the contents of the policies themselves
- The list operations for Networking resource-types return all the information (for example, the contents of security lists and route tables)
- The operation to list instances requires the`read`verb instead of`inspect`, and the contents include the user-provided metadata.
- The operation to view Audit service events requires the`read`verb instead of`inspect`.

Where to create the policy: In the tenancy. Because of the concept of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2), auditors can then inspect both the tenancy and all compartments beneath it. Or you could choose to give auditors access to only specific compartments if they don't need access to the entire tenancy.

```

```

[Let Autonomous Recovery Service admins manage protected databases, recovery service subnets, and protection policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage Autonomous Recovery Service resources in all compartments:
- 

Protected databases
- 

Recovery service subnets
- Protection policies

This policy is applicable if you want to allow a single set of Recovery Service admins to manage all Recovery Service resources in all the compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to Recovery Service resources in a particular compartment, specify the required compartment instead of the tenancy.

```

```

[Let compliance admins manage protection policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage protection policies in all compartments.

This policy is applicable if you want to allow a single set of compliance admins to manage Protection Policies in all the compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to protection policies in a particular compartment, specify the required compartment instead of the tenancy.

```

```

[Let network admins manage a cloud network](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage all components in Networking. This includes cloud networks, subnets, gateways, virtual circuits, security lists, route tables, and so on. If the network admins need to launch instances to test network connectivity, see[Let users launch compute instances](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances).

Where to create the policy: In the tenancy. Because of the concept of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2), NetworkAdmins can then manage a cloud network in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy.

```

```

For policies used in connecting a DRG to VCNs and DRGs in other regions and tenancies, see[IAM Policies for Routing Between VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/drg-iam.htm).

[Let network admins manage load balancers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage all components in Load Balancer. If the group needs to launch instances, see[Let users launch compute instances](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances).

Where to create the policy: In the tenancy. Because of the concept of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2), NetworkAdmins can then manage load balancers in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy.

```

```

If the group wants to manage load balancers and network load balancers, additional policies to use the associated networking resources are required:

```

```

If a particular group needs to update existing load balancers (for example, modify the backend set) but not create or delete them, use this statement:

```

```

[Let network admins manage private service access](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage Private Service Access in Networking.

Where to create the policy: In the tenancy. Because of the concept of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2),`NetworkAdmins`can then manage Private Service Access (PSA) in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy.

```

```

PSA is part of the`virtual-network-family`so the following policy also allows the same ability.

```

```

The next example shows a way to limit access to Object Storage resources in the`objprivate`compartment. With this deny policy, PSA endpoints can still reach this compartment's Object Storage resources. Access to these resources isn't allowed by way of the Internet, Service Gateway or even in the Console.

```

```

[Let users launch compute instances](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do everything with instances launched into the cloud network and subnets in compartment XYZ, and attach/detach any existing volumes that already exist in compartment ABC. The first statement also lets the group create and manage instance images in compartment ABC. If the group doesn't need to attach or detach volumes, you can delete the`volume-family`statement.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartments (ABC and XYZ) to have control over the individual policy statements for their compartments, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

To allow users to create new cloud networks and subnets, see[Let network admins manage a cloud network](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network).

To allow users to determine whether capacity is available for a specific shape before creating an instance, add the following statement to the policy:

```

```

[Let users launch compute instances from a specific custom image](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to launch instances into the cloud network and subnets in compartment XYZ using only the specified custom image. The policy also includes the ability to attach/detach any existing volumes that already exist in compartment ABC. If the group doesn't need to attach/detach volumes, you can delete the`volume-family`statement.

To specify multiple custom images, you can use[conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm#five).

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartments (ABC and XYZ) to have control over the individual policy statements for their compartments, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

[Let image admins manage custom images](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do everything with custom images and compute instances. Also includes the ability to do everything with Object Storage buckets, objects, and namespaces in compartment Y (for creating images from objects and creating pre-authenticated requests to images); to attach/detach any existing volumes in compartment X; and to launch instances into the cloud network and subnets in compartment Z (for creating new instances to base an image on). If the group doesn't need to attach/detach volumes, you can delete the`volume-family`statement.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartments (X, Y, and Z) to have control over the individual policy statements for their compartments, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

[Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with instance configurations, instance pools, and cluster networks in all compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the instance configurations, instance pools, and cluster networks in a particular compartment, specify that compartment instead of the tenancy.

```

```

If a group needs to create instance configurations using existing instances as a template, and uses the API, SDKs, or command line interface (CLI) to do this, add the following statements to the policy:

```

```

If a particular group needs to start, stop, or reset the instances in existing instance pools, but not create or delete instance pools, use this statement:

```

```

If resources used by the instance pool contain default tags, add the following statement to the policy to give the group permission to the tag namespace`Oracle-Tags`:
```

```

If the instance configuration used by the instance pool launches instances in a capacity reservation, add the following statement to the policy:
```

```

If the boot volume used in the instance configuration to create an instance pool is encrypted with a KMS key then, add the following statement to the policy
```

```

[Let users manage Compute autoscaling configurations](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create, update, and delete autoscaling configurations.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the autoscaling configurations in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users list and subscribe to images from the Partner Image catalog](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to list and create subscriptions to images in the Partner Image catalog. It does not include the ability to create instances using images from the Partner Image catalog (see[Let users launch compute instances](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)).

Where to create the policy: In the tenancy. To reduce the scope of access to just creating subscriptions in a particular compartment, specify that compartment instead of the tenancy in the third statement.

```

```

[Let users create Compute instance console connections](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create instance console connections.

Where to create the policy: In the tenancy.

```

```

[Let users manage Compute dedicated virtual machine hosts](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create, update, and delete dedicated virtual machine hosts as well as launch instances on dedicated virtual machine hosts.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the dedicated virtual machine hosts and instances in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users launch Compute instances on dedicated virtual machine hosts](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to launch instances on dedicated virtual machine hosts.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the dedicated virtual machine hosts and instances in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with block storage volumes, volume backups, and volume groups in all compartments with the exception of copying volume backups across regions. This makes sense if you want to have a single set of volume admins manage all the volumes, volume backups, and volume groups in all the compartments. The second statement is required in order to attach/detach the volumes from instances.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the volumes/backups and instances in a particular compartment, specify that compartment instead of the tenancy.

```

```

If the group needs to also copy volume backups and boot volume backups across regions, add the following statements to the policy:
```

```

[Let volume backup admins manage only backups](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with volume backups, but not create and manage volumes themselves. This makes sense if you want to have a single set of volume backup admins manage all the volume backups in all the compartments. The first statement gives the required access to the volume that is being backed up; the second statement enables creation of the backup (and the ability to delete backups). The third statement enables the creation and management of user defined backup policies; the fourth statement enables assignment and removal of assignment of backup policies.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the volumes and backups in a particular compartment, specify that compartment instead of the tenancy.

```

```

If the group will be using the Console, the following policy gives a better user experience:

```

```

The last two statements are not necessary in order to manage volume backups. However, they enable the Console to display all the information about a particular volume and the available backup policies.

[Let boot volume backup admins manage only backups](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with boot volume backups, but not create and manage boot volumes themselves. This makes sense if you want to have a single set of boot volume backup admins manage all the boot volume backups in all the compartments. The first statement gives the required access to the boot volume that is being backed up; the second statement enables creation of the backup (and the ability to delete backups). The third statement enables the creation and management of user defined backup policies; the fourth statement enables assignment and removal of assignment of backup policies.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the boot volumes and backups in a particular compartment, specify that compartment instead of the tenancy.

```

```

If the group will be using the Console, the following policy gives a better user experience:

```

```

The last two statements are not necessary in order to manage volume backups. However, they enable the Console to display all the information about a particular boot volume and the available backup policies.

[Let users create a volume group](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create a volume group from a set of volumes.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the volumes and volume groups in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users clone a volume group](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to clone a volume group from an existing volume group.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the volumes and volume groups in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users create a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create a volume group backup.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the volumes/backups and volume groups/volume group backups in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users restore a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create a volume group by restoring a volume group backup.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the volumes/backups and volume groups/volume group backups in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users create, manage, and delete file systems](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create, manage, or delete a file system or file system clone. Administrative functions for a file system include the ability to rename or delete it or disconnect from it.

Where to create the policy : In the tenancy, so that the ability to create, manage, or delete a file system is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of these administrative functions to file systems in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users create file systems](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create a file system or file system clone.

Where to create the policy : In the tenancy, so that the ability to create a file system is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of these administrative functions to file systems in a particular compartment, specify that compartment instead of the tenancy.

```

```

The second statement is required when users create a file system using the Console. It enables the Console to display a list of mount targets that the new file system can be associated with.

[Let Object Storage admins manage buckets and objects](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with Object Storage buckets and objects in all compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the buckets and objects in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users write objects to Object Storage buckets](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to write objects to any Object Storage bucket in compartment ABC (imagine a situation where a client needs to regularly write log files to a bucket). This consists of the ability to list the buckets in the compartment, list the objects in a bucket, and create a new object in a bucket. Although the second statement gives broad access with the`manage`verb, that access is then scoped down to only the`OBJECT_INSPECT`and`OBJECT_CREATE`permissions with the condition at the end of the statement.

Where to create the policy : The easiest approach is to put this policy in the tenancy. If you want the admins of compartment ABC to have control over the policy, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

Access limited to a specific bucket : To limit access to a specific bucket in a particular compartment, add the condition`where target.bucket.name=' <bucket_name> '`. The following policy allows the user to list all the buckets in a particular compartment, but they can only list the objects in and upload objects to BucketA:

```

```

Access limited to buckets with a specific defined tag : To limit access to the buckets with a specific tag in a given compartment, add the condition`where target.bucket.tag.<TagNamespace>.<TagKeyDefinition>='< TagValue> '`. The following policy allows the user to list all buckets in compartment ABC, however, they can only list the objects in and upload objects to the bucket with the tag`MyTagNamespace.TagKey='MyTagValue'`:

```

```

For more information about using conditions, see[Advanced Policy Features](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Advanced_Policy_Features).

[Let users download objects from Object Storage buckets](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to download objects from any Object Storage bucket in compartment ABC. This consists of the ability to list the buckets in the compartment, list the objects in a bucket, and read existing objects in a bucket.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of compartment ABC to have control over the policy, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

Access limited to a specific bucket: To limit access to a specific bucket in a particular compartment, add the condition`where target.bucket.name=' <bucket_name> '`. The following policy allows the user to list all buckets in a particular compartment, but they can only read the objects in and download from BucketA:

```

```

Access limited to buckets with a specific defined tag

To limit access to the buckets with a specific tag in a given compartment, add the condition`where target.bucket.tag.<TagNamespace>.<TagKeyDefinition>='< TagValue> '`. The following policy allows the user to list all buckets in compartment ABC, however, they can only read the objects in and download the objects from the bucket with the tag`MyTagNamespace.TagKey='MyTagValue'`:

```

```

For more information about using conditions, see[Advanced Policy Features](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Advanced_Policy_Features).

[Let users access customer data in Object Storage encrypted with customer-managed key](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create customer managed key. This consists of the ability to set up policies to access data encrypted with customer managed key.

```

```

The last statement in the above policy example is region specific. That means customers need to repeatedly write this statement for each region. To convenience policy setting, customers can use the following policy setting example:

```

```

[Let users have full access to a folder in an Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability of a group of users to do all actions to an Object Storage bucket and its objects.

Where to create the policy: In the tenancy where the users reside.
```

```

[Let users have read-only access to a folder in an Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability of a group of users to have read-only access to an Object Storage bucket and its objects.

Where to create the policy: In the tenancy where the users reside.
```

```

[Let users have write-once access to a folder in an Object Storage bucket (no read or delete)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability of a group of users to have write-only access to a folder of objects within a bucket Users can't view a list of objects in the bucket, nor delete any objects it contains.

Where to create the policy: In the tenancy where the users reside.
```

```

[Let users have read-write access to a folder in an Object Storage bucket (no listing or overwriting)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability of a group of users to have read and write access to a folder of objects within an Object Storage bucket. Users can't generate a list of objects in the folder, nor overwrite any existing objects in the folder.

Where to create the policy: In the tenancy where the users reside.
```

```

[Let a user have all access to an object pattern in an Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability of a specified user to have full access to all objects that match a specified pattern within an Object Storage bucket.

Where to create the policy: In the tenancy where the user resides.
```

```

[Let database admins manage Oracle Cloud database systems](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with the following system types and their associated resources in all compartments:
- Exadata Database Service on Dedicated Infrastructure instances
- bare metal DB systems
- virtual machine DB systems

This makes sense if you want to have a single set of database admins manage all the bare metal, virtual machine, and Exadata systems in all the compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the database systems in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let database admins manage Exadata Database Service on Cloud@Customer instances](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with the Exadata Database Service on Cloud@Customer resources in all compartments. This makes sense if you want to have a single set of database admins manage all the Exadata Database Service on Cloud@Customer systems in all the compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the Exadata Database Service on Cloud@Customer

systems in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let database admins manage MySQL Database resources](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access:

Ability to do all things with MySQL Database and MySQL HeatWave resources in all compartments. Creating and managing MySQL Database DB Systems also requires limited access to VCNs, Subnets, and Tag namespaces in the tenancy.
Where to create the policy: In the tenancy, granting access to all compartments by[Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../policieshow/Policy_Inheritance.htm).

```

```

[Let database admins manage Oracle Cloud external database resources](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with the following OCI[external database](https://docs.oracle.com/iaas/external-database/index.html)resources in all compartments:
- OCI external container database resources
- OCI external pluggable database resources
- OCI external non-container database resources
- OCI external database connectors

This makes sense if you want to have a single set of database admins manage all the OCI external database resources in all the compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the OCI external database resources in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let database and fleet admins manage Autonomous AI Databases](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with Autonomous AI Database instances in all compartments. Applicable if you want to have a single set of database administrators manage all the Autonomous AI Database databases in all the compartments.

Where to create the policy: In the tenancy, so that the access is granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the Autonomous AI Databases in a particular compartment, specify that compartment instead of the tenancy.

Example 1: For[User Roles Associated with Autonomous AI Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/#GUID-B5518C12-0362-4A98-AB35-3CB84AC83F31). Enables Autonomous AI Database fleet administrator access to the any[workload types](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#db-admins-manage-adb__workload_types), and to manage the following dedicated Exadata infrastructure resources: Autonomous Container Databases and Autonomous VM Clusters.

```

```

Tip  
  
The`autonomous-database-family`aggregate resource-type does not cover the`cloud-exadata-infrastructures`resource-type needed to provision Autonomous AI Database on dedicated Exadata infrastructure. See[Policy Details for Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/ecs-policy-details.html#GUID-A967AE72-E18C-40ED-A928-D865618E9B9E)for information on the cloud Exadata infrastructure permissions. See[Let database admins manage Oracle Cloud database systems](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#db-admins-manage-db-systems)for a sample policy covering cloud Exadata infrastructure resources.

If you must restrict access to the Autonomous VM Cluster and Autonomous Container Database resource types (applicable only to dedicated Exadata infrastructure), then you can do so by creating separate policy statements for database administrators that allow access to only Autonomous AI Databases and their backups. Because a policy statement can only specify one resource type, you must create separate statements for the database and backup resources.

Example 2: For[Autonomous AI Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/). Enables Autonomous AI Database database administrators access to databases and backups of the various workload types, but denies access to Autonomous Container Databases, Autonomous VM Clusters, and Cloud Exadata Infrastructure resources.

```

```

```

```

To reduce the scope of access for databases and backups to either the a specific workload type, use a`where`clause.

Example 3: For[Autonomous AI Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/). Limits Autonomous AI Database access to databases and backups for a specific workload type.

```

```

```

```

In the preceding code examples,`workload_type`is one of the strings listed in the following table.

Autonomous AI Database Workload Type Strings
Database Workload Type workload_type String for Policies
Autonomous AI Transaction Processing`OLTP`
Autonomous AI Lakehouse`DW`
Autonomous AI JSON Database`AJD`
Oracle APEX Application Development`APEX`

[Let security admins manage vaults, keys, and secrets](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with the Vault service in all compartments. This makes sense if you want to have a single set of security admins manage all the vaults, keys, and secret components (including secrets, secret versions, and secret bundles) in all compartments.

Where to create the policy: In the tenancy, so that access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the vaults, keys, and secret components in a particular compartment, specify that compartment instead of the tenancy. To reduce the scope of access to just vaults, keys, or secret components, include only the policy statement that pertains to the respective individual or aggregate resource-type, as appropriate.

```

```

[Let security admins manage all keys in a specific vault in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with keys in a specific vault in compartment ABC.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

[Let security admins use a specific key in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to list, view, and perform cryptographic operations with a specific key in a compartment.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

[Let a user group delegate key usage in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to associate an Object Storage bucket, Block Volume volume, File Storage file system, Kubernetes cluster, or Streaming stream pool with a specific key authorized for use in a specific compartment. With this policy, a user in the specified group does not have permission to use the key itself. Rather, by association, the key can be used by Object Storage, Block Volume, File Storage, Kubernetes Engine, or Streaming on behalf of the user to:
- Create or update an encrypted bucket, volume, or file system and to encrypt or decrypt data in the bucket, volume, or file system.
- Create Kubernetes clusters with encrypted Kubernetes secrets at rest in the etcd key-value store.
- Create a stream pool to encrypt data in the streams in the stream pool.

This policy requires that you also have a companion policy that lets Object Storage, Block Volume, File Storage, Kubernetes Engine, or Streaming use the key to perform cryptographic operations.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

[Let a dynamic group delegate key usage in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to associate a Block Volume volume with a specific key authorized for use in a specific compartment. With this policy, a user in the dynamic group doesn't have permission to use the key itself. Rather, by association, the key can be used by Block Volume on behalf of the user to create or update an encrypted volume, and to encrypt or decrypt data in the volume.

This policy requires that you also have a companion policy that lets Block Volume use the key to perform cryptographic operations.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

[Let Block Volume, Object Storage, Kubernetes Engine, and Streaming services encrypt and decrypt volumes, volume backups, buckets, Kubernetes secrets, and stream pools](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to list, view, and perform cryptographic operations with all keys in compartment ABC. Because Object Storage is a regional service, it has regional endpoints. As such, you must specify the regional service name for each region where you're using Object Storage with Vault encryption. This policy also requires that you have a companion policy that allows a user group to use the delegated key that Object Storage, Block Volume, Kubernetes Engine, or Streaming will use.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

For Object Storage, replace &lt;region_name&gt; with the appropriate region identifier, for example:
- 

objectstorage-us-phoenix-1
- 

objectstorage-us-ashburn-1
- 

objectstorage-eu-frankfurt-1
- 

objectstorage-uk-london-1
- objectstorage-ap-tokyo-1

To determine the region name value of an Oracle Cloud Infrastructure region, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

For Kubernetes Engine, the service name used in the policy is`oke`.

For Streaming, the service name used in the policy is`streaming`.

[Let security admins manage all secrets in a specific vault in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with secrets in a specific vault in compartment ABC.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).

```

```

[Let users read, update, and rotate all secrets](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to read, update, and rotate all secrets in any vault in the tenancy.

Where to create the policy: In the tenancy, so that access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the vaults, keys, and secrets in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users manage their own passwords and credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

No policy is required to let users manage their own credentials. All users can change and reset their own passwords, manage their own API keys, and manage their own auth tokens. For more information, see[User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#User_Credentials).

[Let a compartment admin manage the compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage all aspects of a particular compartment. For example, a group called A-Admins could manage all aspects of a compartment called Project-A, including writing additional policies that affect the compartment. For more information, see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3). For an example of this kind of setup and additional policies that are useful, see[Example Scenario](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#Example).

Where to create the policy: In the tenancy.

```

```

[Restrict admin access to a specific region](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage resources in a specific region. Remember that IAM resources must be managed in the home region. If the specified region is not the home region, then the Admin will not be able to manage IAM resources. For more information about the home region, see[Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../Tasks/managingregions.htm#Managing_Regions).

Where to create the policy: In the tenancy.

```

```

The preceding policy allows PHX-Admins to manage all aspects of all resources in US West (Phoenix).

Members of the PHX-Admins group can only manage IAM resources if the tenancy's home region is US West (Phoenix).

[Restrict user access to view only summary announcements](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to view the summary versions of announcements about the operational status of Oracle Cloud Infrastructure services.

Where to create the policy: In the tenancy.

```

```

The preceding policy allows AnnouncementListers to view a list of summary announcements.

[Let users view details of announcements](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to view the details of announcements about the operational status of Oracle Cloud Infrastructure services.

Where to create the policy: In the tenancy.

```

```

The preceding policy allows AnnouncementReaders to view a list of summary announcements and the details of specific announcements.

[Let streaming admins manage streaming resources](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to do all things with the Streaming service in all compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let streaming users publish messages to streams](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to produce messages to streams with the Streaming service in all compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let streaming users publish messages to a specific stream](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to produce messages to a stream with the Streaming service.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let streaming users publish messages to a stream in a specific stream pool](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to produce messages to a stream with the Streaming service.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let streaming users consume messages from streams](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to consume messages from streams with the Streaming service in all compartments.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users list metric definitions in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to list metric definitions in a specific compartment. For more information, see[Listing Metric Definitions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm).

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the metric definitions in a particular compartment, specify that compartment instead of the tenancy.
```

```

[Let users query metrics in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to query metrics for supported resources in a specific compartment. For more information, see[Creating a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the metrics in a particular compartment, specify that compartment instead of the tenancy.
```

```

[Restrict queries to a specific metric namespace](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to query metrics for resources under a specific metric namespace . For more information, see[Creating a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to the specified metric namespace to just within a particular compartment, specify that compartment instead of the tenancy.
```

```

[Let users publish custom metrics](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to publish custom metrics under a specific metric namespace to the Monitoring service, as well as view metric data, create alarms and topics, and use streams with alarms. For more information about publishing custom metrics, see[Publishing Custom Metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm).

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just metrics in a particular compartment, specify that compartment instead of the tenancy.
Note  
  
To limit the group to the permissions required for selecting streams, replace`use streams`with`{STREAM_READ, STREAM_PRODUCE}`.
```

```

[Let instances make API calls to access monitoring metrics in the tenancy](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to call the Monitoring API for access to monitoring metrics . The instances on which API requests originate must be members of the dynamic group indicated in the policy. For more information about compute instances calling APIs, see[Calling Services from an Instance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../Tasks/callingservicesfrominstances.htm#Calling_Services_from_an_Instance).

Where to create the policy: In the tenancy.

```

```

[Let users view alarms](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to[get alarm details](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm.htm)and[get alarm history](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm-history.htm). Does not include the ability to create alarms or to create or delete topics.

Where to create the policy: In the tenancy. Because of the concept of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2), the group can then view alarms in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy.
```

```

[Let users manage alarms](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to[manage alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm), using streams and existing topics for notifications. Does not include the ability to create or delete topics.

Where to create the policy: In the tenancy. Because of the concept of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2), the group can then view and create alarms in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy.
```

```

[Let users manage alarms and create topics](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to[manage alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm), including[creating topics (and subscriptions) for notifications](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm)(and[using streams for notifications](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-stream.htm)).

Where to create the policy: In the tenancy. Because of the concept of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2), the group can then view and create alarms in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy.
```

```

[Let users access usage reports](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to view usage reports for your tenancy. For more information about usage reports, see[Cost and Usage Reports Overview](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm).

Where to create the policy: This is a special cross-tenancy policy and must be created in the tenancy. For more information, see[Accessing Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/usagereportsoverview.htm#Accessing_Cost_and_Usage_Reports).

```

```

[Let users analyze costs](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to see costs for the tenancy. See[Checking Your Expenses and Usage](https://docs.oracle.com/iaas/Content/Billing/Concepts/costs.htm).

Where to create the policy: In the tenancy so that users in the &lt;Example_Group&gt; can see costs for the entire account.

```

```

[Allow a group to manage topics and subscriptions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to get, create, update, and delete topics in the tenancy, as well as move topics to different compartments in the tenancy. Also includes the ability to create subscriptions in the tenancy and to publish messages (broadcast notification messages) to all subscriptions in the tenancy.

Where to create the policy: In the tenancy.

```

```

[Allow a group to manage subscriptions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to list, create, update, and delete subscriptions for topics in the tenancy. Ability to move subscriptions to different compartments in the tenancy.

Where to create the policy: In the tenancy.

```

```

[Allow a group to publish messages to topics](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to broadcast notification messages to all subscriptions in the tenancy, as well as list, create, update, and delete subscriptions in the tenancy.

Where to create the policy: In the tenancy.

```

```

[Let users create, deploy, and manage functions and applications using Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to create, deploy, and manage OCI Functions applications and functions using Cloud Shell. These policy statements give the group access to Cloud Shell, repositories in Oracle Cloud Infrastructure Registry, logs, metrics, functions, networks, and tracing.

Where to create the policy: In the tenancy, so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the resources in a particular compartment, you can specify the compartment instead of the tenancy for most policy statements. However,`to use cloud-shell`,`to manage repos`, and`to read objectstorage-namespaces`must always be scoped to the tenancy.

```

```

[Let users list Events rules in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to list Events rules.

Where to create the policy: In the tenancy.

```

```

The preceding policy allows RuleReaders to list rules in the tenancy.

[Let admins manage Events rules in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage Events rules, including creating, deleting and updating rules.

Where to create the policy: In the tenancy.

This line gives the user inspect access to resources in compartments to select actions.

```

```

This line gives the user access to defined tags to apply filter tags to rules.

```

```

These lines give the user access to Streaming resources for actions

```

```

These lines give the user access to Functions resources for actions.

```

```

This line give the user access to Notifications topics for actions.

```

```

This line gives the user manage access to rules for Events.

```

```

[Allow a group to access all of Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Read-only access to all of Cloud Guard. In the example policy, the group is "CloudGuard_ReadOnly."

```

```

[Allow a group to access Cloud Guard problems](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Read-only access to Cloud Guard problems. In the example policy, the group is "CloudGuard_ReadOnlyProblems."

```

```

[Allow a group to access Cloud Guard detector recipes](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Read-only access to Cloud Guard detector recipes. In the example policy, the group is "CloudGuard_ReadOnlyDetectors."

```

```

[Allow a group to access Cloud Guard in a single compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Read-only access to Cloud Guard in a single compartment. In the example policy, the group is "CloudGuard_ReadOnly_SingleCompartment" and the compartment name is "cgDemo_RestrictedAccess."

```

```

[Allow a group to administer all aspects of Full Stack Disaster Recovery operations in the entire tenancy](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access : Ability to allow a group to be superusers for all Full Stack Disaster Recovery operations.
Where to create the policy : In the tenancy
```

```

[Allow a group to create Full Stack Disaster Recovery configurations and execute Prechecks](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access : Ability to allow a group to create Disaster Recovery (DR) protection groups, DR plans, and execute Prechecks but not actually create DR plan executions.

Where to create the policy : In the compartment.

```

```

[Allow a group of users to create Full Stack Disaster Recovery configurations in a specific compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access : Ability to allow a group to create Disaster Recovery (DR) protection groups and DR plans but not create any DR plan executions or Prechecks.
Where to create the policy : In the compartment.

```

```

[Allow Object Storage to use Keys in Vault](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Other services to integrate with KMS to use KMS keys.

Where to create the policy: The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment.

Example :`Allow service objectstorage-< region > to use keys in compartment ABC where target.key.id = '<key_OCID>'`

```

```

[Let security admins manage all bastions and sessions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage all resources in the Bastion service in all compartments. This makes sense if you want to have a single set of security admins manage all bastions and sessions in all compartments.

Where to create the policy: In the tenancy, so that access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the bastions and bastion sessions in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let security admins manage bastion sessions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage all sessions on all bastions and in all compartments, including creating, connecting to, and terminating sessions.

Where to create the policy: In the tenancy, so that access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the bastion sessions in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let security admins manage Bastion sessions for a specific target host in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage sessions on a bastion in a specific compartment, and only for sessions that provide connectivity to a specific Compute instance.

Where to create the policy: In the tenancy, so that access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2).

```

```

[Let security admins configure scanning of instances in all compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to configure Oracle Cloud Infrastructure Vulnerability Scanning Service to scan all Compute instances in all compartments, and to view the scanning results. Consider this policy if you want to have a single set of security administrators configure vulnerability scanning for all instances.

Where to create the policy: In the tenancy, which grants access to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the Compute instances in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Let users view vulnerability scan results in all compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to view the results of scanning Compute instances in all compartments for security vulnerabilities. Consider this policy if you have a dedicated team responsible for reviewing or auditing the security of your entire tenancy.

Where to create the policy: In the tenancy, which grants access to all compartments by way of[policy inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the scanning results in a particular compartment, specify that compartment instead of the tenancy.

```

```

[Allow a group to manage connectors](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to list, create, update, and delete connectors in the tenancy. Ability to move connectors to different compartments in the tenancy.

Where to create the policy: In the tenancy.

```

```

See also[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/sch_security.htm#iam-policies)(Securing Connector Hub).

[Allow a group to call Ops Insights ingest operations at tenancy](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to call[Ops Insights](https://docs.oracle.com/iaas/operations-insights/home.htm)ingest operations at the tenancy level only.

Where to create the policy: In the tenancy.

```

```

[Let users create and delete workspaces without networking (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to create, delete, and modify workspaces within a compartment.

```

```

[Let users create and delete workspaces with networking (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to create, delete, and modify workspaces within a virtual network.

```

```

[Let users and resource principal access and use Object Storage for a given workspace (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to create and use Object Storage data assets within all workspaces.

```

```

To give access to an individual workspace, specify the OCID for the workspace where you want to allow access. For example:

```

```

[Let users and resource principal access and use autonomous databases as a target for a given workspace (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to create and use autonomous database data assets within all workspaces.

```

```

To give access to an individual workspace, specify the OCID for the workspace where you want to allow access. For example:

```

```

[Let users search objects within a workspace (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to search the components of Data Integration in a given workspace.

This policy must be applied at the tenancy (root compartment) level.

```

```

[Let users move workspaces to a new compartment (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to move workspaces to a new compartment.

```

```

[Let users publish tasks to the OCI Data Flow service (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to publish the different tasks within all workspaces to the OCI Data Flow service.

```

```

To give access to an individual workspace, specify the OCID for the workspace where you want to allow access. For example:

```

```

[Let users access the OCI Vault service for a given workspace (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to use OCI Vault secrets within all workspaces.

```

```

To give access to an individual workspace, specify the OCID for the workspace where you want to allow access. For example:

```

```

[Let admins manage announcement subscriptions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Type of access: Ability to manage subscriptions that deliver announcements about the operational status of Oracle Cloud Infrastructure services.

Where to create the policy: The easiest approach is to put this policy in the tenancy. Because of the concept of policy inheritance, the group that you grant access can then manage announcement subscriptions in any compartment. To reduce the scope of access to announcements for a particular compartment, specify the compartment instead of the tenancy.

```

```

The preceding policy allows AnnouncementAdmins to view a list of summary announcements and the details of specific announcements.

[Let Resource Analytics Instances manage Resource Analytics resources (Resource Analytics)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to let Resource Analytics instances manage Resource Analytics resources, including resource metadata, compartments, autonomous databases, virtual network family, analytics instance work requests, and analytics instances.

```

```

[Let admins manage Resource Analytics Resources (Resource Analytics)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to let admins manage Resource Analytics resources, including the Resource Analytics family, virtual network family, autonomous data warehouses, and work requests.

```

```

[Let admins inspect the set of subscribed regions of the tenancy (Resource Analytics)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#)

Ability to let admins inspect the set of subscribed regions of the tenancy.

```

```
