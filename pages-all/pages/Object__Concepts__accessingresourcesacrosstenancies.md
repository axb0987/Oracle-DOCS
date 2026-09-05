# Accessing Object Storage Resources Across Tenancies
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/accessingresourcesacrosstenancies.htm
- Fetched: 2026-09-05 02:50 CDT

# Accessing Object Storage Resources Across Tenancies

Learn about how to write policies that gives your tenancy access to Object Storage resources in other tenancies.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).

## Cross-Tenancy Policies

Your organization might also want to share resources with another organization that has its own tenancy. It could be another business unit in your company, a customer of your company, a company that provides services to your company, and so on. In cases like these, you need cross-tenancy policies in addition to the required user and service policies described previously.

To access and share resources, the administrators of both tenancies need to create special policy statements that explicitly state the resources that can be accessed and shared. These special statements use the words Define , Endorse , and Admit .

### Endorse, Admit, and Define Statements

Here's an overview of the special verbs used in cross-tenancy statements:
- Endorse : States the general set of abilities that a group in your own tenancy can perform in other tenancies. The Endorse statement always belongs in the tenancy that contains the group of users crossing the boundaries into the other tenancy to work with that tenancy's resources. In the examples, we refer to this tenancy as the source tenancy.
- Admit : States the kind of ability in your own tenancy that you want to grant a group from the other tenancy. The Admit statement belongs in the tenancy who is granting "admittance" to the tenancy. The Admit statement identifies the group of users that requires resource access from the source tenancy and is identified with a corresponding Endorse statement. In the examples, we refer to this tenancy as the destination tenancy.
- Define : Assigns an alias to a tenancy OCID for Endorse and Admit policy statements. A Define statement is also required in the destination tenancy to assign an alias to the source IAM group OCID for Admit statements.

Include a Define statement in the same policy entity as the Endorse or Admit statement.

The Endorse and Admit statements work together. An Endorse statement resides in the source tenancy while an Admit statement resides in the destination tenancy. Without a corresponding statement that specifies access, a particular Endorse or Admit statement grants no access. Both tenancies must agree on access.
Important  
  
In addition to policy statements, you must also subscribe to a region to share resources across regions.

### Source Tenancy Policy Statements

The source and target tenancy administrators create policy statements that endorse a source IAM group allowed to manage resources in the destination tenancy.

Here's an example of a broad policy statement that endorses the IAM group`StorageAdmins`group to do anything with all Object Storage resources in any tenancy:

```

```

To write a policy that reduces the scope of tenancy access, the source administrator must reference the destination tenancy OCID provided by the destination administrator. Here's an example of policy statements that endorse the IAM group`StorageAdmins`group to manage Object Storage resources in`DestinationTenancy`only:
```

```

When using IAM with Identity Domains, specify the domain:
```

```

```

```

### Destination Tenancy Policy Statements

The destination administrator creates policy statements that:
- Defines the source tenancy and IAM group that's allowed to access resources in your tenancy. The source administrator must provide this information.
- Admits those defined sources to access Object Storage resources that you want to allow access to in your tenancy.

Here's an example of policy statements that endorse the IAM group`StorageAdmins`in the source tenancy to do anything with all Object Storage resources in your tenancy:
```

```

Here's an example of policy statements that endorse the IAM group`StorageAdmins`in the source tenancy to manage Object Storage resources only the`SharedBuckets`compartment:
```

```

```

```

## Using Credentials from the Source Tenancy

Use the credentials as usual from the endorsing (source) tenancy when accessing the resources. The user in the source tenancy must have suitable credentials. A typical`~/.oci/config`file should look something like this:
```

```

Example:
```

```
