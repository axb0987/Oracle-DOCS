# IAM Tenancy and Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-IAM_Tenancy_and_Compartments.htm
- Fetched: 2026-09-05 03:04 CDT

# IAM Tenancy and Compartments

Learn how to use compartments to enhance security as well as recommendations for managing the administrators of a tenancy.
- Compartments are unique to IAM, and offer a mechanism that allows an enterprise customer to meet its central needs by having a single account or tenancy. This single account or tenancy provides full central control and visibility while also allowing the account or tenancy to be subdivided to meet the needs of constituent teams, projects, and initiatives.
- For security and governance reasons, users should only have access to resources they need. For example, enterprise users working on a project or belonging to a business unit should have access only to resources belonging to the project or business unit. Compartments provide an effective mechanism to group tenancy resources based on their access privileges and authorize groups of users to access the compartments on as needed basis. In the example above, a compartment can be created to include all resources belonging to a business unit, and authorize only members of the business unit to access the compartment. Similarly, a groups' access to a compartment can be revoked when they do not need it anymore.
- Keep the following in mind when you create a compartment and assign resources:
- Every resource should belong to a compartment.
- A resource can be reassigned to a different compartment after creation. See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
- A compartment can be deleted after creation. See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
- Resource tags provide a way to logically aggregate resources distributed across multiple compartments. For example, tenancy resources can be tagged as`test`or`production`depending on their use. For more information about resource tags (free-form and defined tags), see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Every tenancy comes with a default administrators group. This group can perform any action on all resources in a tenancy (that is, they have root access to the tenancy). Oracle recommends that you keep the group of tenancy administrators as small as possible. Some security recommendations on managing tenancy administrators:
- Have security policies granting membership of tenancy administrator group strictly on a as-needed basis.
- Tenancy administrators should use high-complexity passwords, along with MFA, and periodically rotate their passwords.
- After account set up and configuration, Oracle recommends that you don't use the tenancy administrator account for day-to-day operations. Instead, create less privileged users and groups.
- Though administrator accounts are not used for daily operations, they are still needed to address emergency scenarios impacting customer tenancy and operations. Specify secure and auditable "break-glass" procedures for using administrator accounts in such emergencies.
- Disable tenancy administration access immediately when an employee leaves the organization.
-
