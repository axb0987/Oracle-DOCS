# Creating an Approved Sender
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-create_an_approved_sender.htm
- Fetched: 2026-09-05 02:01 CDT

# Creating an Approved Sender

Register a sender email address to be used for email delivery.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-create_an_approved_sender.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-create_an_approved_sender.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-create_an_approved_sender.htm#)
- 

- On the Approved Senders list page, select Create Approved Sender . If you need help finding the list page, see[Listing Approved Senders](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-approved-senders.htm).
- In the Create Approved Sender dialog box, provide the following information:

- Enter the email address that you want to list as an approved sender.
- (Optional) Add tags to organize resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask the administrator.
- Select Create Approved Sender .
The email address is added to Approved Senders list.

Tip  
  
Approved senders are unique to regions. If you try to create a duplicate approved sender within a region, the service returns a 409 Conflict error.
Note  
  
When an approved sender is created, it might not be immediately available for use. To work around this specific issue, we recommend that you create an approved sender and try to immediately use it. If an SMTP authorization failure occurs, perform a retry with backoff.
Tip  
  
To send email from many addresses with the same domain:
- Configure DKIM for the domain providing authorization to send from the domain.
- When DKIM is active, create the approved sender @domain.com .
Warning  
  
If DKIM isn't active, you can't create the approved sender.
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/sender/create.html)command and required parameters to create a sender for a tenancy in a given compartment.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To create an approved sender, use the[CreateSender](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Sender/CreateSender)
