# Extend Console Pages Using Schema Documents
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm
- Fetched: 2026-09-05 02:54 CDT

# Extend Console Pages Using Schema Documents

Review requirements, supported types, and examples for schema documents used with Terraform configurations in Resource Manager.

Schema documents are recommended for Terraform configurations when using Resource Manager. Including a schema document allows you to extend pages in the Oracle Cloud Infrastructure Console. Facilitate variable entry in the Create stack page by surfacing SSH key controls and by naming, grouping, dynamically prepopulating values, and more. Define text in the Application Information tab of the Stack details page that opens for a created stack.

## Requirements for Schema Documents

Schema documents for Resource Manager have the following requirements:
- 

YAML format.
- 

Data types must be consistent with the associated[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm).

For example, let's say that you declare the type`number`for the`availability`variable in the schema. In this situation,`availability`must have the same declared type (`number`) in the associated Terraform configuration. (By default, variables with no declared type use`string`.)
- 

Placement under the root folder of the Resource Manager Terraform configuration. (By default, the schema document assumes that the root folder is the working directory.)

## Supported Types (Dynamic Prepopulation and Controls)

This section lists the types supported by Resource Manager for[dynamic prepopulation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__prepop)and controls.

Most types require the compartment OCID (`dependsOn: required: compartmentId`). Some types have additional required or optional items. To determine required and optional items for a type, see[Meta Schema for Validation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#metaschema).

Optionally filter dynamically prepopulated lists by other variables using`dependsOn`. For example, filter subnets by VCN. For more information, see[Dynamic prepopulation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__prepop).
Note  
  

Descriptions in`schema.yaml`files are HTML encoded in the output.

When defined in the Terraform configuration, the following variables automatically prepopulate with values on the Console pages used to[create and edit the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack.htm). The stack's values are used when you select the Terraform actions[Plan](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-plan.htm),[Apply](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-apply.htm), and[Destroy](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-destroy.htm).
- `tenancy_ocid`(tenancy OCID)
- `compartment_ocid`(compartment OCID)
- `region`(region)
- `current_user_ocid`(OCID of the current user)

Type (rendered as a[dynamically prepopulated](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__prepop)dropdown field unless otherwise noted) Resource identifier Comments
`file`-- Surfaces a control for adding a single file by dropping or browsing. When this control is surfaced, a user can upload a file of any extension, such as a license key or certificate. For more information, see[File control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__file).
`oci:apm:domain:id`[Application Performance Monitoring (APM) domain](https://docs.oracle.com/iaas/application-performance-monitoring/doc/create-apm-domain.html)OCID
`oci:blockstorage:policies:id`[Volume backup policy](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#Oracle)
`oci:container:cluster:id`[Kubernetes Clusters](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#kubernetes_clusters)OCID
`oci:core:image:id`[Image](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm#one)OCID
`oci:core:instanceshape:name`[Instance shape](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)name
`oci:core:natgateway:id`[NAT gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)OCID
`oci:core:nsg:id`[Network security group](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)OCID
`oci:core:servicegateway:id`[Service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)OCID
`oci:core:ssh:publickey`-- Surfaces a control for adding one or more public SSH keys by dropping files or pasting key values. For more information, see[SSH key control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__ssh).
`oci:core:subnet:id`[Subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)OCID
`oci:core:vcn:id`[VCN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)OCID
`oci:database:autonomouscontainerdatabase:id`[Autonomous Container Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html#ADBAA-GUID-268B36E1-87D8-4649-A370-226E2AE3FC5C)OCID
`oci:database:autonomousdatabase:id`[Autonomous AI Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html#ADBAA-GUID-B5518C12-0362-4A98-AB35-3CB84AC83F31)OCID
`oci:database:autonomousdatabaseversion:id`[Autonomous AI Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html#ADBAA-GUID-B5518C12-0362-4A98-AB35-3CB84AC83F31)version
`oci:database:database:id`Database OCID for a[Base Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html)service database, or an[Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/index.html)database.
`oci:database:dbhome:id`DB home OCID (applies to[Base Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html)and[Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/index.html))
`oci:database:dbsystem:id`DB system OCID (applies to[Base Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html))
`oci:dbtools:connection:id`[DataBaseToolsConnection](https://docs.oracle.com/iaas/api/#/en/database-tools/latest/datatypes/DatabaseToolsConnectionSummary)OCID See[ListDatabaseToolsConnections](https://docs.oracle.com/iaas/api/#/en/database-tools/latest/DatabaseToolsConnection/ListDatabaseToolsConnections)API for details
`oci:identity:availabilitydomain:name`[Availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)name
`oci:identity:compartment:id`[Compartment](https://docs.oracle.com/iaas/Content/GSG/Concepts/concepts-account.htm#conceptcompartment)OCID
`oci:identity:domains:id`[Identity domain](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)OCID

Specify the tenancy OCID as`compartmentId`. See[ListDomains](https://docs.oracle.com/iaas/api/#/en/identity/latest/DomainSummary/ListDomains).
`oci:identity:dynamicgroups:id`[Dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm)OCID

Specify the tenancy OCID as`compartmentId`. See[ListDynamicGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/ListDynamicGroups).
`oci:identity:faultdomain:name`[Fault domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault)name
`oci:identity:groups:id`[Group](https://docs.oracle.com/iaas/Content/Identity/groups/managinggroups.htm)OCID

Specify the tenancy OCID as`compartmentId`. See[ListGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/ListGroups).
`oci:identity:region:name`[Region](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)name
`oci:identity:tag:value`[Tag key name from tag namespace](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm); see[TagSummary](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagSummary)Surfaces a control for adding defined and freeform tags. For more information, see[Tagging control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__tag).
`oci:kms:key:id`[Vault key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm)OCID; see[ListKeys](https://docs.oracle.com/iaas/api/#/en/key/latest/KeySummary/ListKeys)
`oci:kms:secret:id`[Vault secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)OCID; see[ListSecrets](https://docs.oracle.com//iaas/api/#/en//secretmgmt/latest/SecretSummary/ListSecrets)
`oci:kms:vault:id`[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)OCID
`oci:kubernetes:versions:id`See[GetClusterOptions](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/ClusterOptions/GetClusterOptions)
`oci:loadbalancer:loadbalancer:id`[load balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm)OCID
`oci:ods:project:id`[Data Science project](https://docs.oracle.com/iaas/Content/data-science/using/manage-projects.htm)OCID
`oci:resourcemanager:privateendpoint:id`[Resource Manager private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/private-endpoints.htm)OCID Specify a compartment (`compartmentId`) and a VCN (`vcnId`) for listing private endpoints. For an example, see[Example declaration for private endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__private-endpoints)on this page.

## Meta Schema for Validation

Use the following meta schema file to confirm that your schema document is using supported variable types.

[Meta Schema](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

```

```

## Example Schema Document

Following is an example schema document.

[Example](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

```

```

## How to Control Console Items

Use a schema document to control the display of stack variables and other items on stack details pages in the Console.

This display control is available for stacks created from a Terraform configuration file. Using a schema document, you can define how variables look and behave during stack creation and what text is displayed in the Application information tab for a created stack.

Following are Console display items that the schema document controls. To see relevant instructions and examples, expand a display item that you're interested in.

[Field label and description](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a field label and description for a variable:
- Add the lines`title: <field_label>`and`description: <field_description>`.

Example image for a variable field label and description:
[

Example declaration for a variable field label and description:
```

```

[Formatted variable descriptions](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

The following formats are supported in a variable description:

Format Code
Strong (bold)`<strong>...</strong>`
Emphasis (italics)`<em>...</em>`
Link`<a href='...'>...</a>`
You can also combine supported formatting. Examples:
- Strong and emphasis (bold and italics):`<strong><em>...</em></strong>`OR`<em><strong>...</strong></em>`
- Strong and emphasis in link text (bold and italics in link text):`<a href='...'><strong>...</strong><em>...</em></a>`

Example of formatted variable description:
```

```

[Default value](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a variable with a default value:

- Add the line`default: <default-value>`.

Example image for a variable with a default value:
[

Example declaration for a default value:
```

```

[Multiline text field](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a variable as a multiline text field:
- Add the line`multiline: true`.

To declare a default value with multiple lines:
- Separate each line with`\n`.

Example image for a variable rendered as a multiline text field, with two lines of text entered:
[

Example declaration for a multiline text field:
```

```

[Group and order](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a group (box) of variables, with the variables in a prescribed sequence:

- Add a`variableGroups`block.
- Add a`title`line to this block.
- Add a`variables`block to`variableGroups`.
- Add variables to the`variables`block in the order that you want.

Example image for a group of variables:
[

Example declaration for a group of variables with a prescribed order:
```

```

[SSH key control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a variable as an SSH key control:
- Add the line`type: oci:core:ssh:publickey`.

Example image for an SSH key control:
[

Example declaration for an SSH key control:
```

```

[File control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a variable as a file control:
- 

Add the line`type: file`.
Note  
  
The uploaded file is stored in Base64 format. To use the file, decode the output. For example, add the following code to an`outputs.tf`file in the Terraform configuration.
```

```

Example image for a file control:
[

Example declaration for a file control:
```

```

[Tagging control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a variable as a tagging control:
- 

Add the line`type: oci:identity:tag:value`.
Note  
  
To prepopulate tag values in the Console, access the values from the Terraform configuration. For example, add the following code to a`main.tf`file in the Terraform configuration.
```

```

Example image for a tagging control:
[

Example declaration for a tagging control:
```

```

[Complex data types](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

This section describes complex data types for list, map, and object variables. We recommend including a`title`field for any complex data type.

List and map variable guidelines:
- Define the`valueType`field when specifying the schema variable.
- For any`valueType`variable, set`visible`to`false`.

Object variable guidelines:
- Include an`attributes`field to define the attribute variables of the object.
- For any`attribute`variable, include an`actualName`field that corresponds to the attribute name defined in the Terraform file for the object variable.
- For any`attribute`variable, set`visible`to`false`.

Example declarations, from[Example Schema Document](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#exampleschema):
```

```

[Dynamic prepopulation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To dynamically prepopulate variables with values based on dependencies:

- Add the lines`type: <supported-type>`and`dependsOn: <other_variable>`.

&lt;supported-type&gt; is a type listed at[Supported Types (Dynamic Prepopulation and Controls)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#types).

Example image for a dynamically prepopulated variable:
[

Example declaration for a dynamically prepopulated variable:
```

```

Example declaration for private endpoints:
```

```

Example declarations for VCN depending on compartment, with subnet depending on both compartment and VCN:
```

```

Image example declaration 1, where image depends on compartment only (the one mandatory`dependsOn`field):
```

```

Image example declaration 2, where image depends on compartment, operating system, operating system version, and shape:
```

```

[Enumerated values (single value selection)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render enumerated values for a variable (allowing selection of one value):

- Add the lines`type: enum`and add an`enum`block.

Example image for a variable with enumerated values that allow selection of a single value:
[

Example declaration for a variable with enumerated values:
```

```

[Enumerated values (multiple value selection)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render enumerated values for a variable (allowing selection of multiple values):

- Add the lines`type: enum`and add an`enum`block.
- Add the lines`additionalProps:`and add a`allowMultiple:true`block.

Example image for a variable with enumerated values that allow selection of multiple values:
[

Example declaration for a variable with enumerated values (multiple value selection):
```

```

[Check box](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a variable as a check box:
- Add the line`type: boolean`.

Example image for a check box variable:
[

Example declaration for a check box variable:
```

```

[Visibility dependency](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

Note  
  

Groups have higher priority than the groups' constituent variables. For example, if a variable is visible within a group that isn't visible, then the entire group isn't visible.

Supported operations:
- `and`
- `eq`(equal)
- `ge`(greater than or equal)
- `gt`(greater than)
- `le`(less than or equal)
- `lt`(less than)
- `not`
- `or`
To hide or show variables or variable groups depending on other variables:
- Add the line`visible: <other_variable>`.

Example of variable Use existing vault? , whose visibility depends on the user selection for the variable Enable vault support? :
[

Example declarations that show the "Application Name" and "API Gateway Name" fields (`functions_app_name`and`apigateway_name`) only when the "Provision Functions and API Gateway?" check box (`enable_functions_apigateway`) is selected:
```

```

[Password](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To render a variable as a password:
- Add the line`type: password`.
To require re-entry for confirmation of the entered password:
- Add the line`confirmation: true`.

Example image for a password variable that requires confirmation:
[

Example declaration for a password variable, requiring confirmation:
```

```

[Required variables](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To require a value for a variable:

- Add the line`required: true`.

Example image for a required variable, with validation warning:
[

Example declaration for a required variable:
```

```

[Optional variable](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To mark a variable as optional:

- Add the line`required: false`.

Example image for an optional variable:
[

Example declaration for an optional variable:
```

```

[Validation pattern](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To validate the value entered for a variable against a regular expression pattern:

- Add the line`pattern: <regular-expression>`.

&lt;regular-expression&gt; is the validation pattern specific to the value that you want to validate.

Hyperlink pattern example:`^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$`

Example image for a validation error for an entered value:
[

Example declaration for a variable with a validation pattern:
```

```

[Sensitive variables (Outputs tab, Application information tab)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

The output of a sensitive-marked variable displays as &lt;sensitive&gt; with[an Unlock option in the Application information tab. This tab is visible in the Job details and Stack details pages.

Example image for a sensitive-marked variable ( Generated SSH private key ) on the Application information tab:
[

For more information about the Terraform sensitive argument, see[sensitive - Suppressing Values in CLI Output](https://developer.hashicorp.com/terraform/language/values/outputs#sensitive-suppressing-values-in-cli-output).

To mark a variable as sensitive:
- Add the line`sensitive: true`.

Example declaration for a sensitive-marked variable:
```

```

[Application information tab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

To display the Application information tab for a stack created from your Terraform configuration:
- Add lines for the schema`title`and`description`.
- Optionally add a line for a blue informational text box:`informationalText`.
- Add at least one output in the`outputs`section, optionally grouped using`outputGroups`.
To allow copying of an output value displayed in the Application information tab:
- Set the type: Add the line`type: copyableString`.

Example image for the Application information tab:
[

Example declaration for a schema title, description, and outputs:
```

```

## How to Interact with Console Items

This section describes how to interact with schema-controlled display of stack information in the Oracle Cloud Infrastructure Console.

Stack information is affected by the schema document (if any) that you include in the Terraform configuration for creating the stack. The schema document affects how variables look and behave during stack creation and what text is displayed in the Application Information tab for a created stack.

[Unlock sensitive variables](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#)

An Unlock option on the Application information tab indicates a[sensitive-marked variable](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__sensitive). This option switches between Unlock and Lock .
- To view the value, select Unlock .
- To hide the value, select Lock .

Example image for a sensitive-marked variable ( Generated SSH private key ) on the Application information tab:
[
