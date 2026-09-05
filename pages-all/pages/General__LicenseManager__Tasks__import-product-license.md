# Importing Product Licenses into License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/import-product-license.htm
- Fetched: 2026-09-05 02:10 CDT

# Importing Product Licenses into License Manager

Import product licenses you create into License Manager using a downloadable template.

You can create product licenses using a downloadable, predefined Excel template, and then import them individually or in bulk into License Manager. The following types of licenses are supported for import:
- Full Use : Licenses that have a specific count associated with them. See your support contract for any licensing details, and account for any usage outside of Oracle Cloud Infrastructure when entering quantities for Full Use licenses. You can import several files but they can only be imported one at a time.
- ULA : Unlimited License Agreement. A count doesn't need to be entered for ULA licenses.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/import-product-license.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/import-product-license.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/import-product-license.htm#)
- 

- Open the navigation menu and select Governance &amp; Administration . Under License Manager , select Product Licenses .
The Product licenses list page opens. All product licenses in the selected compartment are displayed in a table.
- Select Import Oracle Product Licenses .
The Import Oracle Product Licenses panel opens.
- Select Download Template .
The`bulkUploadTemplate.xlsx`template is downloaded to your computer. The template file has the following fields:
- Product Name
- Metric
- License Term
- License End Date : A license end date isn't needed for a perpetual license.
- License Level
- License Count
- CSI
- Support Contract End Date

Each row represents one product license. For descriptions of the fields, see[Creating a Product License](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-product-license.htm).
- Update the Excel file with your license information and save it where it can be uploaded to the License Manager.
- On the Import Oracle Product Licenses panel, select Drop a file or select one and browse to the Excel file containing the product licenses to upload it. You can also drag the Excel file into in the panel to upload it.
- Select Import .
The Excel file is uploaded. A confirmation message appears in the Product Licenses page to indicate how many license records were imported, and if any duplicates were found.
- 

Importing license records into License Manager consists of the following tasks performed in order:
- [Downloading the and Completing the Excel Template](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/import-product-license.htm#get-template)
- [Importing the Licenses into License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/import-product-license.htm#import-licenses)

## Downloading the and Completing the Excel Template

Use the[oci license-manager bulk-upload-template get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/bulk-upload-template/get.html)command and required parameters to download the Excel template to your computer:

```

```

The`bulkUploadTemplate.xlsx`template is downloaded to your computer. Complete the template to create a product license file as described in Using the Console .

## Importing the Licenses into License Manager

Use the[oci license-manager license-record import-licenses](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/license-record/import-licenses.html)command and required parameters to import the completed Excel license file into License Manager:

```

```

`compartment-ocid`is the compartment where the license file is uploaded to.

`file_content`is the path of the license file on your computer to be uploaded.

`file_name`is the name of the license file.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Importing license records into License Manager consists of the following tasks performed in order:
- [Downloading the and Completing the Excel Template](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/import-product-license.htm#get-template-api)
- [Importing the Licenses into License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/import-product-license.htm#import-licenses-api)

## Downloading the and Completing the Excel Template

Run the[GetBulkUploadTemplate](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/BulkUploadTemplate/GetBulkUploadTemplate)operation to download the Excel template to your computer.

The`bulkUploadTemplate.xlsx`template is downloaded to your computer. Complete the template to create a product license file as described in Using the Console .

## Importing the Licenses into License Manager

Run the[BulkUploadLicenseRecords](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/BulkUploadLicenseRecordsDetails/BulkUploadLicenseRecords)
