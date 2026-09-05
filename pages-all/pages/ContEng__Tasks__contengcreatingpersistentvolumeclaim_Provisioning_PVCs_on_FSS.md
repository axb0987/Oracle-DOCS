# Provisioning PVCs on the File Storage Service
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm
- Fetched: 2026-09-05 01:54 CDT

# Provisioning PVCs on the File Storage Service

Find out how to provision persistent volume claims for clusters you've created using Kubernetes Engine (OKE) by mounting file systems from the File Storage service.

The Oracle Cloud Infrastructure File Storage service provides a durable, scalable, distributed, enterprise-grade network file system. You use the CSI volume plugin to connect clusters to file systems in the File Storage service.

You can use the File Storage service to provision persistent volume claims (PVCs) in two ways:
- By defining and creating a new storage class (optionally specifying the OCID of an existing mount target), and then defining and creating a new PVC based on the storage class. When you create the PVC, the CSI volume plugin dynamically creates both a new File Storage service file system, and a new persistent volume backed by the new file system. See[Provisioning a PVC on a New File System Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_FSS-Using-CSI-Volume-Plugin).
- By manually creating a file system and a mount target in the File Storage service, then defining and creating a PV backed by the new file system, and finally defining a new PVC. When you create the PVC, Kubernetes Engine binds the PVC to the PV backed by the File Storage service. See[Provisioning a PVC on an Existing File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_FSS_Oracle_managed_keys).

Note the following:
- When using the CSI volume plugin to dynamically create a new file system, do not manually update the properties of the new persistent volume that the CSI volume plugin creates.
- Any File Storage service file systems, mount targets, and exports dynamically created by the CSI volume plugin are given names starting with`csi-fss-`.
- Any File Storage service file systems, mount targets, and exports dynamically created by the CSI volume plugin appear in the Console. However, do not use the Console (or the Oracle Cloud Infrastructure CLI or API) to modify these dynamically created resources. Changes made to Oracle Cloud Infrastructure resources dynamically created by the CSI volume plugin are not reconciled with Kubernetes objects.
- After you create a storage class, you can’t change its parameters (for example, its ZPR security attributes). The CSI volume plugin applies storage class parameters when it creates File Storage resources for a persistent volume claim. The CSI volume plugin doesn’t update resources that it previously created if you later change or recreate a storage class with different parameters.
- If you delete a PVC bound to a PV backed by a file system created by the CSI volume plugin, the CSI volume plugin deletes the file system and PV it created. If the CSI volume plugin also created a new mount target (because you did not specify the OCID of an existing mount target in the storage class definition), the CSI volume plugin also deletes the mount target. Note that if you did specify the OCID of an existing mount target, the CSI volume plugin does not delete the mount target.
- Provisioning a PVC on a new file system dynamically created by the CSI volume plugin is available when clusters are running Kubernetes 1.22 or later. See[Provisioning a PVC on a New File System Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_FSS-Using-CSI-Volume-Plugin).
- Provisioning a PVC by binding it to a PV backed by an existing file system is available when clusters are running Kubernetes 1.18 or later. See[Provisioning a PVC on an Existing File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_FSS_Oracle_managed_keys).

## Support for Virtual Nodes and the File Storage Service

You can use persistent volumes backed by the File Storage service with pods running on managed, self-managed, and virtual nodes.

Use the procedures described in this topic to create storage classes, persistent volumes, and persistent volume claims for managed nodes, self-managed nodes, and virtual nodes. Data encryption is supported both in transit (TLS) and at rest, for managed nodes, self-managed nodes, and virtual nodes. And you can apply the same example Kubernetes manifests for managed nodes, self-managed nodes, and virtual nodes, unless otherwise noted.

When using virtual nodes, note the following:
- As with managed nodes and self-managed nodes, you must specify`ReadWriteMany`as the access mode for persistent volumes used by virtual nodes.
- In the case of virtual nodes, the virtual node provider (rather than the CSI volume plugin) handles ownership and permission changes that you configure with the`fsGroup`and`fsGroupChangePolicy`attributes in a pod’s`securityContext`. The virtual node provider propagates these attributes to the underlying runtime, where the volume ownership and permission behavior is applied. Both`Always`and`OnRootMismatch`are supported values for`fsGroupChangePolicy`

## Encrypting Data At Rest and Data In Transit with the File Storage Service

When using the File Storage service to provision PVCs, you specify in-transit encryption independently of at-rest encryption.

The File Storage service always encrypts data at rest, using Oracle-managed encryption keys by default. However, you have the option to specify at-rest encryption using your own master encryption keys that you manage yourself in the Vault service. How to specify at-rest encryption depends on whether you are provisioning a PVC on:
- a new file system dynamically created by the CSI volume plugin (see[Encrypting Data At Rest on a New File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_new-FSS-Encrypting_at_rest))
- an existing file system that you've manually created (see[Encrypting Data At Rest on an Existing File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_FSS_Encrypting_data_at_rest))

If you want to manage your own master encryption keys to encrypt data at rest, you have to:
- Create a suitable master encryption key in Vault (or obtain the OCID of such a key). See[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).
- Create a policy granting access to the master encryption key. See[Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic_Create_Policies_for_User_Managed_Encryption).

The File Storage service can optionally encrypt data in transit. If you specify in-transit encryption, data in transit is encrypted using a TLS (Transport Layer Security) certificate that is always Oracle-managed, regardless of whether data at rest is encrypted using Oracle-managed keys or using user-managed keys. In-transit encryption secures data being transferred between instances and mounted file systems using TLS v. 1.2 encryption. For more information about in-transit encryption and the File Storage service, see[Using In-transit TLS Encryption](https://docs.oracle.com/iaas/Content/File/Tasks/intransitencryption.htm). How to specify in-transit encryption depends on whether you are provisioning a PVC on:
- a new file system dynamically created by the CSI volume plugin (see[Encrypting Data In Transit on a New File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_new-FSS-Encrypting_in_transit))
- an existing file system that you've manually created (see[Encrypting Data In Transit on an Existing File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_FSS_Encrypting_data_in_transit))

Note that when using the File Storage service to provision PVCs, in-transit encryption is only supported when the compute instances hosting worker nodes are running Oracle Linux 7 and Oracle Linux 8.

## Provisioning a PVC on a New File System Using the CSI Volume Plugin

Note  
  
The following prerequisites apply when provisioning a PVC on a new file system dynamically created by the CSI volume plugin:
- Clusters must be running Kubernetes 1.22 or later to provision a PVC on a new file system dynamically created by the CSI volume plugin.
- 

Appropriate IAM policies must exist to enable the CSI volume plugin to create and manage File Storage resources. More specifically:
- A policy to create and/or manage file systems, mount targets, and export paths. For example:

```

```

- A policy to use VNICs, private IPs, private DNS zones, and subnets. For example:

```

```

- 

To specify ZPR security attributes for a mount target created by the CSI volume plugin, appropriate IAM policies must exist to enable the CSI volume plugin to use the specified security attribute namespace. For example:

```

```

- 

If the compartment to which a node pool, worker node subnet, file system, or mount target belongs, is different to the compartment to which a cluster belongs, IAM policies must exist to enable the CSI volume plugin to access the appropriate location. For example:

```

```

```

```

- 

To specify a particular user-managed master encryption key from the[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)service to encrypt data in file systems, appropriate IAM policies must exist to enable the CSI volume plugin to access that master encryption key. See[Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic_Create_Policies_for_User_Managed_Encryption).

To dynamically provision a PVC on a new file system dynamically created by the CSI volume plugin in the File Storage service:
- (Optional) Create a mount target in the File Storage service. See[Creating a Mount Target](https://docs.oracle.com/iaas/Content/File/Tasks/create-mount-target.htm).

The CSI volume plugin requires an active mount target (that is, a mount target with an assigned IP address) to create a new file system. If you do not create a mount target in advance, specify the subnet in which the CSI volume plugin is to create a new mount target when you define the storage class.
- Define a new storage class that uses the`fss.csi.oraclecloud.com`provisioner:
- Create a manifest file (for example, in a file named fss-dyn-st-class.yaml), specify a name for the new storage class, and specify values for required and optional parameters:
```

```

where:
- `name: <storage-class-name>`: Required. A name of your choice for the storage class.
- `availabilityDomain: <ad-name>`: Required. The name of the availability domain in which to create the new file system (and in which to create the new mount target, if an existing mount target OCID is not specified). For example,`US-ASHBURN-AD-1`. To find out the availability domain name to use, run the`oci iam availability-domain list`CLI command (or use the[ListAvailabilityDomains](https://docs.oracle.com/iaas/api/#/en/identity/latest/AvailabilityDomain/ListAvailabilityDomains)operation). For more information, see[Your Tenancy's Availability Domain Names](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#ad-names).
- `mountTargetOcid: <mt-ocid> | mountTargetSubnetOcid: <mt-subnet-ocid>`: Required. Either the OCID of an existing active mount target (`mountTargetOcid: <mt-ocid>`), or the OCID of a subnet in which to create a new mount target (`mountTargetSubnetOcid: <mt-subnet-ocid>`). Specify either`mountTargetOcid`or`mountTargetSubnetOcid`. If you specify both`mountTargetOcid`and`mountTargetSubnetOcid`in the storage class definition, the existing mount target specified by`mountTargetOcid`is used, and`mountTargetSubnetOcid`is ignored. For example:
- `mountTargetSubnetOcid: ocid1.subnet.oc1.iad.aaaaaaaa2xpk______zva`
- `mountTargetOcid: ocid1.mounttarget.oc1.iad.aaaaaaaa4np______fuy`
- `compartmentOcid: <compartment-ocid>`: Optional. The OCID of the compartment to which the new file system (and the new mount target, if an existing mount target OCID is not specified) is to belong. If not specified, defaults to the same compartment as the cluster. For example,`compartmentOcid: ocid1.compartment.oc1..aaaaaaaay______t6q`
- `kmsKeyOcid: <key-ocid>`: Optional. The OCID of a master encryption key that you manage, with which to encrypt data at rest. If not specified, data is encrypted at rest using encryption keys managed by Oracle. See[Encrypting Data At Rest on a New File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_new-FSS-Encrypting_at_rest). For example,`kmsKeyOcid: ocid1.key.oc1.iad.anntl______usjh`
- `exportPath: <path>`: Optional. The path in an export that uniquely identifies the file system within the mount target. The export path must start with a slash (/) followed by a sequence of zero or more slash-separated elements. For example,`/FileSystem1`. For more information, see[Paths in File Systems](https://docs.oracle.com/iaas/Content/File/Concepts/filesystempaths.htm).

If you include`exportPath: <path>`in a storage class definition, do not specify a path (either as a path or as the sub-path of an existing path) that already exists. If you specify a path that already exists, an error is returned because multiple file systems with the same mount target cannot have the same export path. Therefore, if you do include`exportPath: <path>`in the storage class definition, only use this storage class definition to create one file system.

If you don't include`exportPath: <path>`in the storage class definition, the path defaults to the display name of the file system created by the CSI volume plugin (starting with`/csi-fss-`).
- `exportOptions: "[{<options-in-json-format>}]"`Optional. A set of parameters (in valid JSON format) within the export that specifies the level of access granted to NFS clients when they connect to a mount target. An NFS export options entry within an export defines access for a single IP address or CIDR block range. For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/iaas/Content/File/Tasks/exportoptions.htm). If not specified, the following default is used:
```

```

- `encryptInTransit: "true"|"false"`: Optional. Indicates whether to encrypt data in transit. If you specify`"true"`, be sure to complete the setup steps described in[Encrypting Data In Transit on a New File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_new-FSS-Encrypting_in_transit). If not specified, defaults to`"false"`. For example,`encryptInTransit: "true"`.
- `oci.oraclecloud.com/initial-defined-tags-override: '{"<tag-namespace>": {"<tag-key>": "<tag-value>"}}'`Optional. Specifies a defined tag for the new file system. For example,`oci.oraclecloud.com/initial-defined-tags-override: '{"Operations": {"CostCenter": "42"}}'`

Note that to apply defined tags from a tag namespace belonging to one compartment to a filesystem resource belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See[Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm).
- `oci.oraclecloud.com/initial-freeform-tags-override: '{"<tag-key>": "<tag-value>"}'`Optional. Specifies a free-form tag for the new file system. For example,`oci.oraclecloud.com/initial-freeform-tags-override: '{"Department": "Finance"}'`
- `securityAttributes: '{"<security-attribute-namespace>":{"<security-attribute-key>":{"value":"<security-attribute-value>","mode":"enforce"}}}'`Optional. Specifies Zero Trust Packet Routing (ZPR) security attributes to apply to a new mount target created by the CSI volume plugin. For example,`securityAttributes: '{"<security-attribute-namespace>":{"<security-attribute-key>":{"value":"<security-attribute-value>","mode":"enforce"}}}'`

To apply ZPR security attributes to a mount target created by the CSI volume plugin, specify`mountTargetSubnetOcid`in the storage class definition. If you specify`mountTargetOcid`, the CSI volume plugin uses the existing mount target and does not create a new mount target with the specified security attributes.

Note that assigning ZPR security attributes to a mount target does not, by itself, allow traffic. You must also create ZPR policies that allow the required traffic. Existing network security groups and security lists continue to apply. For more information, see[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm).

For example:
```

```

- Create the storage class from the manifest file by entering:
```

```

For example:
```

```

- 

Create security rules in either a network security group (recommended) or a security list for both the mount target referenced in (or created by) the storage class definition, and for the cluster's worker nodes.
The security rules to create depend on the relative network locations of the mount target and the worker nodes, according to the following scenarios:
- [Scenario B: Mount target and instance in the same subnet](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-b)
- [Scenario A: Mount target and instance in different subnets (recommended)](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-a)

These scenarios, the security rules to create, and where to create them, are fully described in the File Storage service documentation (see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm)).
- Create a PVC to be provisioned by the new file system in the File Storage service, as follows:
- Create a manifest file to define the PVC:
```

```

where:
- `name: <pvc-name>`: Required. For example,`fss-dynamic-claim`
- `storageClassName: "<storage-class-name>"`: Required. The name of the storage class you defined earlier. For example,`fss-dyn-storage`.
- `accessModes: - ReadWriteMany`: Required. Note that`accessModes:`must specify`ReadWriteMany`.
- `storage: 50Gi`: Required. Note that Kubernetes requires that you specify a value for`storage:`in the PVC manifest. However, the File Storage service does not support the specification of a file system size and creates a new file system with a default size, regardless of the value you specify for`storage:`.

For example, the following manifest file (named`fss-dyn-claim.yaml`) defines a PVC named`fss-dynamic-claim`that is provisioned by the file system defined in the`fss-dyn-storage`storage class:
```

```

- Create the PVC from the manifest file by entering:
```

```

For example:
```

```

A new PVC is created. The CSI volume plugin creates a new persistent volume (PV) and a new file system in the File Storage service (along with a new mount target if you didn't specify an existing mount target).

The new PVC is bound to the new PV. Data is encrypted at rest, using encryption keys managed either by Oracle or by you.
- Verify that the PVC has been bound to the new persistent volume by entering:

```

```

The output from the above command confirms that the PVC has been bound successfully:

```

```

- Use the new PVC when creating other objects, such as pods. For example, you could create a new pod from the following pod definition:
```

```

- 

Having created a new pod as described in the example in the previous step, you can verify that the pod is using the new PVC by entering:
```

```

Tip  
  

If you foresee a frequent requirement to dynamically create new PVs and new filesystems when you create PVCs, you can specify that the new storage class you've created is to be used as the default storage class for provisioning new PVCs. See the[Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/)for more details.

### Encrypting Data At Rest on a New File System

The File Storage service always encrypts data at rest, using Oracle-managed encryption keys by default. However, you have the option to encrypt data at rest using your own master encryption keys that you manage yourself in the Vault service.

Depending on how you want to encrypt data at rest, follow the appropriate instructions below:
- To use the CSI volume plugin to dynamically create a new file system that uses Oracle-managed encryption keys to encrypt data at rest, follow the steps in[Provisioning a PVC on a New File System Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_FSS-Using-CSI-Volume-Plugin)and do not include the`kmsKeyOcid: <key-ocid>`parameter in the storage class definition. Data is encrypted at rest, using encryption keys managed by Oracle.
- To use the CSI volume plugin to dynamically create a new file system that uses master encryption keys that you manage to encrypt data at rest, follow the steps in[Provisioning a PVC on a New File System Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_FSS-Using-CSI-Volume-Plugin), include the`kmsKeyOcid: <key-ocid>`parameter in the storage class definition, and specify the OCID of the master encryption key in the Vault service. Data is encrypted at rest, using the encryption key you specify.

### Encrypting Data In Transit on a New File System

In-transit encryption secures data being transferred between instances and mounted file systems using TLS 1.2 (Transport Layer Security) encryption. For more information about in-transit encryption and the File Storage service, see[Using In-transit TLS Encryption](https://docs.oracle.com/iaas/Content/File/Tasks/intransitencryption.htm).

You specify in-transit encryption independently of at-rest encryption. Data in transit is encrypted using a TLS certificate that is always Oracle-managed, regardless of whether data at rest is encrypted using Oracle-managed keys or using user-managed keys.

Note that when using the File Storage service to provision PVCs, in-transit encryption is only supported when the compute instances hosting worker nodes are running Oracle Linux 7 and Oracle Linux 8.

To use the CSI volume plugin to dynamically create a new file system with in-transit encryption:
- Follow the instructions in[Setting up In-transit Encryption for Linux](https://docs.oracle.com/iaas/Content/File/Tasks/intransitencryption.htm#Setting_up_Intransit_Encryption)to set up in-transit encryption on the file system. More specifically:
- Complete the prerequisites by setting up the following security rules in either a network security group (recommended) or a security list for the mount target that exports the file system:
- A stateful ingress rule allowing TCP traffic to a Destination Port Range of 2051 , either from all ports of a source IP address or CIDR block of your choice, or from all sources.
- A stateful egress rule allowing TCP traffic from a Source Port Range of 2051 , either to all ports of a destination IP address or CIDR block of your choice, or to all destinations.

For more information, see[Scenario C: Mount target and instance use TLS in-transit encryption](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-c).
- On each worker node, install the`oci-fss-utils`package from the Oracle Linux yum repository. See[Setting up In-transit Encryption for Linux](https://docs.oracle.com/iaas/Content/File/Tasks/intransitencryption.htm#Setting_up_Intransit_Encryption).
- 

Follow the instructions in[Provisioning a PVC on a New File System Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_FSS-Using-CSI-Volume-Plugin)and include the`encryptInTransit: "true"`parameter in the storage class definition. Data is encrypted in transit, using an encryption key managed by Oracle.

## Provisioning a PVC on an Existing File System

To create a PVC on an existing file system in the File Storage service (using Oracle-managed encryption keys to encrypt data at rest):
- Create a file system with a mount target in the File Storage service, selecting the Encrypt using Oracle-managed keys encryption option. See[Creating a File System](https://docs.oracle.com/iaas/Content/File/Tasks/create-file-system.htm).
- Create security rules in either a network security group (recommended) or a security list for both the mount target that exports the file system, and for the cluster's worker nodes.
The security rules to create depend on the relative network locations of the mount target and the worker nodes, according to the following scenarios:
- [Scenario B: Mount target and instance in the same subnet](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-b)
- [Scenario A: Mount target and instance in different subnets (recommended)](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-a)

These scenarios, the security rules to create, and where to create them, are fully described in the File Storage service documentation (see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm)).
- Create a PV backed by the file system in the File Storage service as follows:
- 

Create a manifest file to define a PV and in the`csi:`section, set:
- `driver`to`fss.csi.oraclecloud.com`
- `volumeHandle`to`<FileSystemOCID>:<MountTargetIP>:<path>`
where:
- `<FileSystemOCID>`is the OCID of the file system defined in the File Storage service.
- `<MountTargetIP>`is the IP address assigned to the mount target.
- `<path>`is the mount path to the file system relative to the mount target IP address, starting with a slash. For example:`ocid1.filesystem.oc1.iad.aaaa______j2xw:10.0.0.6:/FileSystem1`

For example, the following manifest file (named fss-pv.yaml) defines a PV called`fss-pv`backed by a file system in the File Storage service:
```

```

- Create the PV from the manifest file by entering:
```

```

For example:
```

```

- Create a PVC that is provisioned by the PV you have created, as follows:
- Create a manifest file to define the PVC and set:
- `storageClassName`to`""`. Note that you must specify an empty value for`storageClassName`, even though storage class is not applicable in the case of static provisioning of persistent storage. If you do not specify an empty value for`storageClassName`, the default storage class (`oci-bv`) is used, which causes an error.
- `volumeName`to the name of the PV you created (for example,`fss-pv`)

For example, the following manifest file (named`fss-pvc.yaml`) defines a PVC named`fss-pvc`that is provisioned by a PV named`fss-pv`:
```

```

Note that the`requests: storage:`element must be present in the PVC's manifest file, and its value must match the value specified for the`capacity: storage:`element in the PV's manifest file. Apart from that, the value of the`requests: storage:`element is ignored.
- Create the PVC from the manifest file by entering:
```

```

For example:
```

```

The PVC is bound to the PV backed by the File Storage service file system. Data is encrypted at rest, using encryption keys managed by Oracle.

### Encrypting Data At Rest on an Existing File System

The File Storage service always encrypts data at rest, using Oracle-managed encryption keys by default. However, you have the option to encrypt file systems using your own master encryption keys that you manage yourself in the Vault service.

Depending on how you want to encrypt data at rest, follow the appropriate instructions below:
- To create a PVC on a file system using Oracle-managed encryption keys to encrypt data at rest, follow the steps in[Provisioning a PVC on an Existing File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_FSS_Oracle_managed_keys)and select the Encrypt using Oracle-managed keys encryption option as described. Data is encrypted at rest, using encryption keys managed by Oracle.
- To create a PVC on a file system using master encryption keys that you manage to encrypt data at rest, follow the steps in[Provisioning a PVC on an Existing File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_FSS_Oracle_managed_keys)but select the Encrypt using customer-managed keys encryption option and specify the master encryption key in the Vault service. Data is encrypted at rest, using the encryption key you specify.

### Encrypting Data In Transit on an Existing File System

In-transit encryption secures data being transferred between instances and mounted file systems using TLS v. 1.2 (Transport Layer Security) encryption. For more information about in-transit encryption and the File Storage service, see[Using In-transit TLS Encryption](https://docs.oracle.com/iaas/Content/File/Tasks/intransitencryption.htm).

You specify in-transit encryption independently of at-rest encryption. Data in transit is encrypted using a TLS certificate that is always Oracle-managed, regardless of whether data at rest is encrypted using Oracle-managed keys or using user-managed keys.

Note that when using the File Storage service to provision PVCs, in-transit encryption is only supported when the compute instances hosting worker nodes are running Oracle Linux 7 and Oracle Linux 8.

To create a PVC on a file system where data is encrypted in transit:
- Follow the instructions in[Setting up In-transit Encryption for Linux](https://docs.oracle.com/iaas/Content/File/Tasks/intransitencryption.htm#Setting_up_Intransit_Encryption)to set up in-transit encryption on the file system. More specifically:
- Complete the prerequisites by setting up the following security rules in either a network security group (recommended) or a security list for the mount target that exports the file system:
- A stateful ingress rule allowing TCP traffic to a Destination Port Range of 2051 , either from all ports of a source IP address or CIDR block of your choice, or from all sources.
- A stateful egress rule allowing TCP traffic from a Source Port Range of 2051 , either to all ports of a destination IP address or CIDR block of your choice, or to all destinations.

For more information, see[Scenario C: Mount target and instance use TLS in -transit encryption](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm#File_Storage_Security_Rule_Scenarios).
- On each worker node, install the`oci-fss-utils`package from the Oracle Linux yum repository. See[Setting up In-transit Encryption for Linux](https://docs.oracle.com/iaas/Content/File/Tasks/intransitencryption.htm#Setting_up_Intransit_Encryption).
- 

Follow the instructions in[Provisioning a PVC on an Existing File System](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_FSS_Oracle_managed_keys), selecting either the Encrypt using Oracle-managed keys option or the Encrypt using customer-managed keys option as required for data encryption at rest. However, when creating the manifest file to define a PV, set`encryptInTransit`to`"true"`in the`csi`section of the file. For example:
```

```

## Troubleshooting File Storage Service Provisioning of PVCs

### Pod cannot access file system due to insufficient permissions

#### Description

When a pod attempts to access a persistent volume (PV) backed by a file system in the File Storage service, the attempt might fail with a "Permission Denied" message.

#### Cause

When defining a PV backed by a file system in the File Storage service, you set the PV's`accessModes`attribute to`ReadWriteMany`, and you do not have to specify a value for the PV's`fsType`attribute.

The CSI volume plugin is implemented as a CSIDriver object. You use the CSIDriver object's`fsGroupPolicy`attribute to control whether the CSIDriver changes a volume's ownership and permissions to match the`fsGroup`attribute specified in the`securityContext`of a pod mounting the volume. Changing the volume's ownership and permissions enables the pod to access the volume after mounting it.

By default, the CSIDriver object's`fsGroupPolicy`attribute is set to`ReadWriteOnceWithFSType`, indicating that the CSIDriver is to examine the PV definition to determine whether to modify volume ownership and permissions to match the pod's`fsGroup`attribute as follows:
- If the PV's`fsType`attribute is set, the CSIDriver modifies the volume's ownership and permissions to match the`fsGroup`attribute specified in the pod's`securityContext`. As a result, the volume is accessible to the pod.
- If the PV's`fsType`attribute is not set, the CSIDriver does not modify volume ownership and permissions. The volume is only accessible to processes running as root. As a result, a pod that is not running as root receives the "Permission Denied" message when attempting to access a directory or file in the mounted volume.

Here's how to verify that the reason a pod is receiving the "Permission Denied" message is because the CSIDriver object's`fsGroupPolicy`attribute is set to`ReadWriteOnceWithFSType`and the PV's`fsType`attribute is not set. Execute a command on the pod to write a file to a directory on the mounted volume and then examine the properties of the file to confirm whether the group owner matches the`fsGroup`attribute specified in the`securityContext`of the pod. For example, assume a pod has the following manifest:
```

```

- Execute a command on the pod to write a file to a directory on the mounted volume. For example, by entering:
```

```

- Examine the properties of the newly created file to confirm the access rights. For example, by entering:
```

```

Ideally, the output shows the file's group owner to be the same as that specified by the pod's`fsGroup`attribute, giving the pod access to the file. For example:
```

```

However, if the CSIDriver object's`fsGroupPolicy`attribute is set to`ReadWriteOnceWithFSType`and the PV's`fsType`attribute is not set, the output shows the file's group owner as root and the pod does not have access to the file. For example:
```

```

For more information, see[CSI Volume fsGroup Policy](https://kubernetes-csi.github.io/docs/support-fsgroup.html#supported-modes)in the Kubernetes documentation.

#### Action

If you know the volume owner's group ID of the files that the pod accesses, and the volume owner's group ID is not root (0), we recommend you specify a supplemental group in the`securityContext`in the pod spec. For example, if the volume owner's user ID is 0 (root) and the volume owner's group ID is 1000, specify 1000 as a supplemental group in the pod's`securityContext`as follows:
```

```

If you cannot assign the volume owner's group ID as a supplemental group in the pod's`securityContext`, we suggest two alternative solutions:
- [Alternative Solution 1:](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Troubleshooting_insufficientpermissions__AlternativeSolution1)Enable the CSIDriver object to modify volume ownership and permissions to match the`fsGroup`attribute specified in the pod's`securityContext`.
- [Alternative Solution 2:](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Troubleshooting_insufficientpermissions__AlternativeSolution2)Use the file system's Squash export options to enable pods to access files and directories in the volume without changing the volume ownership.

Before choosing a solution, consider the advantages and disadvantages described for each solution.

Alternative Solution 1: Enable the CSIDriver object to modify volume ownership and permissions to match the`fsGroup`attribute specified in the pod's`securityContext`

To enable the CSIDriver object to modify volume ownership and permissions to match the`fsGroup`attribute specified in the pod's`securityContext`, set the CSIDriver object's`fsGroupPolicy`attribute to`File`as follows:
- Obtain the CSIDriver configuration file by entering:
```

```

- In a text editor, edit the fss_csi_driver.yaml file and change the CSIDriver object's`fsGroupPolicy`attribute from`ReadWriteOnceWithFSType`to`File`.

For example, change:
```

```

to:
```

```

Only change the value of`fsGroupPolicy`. Do not change any other value.
- Save and close the fss_csi_driver.yaml file.
- Delete the existing CSIDriver object by entering:
```

```

- Create the new CSIDriver object by entering:
```

```

- Restart the pod that encountered the "Permission Denied" message.

Things to consider before choosing this solution:
- When mounting a large volume with many nested files and directories, you might notice that mounting the volume takes a long time. This volume mount latency is because, when`fsGroupPolicy`is set to`File`, Kubernetes recursively changes the volume ownership of all nested files and directories by calling`chown()`and`chmod()`. To reduce the volume mount latency, try setting the`fsGroupChangePolicy`attribute to`"OnRootMismatch"`in the pod's`securityContext`, as follows:
```

```

Setting`fsGroupChangePolicy`to`"OnRootMismatch"`reduces the volume mount latency because Kubernetes only changes volume ownership in those cases where root level file permissions do not match the pod's`fsGroup`setting.
- 

The group IDs that you specify as values of`fsGroup`for all the pods accessing a volume are added as supplemental group owners of the volume. As a result, access to that volume is restricted to the group IDs that you specified as values of`fsGroup`.

For example, if you create two pods with different`fsGroup`values that both mount the same volume, the group ID you specify for the second pod's`fsGroup`is the volume owner's group, and the first pod still has access to the volume.
- If Kubernetes detects an ownership mismatch between the volume owner and the`fsGroup`defined in the pod spec, Kubernetes changes the volume ownership of all files. If the volume has many nested files and directories, you might notice that mounting the volume takes a long time.

Alternative Solution 2: Use the file system's Squash export options to enable pods to access files and directories in a volume without changing the volume ownership.
Caution  
  
This solution requires you to set the file system's Squash export option to All . Setting Squash to All grants unrestricted file system access to all processes running on the node where the volume is mounted (including to other pods). Therefore, before choosing this solution, review compliance with your security requirements.

You can enable pods to access files and directories in a volume without changing volume ownership by setting the file system's Squash export options. The Squash export options determine whether the source clients accessing the file system have their user ID (UID) and group ID (GID) remapped to Squash UID and Squash GID . For more information, see[NFS Export Options](https://docs.oracle.com/iaas/Content/File/Tasks/exportoptions.htm#Export).

If you decide to use this solution, you do not change the CSIDriver object's`fsGroupPolicy`attribute to`File`.

To set Squash export options when provisioning a PVC on an existing file system:
- Open the navigation menu and select Storage . Under File Storage , select File Systems .
- In the List scope section, under Compartment , select a compartment. All the file systems in the selected compartment are displayed.
- Select the name of the file system that you want to set export options for.
- On the file system's details page, under Resources , select Exports .
- In the Exports list, select the name of the export for which you want to set options.
- On the export's details page, under NFS client Export options , select Edit options .
- 

In the Edit options panel, update the Squash export options as follows:
- Squash: Change to All .
- Squash UID: Change to the volume owner's UID, or to the root UID (0).
- Squash GUID: Change to the volume owner's GID, or to the root GID (0).

For more information, see[NFS Export Options](https://docs.oracle.com/iaas/Content/File/Tasks/exportoptions.htm#Export).
- Select Update .

To set Squash export options when provisioning a PVC on a new file system:
- Follow the instructions in[Provisioning a PVC on a New File System Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_FSS-Using-CSI-Volume-Plugin), but when you create the manifest file for the storage class that uses the`fss.csi.oraclecloud.com`provisioner, set the`exportOptions`parameter to specify values for the Squash export options as follows:
```

```

For example:
```

```

- Create the storage class from the manifest file by entering:
```

```

For example:
```

```

- Follow the remaining instructions in[Provisioning a PVC on a New File System Using the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_FSS-Using-CSI-Volume-Plugin)to create security rules, and to create the PVC.

The CSI volume plugin creates a new persistent volume (PV) and a new file system in the File Storage service. The new file system has the Squash export options that you specified in the storage class.

Things to consider before choosing this solution:
- Setting Squash to All grants unrestricted file system access to all processes running on the node where the volume is mounted (including to other pods). Therefore, before choosing this solution, review compliance with your security requirements.
- Unlike[Alternative Solution 1](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Troubleshooting_insufficientpermissions__AlternativeSolution1), a volume's ownership does not change whenever the volume is mounted by a new pod that has its`fsGroup`attribute set to a different group.
- Unlike[Alternative Solution 1](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Troubleshooting_insufficientpermissions__AlternativeSolution1), there is no volume mount latency when mounting a large volume with many nested files and directories, because Kubernetes does not recursively change the volume ownership of the nested files and directories.
- Unlike[Alternative Solution 1](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic_Troubleshooting_insufficientpermissions__AlternativeSolution1), you do not edit the fss_csi_driver.yaml file and change the CSIDriver object's`fsGroupPolicy`attribute to`File`. Instead, the default attribute value`fsGroupPolicy: ReadWriteOnceWithFSType`
