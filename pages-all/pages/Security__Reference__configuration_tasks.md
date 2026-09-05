# Addressing Basic Configuration Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm
- Fetched: 2026-09-05 03:04 CDT

# Addressing Basic Configuration Issues

This topic lists procedures to address common configuration issues that affect the security of your Oracle Cloud Infrastructure resources.

## Block Volume

[Block volume detached from instance](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: Ensure that only Oracle Cloud Infrastructure administrators can detach block volumes from instances.

Basics: When you detach a block volume it decouples the volume from its associated instance, affecting the data available to the instance. This could impact data availability from business-critical data to the successful completion of scheduled volume backups. To minimize loss of data due to inadvertent volume detachments by an authorized user or malicious volume detachments you should restrict the`VOLUME_ATTACHMENT_DELETE`permission to administrators.

To prevent detachment of block volumes:

The following policy allows the group`VolumeUsers`to manage volumes and volume attachments except for detaching volumes:

```

```

This change prevents`VolumeUsers`from detaching volumes from instances.

More information:
- [Securing Block Volume](https://docs.oracle.com/iaas/Content/Security/Reference/blockstorage_security.htm)
- [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)
- [How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm)
- [For volume-family Resource Types](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm#For3)

## Compute

[Instance created based on unapproved custom image](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: An instance was created from a custom image that is unsupported in your environment.

Basics: When users create instances they can select from platform images, boot volumes from terminated instances, or custom images. Custom images represent a wide variety of images which can include images that aren't approved for your environment. If you use tags in your Oracle Cloud Infrastructure tenancy to identify approved images, verify whether the image the instance is based on is an approved image and terminate the instance if necessary.

To verify the tags for the image the instance was created from:

The following procedure is for the Oracle Cloud Infrastructure Console.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Click the instance you're interested in.
- Click the Image link to view the source image.
- Click the Tags tab to view the tags applied to this image.

If the custom image does not have an approved tag, and the instance needs to be terminated, see[Terminating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/terminatinginstance.htm).

More information:
- [Securing Compute](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm)
- [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
- [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)
- [Image Import/Export](https://docs.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm)
- [Bring Your Own Image (BYOI)](https://docs.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm)

## IAM

[Member of the Administrators group used API keys](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A user who is a member of the Administrators group accessed resources using an API key.

Basics:
- API keys are credentials used to grant programmatic access to Oracle Cloud Infrastructure.
- 

For security and governance reasons, users should only have access to resources they need to interact with.
- For individuals who are members of the Administrators group who also need access to resources through the API, create another user in IAM to which you attach the API keys. Grant the user with the API keys permissions to only the resources they need to interact with programmatically.

To create a user, group, and policy with limited permissions:

The following set of procedures shows you how to set up an example user with limited permissions. In this example, the user needs to be able to launch instances in a specific compartment.

The following procedure is for the Oracle Cloud Infrastructure Console.

[Create a User](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Users .
- Click Create User .
- 

In the Create User dialog:
- Name : Enter a unique name or email address for the new user. The value will be the user's login to the Console and must be unique across all other users in your tenancy.
- Description : Enter a description (required).
- Click Create .

[Create a Group](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Next, create the group ("InstanceLaunchers" ) that you will create the policy for.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Click Create Group .
- 

In the Create Group dialog:
- 

Name: Enter a unique name for your group, for example, "InstanceLaunchers".

Note that the name cannot contain spaces.
- Description: Enter a description (required).
- Click Create .

[Create a Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

In this example, the policy grants members of the group InstanceLaunchers permissions to launch instances in a specific compartment (CompartmentA).
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .
- Click Create Policy .
- 

Enter a unique Name for your policy, for example, "InstanceLaunchersPolicy".

Note that the name cannot contain spaces.
- Enter a Description (required), for example, "Grants users permission to launch instances in CompartmentA".
- Click Show manual editor and enter this statement:
```

```

This statement grants members of the InstanceLaunchers group permissions to launch and manage instances in the compartment called CompartmentA.
- Click Create .

[Add the User to the Group](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Users .
- In the Users list, find the user and click the name.
- 

On the user detail page, click Groups (on the left side of the page). The list of groups that the user belongs to is displayed.
- Click Add User to Group.
- From the Groups list, select InstanceLaunchers.
- Click Add .

[Upload an API signing key for the user](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

The following procedure works for a regular user or an administrator. Administrators can upload an API key for either another user or themselves.
Important  
  

The API key must be an RSA key in PEM format (minimum 2048 bits) . The PEM format looks something like this:

```

```

For more information about generating a public PEM key, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).
- View the user's details:
- If you're uploading an API key for yourself : In the navigation menu , select the Profile menu and then select User settings .
- If you're an administrator uploading an API key for another user : In the Console, click Identity , and then click Users . Locate the user in the list, and then click the user's name to view the details.
- Click Add API Key , and then select Paste API Key .
- 

Paste the key's value into the window and click Add .

The key is added and its fingerprint is displayed (example fingerprint: d1:b2:32:53:d3:5f:cf:68:2d:6f:8b:5f:77:8f:07:13).

More information:
- [Securing IAM](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security.htm)
- [How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
- [Managing User Credentials](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm)
- [Managing Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm)
- [Managing Users](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm)

[Policy grants broad permissions](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A policy grants full management permissions for at least one service in a compartment or in the tenancy.

Basics:
- Access to resources is controlled through policies. A policy is a document that specifies who can access which Oracle Cloud Infrastructure resources that your company has, and how. A policy simply allows a group to work in certain ways with specific types of resources in a particular compartment .
- For security and governance reasons, users should only have access to resources they need.
- Consider carefully the access level a user needs. Policy language provides a default set of verbs (`manage`,`use`,`read`,`inspect`) that allow you to easily scope users' permissions to a set of common tasks. For example, if a user needs to be able to update resources, but does not need to create or delete them, grant them the`use`permission, rather than the`manage`permission.
- 

The policy language is designed to let you write simple statements involving only verbs and resource-types, without having to state the permissions in the statement. For more fine-grained access control, you can use conditions combined with permissions or API operations to reduce the scope of access granted by a particular verb.
- Wherever possible, scope access to the specific compartments a user needs access to, rather than scoping it to the full tenancy.

Tips for writing least-privilege policies:

[Scope the policy to a compartment instead of the tenancy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Each policy consists of one or more policy statements that follow a basic syntax. Where possible, scope policies to compartments, rather than to the tenancy. For example, update a policy like this:
```

```

to include just the compartments needed:
```

```

If the user needs access to multiple compartments, create a policy statement for each compartment. It is then easy to remove access to individual compartments, if necessary.

[Scope permissions to those required to perform a job function](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Oracle defines the possible verbs you can use in your policies. Here's a summary of the verbs, from least amount of access to the most:

Verb Types of Access Covered Target User
`inspect`Ability to list resources, without access to any confidential information or user-specified metadata that may be part of that resource. Third-party auditors
`read`Includes`inspect`plus the ability to get user-specified metadata and the actual resource itself. Internal auditors
`use`Includes`read`plus the ability to work with existing resources (the actions vary by resource type). In general, this verb does not include the ability to create or delete that type of resource. Day-to-day end users of resources
`manage`Includes all permissions for the resource. Administrators

Users who don't need to create or delete resources generally don't need manage permissions. If you have a policy like
```

```

but the user will never create or delete the resource-type, consider rewriting the policy to
```

```

The[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm)includes details of the specific resource-types for each service, and which verb + resource-type combination gives access to which API operations.

[Service-specific links](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

- [Details for the Audit Service](https://docs.oracle.com/iaas/Content/Identity/Reference/auditpolicyreference.htm)
- [Details for Kubernetes Engine](https://docs.oracle.com/iaas/Content/Identity/policyreference/contengpolicyreference.htm)
- [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm)(this includes Networking, Compute, and Block Volume)
- [Details for the Database Service](https://docs.oracle.com/iaas/Content/Identity/Reference/databasepolicyreference.htm)
- [DNS Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/dnspolicyreference.htm)
- [Details For the Email Delivery Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/emailpolicyreference.htm)
- [Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm)
- [Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm)
- [Details for Load Balancing](https://docs.oracle.com/iaas/Content/Identity/policyreference/lbpolicyreference.htm)
- [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm)
- [Details for Container Registry](https://docs.oracle.com/iaas/Content/Identity/Reference/registrypolicyreference.htm)
- [Details for the Search Service](https://docs.oracle.com/iaas/Content/Identity/Reference/searchpolicyreference.htm#Details_for_Search)

[For fine-grained access control, scope access using conditions and API operations](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

In a policy statement, you can use[conditions](https://docs.oracle.com/iaas/Content/Identity/policiesadvfeatures/policyadvancedfeatures.htm#conditions)combined with permissions or API operations to reduce the scope of access granted by a particular verb.

For example, let's say you want group XYZ to be able to list, get, create, or update groups (change their description), but not delete them. To list, get, create, and update groups, you need a policy with`manage groups`as the verb and resource-type. According to the table in[Details for Verbs + Resource Type Combinations](https://docs.oracle.com/iaas/Content/application-dependency-management/concepts/verbs-resource-type.htm), the permissions covered are:
- GROUP_INSPECT
- GROUP_UPDATE
- GROUP_CREATE
- GROUP_DELETE

To restrict access to only the desired permissions, you could add a condition that explicitly states the permissions you want to allow :

```

```

An alternative would be a policy that allows all permissions except GROUP_DELETE:

```

```

Another alternative would be to write a condition based on the specific API operations . Notice that according to the table in[Permissions Required for Each API Operation](https://docs.oracle.com/iaas/Content/application-dependency-management/concepts/permissions-required.htm), both`ListGroups`and`GetGroup`require only the GROUP_INSPECT permission. Here's the policy:

```

```

It can be beneficial to use permissions instead of API operations in conditions. In the future, if a new API operation is added that requires one of the permissions listed in the permissions-based policy above, that policy will already control XYZ group's access to that new API operation.

But notice that you can further scope a user's access to a permission by also specifying a condition based on API operation. For example, you could give a user access to GROUP_INSPECT, but then only to`ListGroups`.

```

```

More information:
- [Securing IAM](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security.htm)
- [How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
- [Advanced Policy Features](https://docs.oracle.com/iaas/Content/Identity/policiesadvfeatures/policyadvancedfeatures.htm)
- [Managing Policies](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm)

[API signing keys over 90 days old](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A user's API signing keys are older than 90 days. Oracle recommends that you rotate API keys at least every 90 days.

Basics:
- API keys are credentials used to grant programmatic access to Oracle Cloud Infrastructure.
- 

It is a security engineering best practice and compliance requirement to rotate API keys regularly, every 90 days or less.
- Ensure that you test the new keys before you deactivate the old keys.

To generate and upload new API keys:

The following procedure is for the Oracle Cloud Infrastructure Console.

[Generate new API keys](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

You can use the following[OpenSSL](http://www.openssl.org/)commands to generate the key pair in the required PEM format. If you're using Windows, you'll need to install[Git Bash for Windows](https://git-scm.com/download/win)and run the commands with that tool.
- 

If you haven't already, create a`.oci`directory to store the credentials:
```

```

- 

Generate the private key with one of the following commands.
- 

Recommended: To generate the key, encrypted with a passphrase you provide when prompted:

```

```

Note: For Windows, you may need to insert`-passout stdin`to be prompted for a passphrase. The prompt will just be the blinking cursor, with no text.

```

```

- 

To generate the key with no passphrase:

```

```

- 

Ensure that only you can read the private key file:

```

```

- 

Generate the public key:

```

```

Note: For Windows, if you generated the private key with a passphrase, you may need to insert`-passin stdin`to be prompted for the passphrase. The prompt will just be the blinking cursor, with no text.

```

```

- 

Copy the contents of the public key to the clipboard using pbcopy, xclip or a similar tool (you'll need to paste the value into the Console later). For example:

```

```
Your API requests will be signed with your private key, and Oracle will use the public key to verify the authenticity of the request. You must upload the public key to IAM (instructions below).

[Get the key's fingerprint](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

You can get the key's fingerprint with the following OpenSSL command.

For Linux and Mac OS X:
```

```

For Windows:
Note  
  
If you're using Windows, you need to install[Git Bash for Windows](https://git-scm.com/download/win)and run the command with that tool.
```

```

When you upload the public key in the Console, the fingerprint is also automatically displayed there. It looks something like this: 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef

[Upload the API signing key for the user](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

You can upload the PEM public key in the Console, located at[https://cloud.oracle.com](https://cloud.oracle.com). If you don't have a login and password for the Console, contact an administrator.
- Open the Console, and sign in.
- 

View the details for the user who will be calling the API with the key pair:
- If you're signed in to the Console as this user: In the navigation menu , select the Profile menu and then select User settings .
- If you're an administrator doing this for another user : Open the navigation menu and select Identity &amp; Security . Under Identity , select Users . Locate the user in the list, and then select the user's name to view the details.
- Select Select API Keys .
- Select Add API Key .
- Select Paste Public Key
- Paste the contents of the PEM public key in the dialog box and select Add . The key's fingerprint is displayed (for example, 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef). Notice that after you've uploaded your first public key, you can also use the[UploadApiKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/UploadApiKey)API operation to upload additional keys. You can have up to three API key pairs per user. In an API request, you specify the key's fingerprint to indicate which key you're using to sign the request.

[Test the new key](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Test the key in a sample API call against Oracle Cloud Infrastructure.

[Delete the old key](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

The following procedure works for a regular user or an administrator. Administrators can delete an API key for either another user or themselves.
- View the user's details:
- If you're deleting an API key for yourself : In the navigation menu , select the Profile menu and then select User settings .
- If you're an administrator deleting an API key for another user : Open the navigation menu and select Identity &amp; Security . Under Identity , select Users . Locate the user in the list, and then select the user's name to view the details.
- Select API Keys .
- Select the Actions menu (three dots) for the API key you want to delete, and then select Delete .
- Confirm when prompted. The API key is no longer valid for sending API requests.

More information:
- [Securing IAM](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security.htm)
- [API Signing Key](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm#API)

[Tenancy administrator privilege grant to an IAM group](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A group other than the Administrators group has been granted administrator privileges.

Basics:
- Granting the tenancy administrator privilege (`manage all-resources in tenancy`) to a group enables the members to have full access to all resources in the tenancy.
- This high-privilege entitlement must be controlled and restricted to only the users who need it to perform their job function.
- Verify with the Oracle Cloud Infrastructure administrator that this entitlement grant was sanctioned and that the membership of the group remains valid after the grant of the administrator privilege.
- Rather than create an alternative group with administrator privileges, consider instead adding users needing administrator privileges to the default Administrators group.

To resolve this issue:

Add users who need administrator privileges to the Administrators group:

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- In the Groups list, select Administrators .
- Select Add User to Group .
- In the Add User to Group dialog, select the user from the User list.
- Select Add .

Remove the policy or policy statement that grants the (non-Administrators) group administration privileges.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.

If you don't see the policy you're looking for, verify that you're viewing the correct compartment. To view policies attached to a different compartment, under List scope , select that compartment from the list.
- Click the policy you want to update.

The policy's details and statements are displayed.
- 

Find the statement that grants administrator privileges to the group. This policy will look like:
```

```

Click the the Actions menu (three dots) and then click Delete .
- If the policy has no other statements, you can delete the policy by clicking Delete next to the policy name.

More information:
- [Securing IAM](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security.htm)
- [Managing Policies](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm)

## Networking: VCN, Load Balancers, and DNS

[No ingress rules in security lists](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A VCN's security lists have no ingress rules. This means that the instances in the VCN can't receive incoming traffic.

Basics:

- Security lists provide stateful and stateless firewall capability to control network access to Compute instances.
- A security list is configured at the subnet level and enforced at the instance level.
- You can associate several security lists with a subnet. A packet is allowed if it matches any rule in any of the security lists used by the subnet.
- If there are no ingress (inbound) rules in any of the subnet's security lists, no traffic is allowed to the instances in that subnet.
- For defense in depth, we recommend that ingress security list rules state a specific known source and not an open source`(0.0.0.0/0)`.
- You can configure an exception in Oracle CASB Cloud Service to reduce alerts from exempted security lists.

To add an ingress rule to an existing security list:

The following procedure is for the Oracle Cloud Infrastructure Console.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Confirm you're viewing the compartment that contains the cloud network you're interested in.
- Click the cloud network you're interested in.
- Click Security Lists .
- Click the security list you're interested in.
- Click Ingress Rules .
- 

Add at least one ingress rule:
- Click Add Ingress Rules .
- Choose whether it's a stateful or stateless rule (see[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful)). By default, rules are stateful unless you specify otherwise.
- Enter the source CIDR. Typical CIDRs you might specify in a rule are the CIDR block for your on-premises network or a particular subnet. If you're setting up a security list rule to allow traffic with a service gateway , instead see[Task 3: (Optional) Update security rules](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm#task_update_security_list).
- Select the protocol (for example, TCP, UDP, ICMP, "All protocols", and so on).
- Enter further details depending on the protocol:
- If you chose TCP or UDP, enter a source port range and destination port range. You can enter "All" to cover all ports. If you want to allow a specific[port](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), enter the port number (for example, 22 for SSH or 3389 for RDP) or a port range (for example, 20-22).
- If you chose ICMP, you can enter "All" to cover all types and codes. If you want to allow a specific[ICMP type](http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml), enter the type and an optional code separated by a comma (for example, 3,4). If the type has multiple codes you want to allow, create a separate rule for each code.
- When you're done, click Add Ingress Rules .

This change enables ingress access from the source CIDR block listed in the rule. Add additional rules if you want to allow ingress from other known sources.

More information:
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm)
- [Parts of a Security Rule](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts)
- [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)
- [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList)

[Security list allows traffic from any IP address (open source)](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A security list has at least one rule with an open source (0.0.0.0/0). This means that traffic could come from any source and is not controlled.

Basics:

- Security lists provide stateful and stateless firewall capability to control network access to Compute instances.
- A security list is configured at the subnet level and enforced at the instance level.
- You can associate several security lists with a subnet. A packet is allowed if it matches any rule in any of the security lists used by the subnet.
- If there are no ingress (inbound) rules in any of the subnet's security lists, no traffic is allowed to the instances in that subnet.
- For defense in depth, we recommend that ingress security list rules state a specific known source and not an open source`(0.0.0.0/0)`.
- You can configure an exception in Oracle CASB Cloud Service to reduce alerts from exempted security lists.

To change the source of a security list rule:

The following procedure is for the Oracle Cloud Infrastructure Console.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Confirm you're viewing the compartment that contains the cloud network you're interested in.
- Click the cloud network you're interested in.
- Click Security Lists .
- Click the security list you're interested in.
- Click Ingress Rules .
- Locate the rule that lists 0.0.0.0/0 as the source CIDR.
- Edit the rule and change 0.0.0.0/0 to the CIDR block of a known source.

This change restricts ingress so packets are allowed only from a specific CIDR block. Add additional rules if you want to allow ingress from other known sources.

More information:
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm)
- [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)
- [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList)

[Security list allows traffic to sensitive ports](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A security list has at least one rule that enables access to a sensitive port.

Basics:

- Security lists provide stateful and stateless firewall capability to control network access to Compute instances.
- A security list is configured at the subnet level and enforced at the instance level.
- You can associate several security lists with a subnet. A packet is allowed if it matches any rule in any of the security lists used by the subnet.
- If there are no ingress (inbound) rules in any of the subnet's security lists, no traffic is allowed to the instances in that subnet.
- For defense in depth, we recommend that ingress security list rules state a specific known source and not an open source`(0.0.0.0/0)`.
- You can configure an exception in Oracle CASB Cloud Service to reduce alerts from exempted security lists.

Recommendation: Update the subnet's security list to enable access to instances through SSH (TCP port 22) or RDP (TCP port 3389) on a temporary, as-needed basis, and only from authorized CIDR blocks (not 0.0.0.0/0). To perform instance health checks, update the security list to allow ICMP pings.

To change an existing security list:

The following procedure is for the Oracle Cloud Infrastructure Console.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Confirm you're viewing the compartment that contains the cloud network you're interested in.
- Click the cloud network you're interested in.
- Click Security Lists .
- Click the security list you're interested in.
- Click Ingress Rules .
- Make one or more of these changes:
- Delete an existing rule.
- Change an existing rule in the list. For example: change the source from 0.0.0.0/0 to the CIDR block of a known source.
- Add a new rule.

More information:
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm)
- [To enable RDP access](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm#prerequisites__enablerdp)
- [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)
- [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList)

[Internet gateway attached to VCN](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A VCN has an internet gateway. The gateway must be authorized to be attached to the VCN and must not unintentionally expose resources to the internet.

Basics:
- Gateways provide external connectivity to hosts in a VCN. For example: an internet gateway enables direct internet connectivity for instances that are in a public subnet and have a public IP address. A dynamic routing gateway (DRG) enables connectivity with the on-premises network over an[Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm)or[FastConnect.](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm)
- To enable traffic through the internet gateway from a particular subnet in the VCN, there must be a rule in the subnet's route table that lists the internet gateway as a route target. To delete the internet gateway from the VCN, you must first delete any route rules that specify the internet gateway as the target.
- You can configure an exception in Oracle CASB Cloud Service to reduce alerts from exempted VCNs.

To remove an internet gateway from a VCN:

Prerequisite: Ensure that there are no route rules that specify the internet gateway as a target.

The following procedure is for the Oracle Cloud Infrastructure Console.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Confirm you're viewing the compartment that contains the cloud network you're interested in.
- Click the cloud network you're interested in.
- Click Internet Gateways .
- Click the Actions menu (three dots) for the internet gateway, and then click Terminate .
- Confirm when prompted.

This change disables direct internet connectivity for the VCN.

More information:
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm)
- [Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm)
- [DeleteInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/DeleteInternetGateway)
- [Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm)

[Instance has a public IP](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: An instance has a public IP address. This means the instance could be publicly addressable if other required components are present and configured correctly in the VCN.

Basics:
- Carefully consider allowing internet access to any instances. For example, don't accidentally allow internet access to sensitive DB systems.
- 

For an instance to be publicly addressable:
- The instance must have a public IP address and reside in a public subnet in the VCN (instances in private subnets cannot have public IP addresses).
- The subnet's security list must be configured to allow traffic for all IPs (0.0.0.0/0) and all ports.
- The VCN must have an internet gateway and be configured to route outbound traffic from the subnet to the internet gateway.
- An instance can have more than one public IP address. A given public IP is assigned to a private IP on a particular VNIC on the instance. An instance can have more than one VNIC, and each VNIC can have more than one private IP.

To remove a public IP address from an instance:

The following procedure is for the Oracle Cloud Infrastructure Console.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Confirm you're viewing the compartment that contains the instance you're interested in.
- Click the instance to view its details.
- 

Click Attached VNICs .

The primary VNIC and any secondary VNICs attached to the instance are displayed.
- 

Click the VNIC you're interested in.
- Click IPv4 Addresses .

The VNIC's primary private IP and any secondary private IPs are displayed.
- For the private IP you're interested in, click the Actions menu (three dots) , and then click Edit .
- In the Public IP Address section, for Public IP Type , select the radio button for No Public IP .
- Click Update .

The public IP is unassigned from the instance.

More information:
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm)
- [Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm)
- [DeletePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/DeletePublicIp)
- [Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm)

[Load balancer has no inbound rules or listeners](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A load balancer's subnet security lists have no ingress rules, or a load balancer has no listener. In this case, the load balancer can't receive incoming traffic.

Basics:
- Load balancers provide automated traffic distribution from one entry point to multiple servers reachable from your virtual cloud network (VCN). Each load balancer exists in a subnet governed by security list rules. A load balancer receives incoming data traffic from one or more listeners.
- Security lists provide stateful and stateless firewall capability to control network access to your load balancer and backend servers.
- If there are no ingress (inbound) rules in any of the subnet's security lists, no traffic is allowed to the instances in that subnet.
- For defense in depth, configure ingress security list rules to state a specific known source and not an open source (0.0.0.0/0).
- A listener is a logical entity that checks for incoming traffic on the load balancer's IP address.
- To handle TCP, HTTP, and HTTPS traffic, you must configure at least one listener per traffic type.
- You can apply path route rules to a listener to route traffic to the correct backend set without using multiple listeners or load balancers. A path route is a string that the listener matches against an incoming URI to determine the appropriate destination backend set.
- Ensure that your Oracle Cloud Infrastructure load balancers use inbound rules or listeners to allow access only from known resources.
- Exceptions can be configured in CASB to reduce alerts from exempted load balancers.
To enable a listener to accept traffic:

The following procedure is for the Oracle Cloud Infrastructure Console.

To enable a listener to accept traffic, you must update your VCN's security list rules:

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Under List Scope , select a compartment that you have permission to work in. The list of VCNs in the current compartment appears.
- Select the name of the VCN containing your load balancer, and then select Network security groups or Security lists . A list of the security groups or lists in the cloud network appears.
- Select the name of the NSG or security list that applies to your load balancer.
- Add or edit the existing rules to give access from the appropriate resources. An NSG's security rules appear on the Network security group details page. From there you can add, edit, or remove rules. The Security list details page provides access to separate tables in which you can add or edit Ingress rules or Egress rules . For details on rule configuration, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).

To create a listener:

Usually, you create a listener as part of the load balancer creation workflow. To create a listener for an existing load balancer:

- Under Load balancers , select Load balancer .

The Load balancers list page opens. All existing load balancer resources in the selected compartment are displayed in a list table.
- To view the resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Select a State from the list to limit the load balancers displayed to that state.
- Select the load balancer for which you want to create a listener. The load balancer's Details page appears.
- Select Listeners under Resources . The Listeners list appears. All listeners are listed in tabular form.
- Select Create listener . The Create listener dialog box appears.
- Complete the following:
- Name : Enter a friendly name for the listener. The name must be unique, and can't be changed.
- Hostname : (Optional) Select up to 16 virtual hostnames for this listener.
Note  
  
To apply a virtual hostname to a listener, the name must be part of the load balancer's configuration. If the load balancer has no associated hostnames, you can create one on the Hostnames page. See[Virtual Hostnames for Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Tasks/hostname_management.htm)for more information.
- Protocol : Specify the protocol to use: HTTP , HTTP/2 , TCP , or HTTPS .
- Port : Specify the port on which to listen for incoming traffic.
- Use SSL : (Required for HTTP/2 and HTTPS, optional for HTTP and TCP) Select to enable. The following settings are required to associate an SSL certificate bundle with the listener to enable SSL handling. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information on using SSL certificates with load balancers.

The load balancer automatically detects changes and consumes the current version of the Certificates service entities (certificates, certificate authorities, and CABundles) for use in SSL configuration. See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for more information on automated certificate rotations.
- Certificate resource : Select the certificate resource type from the list:

The method of importing the certificate varies depending on the certificate resource type you select.

Certificate service managed certificate : Select the certificate in the specified compartment from the Certificate list. Select Change compartment to choose a different compartment from where to select the certificate.
- Advanced options are available with this selection. Select Show advanced options and select the Advanced SSL tab. This option is described later in this topic.
- Load balancer managed certificate : Select one of these options to import the certificate:

Choose SSL certificate file : Drag the certificate file, in PEM format, into the SSL certificate field. You can also choose the Paste SSL certificate option to paste a certificate directly into this field. If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.

Specify private key : (Required for SSL termination, optional for all else) Select box to provide a private key for the certificate.

Choose private key file : Drag the private key, in PEM format, into the Private key field. You can also choose the Paste private key option to paste a private key directly into this field.

Enter private key passphrase : (Optional) Specify the private key passphrase.
- Enable session resumption : Select to resume the previous encryption session rather than complete a new SSL connection before each request. Enabling session resumption improves performance but provides a lower level of security. De-select the feature to force a new SSL connection before each request. Disabling session resumption improves security but reduces performance.
- Verify peer certificate : (Optional) Select this option to enable peer certificate verification. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information.

Mutual TLS (mTLS) isn't supported for communication between a load balancer and its backend servers. You can use mTLS for communication between load balancers and users.
- Verify depth : (Optional) Specify the maximum depth for certificate chain verification. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information.
- Backend set : Specify the default backend set to which the listener routes traffic.
- Idle timeout in seconds : (Optional) Specify the maximum idle time in seconds. This setting applies to the time allowed between two successive receive or two successive send network input/output operations during the HTTP request-response phase. The maximum value is 7200 seconds. For more information, see[Load Balancer Timeout Connection Settings](https://docs.oracle.com/iaas/Content/Balance/Reference/connectionreuse.htm).
- (Optional) Select the Proxy Protocol tab to enable and configure proxy protocol on the load balancer. See[Proxy Protocol](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm#proxy-protocol)for more information on this feature.
- Select Enable Proxy Protocol to enable this feature.
- Select which proxy protocol version you want to use:
- Version 1 : Supports a human-readable header (text) format and is typically a single line of a log entry. Use this option for debugging during the early adoption stage when few implementations exist.
- Version 2 : Combines support for the human-readable header from Version 1 with a binary encoding of the header for greater efficiency in producing and parsing. Use this option for IPv6 addresses, which are difficult to generate and parse in ASCII form. Version 2 also better supports custom extensions. By default, PP2 Type Authority is selected as the only Version 2 option available.
- Select either a Routing policy or a Path route set .
- Routing policy : (Optional) Specify the name of the routing policy that applies to this listener's traffic.
- Path route set : (Optional) Specify the name of the set of path-based routing rules that applies to this listener's traffic.

To apply a[path route set](https://docs.oracle.com/iaas/Content/Balance/Tasks/path-route-set_management.htm)to a listener, the path route set must be part of the load balancer's configuration.

To remove a path route set from an existing listener, choose None as the Path Route Set option. The path route set remains available for use by other listeners on this load balancer.
- Rule sets : (Optional) Select a[rule set](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrulesets.htm)to apply to this listener's traffic. To apply a rule set to a listener, the set must be part of the load balancer's configuration. To remove a rule set from the list, select the corresponding red box. The rule set remains available for use by other listeners on this load balancer.
- Show advanced options : Select to display the following options:
- Advanced SSL : (Only present if the Certificate Service Managed Certificate certificate resource is selected.) Select one of these options if you picked Certificate Service Managed Certificate when selecting the certificate resource for the listener.

CA bundle : Select the certificate authority bundle in the specified compartment from the list. Select Change compartment to choose a different compartment from where to select the certificate authority bundle.

Certificate authority : Select the certificate authority in the specified compartment from the list. Select Change compartment to choose a different compartment from where to select the certificate authority bundle.
- TLS version : Specify the Transport Layer Security (TLS) versions: 1.0 , 1.1 , 1.2 (recommended), and 1.3 .

You can select any combination of versions. Choose the ones you want from the list. If you do not specify the TLS versions, the default TLS is version 1.2 only.

Select cipher suite : Select a set of cipher suites from the list. (default). All choices present in the list have at least one cipher associated with each TLS version you selected.

Create an SSL certificate using the signing algorithm that's based on the ciphers that are enabled for your security policy.
- Show cipher suite details : Select to display the individual ciphers the selected cipher suite contains.
- Server order preference : Select Enable to give preference to the server ciphers over the client.
- Select Create listener .

When you create a listener, you must also[update your VCN's security list rules](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#lb-enable-traffic)to allow traffic to that listener.

More information:
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm)
- [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)
- [Load Balancer Management](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm)
- [Listeners for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm)
- [Request Routing for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm)

[Load balancer has no backend sets](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A load balancer has no backend set. In this case, the load balancer has no place to distribute incoming data and no means to monitor backend server health.

Basics:
- A backend set is a logical entity defined by a load balancing policy, a health check policy, and a list of backend servers.
- The backend set determines the load balancer's traffic distribution policy, such as:
- IP Hash
- Least Connections
- Weighted Round Robin
- You specify the test parameters to confirm the health of backend servers when you create a backend set.
- If you have an existing load balancer with no backend set, you can specify the backend servers that receive traffic from the load balancer after you create a backend set.
- You can configure an exception in Oracle CASB Cloud Service to reduce alerts from exempted load balancers.

To create a backend set:

The following procedure is for the Oracle Cloud Infrastructure Console.

Usually, you create a backend set as part of the load balancer creation workflow. To create a backend set for an existing load balancer:

- Under Load balancers , select Load balancer .

The Load balancers list page opens. All existing load balancer resources in the selected compartment are displayed in a list table.
- To view the resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Select a State from the list to limit the load balancers displayed to that state.
- Select the load balancer to which you want to add a backend set. The load balancer's Details page appears.
- Select Backend sets under Resources . The Backend sets list appears. All backend sets are listed in tabular form.
- Select Create backend set . The Create backend set dialog box appears.
- 

Complete the following:
- Name : Enter a friendly name for the backend set. It must be unique within the load balancer, and it can't be changed. Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names can't contain spaces.
- Traffic distribution policy : Select the load balancer policy for the backend set. The available options are:
- IP hash
- Least connections
- Weighted round robin

You can't add a backend server marked as Backup to a backend set that uses the IP Hash policy. For more information on these policies, see[Load Balancer Policies](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).
- Use SSL : Select to associate an SSL certificate resource with the backend set.

The load balancer automatically detects changes and consumes the current version of the Certificates service entities (certificates, certificate authorities, and CABundles) for use in SSL configuration. See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for more information on automated certificate rotations.

If no certificate resources attached to the load balancer exist, this option is disabled.

Certificate resource : Select the certificate resource type from the list:

The method of importing the certificate varies depending on the certificate resource type you select. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for information on how load balancers use SSL certificates.

See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for general information on using SSL with your web application firewall policy.
- Certificate service managed certificate

Select the CA bundle or Certificate authority option, and then select your choice from the associated list. Select Change compartment to choose a different compartment from which to select the CA bundle or certificate authority.

Advanced options are available with this selection. Select Show advanced options and select the Advanced SSL tab. This option is described later in this topic.
- Load balancer managed certificate : Select one of these options to import the certificate:

Choose SSL certificate file : Drag the certificate file, in PEM format, into the SSL certificate field. You can also choose the Paste SSL certificate option to paste a certificate directly into this field.

If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.

Specify private key : (Required for SSL termination.) Select to provide a private key for the certificate.

Choose private key file : Drag the private key, in PEM format, into the Private key field.

Enter private key passphrase : Specify the private key passphrase. Alternatively, you can choose the Paste private key option to paste a private key directly into this field.

Verify peer certificate : Select this option to enable peer certificate verification. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information.

Verify depth : Optional. Specify the maximum depth for certificate chain verification. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information.
- Session persistence : Specify how the load balancer manages session persistence. See[Load Balancer Session Persistence](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm)for important information on configuring these settings.
- Disable session persistence : Choose this option to disable cookie-based session persistence.
- Enable application cookie persistence : Choose this option to enable persistent sessions from a single logical client when the response from a backend application server includes a`Set-cookie`header with the cookie name you specify.
- Cookie name : The cookie name used to enable session persistence. Specify * to match any cookie name.
- Disable fallback : Check this box to disable fallback when the original server is unavailable.
- Enable load balancer cookie persistence : Choose this option to enable persistent sessions based on a cookie inserted by the load balancer.
- Cookie name : Specify the name of the cookie used to enable session persistence. If blank, the default cookie name is`X-Oracle-BMC-LBS-Route`.

Ensure that any cookie names used at the backend application servers are different from the cookie name used at the load balancer.
- Disable fallback : Check this box to disable fallback when the original server is unavailable.
- Domain name: : Specify the domain in which the cookie is valid.

This attribute has no default value. If you don't specify a value, the load balancer doesn't insert the domain attribute into the`Set-cookie`header.
- Path : Specify the path in which the cookie is valid. The default value is`/`.
- Expiration period in seconds : Specify the amount of time the cookie remains valid. If blank, the cookie expires at the end of the client session.
- Attributes

Secure : Specify whether the`Set-cookie`header contains the`Secure`attribute. If selected, the client sends the cookie only using a secure protocol.

If you enable this setting, you can't associate the corresponding backend set with an HTTP listener.

HTTP only : Specify whether the`Set-cookie`header contains the`HttpOnly`attribute. If selected, the cookie is limited to HTTP requests. The client omits the cookie when providing access to cookies through non-HTTP APIs such as JavaScript channels.
- Health check : Specify the test parameters to confirm the health of backend servers.
- Protocol : Specify the protocol to use, either HTTP or TCP. Configure your health check protocol to match your application or service. See[Health Checks for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/load_balancer_health_management.htm)for more information.
- Port : (Optional) Specify the backend server port against which to run the health check. You can enter the value 0 to have the health check use the backend server's traffic port.
- Force plaintext health checks : (HTTP only) (Optional) Check to send the health check to the backend server without SSL. This option is only available when the backend server has its protocol is set to HTTP. It has no effect when the backend server doesn't have SSL enabled. When SSL is disabled, health checks are always plaintext.
- Interval in milliseconds : (Optional) Specify how often to run the health check, in milliseconds. The default is 10000 (10 seconds).
- Timeout in milliseconds : (Optional) Specify the maximum time in milliseconds to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default is 3000 (3 seconds).
- Number of retries : (Optional) Specify the number of retries to try before a backend server is considered "unhealthy." This number also applies when recovering a server to the "healthy" state. The default is '3.'
- Status code : (HTTP only) (Optional) Specify the status code a healthy backend server must return.
- URL path (URI) : (HTTP only) Specify a URL endpoint against which to run the health check.
- Response body regex : (HTTP only) (Optional) Provide a regular expression for parsing the response body from the backend server.
- Show advanced options : Select this link to access more options. Select the tab for the corresponding functionality:
- Advanced SSL tab: (Only present if the Certificate Service Managed Certificate certificate resource is selected.) Select one of these options if you picked Certificate Service Managed Certificate when selecting the certificate resource for the listener. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for information on how load balancers use SSL certificates.

CA bundle : Select the certificate authority bundle in the specified compartment from the list. Select Change compartment to choose a different compartment from where to select the certificate authority bundle.

Certificate authority : Select the certificate authority in the specified compartment from the list. Select Change compartment to choose a different compartment from where to select the certificate authority bundle.
- TLS version: Optional. Specify the Transport Layer Security (TLS) versions: 1.0 , 1.1 , 1.2 (recommended), and 1.3

You can select any combination of versions. Choose the ones you want from the list. If you don't specify the TLS versions, the default TLS is version 1.2 only.

Select cipher suite : Select a set of cipher suites from the list. All choices present in the list have at least one cipher associated with each TLS version you selected.
- Select Create .

After your backend set is provisioned, you must specify backend servers for the set. See[Backend Servers for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendservers.htm)for more information.

More information:
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm)
- [Backend Sets for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm)
- [Health Checks for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/load_balancer_health_management.htm)
- [Load Balancer Management](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm)

[Load balancer SSL certificate expires in X days](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: A load balancer's SSL certificate expires soon. When the certificate expires, data traffic can be interrupted and security compromised.

Basics:
- To ensure continuous security and usability, SSL certificates must be rotated on a timely basis.
- You can configure an exception in Oracle CASB Cloud Service to reduce alerts from exempted load balancers.

To rotate a load balancer's certificate bundle:

The following procedure is for the Oracle Cloud Infrastructure Console.

- Update your client or backend server to work with a new certificate bundle.
Note  
  
The steps to update your client or backend server are unique to your system.
- Upload the new SSL certificate bundle to the load balancer:
- Under Load balancers , select Load balancer . The Load balancers page appears.
- Select the name of the Compartment that contains the load balancer you want to change, and then select the load balancer's name.
- Select the load balancer you want to configure. The load balancer's Details page appears.
- Select Certificates under Resources . The Certificates list appears. All certificates are listed in tabular form.
- Complete the following:
- Certificate name : Enter a friendly name for the certificate bundle. It must be unique within the load balancer, and it can't be changed in the Console. (It can be changed using the API.)
- Choose SSL certificate file : Drag the certificate file, in PEM format, into the SSL certificate field.

You can also choose the Paste SSL certificate option to paste a certificate directly into this field.
Important  
  
If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.
- Specify CA certificate : (Recommended for backend SSL termination configurations.) Select to provide a CA certificate.
- Choose CA certificate file : Drag the CA certificate file, in PEM format, into the CA certificate field.

You can also choose the Paste CA certificate option to paste a certificate directly into this field.
- Specify private key : (Required for SSL termination.) Select to provide a private key for the certificate.
- Choose private key file : Drag the private key, in PEM format, into the Private key field.

You can also choose the Paste private key option to paste a private key directly into this field.
- Enter private key passphrase : (Optional) Specify the private key passphrase.
- Select Add certificate . Next, edit each applicable listeners or backend sets (as needed) so they use the new certificate bundle:
- 

Edit the listener:
- Under Load balancers , select Load balancer .
- Choose the Compartment that contains the load balancer you want to change, and then select the load balancer's name.
- Select Listeners under Resources . The Listeners list appears. All listeners are listed in tabular form.
- Select the Actions menu (three dots) next to the listener you wan to edit, then select Edit Listener .
- In the Certificate name list, choose the new certificate bundle.
- Select Submit .
- Edit a backend set:
Important  
  
Updating the backend set temporarily interrupts traffic and can drop active connections.
- Under Load balancers , select Load balancer .

The Load balancers list page opens. All existing load balancer resources in the selected compartment are displayed in a list table.
- To view the resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Select a State from the list to limit the load balancers displayed to that state.
- Select the load balancer whose backend set you want to edit. The load balancer's Details page appears.
- Select Backend sets under Resources . The Backend sets list appears. All backend sets are listed in tabular form.
- Select the name of the backend set you want to edit. The backend set's Details page appears.
- Select Edit backend set . The Edit backend set dialog box appears.
- Select Use SSL .
- In the Certificate name list, choose the new certificate bundle.
- Select Save changes .
- 

(Optional) Remove the expiring SSL certificate bundle.
Note  
  
You can't delete an SSL certificate bundle that's associated with a listener or backend set. Remove the bundle from any other listeners or backend sets before deleting.
- Under Load balancers , select Load balancer .
- Select the name of the Compartment that contains the load balancer you want to change, and then select the load balancer's name.
- Select the load balancer you want to configure.
- In the Resources menu, select Certificates .
- For the certificate you want to delete, select the Actions menu (three dots) , and then select Delete .
- Confirm when prompted.

More information:
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm)
- [SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)
- [Listeners for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm)
- [Backend Sets for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm)
- [Load Balancer Management](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm)

## Object Storage

[Public buckets detected](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/configuration_tasks.htm#)

Issue: Public buckets were detected in your tenancy. Confirm that the creation of each public bucket is intentional and authorized. If the bucket is not sanctioned for public access, follow the procedure for changing the visibility of a bucket and make the bucket private.

Basics:
- Carefully assess the business requirement for public access to a bucket. When you enable anonymous access to a bucket, users can obtain object metadata, download bucket objects, and optionally list bucket contents.
- Changing the type of access is bi-directional. You can change a bucket's access from public to private or from private to public.
- Changing the type of access doesn't affect existing pre-authenticated requests. Existing pre-authenticated requests still work.

To change the visibility of a bucket (private or public):

The following procedure is for the Oracle Cloud Infrastructure Console.

- On the Buckets list page, find the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- From the Actions menu for the bucket you want, select Edit visibility .

The Edit visibility panel opens.
- 

Select Public or Private .

If you select Public to enable public access, decide whether you want to let users list the bucket contents. To set the visibility of bucket object lists, select Allow users to list objects from this bucket .
- Select Update .

More information:
- [Securing Object Storage](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm)
- [Object Storage Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm)
- [Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
