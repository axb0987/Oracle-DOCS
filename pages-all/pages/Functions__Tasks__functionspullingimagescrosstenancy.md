# Pulling Images from Repositories in other Tenancies
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspullingimagescrosstenancy.htm
- Fetched: 2026-09-05 02:09 CDT

# Pulling Images from Repositories in other Tenancies

Find out about the IAM policies that are required for a function in an application in one tenancy to pull an image from a repository in another tenancy, using OCI Functions.

When a function is invoked for the first time, OCI Functions pulls the function's image from a repository in Oracle Cloud Infrastructure Registry, runs the image as a container, and executes the function. Typically, the function's application is in the same tenancy as the repository containing the image. However, provided the necessary cross-tenancy policies exist, the function's application can be in a different tenancy to the repository containing the image.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and refer to:
- [Creating Policies to Control Access to Network and Function-Related Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm)
- [Details for Functions](https://docs.oracle.com/iaas/Content/Identity/Reference/functionspolicyreference.htm)

## Cross-Tenancy Policies

Your organization might want functions in an application in one tenancy to pull images created by another organization and stored in a repository in its own tenancy. The other organization could be another business unit in your company, a customer of your company, a company that provides services to your company, and so on. In cases like these, you need cross-tenancy policies in addition to the required user and service policies described in[Creating Policies to Control Access to Network and Function-Related Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm).

### Endorse, Admit, and Define statements

To access and share resources between two tenancies, the administrators of both tenancies have to create special policy statements that explicitly state the resources that can be accessed and shared. These special statements use the words Define , Endorse , and Admit .

Here's an overview of the special verbs used in cross-tenancy statements:
- Endorse : States the general set of abilities that a group in your own tenancy can perform in other tenancies. The Endorse statement always belongs in the tenancy with the group crossing the boundaries into the other tenancy to work with that tenancy's resources. In the examples, this tenancy is referred to as the source tenancy.
- Admit : States the kind of ability in your own tenancy that you want to grant a group from another tenancy. The Admit statement belongs in the tenancy that is granting "admittance" to the tenancy. The Admit statement identifies the group that requires resource access from the source tenancy (where it is identified with a corresponding Endorse statement). In the examples, this tenancy is referred to as the destination tenancy.
- 

Define : Assigns an alias to a tenancy OCID for Endorse and Admit policy statements.

Define statements must be included in the same policy entity as the Endorse or the Admit statement.

The Endorse and Admit statements work together, but they reside in separate policies, one in each tenancy. Without a corresponding statement that specifies access, a particular Endorse or Admit statement grants no access. Agreement is required from both tenancies.

### Source policies

To enable functions in applications in a source tenancy to pull images from repositories in a destination tenancy, the source administrator creates an IAM policy in the source tenancy that:
- defines the destination tenancy containing the resources to be accessed (the destination administrator must provide the OCID of the destination tenancy)
- endorses functions in applications in the source tenancy to pull images from repositories in the destination tenancy

The policy statements in the source tenancy have the format:
```

```

where:
- `<destination-tenancy>`is a convenient alias for the tenancy containing the image. For example,`image-tenancy`
- `<tenancy-ocid>`is the OCID of the tenancy containing the image. For example,`ocid1.tenancy.oc1..aaaa______ggq`

For example:
```

```

### Destination policies

To enable functions in applications in a source tenancy to pull images from repositories in a destination tenancy, the destination administrator creates an IAM policy in the destination tenancy that:
- defines the source tenancy that is allowed to access resources in the destination tenancy (the source administrator must provide the OCID of the source tenancy)
- admits functions in applications in the source tenancy to pull images from repositories in the destination tenancy

The policy statements in the destination tenancy containing the image have the format:
```

```

where:
- `<source-tenancy>`is a convenient alias for the tenancy containing the function's application. For example,`application-tenancy`
- `<tenancy-ocid>`is the OCID of the tenancy containing the function's application. For example,`ocid1.tenancy.oc1..aaaa______abc`

For example:

```

```
