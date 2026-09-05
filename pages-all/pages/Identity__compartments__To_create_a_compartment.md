# Creating a Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_create_a_compartment.htm
- Fetched: 2026-09-05 02:20 CDT

# Creating a Compartment

Create compartments in an IAM tenancy to organize and isolate your cloud resources.

If you belong to the Administrators group or if an administrator has created a policy that allows you to manage compartments, then you have the required access for creating compartments. Policies that manage compartments can be scoped to the tenancy level or to the compartment level.

When creating a compartment, you must provide a name for it that's unique within its parent compartment, with a maximum 100 characters, including letters, numbers, periods, hyphens, and underscores. You must also provide a description, which is a nonunique, changeable description for the compartment, from 1 to 400 characters. Oracle also assigns the compartment a unique ID called an Oracle Cloud ID (OCID). For more information, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You can create subcompartments in compartments to create hierarchies up are six levels deep, as shown in the following Console image.

[

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_create_a_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_create_a_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_create_a_compartment.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments .
A list of the compartments you have access to in the tenancy is displayed.
- Navigate to the compartment in which you want to create the compartment.
- To create the compartment in the tenancy (root compartment) select Create compartment .
- Otherwise, select through the hierarchy of compartments until you reach the detail page of the compartment in which you want to create the compartment. Then, on the details page, select Create compartment .
- Enter the following information:
- Name: A unique name for the compartment with a maximum of 100 characters, including letters, numbers, periods, hyphens, and underscores). The name must be unique within the parent compartment. Avoid entering confidential information.
- Description: A friendly description. You can change this later.
- Parent compartment: The compartment that you're in is displayed. To choose another compartment to create this compartment in, select it from the list.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. You can apply tags later.
- Select Create compartment .
You might also want to write a policy for the compartment. See[Creating a Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/../policymgmt/managingpolicies_topic-To_create_a_policy.htm).
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/create.html)command and required parameters to create a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/CreateCompartment)
