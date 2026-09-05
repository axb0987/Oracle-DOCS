# Listing Approved Senders
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-approved-senders.htm
- Fetched: 2026-09-05 02:01 CDT

# Listing Approved Senders

List approved senders in Email Delivery.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-approved-senders.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-approved-senders.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-approved-senders.htm#)
- 

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Approved Senders . The Approved Senders list page opens. All the approved senders in the selected compartment and region are displayed in a table.

Ensure that you're in the correct compartment. The user must be in a group with permissions to manage`approved-senders`in this compartment.
- To view the resources in a different compartment, use the Compartment filter to switch compartments. You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- To find an approved sender by name, enter the name in the search box above the list table.
- 

Use the[list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/sender/list.html)command and required parameters to list senders for a tenancy in a given compartment.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSenders](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Sender/ListSenders)operation to list all the senders in a compartment.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
