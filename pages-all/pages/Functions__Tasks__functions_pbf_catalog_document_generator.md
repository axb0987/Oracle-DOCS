# Document Generator Function
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_document_generator.htm
- Fetched: 2026-09-05 02:07 CDT

# Document Generator Function

Find out how to use the Document Generator pre-built function in OCI Functions to generate documents based on Office templates and JSON data.

## Common Usage Scenarios

Common ways to use the Document Generator function include:
- Place an Office Template and JSON data in object storage and directly invoke the function to generate PDF documents and store the results in object storage.

Services related to the Document Generator function include:
- [Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm)

## Prerequisites And Recommendations

The following are best practices when using this pre-built function:
- Make sure that the VCN linked to the application facilitates access to other OCI services by using a service gateway, internet gateway, or NAT gateway.
- Set the default memory size to 512 MB for most tasks. Using bigger data sets, bundling fonts, or using batch processing might require more memory. For example, a 3072 MB memory allocation can typically support the generation of documents containing approximately 15,000 rows of data.
- For batch processing, set the pre-built function timeout to 300 seconds.

## Configuring the Document Generator Function

To configure a Document Generator function, perform the following steps:

- On the Pre-Built Functions page, select Document Generator , and then select Create function .
- Configure the Name , Compartment , and Application as follows:

- Name: A name of your choice for the new function. The name must start with a letter or underscore, followed by letters, numbers, hyphens, or underscores. Length can be 1–255 characters. Avoid entering confidential information.

To create the function in a different compartment, select Change Compartment .
- Application: Select the application in which you want to create the function.

If a suitable application doesn't already exist in the current compartment, select Create new application and specify the following details:
- Name: A name for the new application. Avoid entering confidential information.
- VCN: The VCN (virtual cloud network) in which to run functions in the application. Optionally, select VCN compartment: to select a VCN from a different compartment.
- Subnets: The subnet (or subnets, up to a maximum of three) in which to run functions. Optionally, select Subnets compartment: to select a subnet from a different compartment.
- Shape: The processor architecture of the compute instances on which to deploy and run functions in the application. All the functions in the application are deployed and run on compute instances with the same architecture. The function's image must contain the necessary dependencies for the architecture you select.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Security attributes: If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- Configure the IAM policy for pre-built functions.

By default, OCI Functions creates a dynamic group and an IAM policy with the policy statements required to run the pre-built function. Proceed as follows:
- If you want OCI Functions to automatically create the dynamic group and policy, make no changes to accept the default behavior.
- If you don't want OCI Functions to automatically create the dynamic group and policy, select Do not create a dynamic group and IAM policy .
Important  
  
If you select the Do not create a dynamic group and IAM policy option, you must define the dynamic group and the IAM policy yourself. For more information, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_document_generator.htm#functions_pbf_catalog_document_generator_plus__permissions-document-generator).
- Configure function memory and timeout values as follows:

- Memory (in MBs): The maximum amount of memory that the function can use while running, in megabytes. This is the memory available to the function image. (Default: 512 MB)
- Timeout (in seconds): The maximum amount of time that the function can run for, in seconds. If the function doesn’t complete in the specified time, the system cancels the function. (Default: 300)
- (Optional) Configure Provisioned concurrency to minimize any initial delays when invoking the function by specifying a minimum number of concurrent function invocations for which you want to have execution infrastructure constantly available. (Default: Not selected)

If selected, specify the number of provisioned concurrency units assigned to this function. Default: 10.

For more information about provisioned concurrency, see[Reducing Initial Latency Using Provisioned Concurrency](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingprovisionedconcurrency.htm).
- Set the function configuration parameters as described in[Configuration Options](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_document_generator.htm#functions_pbf_catalog_document_generator_plus).
- Optionally enter any tags in the Tags section. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

The deploy dialog displays the tasks to deploy the function (see[Finishing Pre-Built Function Deployment](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_finishing_prebuilt_deploy.htm)).

## Configuration Options

### Configuration Parameters

Name Description Required
`PBF_LOG_LEVEL`Logging level, options are`DEBUG`,`INFO`,`WARN`, and`ERROR`. Defaults to`INFO`. No

### Permissions

Running a function requires certain IAM policies. If you selected the Do not create a dynamic group and IAM policy option when creating the function, you must define the dynamic group and the IAM policy yourself.

To set the proper policies, perform the following steps:
- Create a dynamic group with the rule:

```

```

- Configure an IAM policy using the dynamic group:

```

```

Note  
  
Replace`<function-ocid>`with the OCID of the function that you created in preceding steps.
Note  
  
Replace`<dynamic-group-name>`with the name of the dynamic group that you created using the function's OCID.
Note  
  
Replace`<compartment_ocid>`with the OCID of the compartment that contains the function.

### Invoking This Function

You can invoke the function in the following ways:
- Invoke the function directly as documented in[Invoking Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm)by creating a request body as shown in the following JSON example.

HTTP Request and Response Payloads

For a full list of request and response values, see[Pre-Built Function Document Generator API](https://docs.oracle.com/iaas/api/#/en/functionsdocgenpbf/latest/).

### Example Requests and Responses

Example 1: Generating a single PDF

Request:
```

```

Response - success:
```

```

Response - failure:
```

```

For more information, see:
- [RequestSingle Reference](https://docs.oracle.com/iaas/api/#/en/functionsdocgenpbf/latest/RequestSingle)
- [ResponseSingle Reference](https://docs.oracle.com/iaas/api/#/en/functionsdocgenpbf/latest/datatypes/ResponseSingle)
- [ResponseError Reference](https://docs.oracle.com/iaas/api/#/en/functionsdocgenpbf/latest/datatypes/ResponseError)

Example 2: Generating multiple PDFs - data specified inline

Request:
```

```

Response - success:
```

```

For more information, see:
- [RequestBatch Reference](https://docs.oracle.com/iaas/api/#/en/functionsdocgenpbf/latest/datatypes/RequestBatch)
- [ResponseBatch Reference](https://docs.oracle.com/iaas/api/#/en/functionsdocgenpbf/latest/datatypes/ResponseBatch)

### Document Names in Batch Output

With`"responseType": "BATCH"`, multiple documents are produced. Output document names must be unique.

You can control the naming of these documents using:
- `{documentId}`in the document name
- basic tags in the document name

Using DocumentId in the Document Name

You can control the naming of documents produced as batch output using`{documentId}`in the document name.

output.objectName format Description Examples
`invoice{documentId}.pdf`No padding. Starts at 1. invoice1.pdf, invoice2.pdf
`invoice{documentId|zeroPadding=auto}.pdf`Automatic padding based on number of documents in batch. Starts at 1. invoice01.pdf ... invoice10.pdf
`invoice{documentId|firstId=51}.pdf`No zero padding. Starts at 51. invoice51.pdf, invoice52.pdf
`invoice{documentId|firstId=51,zeroPadding=5}.pdf`5 digits left padding with 0. Starts at 51. invoice00051.pdf, invoice00052.pdf
`invoice{documentId|zeroPadding=5}.pdf`5 digits left padding with 0. Starts at 1. invoice00001.pdf, invoice00002.pdf

Using Basic Tags in the Document Name

You can control the naming of documents produced as batch output using basic tags in the document name. The basic tags will use the JSON data related to that document.

output.objectName format JSON data Examples
`invoice{invoice_number}.pdf``[ {"name":"Bob", "invoice_number":101}, {"name":"Alice", "invoice_number":102} ]`invoice101.pdf, invoice102.pdf
`doc.{name}.{invoice_number}.pdf``[ {"name":"Bob", "invoice_number":101}, {"name":"Alice", "invoice_number":102} ]`doc.Bob.101.pdf, doc.Alice.102.pdf
`movie{movies.0.movieName}.pdf``[ {"movies": [ {"movieName": "Arrival"} ] }, {"movies": [ {"movieName": "Matrix"} ] } ]`movieArrival.pdf, movieMatrix.pdf

### Supported Document Types

From Template (contentType) To Output (contentType)
Microsoft Word &gt;= 2010 (`application/vnd.openxmlformats-officedocument.wordprocessingml.document`) PDF (application/pdf)
Microsoft Word &gt;= 2010 (`application/vnd.openxmlformats-officedocument.wordprocessingml.document`) Microsoft Word &gt;= 2010 (`application/vnd.openxmlformats-officedocument.wordprocessingml.document`)
Microsoft Excel &gt;= 2010 (`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`) PDF (application/pdf)
Microsoft Excel &gt;= 2010 (`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`) Microsoft Excel &gt;= 2010 (`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`)

### Fonts

The following fonts are available when generating a PDF:
- Caladea
- Cookie
- Carlito
- DejaVu
- LiberationMono (Courier)
- LiberationSans (Arial)
- LiberationSerif (Times New Roman)
- NotoSans-Black
- NotoSans-BoldItalic
- NotoSans-ExtraLight
- NotoSans-Light
- NotoSans-MediumItalic
- NotoSans-SemiBoldItalic
- NotoSans-BlackItalic
- NotoSans-ExtraBold
- NotoSans-ExtraLightItalic
- NotoSans-LightItalic
- NotoSans-Regular
- NotoSans-Thin
- NotoSans-Bold
- NotoSans-ExtraBoldItalic
- NotoSans-Italic
- NotoSans-Medium
- NotoSans-SemiBold
- NotoSans-ThinItalic
- NotoSansJP-Bold
- NotoSansJP-Regular
- NotoSansKR-Regular
- NotoSansKR-Bold
- NotoSansSC-Regular
- NotoSansSC-Bold
- NotoSansTC-Regular
- NotoSansTC-Bold.otf
- NotoSansArabic-Regular
- NotoSansArabic-Bold
- NotoSansHebrew-Regular
- NotoSansHebrew-Bold
- NotoSerif-Bold
- NotoSerif-BoldItalic
- NotoSerif-Italic
- NotoSerif-Regular
- OracleSans-Bold
- OracleSans-Regular
- Oswald-Bold
- Oswald-ExtraLight
- Oswald-Light
- Oswald-Medium
- Oswald-Regular
- Oswald-SemiBold

If you need a font that is not in this list, you can specify a font bundle in the Document Generator request. A font bundle is a zip file containing .ttf and .otf files that will be used during PDF generation. For an example, see[RequestSingle Reference](https://docs.oracle.com/iaas/api/#/en/functionsdocgenpbf/latest/RequestSingle).

### Protecting a Generated PDF Document with a Password

When generating a single PDF (with`"requestType": "SINGLE"`) or multiple PDFs (with`"requestType": "BATCH"`), you can specify a password to protect the generated PDF. Having generated the PDF, the password has to be entered before the PDF can be opened.

To specify the password to protect the generated PDF, include`"documentOpenPassword" : "<a-password>"`in an`"options"`section of the request. The value of`<a-password>`must be an alphanumeric string of between 1 and 127 characters in length.

For example:

```

```

### Document Generator Template Tags

For a full list of template tags, see:
- [Document Generator MS Word Tags](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm)
- [Document Generator MS Excel Tags](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../non-dita/DocGenPBF-xls/markdown/DocGen-Excel-Template-Tags.htm)

### Troubleshooting

OCI Functions common status codes

The following table summarizes common OCI Functions errors that you might encounter when working with pre-built functions:

Error Code Error Message Action
200 Success None
404 NotAuthorizedOrNotFound Verify that the required policies are configured (see[Running Fn Project CLI commands returns a 404 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#Running_Fn_Project_CLI_commands_returns_a_404_error)).
444 Timeout

The connection between the client and OCI Functions was interrupted during function execution (see[Invoking a function causes the client to report a timeout, and a 444 error is shown in the function's logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_Function_timeout_client_message_and_a_444_error)). A retry might solve the issue.

Note that most clients have an inner timeout of 60 seconds. Even when the pre-built function timeout is set to 300 seconds, the following might be required:
- When using the OCI CLI : Use --read-timeout 300
- When using the OCI SDK : Set the read timeout to 300 when creating the client
- When using DBMS_CLOUD.SEND_REQUEST : Use UTL_HTTP.set_transfer_timeout(300);

For more information, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsinvokingfunctions.htm).
502, 504 (various) Most issues return a 502 status code (see[Invoking a function returns a Function failed message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_Functionfailed_message_and_a_502_error)). A 502 error with the message "error receiving function response" might be resolved by increasing the memory allocation. A 502 might occur occasionally when the function is in some transient state. A retry might solve the issue.

To further identify the cause, enable logging features for the pre-built function (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsexportingfunctionlogfiles.htm)). For detailed information on troubleshooting a function, see[Troubleshooting OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting.htm).

Document Generator pre-built function status codes

Status Code Description
200 Success
207 For a responseType=BATCH, verify the response code for each individual document.
400

Validation error or Processing error.

If the message`Output file could not be generated. Try increasing the Function Memory`is returned, increase the memory allocation.
500 Internal error.

To further identify the cause, enable logging features for the pre-built function (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsexportingfunctionlogfiles.htm)).

Log Analysis Tips

All the pre-built functions provide an option to specify the logging level as a configuration parameter. You can set the logging level to`DEBUG`to get more information.

Since an application has multiple functions, the pre-built function log entries are identified by the prefix "PBF | &lt;PBF NAME&gt; ".

For example, a log entry for the Document Generator pre-built function looks similar to the following:
```

```
