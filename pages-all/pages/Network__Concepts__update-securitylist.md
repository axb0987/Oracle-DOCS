# Updating Rules in a Security List
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm
- Fetched: 2026-09-05 02:42 CDT

# Updating Rules in a Security List

Update the rules used in a security list in a Virtual Cloud Network (VCN).

You can add and remove rules from the security list. A security list can have no rules. Notice that when you update a security list in the API, the new set of rules replaces the entire existing set of rules.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the security list you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Security Lists section.
- Under Resources , select Security Lists .
- Select the security list you're interested in. Depending on the option that you see:

- Select the Security rules tab. Ingress Rules is the first table of security rules on the page. Egress Rules is the second table of security rules on the page.
- Under Resources , you can select Ingress Rules or Egress Rules to switch between the different types of rules.
- To add a rule, select Add Ingress Rules (or Add Egress Rules ). See details of adding a rule in[Creating a Security List](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/creating-securitylist.htm).
- To delete an existing rule, depending on the option that you see:

- Select the checkbox next to the rule and then select Actions and then select Remove .
- Select the checkbox next to the rule and then select Remove .
- If you wanted to edit an existing rule, depending on the option that you see:

- Select the checkbox next to the rule and then select Actions and then select Edit .
- Select the checkbox next to the rule and then select Edit .
- 

Use the[network security-list update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/update.html)command and required parameters to update the rules used in a particular security list:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList)
