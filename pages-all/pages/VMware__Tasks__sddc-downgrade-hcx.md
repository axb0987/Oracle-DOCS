# Downgrading a VMware Solution SDDC's HCX License
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-downgrade-hcx.htm
- Fetched: 2026-09-05 03:09 CDT

# Downgrading a VMware Solution SDDC's HCX License

Learn how to downgrade the SDDC's HCX license from Enterprise to Advanced.

Downgrading an SDDC's HCX license to Advanced decreases the number of on-premises connection keys issued from 10 to 3.
Important  
  

- SDDCs that use standard shapes already include the Enterprise license at no cost. Downgrade to Advanced license isn't supported for standard shape SDDCs.
- You must specify 3 license keys to retain after the downgrade. The downgrade request remains in a pending state until the HCX Monthly Billing Cycle End Date. You can cancel the downgrade request as long as it's still in a`pending`state, See[Canceling a VMware Solution SDDC's HCX License Downgrade](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-cancel-downgrade-hcx.htm).

For more information, see[HCX License Types](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#HCX-license-types).

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-downgrade-hcx.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-downgrade-hcx.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-downgrade-hcx.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select the Change link on the right side of HCX license type .
The Change HCX License panel opens.
- Select I consent to downgrade to the Advanced License (No additional cost)
The panel lists HCX On-Premises Connector activation keys.
- Select 3 license keys to remain active after Enterprise features end.
- Select Save Changes .

Important  
  
The downgrade request remains in a`PENDING`state until the HCX Monthly Billing Cycle End Date. A notification appears on the SDDC Details page that shows the date that Enterprise features end. To cancel the pending downgrade, select Cancel downgrade to the right of the notification.
- 

Use the[sddc downgrade-hcx](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/sddc/downgrade-hcx.html)command and required parameters to downgrade the SDDC's HCX license:
```

```

Specify the HCX on-premise license keys to be reserved when downgrading from HCX Enterprise to HCX Advanced. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

The[`--generate-param-json-input`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/oci.html#cmdoption-generate-param-json-input)option can be used to generate an example of the JSON which must be provided. We recommend storing this example in a file, modifying it as needed and then passing it back in by using the`file://`syntax. For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DowngradeHcx](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Sddc/DowngradeHcx)
