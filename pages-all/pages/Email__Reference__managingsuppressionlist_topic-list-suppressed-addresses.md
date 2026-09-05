# Listing Suppressed Addresses
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-list-suppressed-addresses.htm
- Fetched: 2026-09-05 02:01 CDT

# Listing Suppressed Addresses

List the email addresses in suppression list that aren't part of your sending list.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-list-suppressed-addresses.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-list-suppressed-addresses.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-list-suppressed-addresses.htm#)
- 

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Suppression List .
The Suppression List page opens. All the suppressed recipient email addresses in the selected compartment and region are displayed in a table.
- To view the resources in a different compartment, use the Compartment filter to switch compartments. You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- To find a suppressed recipient email address by name, enter the name in the search box above the list table.
- 

Use the[list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/suppression/list.html)command and required parameters to list the suppressed recipient email addresses for a tenancy in a given compartment.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSuppressions](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Suppression/ListSuppressions)operation to list all the suppressed recipient email addresses in a compartment.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
