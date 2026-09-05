# Creating a Product License in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-product-license.htm
- Fetched: 2026-09-05 02:10 CDT

# Creating a Product License in License Manager

Create a product license in License Manager.

You can create either Oracle or third-party licenses. Adding third-party licenses is similar to the process of adding Oracle products, however, you're restricted to OCPUs as the only metric. Work with your third-party vendor to better understand how a licensing term translates.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-product-license.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-product-license.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-product-license.htm#)
- 

- On the Product Licenses page, select Add Product License . If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm).
The Add Product License panel opens.
- Select one of the following options:

- Oracle : The license vendor for all Oracle products.
- Third Party : The license vendor for all non-Oracle product licenses.
- Perform the following tasks depending on the vendor type you selected:

- Oracle : Select a Product from the list:
- Oracle Database Enterprise Edition
- Oracle Database Standard Edition
- Oracle Database Standard Edition One
- Oracle Database Standard Edition 2

You can also create a license by selecting Options and choosing the following from the Product list:
- Real Application Clusters
- Multitenant
- Active Data Guard

Select a Metric that matches your licensing terms, whether Processors or Named User Plus .
- Third Party : In Vendor and Product , enter the vendor and product names.
- Enter the Metric depending on the vendor type you selected:

- Oracle : Select the option that matches your licensing terms:
- Processors
- Named User Plus
- Third Party : The metric value is fixed as OCPU .
- Enter the following information for License record :

- Record Name : Specify a license record name. Avoid entering confidential information.
- Customer Support Identifier (CSI) : (Oracle only) See your support contract and enter the CSI corresponding to the license.
- Unique identifier : (Third Party only) Enter a unique identifier based on your contract with your licensor.
- License Term : You can specify if your license is unlimited (Unlimited License Agreement licenses), or has a specific count associated with it (Full Use licenses). Select either Perpetual or Term-Limited .

If selecting Perpetual , specify the Support Contract End Date .

If selecting Term-Limited , specify both the License End Date and the Support Contract End Date .
- License Quantity : Specify the license quantity available for use based on your contractual terms, and accounting for licenses used on-premises or on other cloud platforms. Select either Count or Unlimited .

If selecting Count , specify a license quantity value in the field (default is 1).
Note  
  
You can add more license records after you create the product license.
- (Optional) To track license usage on Compute resources, you can associate a compute image with your license. An image is a template of a virtual hard drive that determines the operating system and other software for an instance.

Under Image , select Choose Image . The Browse All Images panel opens. The Image Source field changes based on whether the license you are creating is an Oracle or Third Party license.

When creating an Oracle license, Oracle Images is selected and the list of available images is displayed. Choose from the list of BYOL Oracle enterprise images and solutions enabled for Oracle Cloud Infrastructure. For any image under Image Name , you can select the down arrow ( ) to expand the Image Build details, and select the version number for the particular image. Only one image can be selected when creating the product license, but you can add more images after creation.

When creating a third-party license, Partner Images is selected and the list of available third-party partner images is displayed, in terms of the Image Name and the Publisher . Select the down arrow ( ) to expand the Image Build details, and select the version number for the particular partner image. As with Oracle images, one image can be selected when creating the product license, but you can add more images after creation.

After choosing the image, select the option to indicate that you agree to the legal terms for the chosen image. Select Select Image .
- If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Add .
A notification is displayed that the new license was saved successfully, and a new[license details](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-product-license.htm)page (for the license you created) opens. The new license is also added to the Product Licenses page.
- 

Use the[oci license-manager product-license create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/create.html)command and required parameters to create a product licenses in a compartment:

```

```

`is-vendor-oracle`indicates whether the product license vendor is Oracle (`true`) or a third-party (`false`).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/CreateProductLicense)
