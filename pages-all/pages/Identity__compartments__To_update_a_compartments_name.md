# Renaming a Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_update_a_compartments_name.htm
- Fetched: 2026-09-05 02:20 CDT

# Renaming a Compartment

Edit or update a compartment's name in an IAM tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_update_a_compartments_name.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_update_a_compartments_name.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_update_a_compartments_name.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments .

A list of the compartments that you have access to in the tenancy is displayed.
- For the compartment you want to rename, select the Actions menu (three dots) , and then select Rename compartment .

Tip  
  
You can't change the name of the root compartment.
- Enter the new name. The name must be unique within the parent compartment. The name can have a maximum of 100 characters, including letters, numbers, periods, hyphens, and underscores. Avoid entering confidential information.
- Select Update .
- 

Use the[update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/update.html)command and required parameters to update a compartment's name:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/UpdateCompartment)
