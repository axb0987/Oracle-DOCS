# IAM Users and Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-IAM_Users_and_Groups.htm
- Fetched: 2026-09-05 03:04 CDT

# IAM Users and Groups

Learn how to effectively manage users and groups for enhanced security.
- Create an IAM user for everyone in the customer organization who needs access to resources. Do not share IAM user accounts across multiple users, especially those with administrative accounts. Using distinct IAM users enables enforcing least privilege access for each user, and captures their actions in audit logs.
- The recommended unit of administration is IAM groups, which makes it easier to manage and keep track of security permissions (as opposed to individual users). Create IAM groups with permissions to do commonly needed tasks (for example, network administration, volume administration), and assign users to these groups on an as-needed basis. IAM permissions can be used to give a group access to resources across multiple compartments in a tenancy.
- Periodically review membership of IAM users in IAM groups, and remove IAM users from groups they do not need access to anymore. Using group membership to manage user access scales well with increasing number of users.
- Deactivate IAM users who do not need access to tenancy resources. Deleting an IAM user removes the user permanently. You can temporarily deactivate an IAM user by doing the following:
- Rotate the user password and throw it away.
-
