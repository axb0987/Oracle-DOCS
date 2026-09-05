# Creating User Permissions
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-create-policy.htm
- Fetched: 2026-09-05 02:00 CDT

# Creating User Permissions

Learn how to create a policy to allow a group to manage email-family resources.

## Using the Console

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- To attach the policy to a different compartment, use the Compartment filter to switch compartments. You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. Where the policy is attached controls who can later change or delete it (see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)). For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Click Create Policy .
- Enter the following:

- Name: A unique name for the policy. The name must be unique across all policies in your tenancy. You can't change this later.
- Description: A friendly description.
- Compartment: Select a compartment you want to create the policies in, if not already selected.
- Policy Builder: Enter Email Management as the policy use case.
- Select a default policy template listed under Common policy templates .
- Select Group or Dynamic groups , and the location.
Note  
  

To change the policy statements, enable the Show manual editor slider next to Policy Builder .

Enter the following policy statements under Policy Statements :

```

```

For more information about policies and policy syntax, see[Policy Basics](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm).
Note  
  

If you're using SMTP credentials of users who aren't in the "Default" Identity Domain, you need to include the name of your Identity Domain in your policy statement. For more information, see[How Policies Work (with Identity Domains)](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm).
- Select Create .
