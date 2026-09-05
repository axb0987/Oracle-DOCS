# Managing Tags for an Approved Sender
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-manage_tags_for_an_approved_sender.htm
- Fetched: 2026-09-05 02:01 CDT

# Managing Tags for an Approved Sender

View or edit tags for an approved sender, or add more tags.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-manage_tags_for_an_approved_sender.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-manage_tags_for_an_approved_sender.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingapprovedsenders_topic-manage_tags_for_an_approved_sender.htm#)
- 

- On the Approved Senders list page, click the approved sender which you want to view or edit tags. If you need help finding the list page, see[Listing Approved Senders](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-approved-senders.htm).
- From the Actions menu for the approved sender, select Manage tags .
- In the Manage Tags dialog box, select Add tag to add a tag.
- Enter the following information for the tag:

- Namespace: To apply a defined tag, select its tag namespace from the list. To add a free-form tag, select None .
- Key: If you're applying a defined tag, select a key that's associated with the tag namespace. If you're adding a free-form tag, enter a key. Keys for free-form tags are case-sensitive.
- Value: Enter a value or select one from the list. Values are case-sensitive.
For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Select Save .
- On the Approved Sender Details page , click Tags tab to view the tags associated with the email address.
- 

Use the[oci iam domain get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/get.html)command and required parameters to &lt;task-being-performed&gt;:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
