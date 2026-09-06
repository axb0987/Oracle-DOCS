# Access an ATP Database Configured as a Private Endpoint
- Source: https://docs.oracle.com/iaas/visual-builder/doc/access-atp-pe-instance.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/visual-builder/doc/access-atp-pe-instance.html#dcoc-content-body)

# Access an ATP Database Configured as a Private Endpoint

If you want to use an ATP database that is protected using a private endpoint (ATP-PE), you can configure the database instance to allow a public Visual Builder instance to connect to the database directly, without requiring a public load balancer.

Similarly, if you are already using an ATP database configured to use a public endpoint, and you want to switch to ATP-PE, you need to update the allowlists in the ATP-PE settings and the VB instance settings to allow connections to the database. For more on adding a VB instance to allowlists, see[Allow Your Instance to Access Services](https://docs.oracle.com/iaas/visual-builder/doc/allow-your-instance-access-services.html#GUID-AF212E4A-48A7-47A7-9B33-D2F7D96E8918).

To connect your public VB instance to an ATP-PE instance:
- On the Visual Builder Instances page, find the instance you want to work with and open its details page.
- Collect the required details about your Visual Builder instance.

To configure the access list in ATP-PE, you'll need to provide Visual Builder network gateway details:
- If VB and ATP-PE are in the same OCI region, you need theVB service VCN OCID and the VB management VCN OCID.
- If VB and ATP-PE are in different OCI regions, you need the service outbound IP and the management outbound IP

You can view an instance's VB service NAT gateway IP and VCN OCID in the instance's Visual Builder Instance Information tab in the OCI console. If the instance also has a VB management NAT gateway IP and VCN OCID, they will also be displayed in the tab:  

  
[Description of the illustration admin-instacedetails-ocid.png](https://docs.oracle.com/iaas/visual-builder/doc/img_text/admin-instacedetails-ocid.html)  

- Configure the ATP-PE instance's access control rule.
- Open the ATP-PE instance's details page.
- Select More actions , then select Update network access .
- In the Update network access panel, select Allow public access in the Private endpoint access pane.
- Enter the required VB VCN OCIDs or IP addresses. Click Add access control rule .

For example, if the VB and ATP-PE instances are in the same OCI region, you should select Virtual cloud network OCID in the two IP notation type drop-down lists, and enter the two required VCN OCIDs in the Values fields:  

  
[Description of the illustration allow-access-atp-pe-db.png](https://docs.oracle.com/iaas/visual-builder/doc/img_text/allow-access-atp-pe-db.html)  

For details on the ATP access control settings, see[Use a Private Endpoint with Public Access Allowed](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/private-endpoints-autonomous.html#GUID-5CB6F1BE-0E7A-4F90-9275-6EE7E288AE74)and[Configure Private Endpoint Advanced Options](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/private-endpoints-autonomous.html#GUID-D5853754-F782-472E-922B-68E6B03395BE)in the Oracle Autonomous Database documentation.
- Download the ATP wallet.

If you are switching from an ATP database to ATP-PE, you will need to download the updated ATP wallet.
- File a Service Request to update the ATP connection string and wallet in the Visual Builder backend.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
