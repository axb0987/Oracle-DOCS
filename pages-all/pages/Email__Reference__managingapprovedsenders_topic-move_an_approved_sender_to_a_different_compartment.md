# Moving an Approved Sender
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-move_an_approved_sender_to_a_different_compartment.htm
- Fetched: 2026-09-05 02:01 CDT

# Moving an Approved Sender

Move an approved sender to a different compartment.

To manage approved senders and use approved senders to send mail, user groups must have an associated identity policy in the new compartment. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-move_an_approved_sender_to_a_different_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-move_an_approved_sender_to_a_different_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-move_an_approved_sender_to_a_different_compartment.htm#)
- 

- On the Approved Senders list page, select the approved sender that you want to move to a new compartment. If you need help finding the list page, see[Listing Approved Senders](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-approved-senders.htm).
- From the Actions menu for the approved sender, select Move resource .
- In the Move resource dialog box, select the destination compartment from the list.
- Select Move resource .
The approved sender is moved to a different compartment.
- 

Use the[change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/sender/change-compartment.html)command and required parameters to move a sender into a different compartment.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To move an approved sender, use the[ChangeSenderCompartment](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Sender/ChangeSenderCompartment)
