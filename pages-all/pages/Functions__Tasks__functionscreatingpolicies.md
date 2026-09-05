# Creating Policies to Control Access to Network and Function-Related Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm
- Fetched: 2026-09-05 02:08 CDT

# Creating Policies to Control Access to Network and Function-Related Resources

Find out how to create policies to control access of both users and the OCI Functions service to network and function-related resources.

Before users can start using OCI Functions to create and deploy functions, as a tenancy administrator you have to create a number of Oracle Cloud Infrastructure policy statements to grant access to function-related and network resources.

Use the Policy Builder to create a suitable policy, by selecting Functions as the Policy Use Case , and then selecting the[Let users create, deploy, and manage functions and applications](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm#functions-create-manage-cloudshell)policy template. That policy template contains all the necessary policy statements required to use OCI Functions. See[Writing Policy Statements with the Policy Builder](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-Using_the_Policy_Builder.htm).

Alternatively, you can create one or more policies containing the policy statements (follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)).

## Policy statements

[Policy Statements to Give OCI Functions Users Access to Oracle Cloud Infrastructure Registry Repositories](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#)

Purpose: Create in: Statement:
Enables users to obtain the Object Storage namespace string of the tenancy Root compartment`Allow group <group-name> to read objectstorage-namespaces in tenancy`
Gives users access to repositories in Oracle Cloud Infrastructure Registry Compartment that owns the repository, or the root compartment`Allow group <group-name> to manage repos in tenancy|<compartment-name>`

When OCI Functions users work with functions, they have to access repositories in Oracle Cloud Infrastructure Registry. Users can only access repositories that the groups to which they belong have been granted access. To enable users to access a repository, policy statements must grant the groups access to that repository.

The policy statement`Allow group <group-name> to read objectstorage-namespaces in tenancy`enables users to obtain the auto-generated Object Storage namespace string of the tenancy, which is required to log in to Oracle Cloud Infrastructure Registry. This policy statement also provides access to function logs stored in a storage bucket in Oracle Cloud Infrastructure Object Storage (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm)).

If you use the policy statement`Allow group <group-name> to manage repos in tenancy`to give users access to repositories in Oracle Cloud Infrastructure Registry, note that this policy statement gives the group permission to manage all repositories in the tenancy. If you consider this to be too permissive, then you can restrict the repositories to which the group has access by including a where clause in the`manage repos`statement. Note that if you do include a where clause, you must also include a second statement in the policy to enable the group to inspect all repositories in the tenancy (when using the Console). For example, the following policy statements restrict the group to accessing only repositories with names that start 'acme-web-app', but also enables the group to inspect all repositories in the tenancy:

```

```

```

```

[Policy Statements to Give OCI Functions Users Access to Function-Related Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#)

Purpose: Create in: Statement:
Gives users access to function-related resources Compartment that owns function-related resources`Allow group <group-name> to manage functions-family in compartment <compartment-name>`
Gives users access to metrics emitted by OCI Functions Compartment that owns function-related resources`Allow group <group-name> to read metrics in compartment <compartment-name>`

When OCI Functions users create functions and applications, they have to specify a compartment for those function-related resources (including for metrics emitted by OCI Functions). Users can only specify a compartment that the groups to which they belong have been granted access. To enable users to specify a compartment, policy statements must grant the groups access to that compartment.

The policy statement`Allow group <group-name> to manage functions-family in compartment <compartment-name>`gives users access to function-related resources.

The policy statement`Allow group <group-name> to read metrics in compartment <compartment-name>`gives users access to metrics emitted by OCI Functions.

[Policy Statement to Give OCI Functions Users Access to Logging Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#)

Purpose: Create in: Statement:
Gives users access to logging resources Root compartment

`Allow group <group-name> to manage logging-family in compartment <compartment-name>`

When OCI Functions users define an application, they can enable logging to store and view function logs in the Oracle Cloud Infrastructure Logging service. Users can only view logs that the groups to which they belong have been granted access. To enable users to store and view function logs in the Oracle Cloud Infrastructure Logging service, a policy statement must grant the groups access to logging resources.

The policy statement`Allow group <group-name> to manage logging-family in compartment <compartment-name>`gives users full access to logging resources in the compartment that will own logging resources

[Policy Statement to Give OCI Functions Users Access to Network Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#)

Purpose: Create in: Statement:
Gives users access to network resources Compartment that owns network resources`Allow group <group-name> to use virtual-network-family in compartment <compartment-name>`

When OCI Functions users create a function or application, they have to specify a VCN and a subnet in which to create them. Users can only specify VCNs and subnets in compartments that the groups to which they belong have been granted access. To enable users to specify a VCN and subnet, a policy statement must grant the groups access to the compartment.

When OCI Functions users want to define ingress and egress rules that apply to all the functions in a particular application using an NSG, they can add the application to that NSG. To add an application to an NSG, a similar policy statement must grant the groups to which users belong access to the compartment to which the NSG belongs. Note that the NSG might belong to a different compartment to the function's subnet. For more information, see[Adding Applications to Network Security Groups (NSGs)](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingnsgs.htm).

[Policy Statement to Give OCI Functions Users Access to Security Attribute Namespaces](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#)

Purpose: Create in: Statement:
Gives users access to security attribute namespaces for ZPR Root compartment`Allow group <group-name> to use security-attribute-namespaces in <location>`

When OCI Functions users create or update an application in a Zero Trust Packet Routing (ZPR) enabled tenancy, they can add security attributes to the application. Security attributes are defined in a security attribute namespace. To add a security attribute to an application, users must have already been granted access to the namespace containing the security attribute by an IAM policy.

For example:
```

```

If you use the policy statement`Allow group <group-name> to use security-attribute-namespaces in tenancy`to give users access to security attribute namespaces, note that this policy statement gives the group permission to use all security attribute namespaces in the tenancy. If you consider this to be too permissive, then you can restrict the security attribute namespaces to which the group has access by including a where clause in the statement. For example:
```

```

Note that if you do include a where clause, you must also include a second statement in the policy to enable the group to inspect all security attribute namespaces in the tenancy (when using the Console). For example:
```

```

When security attributes have been added to an application, the functions in the application can only access other OCI resources if access is allowed by a ZPR policy.

For more information, see[Adding Security Attributes to Applications, and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm).

[Policy Statements to Give the OCI Functions Service and OCI Functions Users Access to Tracing Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#)

Purpose: Create in: Statement:
Gives the OCI Functions service access to tracing resources Compartment that owns tracing resources, or the root compartment

`Allow service faas to use apm-domains in tenancy|compartment <compartment-name>`
Gives users access to tracing resources Compartment that owns tracing resources, or the root compartment

`Allow group <group-name> to use apm-domains in tenancy|compartment <compartment-name>`

When OCI Functions users want to investigate why a function doesn't run or perform as expected, they can use tracing to debug execution and performance issues. To use tracing, users have to enable tracing for the application containing the function, and then enable tracing for one or more functions. Users can then view function traces in the Application Performance Monitoring (APM) Trace Explorer. For more information, see[Distributed Tracing for Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm).

Users can only enable tracing if the group to which they belong can access existing APM domains (or create new APM domains), and if OCI Functions can access APM domains. To enable users to turn on tracing and view traces, policy statements must grant the group and OCI Functions access to APM domains.

The policy statement`Allow group <group-name> to use apm-domains in tenancy|compartment <compartment-name>`gives users access to tracing resources in the compartment or in the entire tenancy. If you want to enable users to create new APM domains (and delete APM domains), specify`manage apm-domains`instead of`use apm-domains`.

The policy statement`Allow service faas to use apm-domains in tenancy|compartment <compartment-name>`gives OCI Functions access to APM domains in the compartment or in the entire tenancy.

[Policy Statements to Give the OCI Functions Service and OCI Functions Users Access to Oracle Vault Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#)

Purpose: Create in: Statement:
Gives the OCI Functions service access to verify master encryption keys in Oracle Cloud Infrastructure Vault Compartment that owns the vault and/or master encryption key, or the root compartment

`Allow service faas to {KEY_READ} in tenancy|compartment <compartment-name> where request.operation='GetKeyVersion'`

If functions and encryption keys are in different tenancies:
- Use the following policies in the functions' tenancy:

`Define tenancy KeyTenancy as {<key-tenancy-ocid>}`

`Endorse any-user to { KEY_INSPECT, KEY_VERIFY } in tenancy KeyTenancy where all { request.principal.type = 'fnapp', request.operation='Verify' }`
- Use the following policies in the encryption keys' tenancy:

`Define tenancy FunctionTenancy as {<function-tenancy-ocid>}`

`Admit any-user of tenancy FunctionTenancy to { KEY_INSPECT, KEY_VERIFY } in tenancy where all { request.principal.type = 'fnapp', request.operation='Verify' }`

(if you require more restrictive policy statements, see below for examples)
Gives the OCI Functions service access to signed images in Oracle Cloud Infrastructure Registry Root compartment

If functions and images are in different tenancies:
- Use the following policies in the functions' tenancy:

`Define tenancy ImageTenancy as {<image-tenancy-ocid>}`

`Endorse any-user to { REPOSITORY_INSPECT, REPOSITORY_READ } in tenancy ImageTenancy where all { request.principal.type = 'fnapp', request.principal.repo_name = target.repo.name, request.operation='ListContainerImageSignatures' }`
- Use the following policies in the images' tenancy:

`Define tenancy FunctionTenancy as {<function-tenancy-ocid>}`

`Admit any-user of tenancy FunctionTenancy to { REPOSITORY_INSPECT, REPOSITORY_READ } in tenancy where all { request.principal.type = 'fnapp', request.principal.repo_name = target.repo.name, request.operation='ListContainerImageSignatures' }`
Gives users access to vaults and master encryption keys in Oracle Cloud Infrastructure Vault Compartment that owns the vault and/or master encryption key, or the root compartment

`Allow group <group-name> to read vaults in tenancy|compartment <compartment-name>`

`Allow group <group-name> to use keys in tenancy|compartment <compartment-name>`

(if you require more restrictive policy statements, see below for examples)
Gives users access to signed images in Oracle Cloud Infrastructure Registry Root compartment

`Allow group <group-name> to read repos in tenancy`

Users can configure OCI Functions applications to only allow the creation, updating, deployment, and invocation of functions based on images in Oracle Cloud Infrastructure Registry that have been signed by particular master encryption keys.

To create a signature verification policy, and to create and deploy signed function images, users must have access to master encryption keys in vaults defined in Oracle Cloud Infrastructure Vault. Similarly, to enforce a signature verification policy defined for an application, the OCI Functionsservice must also have access to master encryption keys defined in Oracle Cloud Infrastructure Vault.

You can restrict the master encryption keys that can be used for function image signing, and signature verification. For example, by using policies like:

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

For more information and examples, see[Signing Function Images and Enforcing the Use of Signed Images from Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm)
