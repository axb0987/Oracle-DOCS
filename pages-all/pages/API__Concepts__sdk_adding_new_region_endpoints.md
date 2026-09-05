# Adding Regions
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_adding_new_region_endpoints.htm
- Fetched: 2026-09-05 01:35 CDT

# Adding Regions

You can add new regions to an Oracle Cloud Infrastructure SDK.

At a high level, there are three methods for adding a region to an SDK:
- Create a regions config file on the machine running the SDK containing the region's information
- Set the`OCI_REGION_METADATA`region metadata environment variable
- If the SDK is running on an OCI instance within the region in question, programmatically opt-in to resolving the region's info from the instance metadata service

## Regions Metadata Schema

The schema for a single region's metadata, regardless of method used, is as follows:
```

```

The values for the field names above map exactly to the field names/values as described[here](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#AboutRegionsandAvailabilityDomains).
The following example shows the Sydney OC1 region:
```

```

## Regions Environment Variable

You can set the`OCI_REGION_METADATA`environment variable to specify the principal region. The value is a JSON blob, stored as a string. For example:

```

```

## Regions Config File

The regions configuration file (`~/.oci/regions-config.json`) enables you to provide metadata about regions which the SDK may otherwise not know about.

The Regions Configuration File will contain the metadata for one or more regions. The file's contents is a JSON array, where each item in the array is an object matching the region metadata schema.
The following example shows a valid regions configuration file:
```

```

## Programmatically Resolving from the Instance Metadata Service

The Instance Metadata Service will return the metadata for a single region - the region the instance hosting the instance metadata service is a part of. This option is not enabled by default, since the SDK may not be running within an OCI instance. This section shows examples on how to enable retrieving region metadata from the Instance Metadata Service.

### Examples

This section shows examples of how to opt-in to the Instance Metadata Service.
SDK for Java
```

```

SDK for Python
```

```

SDK for Ruby
```

```

SDK for Go
```

```

SDK for .NET
```

```

PowerShell Modules
```

```

CLI
```

```

Terraform
```

```
