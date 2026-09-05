# Customizing User Schemas
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm
- Fetched: 2026-09-05 02:18 CDT

# Customizing User Schemas

When you start using identity domains, you might load a different set of user identities based on requirements from various departments within or outside of your organization. Schema Customization allows you to create identity domain-specific custom schemas to supplement the out-of-the-box (OOTB) attributes for a resource and allows user schemas to be extended.

A custom schema is available OOTB as an empty schema with no attributes defined. The following "Custom User" schema is an example of an empty custom schema with no attributes. This custom schema is used as an example for all example request payloads in this use case.
```

```

Note  
  
You can't update the following properties. Any attempt to update these properties is ignored.
- 

type
- 

idcsSearchable
- 

uniqueness
- 

caseExact
- 

idcsSensitive
- 

multiValued
- 

required

## Adding Custom User Schema Attributes

The following links provide information and example requests for adding custom user schema attributes using both the PUT and PATCH methods. Information on the validations performed when adding attributes is also included.
- 

[Adding Custom User Schema Attributes Using PUT](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#addingattributestoemptyschema)
- 

[Adding Custom User Schema Attributes Using PATCH](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#addingattributestocustomschema)
- 

[Validations Performed When Adding Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#validationsadd)

## Updating Custom User Schema Attributes

The following links provide information and example requests for updating custom user schema attributes using both the PUT and PATCH methods. Information on validations performed when updating attributes is also included.
- 

[Updating Custom User Schema Attributes Using PUT](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#updatingattributesincustomschema)
- 

[Updating Custom User Schema Attributes Using PATCH](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#replaceattributesincustomschema)
- 

[Validations Performed When Updating Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#validationsupdate)

## Removing Custom Schema Attributes

The following links provide information and example requests when removing custom user schema attributes using both the PUT and PATCH methods. Information on validations performed when removing attributes is also included.
- 

[Removing Custom User Schema Attributes Using PUT](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#removingattributesfromcustomschema)
- 

[Removing Custom User Schema Attributes Using PATCH](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#replaceattributeswithfiltersincustomschema)
- 

[Validations Performed When Removing Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#validationsincustomschema)

## Enabling the Import of Custom User Schema Attributes

The following link provides information and example requests when importing custom user schema attributes.
- 

[Enabling the Import of Custom User Schema Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#settingcolnamevalue)

## Adding Custom User Schema Attributes Using PUT

Populate an empty custom schema by adding new attributes using the PUT method.

In this example, we're updating the following attributes:

Attribute Type

subDivision

string

branchAddress

string

Example PUT Request
```

```
Example JSON Response
```

```

## Adding Custom User Schema Attributes Using PATCH

This example shows you how to use PATCH "op": "add" to add custom attributes.

The validations performed while making these operations are similar to the PUT method. See the[Validations Performed When Adding Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm#validationsadd)section for more information.

Update the custom schema to add new attributes using PATCH. In this example, the PATCH "add" operation is used, and the attribute name is picked from the request payload for patching. If the name specified already exists, it's replaced automatically. If it doesn't exist, the attribute is automatically added. If the name property is missing, an error message appears.

Example PATCH Request
```

```

Example JSON Response
```

```

## Validations Performed When Adding Attributes

When you add custom attributes, identity domains perform certain validations. The following table describes the validations based on the Add operation.

Add Validations

This table describes the validations that identity domains perform when you add new custom attributes to the target schema.

Attribute Name Validations Performed

name

Check for duplicates. This value must be unique across the custom schema.

idcsDisplayName

Check for duplicates. This value must be unique across the custom schema.

idcsMaxLength

Value can't be less than 2.

idcsMinLength

Value can't be less than 1.

returned

Value must be a valid return value such as always, default, request, or never.

type

Value must be a string that can be single or multivalued.

mutability

Value must be a valid mutability like readWrite, readOnly, immutable, or writeonly.

idcsCsvAttributeNameMappings.columnHeaderName

Value must be unique across the custom schema.

idcsCsvAttributeNameMappings.multiValueDelimiter

Mandatory attribute for multivalued attributes having idcsCsvAttributeNameMappings.

## Updating Custom User Schema Attributes Using PUT

Update attributes in your custom schema using the PUT method.

### Updating Attributes

In this example, we're updating the attributes for "subDivision" and "branchAddress."

Example PUT Request
```

```

Example JSON Response
```

```

### Updating Multi-Valued String Attributes

You can update multivalued string attributes in your existing custom schema using the PUT method. In this example, we're adding the "hobbies" multivalued string attribute.

Example PUT Request
```

```

## Updating Custom User Schema Attributes Using PATCH

Replace attributes in the custom schema using the PATCH method.

### Using the Replace Operation

In this example, the PATCH "replace" operation is used, and the attribute name is picked from the request payload for patching. If the name specified already exists, it replaces it automatically. If it doesn't exist, an error message appears.

Example PATCH Request
```

```

Example JSON Response
```

```

### Using the Replace Operation with Filters

- 
In this example, the PATCH "replace" operation is used with filters to update to "true" all attributes that have the "required" property with the "returned" attribute set to "always":
```

```

- 
In this example, the PATCH "replace" operation is used with filters to update to "false" all attributes with the "auditable" property set to "true".
```

```

Example JSON Response
```

```

### Using the Replace Operation to Update a Multi-Valued String Attribute

You can replace multivalued string attributes in your custom schema using the PATCH method. In this example, the PATCH "replace" operation is used, and the attribute name is picked from the request payload for patching. If the name specified already exists, it replaces it automatically. If it doesn't exist, an error message appears.

Example PATCH Request
```

```

## Validations Performed When Updating Attributes

Whenever you replace custom attributes, identity domains perform certain validations. The following table describes the validations based on the Replace/Update operation.

Replace/ Update Validations

This table describes the validations that identity domains perform when you update existing custom attributes to the target schema.

Attribute Name Validations Performed

idcsMinLength

Value can't be less than 1. It can't be over the column limit allocated for the attribute.

For example, if the U_VC_40 column was allocated, then idcsMinLength can't exceed 40.

idcsMaxLength

Value can't be less than 1. It must be equal to or greater than the idcsMaxLength value for the attribute, and can't be over the column limit allocated for the attribute.

For example, if the U_VC_40 column was allocated, then idcsMaxLength can't exceed 40.

idcsMinValue

Value can't be less than what currently exists in the store.

idcsMaxValue

Value can't be greater than what currently exists in the store.

canonicalValues

Values must be a super set of what currently exists in the store.

idcsCsvAttributeName

Value must be unique across the custom schema.

name

Value must be unique across the custom schema.

idcsDisplayName

Value must be unique across the custom schema.

## Removing Custom User Schema Attributes Using PUT

Remove attributes in your custom schema using the PUT method.

If the custom attributes "subDivision" and "branchAddress" already exist in the custom schema, then you can remove branchAddress using the following PUT request.
Note  
  
It is recommended that you remove attributes from the custom schema only when you're putting together a custom schema for the first time. Removing attributes after you have built a custom schema could cause issues, as many users may have already been provisioned using the custom attributes. To remove custom schema attributes after users have been provisioned using the attributes, you must first delete all the data that pertains to the custom schema attributes from the database.

Example PUT Request
```

```

Example JSON Response
```

```

## Removing Custom User Schema Attributes Using PATCH

This section describes the use of PATCH`"op":"remove"`when removing custom user schema attributes.

### Using the Remove Operation with Filters

- 
In this example, the PATCH "remove" operation is used with filters to remove the "subDivision" attribute.
```

```

- 
In this example, the PATCH "remove" operation is used with filters to remove all attributes with the "required" property set to "false".
```

```

Example JSON Response
```

```

## Validations Performed When Removing Attributes

Whenever you remove custom attributes, identity domains perform certain validations.

When custom attributes are removed using PUT or PATCH, identity domains perform delete validations to ensure that no data has been previously provisioned in the database for that attribute. If data has been provisioned, then the remove operation fails.

## Enabling the Import of Custom User Schema Attributes

To import data into your new schema attributes using a .csv file, you must first set column name values for the new attributes.

In this example, a new user attribute was created called`employeeStatus.`To set the column name value for this attribute so that you can import data to that attribute from a .csv file, internally map the attribute to`idcsCsvAttributeNameMappings`.

Example PATCH Request

The following request example shows how to set the column name value for the`employeeStatus`string custom attribute.
```

```

You can now import data using a .csv file that includes a column (with data) that's named Employee Status.

The following request example shows how to set a column name for a string array custom attribute named Favorite Colors whose values would be comma delimited in a .csv file.
```

```

More Information
- 

See[Importing](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Importing.htm)
