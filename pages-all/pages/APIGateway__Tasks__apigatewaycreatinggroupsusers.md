# Create Groups and Users to Use API Gateway, if these don't exist already
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggroupsusers.htm
- Fetched: 2026-09-05 01:37 CDT

# Create Groups and Users to Use API Gateway, if these don't exist already

Find out how to create groups and users for use with API Gateway.

Before users can start using the API Gateway service to create API gateways and deploy APIs on them, as a tenancy administrator you have to create Oracle Cloud Infrastructure user accounts, along with a group to which the user accounts belong. Later on, you'll define policies to give the group (and the user accounts that belong to it) access to API Gateway-related resources. If a suitable group and user accounts already exist, there's no need to create new ones.

To create groups and users to use the API Gateway service:
- Log in to the Console as a tenancy administrator.
- If a suitable group for API Gateway users doesn't exist already, create such a group as follows:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select a domain, and select the User management tab. A list of the groups in the domain is displayed in the Groups section.
- Select Create group in the Groups section and create a new group (see[Creating a Group](https://docs.oracle.com/iaas/Content/Identity/groups/create-groups.htm)). Give the group a meaningful name (for example,`api-gateway-developers`) and description. Avoid entering confidential information.
- If suitable user accounts for API Gateway users don't exist already, create users as follows:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select a domain, and select the User management tab. A list of the users in the domain is displayed in the Users section.
- Select Create in the Users section and create one or more new users (see[Creating a User](https://docs.oracle.com/iaas/Content/Identity/users/create-user-accounts.htm)).
- If they haven't been added already, add users to the group to use the API Gateway service as follows:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select a domain, and select the User management tab.
- Add users to the group authorized to use the API Gateway service by selecting the name of the group in the Groups section, selecting the Users tab, and then selecting Assign user to group (see[Adding Users to a Group](https://docs.oracle.com/iaas/Content/Identity/groups/add-users-to-groups.htm)
