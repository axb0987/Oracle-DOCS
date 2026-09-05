# Getting Started with Security Advisor
- Source: https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Concepts/get-started.htm
- Fetched: 2026-09-05 03:05 CDT

# Getting Started with Security Advisor

Before creating secure resources with Oracle Cloud Infrastructure Security Advisor, complete these prerequisite tasks.

To use Oracle Cloud Infrastructure, you must be granted security access in a policy by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment to work in.

For more information about how policies work, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm).

## Required IAM Policies for Creating Buckets

- The following policy lets the specified group do everything with buckets and objects in the specified compartment:
```

```

- The following policy lets the specified group do everything with vaults in the specified compartment, which might not be the same compartment as the bucket compartment. (If you prefer, you can write a policy that grants the`use vaults`permission instead. With that permission, the specified group can use existing vaults, but can't create new ones.)
```

```

- The following policy lets the specified group do everything with keys in the specified compartment, which must be the same compartment as the vault compartment:
```

```

- The following policy lets the Object Storage service list, view, and perform cryptographic operations with all keys in the specified compartment:
```

```

In the preceding example, replace &lt;region_name&gt; with the appropriate region identifier, for example:
- 

`objectstorage-us-phoenix-1`
- 

`objectstorage-us-ashburn-1`
- 

`objectstorage-eu-frankfurt-1`
- 

`objectstorage-uk-london-1`
- 

`objectstorage-ap-tokyo-1`

To identify the region name value of an Oracle Cloud Infrastructure region, see[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

## Required IAM Policies for Creating File Systems

- The following policy lets the specified group do everything with file systems and mount targets in the specified compartment:
```

```

- The following policy lets the specified group do everything with vaults in the specified compartment, which might not be the same compartment as the file system compartment. (If you prefer, you can write a policy that grants the`use vaults`permission instead. With that permission, the specified group can use existing vaults, but cannot create new ones.)
```

```

- The following policy lets the specified group do everything with keys in the specified compartment, which must be the same compartment as the vault compartment:
```

```

- The following group and policy lets File Storage file systems list, view, and perform cryptographic operations with all keys in the specified compartment.
- 

Create a[dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm)for the file systems with a rule such as the following:
```

```

- 

Create a policy that gives the dynamic group of file systems access to use Vault secrets:
```

```

- 

In addition to creating policies for resource principal access, the File Storage service user should be granted access to read the keys using a policy such as the following:
```

```

The name of the File Storage service user depends on your realm . For realms with realm key numbers of 10 or less, the pattern for the File Storage service user is`FssOc <n> Prod`, where n is the realm key number. Realms with a realm key number greater than 10 have a service user of`fssocprod`. For more information about realms, see[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

## Required IAM Policies for Creating Compute Instances

- The following policy lets the specified group list and use all components in Networking in the specified compartment. This includes virtual cloud networks (VCNs), subnets, gateways, virtual circuits, security lists, route tables, and so on.
```

```

- The following policy lets the specified group create and manage instance images in the specified compartment:
```

```

- The following policy lets the specified group do everything with vaults in the specified compartment, which might not be the same compartment as the instance compartment. (If you prefer, you can write a policy that grants the`use vaults`permission instead. With that permission, the specified group can use existing vaults, but cannot create new ones.)
```

```

- The following policy lets the specified group do everything with keys in the specified compartment, which must be the same compartment as the vault compartment:
```

```

- The following policy lets the Block Volume service list, view, and perform cryptographic operations with all keys in the specified compartment. The Block Volume service is responsible for the boot volume attached to the instance.
```

```

## Required IAM Policies for Creating Block Volumes

- The following policy lets the specified group do everything with block storage volumes, volume backups, and volume groups in the specified compartment:
```

```

- The following policy lets the specified group do everything with vaults in the specified compartment, which might not be the same compartment as the volume compartment. (If you prefer, you can write a policy that grants the`use vaults`permission instead. With that permission, the specified group can use existing vaults, but can't create new ones.)
```

```

- The following policy lets the specified group do everything with keys in the specified compartment, which must be the same compartment as the vault compartment:
```

```

- The following policy lets the Block Volume service list, view, and perform cryptographic operations with all keys in the specified compartment:
```

```
