# Editing a User Attribute
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/edit-custom-schema-attributes.htm
- Fetched: 2026-09-05 02:28 CDT

# Editing a User Attribute

After you create a custom attribute for the user schema for IAM, you might need to change its settings. For example, you might need to adjust the description or the minimum and maximum length.

- On the User attributes list page, in the Filter attribute field, select Custom . If you need help finding the list page or the attribute, see[Listing User Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/listing-schema.htm).
- From the Actions menu (three dots) for the custom attribute that you want to edit, select Edit attribute .
- You can edit the values for the following fields: Display name , Description , Minimum length , Maximum length , and End-user permissions . For more information about these fields, see[Creating a Custom User Attribute](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/add-custom-schema-attributes.htm).

Note  
  
You can't increase the value of the Minimum length field or decrease the value of the Maximum length field. Also, if the value of the Maximum length field was set to below 40 when the custom schema attribute was added, then you can't increase it above 40. However, if the value was set to above 40, then you can increase the maximum length to 4,000.
-
