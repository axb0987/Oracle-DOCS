# Editing Image Capabilities for Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities-tasks.htm
- Fetched: 2026-09-05 01:50 CDT

# Editing Image Capabilities for Custom Images

Edit the image capabilities for a custom image.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities-tasks.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities-tasks.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities-tasks.htm#)
- 

- Navigate to the Compute Custom images list page. If you need help finding the list page, see[Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/custom-images-list.htm).
- Select the custom image that you're interested in.
- 

Edit the image capabilities that you want to configure. For details about each image capability, see[Schema Elements](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm#configuringimagecapabilities__configuringimagecapabilities_topic-schema_elements).
- 

Select Save changes .
- 

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). To work with image capability schemas using the CLI, open a command prompt and run any of the following commands.

#### CLI Examples

To list out the global image capability schema:

```

```

To list out the global image capability schema versions:

```

```

To retrieve the global image capability schema version:

```

```

To list the image capability schemas in the specified compartment:

```

```

To retrieve the image capability schema for the specified ID:

```

```

To update the specified image capability schema:

```

```

To create an image capability schema:

```

```

When you create the schema, you specify the image OCID for the custom image you want to apply the image capability schema to.

To delete the specified image capability schema:

```

```

#### Usage Example

This example shows how to use the CLI to update the image capability schema for a custom image. For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Open a command prompt, and run the following command to retrieve the current global schema for the region:

```

```

The response is similar to the following:
```

```

- Using the OCID and version name of the global image capability schema that you retrieved in the previous step, run the following command to get the global image capability schema:

```

```

The response contains the[global image capability schema](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm#configuringimagecapabilities__configuringimagecapabilities_topic-global_image_capability_schema).
- 

Locate the schema element that you want to update, and then do the following:
- Copy the schema element that you want to update. This example uses the Storage.ParaVirtualization.EncryptionInTransit schema element.
- 

If the schema element contains a`source`field, change the value from GLOBAL to IMAGE. For example:
```

```

- Save the updated schema elements as a`.json`file.
- 

To verify whether the image is already using image capability, run the following command:

```

```

- 

If the image is using image capability, the response contains a line similar to the following:
```

```

The response also contains the image capability schema OCID.
- 

If the image is not using image capability, create an image capability schema for the image by running the following command:

```

```

&lt;schema_data_file&gt; is the path to the`.json`file that contains the schema elements that you want to update, which you created in the previous step.

The response is similar to the following:
```

```

- 

To update the image capability schema, run the following command:

```

```

&lt;schema_data_file&gt; is the path to the`.json`file that contains the schema elements that you want to update.
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the following API operations for working with image capability schemas:
- [ListComputeGlobalImageCapabilitySchemas](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGlobalImageCapabilitySchemaSummary/ListComputeGlobalImageCapabilitySchemas)
- [ListComputeGlobalImageCapabilitySchemaVersions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGlobalImageCapabilitySchemaVersionSummary/ListComputeGlobalImageCapabilitySchemaVersions)
- [GetComputeGlobalImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGlobalImageCapabilitySchema/GetComputeGlobalImageCapabilitySchema)
- [GetComputeGlobalImageCapabilitySchemaVersion](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGlobalImageCapabilitySchemaVersion/GetComputeGlobalImageCapabilitySchemaVersion)
- [ListComputeImageCapabilitySchemas](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchemaSummary/ListComputeImageCapabilitySchemas)
- [GetComputeImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/GetComputeImageCapabilitySchema)
- [CreateComputeImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/CreateComputeImageCapabilitySchema)
- [UpdateComputeImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/UpdateComputeImageCapabilitySchema)
- [DeleteComputeImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/DeleteComputeImageCapabilitySchema)
- [ChangeComputeImageCapabilitySchemaCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/ChangeComputeImageCapabilitySchemaCompartment)
