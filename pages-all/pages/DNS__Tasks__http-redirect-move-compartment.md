# Moving an HTTP Redirect Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm
- Fetched: 2026-09-05 01:59 CDT

# Moving an HTTP Redirect Between Compartments

You can move an HTTP redirect from one compartment to another.

See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm)for information about compartments and access control.

See[HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm)for a resource overview and more information.

For general service information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm#)
- 

- On the HTTP redirects list page, find the HTTP redirect you want to move. If you need help finding the list page, see[Listing HTTP Redirects](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-list.htm).
- From the Actions menu (three dots) for the HTTP redirect, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[http-redirect change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/http-redirect/change-compartment.html)command and required parameters to move an HTTP redirect to a different compartment.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeHttpRedirectCompartment](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/ChangeHttpRedirectCompartment)
