# Editing the Amazon S3 Compatibility API and Swift API Compartment Designations
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_edit_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm
- Fetched: 2026-09-05 02:50 CDT

# Editing the Amazon S3 Compatibility API and Swift API Compartment Designations

Change your tenancy's Amazon S3 Compatibility API and Swift API compartment designations in your tenancy.

If your permissions allow, you can change the Amazon S3 Compatibility API and Swift API compartment designations. Use the following guidance when creating designated compartment names:
- Must be unique across all the compartments in your tenancy.
- Can be from 1 to 100 characters in length.
- Must not contain confidential information.
- Valid are letters (upper or lowercase), numbers, hyphens, and underscore.

See[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments.htm#permissions)for more information on permissions associated with this feature.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_edit_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_edit_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_edit_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm#)
- 

- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
Your tenancy's details page opens.
- From the Actions menu , select Edit object storage settings .
The Edit object storage settings panel opens.
- Select the compartment that you want for the Amazon S3 compatibility API designated compartment .
- Select the compartment that you want for the Swift API designated compartment .
- Select Save .

The new Amazon S3 Compatibility API and Swift API designated compartments are displayed in the tenancy's details page.
- 

Use the[oci os ns update-metadata](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/ns/update-metadata.html)command and required parameters to change the compartment designation of a Amazon S3 Compatibility API and Swift API in your tenancy.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Amazon S3 Compatibility API

Use this command to specify the default Amazon S3 compartment for the specified namespace in your tenancy.

```

```

`compartment_ocid`specifies a compartment that's not the root compartment of your tenancy.

For example:
```

```

## Swift API

Use this command to specify the default Swift compartment for the specified namespace in your tenancy.

```

```

`compartment_ocid`specifies a compartment that's not the root compartment of your tenancy.

For example:
```

```

- 

Run the[UpdateNamespaceMetadata](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Namespace/UpdateNamespaceMetadata)
