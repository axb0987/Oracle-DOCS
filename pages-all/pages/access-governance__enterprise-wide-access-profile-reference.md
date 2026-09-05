# Enterprise-wide Access Profile Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/enterprise-wide-access-profile-reference.htm
- Fetched: 2026-09-05 03:14 CDT

# Enterprise-wide Access Profile Reference

Use the Enterprise-wide Browser functionality of Oracle Access Governance to view access insights available across your enterprise. You can view access information using various perspectives, such as Identities, Identity Collections, Roles, Permissions, Policies, Resources, Organizations. Each one offers a different angle to the enterprise access information.

Get the reference information of details provided by each access component.
Note  
  
Some account attribute values might be masked (displayed as asterisks, "********") based on your organization's policies. See:[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes).

## Identities

While exploring access profile details in an Enterprise-wide Browser , for an identity, you can view its associated roles, permissions, accounts, ownership, organizations, identity collections, identity attributes, cloud resources, delegations, and policies. You will see the same set of information when exploring your own accesses within Oracle Access Governance, or when managers view identity details for their team members.

For Identities, you can see the following information:

Identity Access Profile Information
Access Component Description
Identity Collections Count and details of the identity collection associated with the identity. You can further browse through this identity collection by selecting the View details link. This can either be Oracle Access Governance identity collection or an ingested identity collection, such as OCI groups.
Permissions Count and access rights detail associated with this identity. It gives clarity of how this access was granted, for which resource this permission has been granted, and whether it is a role, permission, or a privilege assigned to the identity. For each permission, use the More actions icon to view permission, resource, and account details. You can even run access reviews for entitlements assigned to identities.
Organizations Count and details of Oracle Access Governance organizations associated with the selected identity.
Accounts Get count and account details associated with this identity. It gives you details like account name, the orchestrated system name associated with the account, resource name, how the access has been granted, password change status. When viewing access information for an entire enterprise from the Enterprise-wide Browser page, you can click the More actions icon to browse further or create access reviews.

When viewing your own accesses using the My Access menu option, if the account is provisioned within Oracle Access Governance and Password Change status flag is set to Applicable , then you can change your password. To do so, select Change password and follow the instructions to change your password.
Roles Count and details of roles assigned to this identity using the Oracle Access Governance Access Control framework. If you want to see the ingested roles available from Managed Systems, then see the Permissions tab.
Policies Count and details of policies used for granting access to the selected identity. You can further browse a policy to view policy statement details by selecting the View details link. The policies assigned can either be Oracle Access Governance policies or cloud policies ingested from OCI.
Violations Count and details of violations triggered by access guardrails. This includes all or open violations related to access requests either made by you or assigned to you. Select the View details link to view insights into specific security risk. Select the View access bundle details to view access bundle details that was requested.
Cloud Resources Count and cloud resource details that specify resource name, its type, the associated privilege granted to the identity along with the policy name that granted this privilege. You can also get insights on compartment and tenancy name for that resource. For further insights on resource, select the View details link where you can view reference count summary for that resource along with the pie charts showing the breakdown of identities (in percentage %) having access to the selected resource based on organization, job-code, and location.
Ownership Count and details of access controls components owned by this identity, such as identity collections, roles, policies,
Delegations Details of delegations set for this identity. Someone with the Enterprise-wide Access Administrator application role can view delegation details, but cannot edit them.
Identity Attributes Core and custom identity attributes along with its value. The attributes are logically sectioned under meaningful headings for relevancy.

## Identity Collections

While exploring access insights across an enterprise, you can choose Identity Collections as your perspective view. This gives you the ability to view access management information at a group level. You can view identity collections created within Oracle Access Governance or Oracle Cloud Infrastructure (OCI) groups ingested into Oracle Access Governance.

From the Identity Collections perspective view, you can view the following details:

Identity Collections Reference
Access Component Description
Access Summary For an identity collection, get access information, such as policies associated with this identity collection.
- For Oracle Cloud Infrastructure (OCI) Identity Collections, you can view details related to policy statements associated with each policy.
- For Oracle Access Governance Identity Collections, you can view policies and its association type like access bundles or role. Here, you can view the association details that lets you know the permissions and resources assigned to the selected identity collection. You can further navigate to view each component and its details.
Identities List of identities or members part of the selected identity collection. Select the View details link to get access details on each identity. Click the bar chart icon to view Member summary. Here, you can view the bifurcation of members in the identity collection based on source organization, organization, job code, location, or employee type.
Resources Get count and access information on resources associated with this identity collection. From the reference count summary section, click the resource count to view resource details, such as its name, type and number of identities having access to this resource. You can browse further to view details of each resource.
Access Bundles Get count and access information on access bundles associated with this identity collection. From the reference count summary section, click the Access bundles count to view its details, such as its name, granted permission type, its associated orchestrated system, resource and resource type. You can browse further to view details of each access bundle.
Policies Get count and access information on policies associated with this identity collection. From the reference count summary section, click the Policies count to view its details, such as its name, provider (OCI or Oracle Access Governance). owner, and so on. You can browse further to view association and reference details of each policy.
Roles Get count and access information on roles associated with this identity collection. From the reference count summary section, click the roles count to view its details, such as its name, who can request this role and its status. You can browse further to view access information and reference details of each role.

## Organizations

While exploring access insights across an enterprise, you can choose Organizations as your perspective view. You can view organizations created within Oracle Access Governance.

From the Organizations perspective view, you can view the following details:

Organizations Reference
Access Component Description
Organization Details For an organization, get its creation rules along with identity list part of this organization.
Identities List of identities or members part of the selected organization. Select the View details link to get access details on each identity. Click the bar chart icon to view Member summary. Here, you can view bifurcation of members in the organization based on source organization, organization, job code, location, or employee type.

## Permissions

While exploring access insights across an enterprise, you can choose Permissions as your perspective view. This gives you the ability to view available permissions, roles, access bundles associated with various resources.

From the Permissions perspective view, Granted permission type and Access Governance type determines what entity details you can view for Permissions. For example, for Access Governance type Access Bundle , you can view associated identities, identity collections, roles, and policies.

Permission Details
Access Governance Type Granted Permission Type Viewable Details
Access Bundle Access Bundle
Note  
  
Applicable for Oracle Access Governance access bundles.
- Identities
- Identity Collection
- Roles
- Policies
Role Role
Note  
  
Applicable for Oracle Cloud Infrastructure (OCI), and Oracle Identity Governance (OIG) roles. To view access details about Roles defined withinOracle Access Governance, select Roles as your perspective view. Identities
Permission Ingested permissions loaded from Managed systems and have not been provisioned using Oracle Access Governance, such as Permission, Privilege (applicable for Database systems), AD Group, and so on. Identities

Permissions Reference
Access Component Description
Identities Get count and list of identities who are assigned a specific role, entitlement or access bundle. From the reference count summary section, click the Identities to view a list of identities having access to the associated permission. Select the View details link to further browse each identity.
Policies Get count and access information on policies to which this access bundle is associated. From the reference count summary section, click the Policies count to view its details, such as its name, provider Oracle Access Governance), owner, and so on. You can browse further to view association and reference details of each policy.
Identity Collections Get count and access information on identity collections that has access to the selected access bundle. From the reference count summary section, click the Identity Collections count to view its details, such as its name, owner, member count, status and so on.
Roles Get count and access information on roles to which this access bundle is associated. From the reference count summary section, click the roles count to view its details, such as its name, who can request this role and its status. You can browse further to view access information and reference details of each role.

## Policies

While exploring access profile details for an enterprise, you can choose Policies as your perspective view. Here, you can browse through Oracle Access Governance policies and Oracle Cloud Infrastructure policies.

If you browse through an OCI policy, you will see OCI policy statements, Identities, Identity Collections (OCI groups), Resources, and if you browse through Oracle Access Governance policy, you will see Identities, Identity Collections, Resources, Access Bundles, and Roles.

Policies Reference
Access Component Description
Identities List of identities assigned permissions and resources through this policy. From the reference count summary section, click the Identities to view a list of identities having access to the associated policy. Select the View details link to further browse each identity.
Identity Collections List of identity collection assigned permissions and resources through this policy. From the reference count summary section, click the Identity collections to view a list of identity collections having access to the associated policy. Select the View details link to further browse each identity collection.
Access Bundles Get count and access information on access bundles associated with this policy. This is applicable only for Oracle Access Governance policy. From the reference count summary section, click the Access bundles count to view its details, such as its name, granted permission type, its associated orchestrated system, resource and resource type. You can browse further to view details of each access bundle.
Resources Get count of resources associated with this policy and resource details. From the reference count summary section, click the resource count to view resource details, such as its name, type and number of identities having access to this resource. You can browse further to view details of each resource.
Roles Get count and access information on roles associated with this policy. You can view the identities association details and to what they have access. From the reference count summary section, click the roles count to view its details, such as its name, who can request this role and its status. You can browse further to view access information and reference details of each role.

## Resources

While exploring access insights across an enterprise, you can choose Resources as your perspective view. This gives you the ability to view resource and its details ingested into Oracle Access Governance.

From the Resources perspective view, you can view the following details:

Resources Reference
Access Component Description
Identities List of identities or members having access to the selected resource. From the reference count summary section, click the Identities count link to view a list of identities having access to the associated policy. Select the View details link to further browse each identity.
Identity Collections Get count and access information on resources associated with this identity collection. From the reference count summary section, click the Resource count link to view resource details, such as its name, type and number of identities having access to this resource. You can browse further to view details of each resource.
Access Bundles Get count and access information on access bundles that associate this resource for granting access to identities. From the reference count summary section, click the Access bundles count link to view its details, such as its name, granted permission type, its associated orchestrated system, resource and resource type. You can browse further to view details of each access bundle.
Policies Get count and access information on policies granting access to this recource. From the reference count summary section, click the Policies count link to view its details, such as its name, provider (OCI or Oracle Access Governance). owner, and so on. You can browse further to view association and reference details of each policy.
Roles Get count and access information on roles having access to this resource. From the reference count summary section, click the Roles count link to view its details, such as its name, who can request this role and its status. You can browse further to view access information and reference details of each role.
Accounts Get count and access information on accounts having access to this resource. From the reference count summary section, click the Accounts count link to view its details.
Permissions Get count and access information on permissions available to manage different level of access for this resource. From the reference count summary section, click the Permissions count link to view its details.

## Roles

While exploring access insights across an enterprise, you can choose Roles as your perspective view. This gives you the ability to view roles created within Oracle Access Governance.

From the Roles perspective view, you can view reference count information along with the included access. Here are the following details:

Roles Reference
Access Component Description
Identities List of identities or members who are assigned a specific role. From the reference count summary section, click the Identities to view a list of identities having access to the associated policy. Select the View details link to further browse each identity.
Identity Collections Get count and access information on resources associated with this identity collection. From the reference count summary section, click the resource count to view resource details, such as its name, type and number of identities having access to this resource. You can browse further to view details of each resource.
Policies Get count and access information on policies associated with this identity collection. From the reference count summary section, click the Policies count to view its details, such as its name, provider (OCI or Oracle Access Governance). owner, and so on. You can browse further to view association and reference details of each policy.
