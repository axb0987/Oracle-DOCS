# Using the CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm
- Fetched: 2026-09-05 01:36 CDT

# Using the CLI

This topic describes how to use the CLI to access Oracle Cloud Infrastructure and carry out service-related tasks. This topic assumes that you have[configured the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm)and are ready to start using it.
Tip  
  
The CLI has an interactive mode that provides automatic command completion and parameter information and suggestions. For more information, see[Using Interactive Mode](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing_topic-Using_Interactive_Mode.htm).

To explore further,[Getting Started with the Command Line Interface](https://docs.oracle.com/iaas/Content/GSG/Tasks/gettingstartedwiththeCLI.htm)provides an end-to-end walk-through of using the CLI to launch an instance.

## Command Line Syntax

Most commands must specify a service, followed by a resource type and then an action. The basic command line syntax is:
```

```

For example, this syntax is applied as follows:

- `compute`is the &lt;service&gt;
- `instance`is the resource &lt;type&gt;
- `launch`is the &lt;action&gt;, and
- the rest of the command string consists of &lt;options&gt;.

The following command to launch an instance shows a typical command line construct.

```

```

In the previous example, you can provide a friendly name for the instance using the`--display-name`option. Avoid entering confidential information.

## Basic Examples

This section provides examples of basic operations using the CLI.
Note  
  

Using Environment Variables for OCIDs

Several of the CLI examples use environment variables for OCIDs, such as:

- $T for a tenancy OCID
- $C for a compartment OCID

For example:

```

```

To get a namespace, run the following command.

```

```

To list compartments, run the following command.

```

```

To get a list of buckets, run the following command.

```

```

To list users and limit the output, run the following command.

```

```

To add a user to a group, run the following command.

```

```

## Getting Help with Commands

You can get help for any command using`--help`,`-h`, or`-?`. For example:

```

```

```

```

```

```

### Viewing all the CLI Help

You can view the[command line help](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Determining the Installed Version of the CLI

To get the installed version of the CLI, run the following command.

```

```

## Authenticating Using Instance Principals

Instance principals is an IAM service feature that enables instances to be authorized actors (or principals) that can perform actions on service resources. Each compute instance has its own identity, and it authenticates using the certificates that are added to it. These certificates are automatically created, assigned to instances and rotated, preventing the need for you to distribute credentials to your hosts and rotate them.

To enable instance principal authorization from the CLI, you can set the authorization option (`--auth`) for a command.

For example:

```

```

You can also enable instance principle authorization by setting the`OCI_CLI_AUTH`environment variable.
For example:

```

```

Note  
  
The value set for`--auth`parameter takes precedence over the environment variable.

For more information on instance principals, see[Calling Services from an Instance](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

## Using a Proxy Server

The CLI uses HTTP requests to make calls to Oracle Cloud Infrastructure services. If you need to use a proxy server for outgoing HTTP requests in your environment, you can use one of the following methods:

Use the --proxy parameter on the command line

You can specify a proxy server on the command line by including the`--proxy`parameter when calling a CLI command.

For example:

```

```

Add a proxy entry to the CLI configuration file

For details, see[Specifying a Proxy Server](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm#cliconfigure_topic_Proxy_Server).

Use environment variables

Set the`HTTP_PROXY`and`HTTPS_PROXY`environment variables to point to your proxy server.
For example, on Linux:

```

```

On Windows, using PowerShell:

```

```

## Using Dates and Times in CLI Commands

The CLI supports the following accepted date formats.
- 

UTC with milliseconds

```

```

- 

UTC without milliseconds

```

```

- 

UTC with minute precision

```

```

- 

Timezone with milliseconds

```

```

- 

Timezone without milliseconds

```

```

- 

Timezone with offset with minute precision

```

```

- 

Date Only (This date will be taken as midnight UTC of that day)

```

```

- 

Epoch seconds

```

```

Note  
  
In our datetime formats, the`T`can be replaced with a space. For example, both`"2017-09-15 20:30:00.123Z"`and`2017-09-15T20:30:00.123Z`are acceptable. (Note that if you do not include the`T`, you must wrap the value in quotes.) We also support time zones with and without the colon. Both`+10:00`and`+1000`are acceptable.

## Managing CLI Input and Output

The CLI provides several options for managing command input and output.

### Passing Complex Input

Complex input, such as arrays and objects with more than one value, are passed in JSON format and can be provided as a string at the command line, as a file, or as a command line string and as a file.

### MacOS, Linux, or Unix

The following command shows how to pass two values for the`--metadata`object.

```

```

### Windows
On Windows, to pass complex input to the CLI as a JSON string, you must enclose the entire block in double quotes. Inside the block, each double quote for the key and value strings must be escaped with a backslash (\) character.

The following command shows how to pass two values for the`--metadata`object on Windows.

```

```

Note  
  

JSON Errors

The error message "Parameter '&lt;PARAMETER NAME&gt;' must be in JSON format." indicates that the value you passed for the parameter with name "PARAMETER NAME" was not valid JSON. This error is typically a result of the JSON string not being escaped correctly.

For more information about using JSON strings, see[Advanced JSON Options](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)

### Format Output as a Table

By default, all responses to a command are returned in JSON format. For example, a response like the following is returned when you issue the command to get a list of regions.
```

```

In some cases, readability can become an issue, which is easily resolved by formatting a response as a table. To get a response to a command formatted as a table, run the following command.

```

```

The following sample list of regions is returned as a two column table.
```

```

### Using Queries

You can filter output using the`--query`option for JSON. This option uses the JMESPath query language for JSON.

Filtering is very useful when dealing with large amounts of output. For example, the following command returns a list of all compartments:

```

```

This command returns a lot of information. Some of the fields returned include compartment-id, name, lifecycle-state, and defined-tags.

Selecting Fields to Display

You can select just the fields you want by specifying the name of the array and the name of one or more fields, passed as a comma-delimted array:
`<name of the array>[].[<the name of the field>]`
Note  
  

- Field names are case-sensitive. Provide the name of the field exactly as it is specified in the JSON object.
- If non-existing field names are specified, the query will include`null`in your output.
- If the field names contain special characters or spaces, wrap the field name in escaped double quotes (`\"`for bash or`\`"`for PowerShell).
For example, to return just the name of the compartment and the lifecycle state:
```

```

This will return output similar to the following:
```

```

You can also retrieve information as objects with customized field names:
```

```
For example:
```

```

This will return output similar to the following:
```

```

Specifying Search Conditions
You can specify a search condition for the returned information. For example, to only return a compartment named`blocktest`:
```

```

This will return information similar to the following:
```

```

You can specify multiple search conditions. The following example retrieves the name and lifecycle status of compartments created before 2019 that have the tag MySpecialTag:
```

```

This command will return output similar to the following:
```

```

For more information about the JMESPath query language for JSON, see[JMESPath](http://jmespath.org/).

## Advanced JSON Options

You can get the correct JSON format for command options and commands.
- 

For a command option, use`--generate-param-json-input`and specify the command option that you want to get the JSON for. To generate the JSON for creating or updating a security rule, run the following command.

```

```

- 

For an entire command, use`--generate-full-command-json-input`. To generate the JSON for launching an instance, run the following command.

```

```

### Order of Precedence for JSON Input

The CLI supports combining arguments on the command line with file input. However, if the same values are provided in a file and on the command line, the command line takes precedence.

### Using a JSON File for Complex Input

You can pass complex input from a file by referencing it from the command line. For Windows users, this removes the requirement of having to escape JSON text. You provide a path to the file using the`file://`prefix.

### Path Types

Using`testfile.json`as an example, the following types of paths are supported.
- Relative paths from the same directory, for example:`file://testfile.json`and`file://relative/path/to/testfile.json`
- Absolute paths on Linux, MacOS or Unix, for example:`file:///absolute/path/to/testfile.json`
- Full file paths on Windows, for example:`file://C:\path\to\testfile.json`
Note  
  

File Path Expansions

File path expansions, such as "~/", "./", and "../", are supported. On Windows, the "~/" expression expands to your user directory, which is stored in the %USERPROFILE% environment variable. Using environment variables in paths is also supported.

### File Locations

The following file locations are supported.
- 

Your home directory.

```

```

- 

The current directory.

```

```

- 

The /tmp directory (Linux, Unix, or MacOS).

```

```

- 

The C:\temp directory (Windows).

```

```

### Examples of Using a JSON File as Input

The examples in this section use JSON that's generated for a command option and an entire command. The JSON is saved in a file, edited, and then used as command line input.

### Use File Input for a Command Option

This end-to-end example shows how to generate the JSON for a security list id option used to create a subnet. The JSON is saved in a file, edited, and then used as command line input.

[Response from the Command](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm#)

```

```

[Response from the Command](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm#)

```

```

[Use a JSON File as Input for a Security List Option](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm#)

- 

To generate the JSON for the`security-list-ids`option, run the following command.

```

```

- 

Create a file and add the following content, which was returned in step 1. This content doesn't have to be escaped or on a single line, it just has to contain valid JSON.
```

```

- 

Edit the file and replace the "string" values with values, as shown in the following example.

```

```

- Save the file as "security-list.json".
- 

To create the subnet using "security-list.json" as input, run the following command.

```

```

#### Use File Input for an Entire Command

This end-to-end example shows how to generate the JSON to create a virtual cloud network (VCN). The JSON is saved in a file, edited, and then used as command line input.

[Use a JSON File as Input to Create a VCN](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm#)

- 

To generate the JSON needed to create a VCN, run the following command.

```

```

- 

Create a file and add the following content, which was returned in step 1. This content doesn't have to be escaped or on a single line, it just has to contain valid JSON.
```

```

- 

Edit the file and replace the "string" values with values, as shown in the following example.

```

```

- Save the file and name it "create-vcn.json"
- To create the VCN using "create-vcn.json" as input, run the following command.

```

```

## Advanced Examples

The following examples show how you can use the CLI to complete complex tasks in Oracle Cloud Infrastructure.

### Working with Object Storage

You can use the CLI for several object operations with the Object Storage service.

### Uploading and Downloading Files

Objects can be uploaded from a file or from the command line (STDIN), and can be downloaded to a file or to the command line (STDOUT).

Upload an object:

```

```

Upload object contents from the command line (STDIN):

```

```

Download an object:

```

```

Print object contents to the command line (STDOUT):

```

```

### Bulk Operations in Object Storage

The CLI supports the following bulk operations in Object Storage:
- 

Uploading files in a directory and all its subdirectories to a bucket

```

```

- 

Downloading all objects, or all the objects that match a specified prefix, in a bucket

```

```

- 

Deleting all objects, or all the objects that match a specified prefix, in a bucket

```

```

Bulk operations support several options that let you:
- Overwrite or skip files/objects using`--overwrite`or`--no-overwrite`. ( Note : If you pass neither of these options you are prompted for confirmation every time there is something to overwrite.)
- Limit delete, upload, or download operations using`--prefix`and/or`--delimiter`
- Preview a bulk deletion with`--dry-run`

To get more information about the commands for bulk operations, run the following help commands:
```

```

### Multipart Operations in Object Storage

Multipart operations for Object Storage include object uploads and downloads.

### Multipart Uploads

Large files can be uploaded to Object Storage in multiple parts to speed up the upload. By default, files larger than 128 MiB are uploaded using multipart operations. You can override this default by using the`--no-multipart`option.

You can configure the following options for the`oci os object put`command:
- `--no-multipart`overrides an automatic multipart upload if the object is larger than 128 MiB. The object is uploaded as a single part, regardless of size.
- `--part-size`in MiB, to use in a multipart operation. The default part size is 128 MiB and a part size that you specify must be greater than 10 MiB. If the object is larger than the`--part-size`, it is uploaded in multiple parts.
- `--parallel-upload-count`, to specify the number of parallel operations to perform. You can use this value to balance resources and upload times. A higher value may improve times but consume more system resources and network bandwidth. The default value is 10.

The`--resume-put`command allows you to resume a large file upload in cases where the upload was interrupted.
Note  
  

Multipart Uploads from STDIN

Objects uploaded from STDIN are uploaded in multiple parts. If the object content is smaller than 10 MiB, the upload is only 1 part, and the MultipartUpload API is used for the upload. Specifying`--no-multipart`when uploading from STDIN will result in an error.

The following example shows the command for a multipart upload if the object is larger than 200 MiB.

```

```

For more information about multipart uploads, see[Using Multipart Uploads](https://docs.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm).

### Multipart Downloads

Large files can be downloaded from Object Storage in multiple parts to speed up the download.

You can configure the following options for the`oci os object get`command:
- `--multipart-download-threshold`lets you specify the size, in MiB at which an object should be downloaded in multiple parts. This size must be at least 128 MiB.
- `--part-size`, in MiB, to use for a download part. This gives you the flexibility to use more (smaller size) or fewer (larger size) parts as appropriate for your requirements. For example, compute power and network bandwidth. The default minimum part size is 120 MiB.
- `--parallel-download-count`lets you specify how many parts are downloaded at the same time. A higher value may improve times but consume more system resources and network bandwidth. The default value is 10.

The following example shows the command to download any object with a size greater than 500 MiB. The object is downloaded in 128 MiB parts.

```

```
