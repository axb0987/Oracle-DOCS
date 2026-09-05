# Generating SDKs for an API Resource
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaygeneratingsdk.htm
- Fetched: 2026-09-05 01:38 CDT

# Generating SDKs for an API Resource

Find out how to generate an SDK for an API from an API description with the API Gateway service to give developers programmatic access to back-end services.

When using the API Gateway service, you have the option to generate SDKs (Software Development Kits) for an API resource. If you use the API resource to deploy an API on an API gateway, the SDKs you generate give developers programmatic access to the API. To make it easy to integrate with the API, you can generate SDKs for a number of languages and platforms including:
- Android
- Java
- JavaScript
- Swift
- TypeScript

Having generated an SDK, you can download a zip file containing the SDK resources (API client libraries, configurations, and documentation) and distribute it to developers writing code accessing the API.

To generate an SDK for an API resource, you must have created an API description for the API resource. You create an API description by uploading an API description file (sometimes called an 'API specification', or 'API spec') written in a supported language. Currently, OpenAPI Specification version 2.0 (formerly Swagger Specification 2.0) and version 3.0 are supported. For more information about API resources and API descriptions, see[Creating an API Resource with an API Description](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm).

Generating an SDK using the API Gateway service is optional. You can deploy an API on an API gateway without generating an SDK. Likewise, you can provide programmatic access to an API you've deployed on an API gateway with an SDK you've created in a different tool. You can also use the API Gateway service simply to generate an SDK from an API description file, without using the associated API resource to deploy an API on an API gateway.

Note the following:
- An API resource can have:
- zero SDKs
- one or more SDKs for the same language or platform
- one or more SDKs for different languages or platforms
- You can only ever generate a completely new SDK. Every generated SDK has a unique identifier (OCID). You cannot "re-generate" an existing SDK that has already been generated (although you can change the display name of an existing SDK).
- It is your responsibility to manage generated SDKs. If you upload an updated version of an API description file from which you previously generated an SDK, a new SDK is not generated automatically. You have to decide whether to generate a new SDK, or not. If you do generate a new SDK, you have to decide whether to delete the existing SDK, or retain it.
- You can only generate an SDK if an uploaded API description file has not failed validation checks. Note that you can generate an SDK if the uploaded API description file passed validation checks with warnings. However, we recommend you resolve any warnings before generating the SDK.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaygeneratingsdk.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaygeneratingsdk.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaygeneratingsdk.htm#)
- 

To generate an SDK for an API resource from an uploaded API description file, using the Console:
- On the APIs list page, select the API resource for which you want to generate an SDK. If you need help finding the list page, see[Listing API Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-apis.htm).
- If you haven't already uploaded an API description file, follow the instructions in[Creating an API Resource with an API Description](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm)to create an API resource and specify an API description file to upload.
- On the SDKs tab, select Create SDK .
- In the Create SDK dialog:
- Specify:
- Name: The name of the new SDK. Avoid entering confidential information.
- Programming Language: The programming language or platform for which you want to generate an SDK from the uploaded API description file.
- &lt;Language&gt; Properties: Depending on the programming language or platform you choose, specify values for language-specific or platform-specific properties. Required properties are always shown. Select Show Optional Properties to see and enter values for additional, optional properties.
- (Optional) In the Tags section, select Add tag to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to generate the new SDK.

The SDK is generated. Note that it can take a few minutes to generate the SDK.

When the SDK has been generated successfully, the SDK details page shows the programming language or platform that you specified for the SDK (and the values of any required and optional properties).
- Select Download SDK to obtain a zip file containing the SDK resources (API client libraries, configurations, and documentation) that have been generated from the API description file for the API resource.

Having successfully generated the SDK for the API resource, you can distribute the zip file to developers who are writing code accessing the API.
- 

To generate an SDK for an API resource from an uploaded API description file, using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

Open a command prompt and run`oci api-gateway sdk-language-type`to find out the programming languages and platforms for which you can generate an SDK:

```

```

You see the supported programming languages and platforms, and the required and optional parameters to use with each.
- Run`oci api-gateway sdk create`to generate the SDK:

```

```

where:
- `<language>`is the programming language or platform for which you want to generate an SDK from the uploaded API description file.
- `<api-ocid>`is the OCID of the API resource for which you want to generate the new SDK.
- `--parameters '{"<first-parameter-name>": "<first-parameter-value>", "<second-parameter-name>": "<second-parameter-value>"}'`are the name and value of any required and/or optional parameters to set for the programming language or platform you've chosen.

For example:

- 

```

```

- 
```

```

The response to the command includes:
- The SDK's OCID.
- The lifecycle state (for example, SUCCEEDED, FAILED).
- The id of the work request to create the SDK (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the SDK has been created (or the request has failed), include either or both the following parameters:
- `--wait-for-state SUCCEEDED`
- `--wait-for-state FAILED`

For example:

```

```

Note that you cannot use the SDK until the work request has successfully created it.
- 

(Optional) To see the status of the work request that is creating the SDK, enter:

```

```

- 

(Optional) To view the logs of the work request that is creating the SDK, enter:

```

```

- 

(Optional) If the work request that is creating the SDK fails and you want to review the error logs, enter:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the:
- [CreateSdk](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Sdk/CreateSdk)operation to create an SDK for an API resource from an uploaded API description file.
- [ListSdks](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Sdk/ListSdks)operation to list SDKs that have already been generated.
- [GetSdk](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Sdk/GetSdk)operation to see details of an existing SDK.
- [UpdateSdk](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Sdk/UpdateSdk)operation to change the display name of an existing SDK.
- [DeleteSdk](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Sdk/DeleteSdk)operation to delete an SDK.
- [ListSdkLanguageTypes](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/SdkLanguageTypeSummary/ListSdkLanguageTypes)operation to list the programming languages and platforms for which you can generate an SDK, along with any required and optional parameters.

## Examples of Using Generated SDKs

Having used API Gateway to generate an SDK from an API resource's API description file, you can download and install the SDK, and then use it to call the API deployed on an API gateway.

The steps to download, install, and use a generated SDK depend on the SDK's language and the functionality of the API.

The examples in this section assume an SDK has been generated for a blog API in each of the different languages. Use the examples as guides, which you can extend and adapt to meet your own requirements.

### Example 1: Using an Android SDK Generated for an API Resource

Tools and versions used in this example:
- Gradle 6.5
- Maven 3.6.3
- Android Studio 4.1.2

To use an Android SDK that API Gateway generated from an API resource's API description file:
- Download the zip file containing the Android SDK that API Gateway generated, and extract its contents.
- In the root directory extracted from the zip file, install the generated SDK into the local Maven repository by running:

```

```

- 

Decide which Android project will use the generated Android SDK. Either open an existing Android project that has Gradle as the package manager, or create a new Android project as follows:
- Open Android Studio. Under File , go to New and select New Project .
- Select No Activity , and select Next .
- For Language , select Java and select Finish .
- Update the module's build.gradle file to add the generated SDK as a dependency. For example:

```

```

Note that`test-project`has been added under`dependencies`.
- Run the project build on Android Studio.
- When the build has completed, import the generated SDK classes and use them in one or more of the Android project's Java classes. For example:
```

```

Use the above example as a guide, which you can extend and adapt to meet your own requirements.

### Example 2: Using a Java SDK Generated for an API Resource

Tools and versions used in this example:
- Maven 3.6.3
- Java 1.8.0

To use a Java SDK that API Gateway generated from an API resource's API description file:
- Download the zip file containing the Java SDK that API Gateway generated, and extract its contents.
- In the root directory extracted from the zip file, install the generated SDK into the local Maven repository by running:

```

```

- Decide which Maven project will use the generated Java SDK. Either update an existing Maven project, or create a new Maven project by running:

```

```

- Update the Maven project's pom.xml file to add the generated SDK as a dependency. For example:

```

```

- In the Maven project's root directory, run:
```

```

- When the Maven installation is complete, import the generated SDK classes and use them in the Maven project. For example:

```

```

Use the above example as a guide, which you can extend and adapt to meet your own requirements.

### Example 3: Using a JavaScript SDK Generated for an API Resource

Tools and versions used in this example:
- Npm 6.14.0

To use a JavaScript SDK that API Gateway generated from an API resource's API description file:
- Download the zip file containing the JavaScript SDK that API Gateway generated, and extract its contents.
- In the root directory extracted from the zip file, run:

```

```

```

```

- In the root directory of an existing npm project, run:
```

```
For example:
```

```

- In the .js file from which to call the services, import and use the generated SDK. For example:

```

```

In this example, the name of the generated SDK is`blog`. Look in the extracted package.json file to find the name of the generated SDK.

Use the above example as a guide, which you can extend and adapt to meet your own requirements.

### Example 4: Using a Swift SDK Generated for an API Resource

Tools and versions used in this example:
- XCode 12.4
- Swift 5.3.1
- CocoaPods 1.10.1

To use a Swift SDK that API Gateway generated from an API resource's API description file:
- Download the zip file containing the Swift SDK that API Gateway generated, and extract its contents.
- Decide which XCode project will use the generated Swift SDK. Either update an existing XCode project, or create a new XCode project as follows:
- Open XCode. Under File , go to New and select Project .
- Select App , and select Next .
- For Language , select Swift and select Next .
- Specify a location for the project and select Create to create the XCode project.
- If the root directory of the XCode project does not already contain a Podfile, create a Podfile by running:

```

```

- Update the Podfile to add a reference to the generated SDK. For example:

```

```

- In the XCode project's root directory, run:

```

```

Example output:

```

```

- Close any open instances of XCode.
- In the XCode project's root directory, open the .xcworkspace file to see the pod.
- Update any swift file to import the pod and start using the generated SDK. For example, update the ViewController.swift file to import the mysdk pod as follows:

```

```

Use the above example as a guide, which you can extend and adapt to meet your own requirements.

### Example 5: Using a TypeScript SDK Generated for an API Resource

Tools and versions used in this example:
- yarn 1.22.10
Note  
  
This example shows how to build and consume a generated TypeScript SDK using yarn. If you want to consume a generated TypeScript SDK using NPM, follow the steps to consume a generated JavaScript SDK using NPM that are shown in[Example 3: Using a JavaScript SDK Generated for an API Resource](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaygeneratingsdk.htm#using-generated-javascript-sdk).

To use a TypeScript SDK that API Gateway generated from an API resource's API description file:
- Download the zip file containing the TypeScript SDK that API Gateway generated, and extract its contents.
- In the root directory extracted from the zip file, run:

```

```

```

```

```

```

- In the root directory of the project that you want to use the generated SDK:
- Run:

```

```

where`<project name>`is the name of the generated SDK. Look in the extracted package.json file to find the name of the generated SDK. For example:

```

```

- Run:

```

```

- Update the ts file of the project that you want to use the generated SDK. For example:

```

```
