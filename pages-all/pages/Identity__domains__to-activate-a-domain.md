# Activating an Identity Domain
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm
- Fetched: 2026-09-05 02:21 CDT

# Activating an Identity Domain

You might create an identity domain in IAM that you need only temporarily, for example, for testing purposes. You can deactivate the identity domain when it's not in use and then reactivate it when it's needed.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm#)
- 

- On the Domains list page, select the domain that you want to activate. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).
- Perform one of the following actions depending on what you see:
- From the Actions menu, select Activate .
- Select Activate .
- Select Activate domain to confirm the activation.

The identity domain is in an Active status.
- 

Use the[oci iam domain activate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/activate.html)command and required parameters to activate an identity domain:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ActivateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/ActivateDomain)
