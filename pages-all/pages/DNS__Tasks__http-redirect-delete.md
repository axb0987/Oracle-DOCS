# Deleting an HTTP Redirect
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-delete.htm
- Fetched: 2026-09-05 01:59 CDT

# Deleting an HTTP Redirect

You can delete an HTTP redirect.

See[HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm)for a feature overview and more information.

For general service information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-delete.htm#)
- 

- On the HTTP redirects list page, find the HTTP redirect you want to delete. If you need help finding the list page, see[Listing HTTP Redirects](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-list.htm).
- From the Actions menu (three dots) for the HTTP redirect you want to delete, select Delete .
- When prompted, confirm the deletion.
You need to remove any associated ALIAS or CNAME records to ensure proper resolution. See[DNS Zone Management](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm).
- 

Use the[http-redirect delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/http-redirect/delete.html)command and required parameters to delete an HTTP redirect.
```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteHttpRedirect](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/DeleteHttpRedirect)
