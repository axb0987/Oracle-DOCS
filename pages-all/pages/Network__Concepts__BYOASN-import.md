# Importing an ASN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-import.htm
- Fetched: 2026-09-05 02:40 CDT

# Importing an ASN

Import your Autonomous System Number (ASN) to OCI and use your existing ASN within the OCI environment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-import.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-import.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-import.htm#)
- 

- Confirm you're viewing the region you're interested in.
- Open the navigation menu and select Networking . Under IP management , select BYOASN .
- Select Import your ASN .
- On the Import your ASN page, enter the following information:

- A name for the ASN.
- The compartment in which you want to create the ASN, which could be different from the compartment you're currently working in.
- The ASN that you intend to bring to your tenancy.
- (Optional) In the Tags section, add one or more tags for the ASN.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see Resource Tags. If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Import your ASN .
The details page for that ASN import request appears.
- In the Next Steps section, make a copy of the validation token.
- Add the validation token to the RIR account information associated with your ASN. Each RIR uses a slightly different method:

- ARIN : Add the token string in the "Public Comments" section associated with your address range.
- RIPE NCC : Add the token string as a new "descr" field associated with your address range.
- APNIC : Add the token string to the "remarks" field for your address range by emailing it to helpdesk@apnic.net. The email must be sent from the APNIC authorized contact account for the IP address range.
Note  
  

The validation token must be associated with the ASN information. Don't add it to the information for the organization that owns the ASN.
Note  
  

The BYOASN workflow takes up to 10 business days to complete, during which Oracle validates your ASN and IP Prefix combinations with service providers. To speed up the process, ensure to let your Oracle Account team know which IP prefix you plan to link to the ASN.
- Wait until the token registration is complete before you select the Finish import button (in the next step).
- Return to the details page for the BYOASN request and select Finish import .
- Select Finish import , confirming that you want to validate the BYOASN request. View the work requests to see the status.

Note  
  

If you plan to advertise your IP Prefix using your own ASN, imported through BYOASN, you must create a Route Origin Authorization (ROA) with your RIR, using Oracle ASN (31898) and your own ASN. Set an expiry date at least 6 months in the future. Follow the instructions appropriate for your RIR:
- ARIN:[ROA Requests](https://www.arin.net/resources/manage/rpki/roa_request/)
- RIPE NCC:[Managing ROAs](https://www.ripe.net/manage-ips-and-asns/resource-management/rpki/resource-certification-roa-management/)
- APNIC:[Route/ROA management](https://www.apnic.net/wp-content/uploads/2017/01/route-roa-management-guide.pdf)
- 

Use the`network byoasn create`command and required parameters to import an ASN within the OCI environment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

- 

Run the[CreateByoasn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/CreateByoasn)operation to import an ASN.

Run the[ValidateByoasn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/ValidateByoasn)
