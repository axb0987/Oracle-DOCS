# Setup OCI Serverless Fn to Connect with REST-based Identity Aware Application
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/setup-oci-serverless-function-to-connect-with-rest-based-identity-aware-syst.htm
- Fetched: 2026-09-05 03:16 CDT

# Setup OCI Serverless Fn to Connect with REST-based Identity Aware Application

## How Does the Generic REST Orchestrated System Use OCI Functions?

Oracle Access Governance leverages OCI Functions for REST API integrations. Each Generic REST Orchestrated System you create is associated with an OCI function which contains the logic to process requests and generate responses. It calls REST APIs of the Managed System for data reconciliation and provisioning operations when triggered by Oracle Access Governance.

For full details of how to use OCI Functions refer to[Oracle Cloud Infrastructure Functions](https://docs.oracle.com/iaas/Content/Functions/home.htm).

## Configuring Your Tenancy to Enable OCI Functions

Before you can use OCI Functions to create and deploy functions, you must create Oracle Cloud Infrastructure resources to support this. Resources you need to create include a user account, a group to which the user account will belong, a compartment, virtual cloud network (VCN), vaults and secrets, and policies to give the group (and the user accounts that belong to it) access to function-related resources. If suitable resources already exist, there is no need to create new ones.

### Create Compartment
If you do not have a suitable compartment in which you can create network resources and OCI Functions resources:
- Sign on to the Oracle Cloud Infrastructure Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security → Identity → Compartments .
- Select Create Compartment and add a compartment, for example ocifn_compartment : For details on creating a compartment see[To create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To)

Note  
  
You create a compartment to own:
- Network resources
- Function-related resources You can create a single compartment to contain both sets of resources, or you can create separate compartments for network resources and function-related resources.

### Create VCN and Subnets
If you do not have a suitable VCN in which to create network resources:
- Sign on to the Oracle Cloud Infrastructure Console as a tenancy administrator.
- Open the navigation menu and select Networking → Virtual cloud networks .
- Select Start VCN Wizard to create a new VCN.
- In the dialog, select Create VCN with Internet Connectivity and click the Start VCN Wizard .
- In the wizard, enter the following details:
- VCN Name : Enter the VCN name, for example ocifn_vcn .
- Compartment : Enter the compartment within which the VCN resources will be created, for example ocifn_compartment .
- Click Next , then click Create to create the VCN and related network resources.

For details of all options when creating the VCN see[Creating the VCN and Subnets to Use with OCI Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionscreatingvcn.htm).

### Create OCI Vault and Secret

If you do not have a suitable vault in which to store client credentials:

- Sign on to the Oracle Cloud Infrastructure Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security → Key Management &amp; Secret Management
- Click Create Vault .
- Select the compartment into which the Vault will be created, and give the Vault a Name. Click Create Vault .
- Open the Vault you created and click Create Key . Create the Key in the same compartment you created your Vault. Give the Key a name and click Create Key .
- From the Resources menu, select Secrets . Click Create Secret .
- On the Create Secret page, add details for compartment, name, and description. Select the key you created from the Encryption Key drop down list. Select the Manual secret generation option, and enter your client code and client secret in one of the following formats into the Secret Contents field.
- OAuth-based Authorization

```

```
For sample code to create authorization token for OAuth-based authorization, see[OAuth Authorization - Sample Token Creation Code](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm#rest-oauthtoken).
- Basic Authorization

```

```
For sample code to create authorization token for Basic authorization, see[Basic Authorization - Sample Token Creation Code](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm#rest-basicauthtoken)
- Select Create Secret to save your changes.

The secret you have created can be used to pass client secrets in your request function. Select the secret you created and copy the value of the secret OCID, which will look something like`ocid1.vaultsecret.oc1.iad.dyyyyehdl4ggaawnqt47hfj48ltofzkdg6wy5fjne859jg0`.
Edit the`<SampleBase>/grc-request-template/src/main/resources/request/applications/<YourApplicationName>/config.yaml`file and add the details of the secret and region, for example:
```

```

For further details on OCI Vault Secrets see[Managing Vault Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm).

### Create or Update your Dynamic Group

In order to use OCI Vault and Secret Services, your function must be part of a dynamic group. For details on how to create your dynamic group, follow the instructions given in[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm).
As part of the creation of your dynamic group you will be required to define a set of matching rules to define the group member. When specifying the matching rule it is recommended that you match all functions in a compartment with the following rule:
```

```

### Create Policy for OCI Vault and Secret

Create a new policy that allows the dynamic group created in above step to read secret-family in your tenancy. For further information on creating OCI policies see[Policy Syntax](https://docs.oracle.com/iaas/Content/Identity/Concepts/policysyntax.htm)

- Sign on to the Oracle Cloud Infrastructure Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security → Identity → Policies .
- Select Create Policy , specify a name for the policy, for example ocifn_policy , and select the tenancy's root compartment.
- Add a policy statement similar to:
```

```

### Create Policy for Group and Service
If one or more OCI Functions users, for example ocifn_user is not a tenancy administrator:
- Sign on to the Oracle Cloud Infrastructure Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security → Identity → Policies .
- Select Create Policy , specify a name for the policy, for example ocifn_policy , and select the tenancy's root compartment.
- Using Policy Builder, select Functions from the Policy use cases list, and base your policy on the Let users create, deploy, and manage functions and applications template.
- Select the group created earlier, ocifn_group and the ocifn_compartment for the location. This should give you a policy statement similar to:
```

```

For more details on creating policies for OCI Functions see[Creating Policies to Control Access to Network and Function-Related Resources](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm)

## Create an Application to Group Your OCI Functions

In OCI Functions, an application is a logical grouping of functions. The properties you specify for an application determine resource allocation and configuration for all functions in that application. You have to create a function within an application, so at least one application must exist before you can create a function in OCI Functions.
To create an application:
- Sign on to the Oracle Cloud Infrastructure Console as a functions developer.
- Open the navigation menu and select Developer Services → Functions → Applications .
- Select the compartment you are using for Generic REST orchestrated system functions.
- Click Create application .
- Add a name for the application, for example agcs-generic-rest-connector . You will deploy your functions into this application, and specify this application when invoking the function.
- Select the VCN and subnet in which to run the function.
- Click Create .

For full details on creating applications with OCI Functions see[Creating Applications](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionscreatingapps.htm).

## Setup Environment for Developing OCI Functions

In order to create and deploy your OCI Functions you need to install and setup a development environment.
Before you can create OCI functions for the Generic REST Orchestrated System. you need to install and configure a development environment, if you do not already have one available. Setup of a development environment can be done in a number of ways, and includes some or all of the following steps:
- Install and start Docker
- Setup API signing key and OCI profile
- Install Fn Project command line interface (CLI)
- Setup Fn Project CLI context provider
- Complete Fn Project CLI context configuration
- Generate auth token
- Log into registry
Full details of how to setup your development environment in different in different contexts can be found in the Oracle Cloud Infrastructure documentation as follows:
- [Cloud Shell](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm)
- [Local Host](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm)
- [OCI Compute Instance](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartocicomputeinstance.htm)

Once your development environment is setup, you can start to develop and deploy functions for the Generic REST Orchestrated System.

## Develop and Deploy Function to OCI

In order to deploy the Generic REST Orchestrated System you need to develop and deploy an OCI function which enables you to connect to the identity-aware system that you want to integrate with Oracle Access Governance using REST.

To develop and deploy OCI Functions for use with the Generic REST Orchestrated System:

### Setup Sample Implementation

To help with development of your OCI Functions a sample implementation is provided with the Generic REST Orchestrated System. To download this example you should follow the instructions given in the[Select System](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-generic-rest.htm#rest-configure)procedure.
The sample implementation downloaded, idm-agcs-generic-rest-reference-implementation.zip , comprises four use cases. When unzipping the file, you will see the following four directories from which you can choose a sample that meets your requirements.
Note  
  
In the details that follow, the directory to which you have unzipped the sample implementation is referred to as`<SampleBase>`. Use this to locate the files mentioned. For example:

If you unzip the sample implementation to a directory, say,`/myagfunctions`then the file`<SampleBase>/grc-schema-template/src/main/resources/schema/config.yaml`can be found at`/myagfunctions/grc-schema-template/src/main/resources/schema/config.yaml`.
- idm-agcs-serverless-getting-started-sample : This is a basic and easy-to-understand sample with minimal code, demonstrating how functions work. This use case is ideal for customers needing to integrate a single application with the Generic REST connector, requiring minimal configuration. Initial set up is with an Oracle Identity Cloud Service (IDCS) application. Detailed steps to configure and deploy this function can be found in the `README.md` file within this directory.
- idm-agcs-serverless-idcs-application-sample : This sample focuses on the IDCS application example with minimal configuration. It includes the framework to add more applications in the future within this function. Configuration and deployment steps are detailed in the `README.md` file located in this directory.
- idm-agcs-serverless-azuread-application-sample : This sample is specifically for customers who need an AzureAD application example with minimal configuration. It contains the framework to add more applications in the future within this function. Detailed steps to configure and deploy this function are available in the `README.md` file inside this directory.
- idm-agcs-serverless-multi-application-sample : This sample is for customers needing both IDCS and AzureAD application examples with minimal configuration. It includes the framework to add more applications in the future within this function. The `README.md` file in this directory provides all necessary steps to configure and deploy this function.

### Create Functions for Your Application

Create the functions for your own REST-based identity-aware system, by referring to the reference templates, and configuring the functions as defined below, with values specific to your application.

GRC-SCHEMA-TEMPLATE
Item Description
Input Orchestrated System name
Configuration

List of configured custom REST identity aware systems:`<SampleBase>/grc-schema-template/src/main/resources/schema/config.yaml`
For example, from the sample implementation:
```

```

List of Orchestrated Systems linked to custom REST identity aware system:`<SampleBase>/grc-schema-template/src/main/resources/schema/applications/<YourApplicationName>/config.yaml`
For example, from the sample implementation:
```

```

Output
JSON Schema template document, with one or more entity schemas, including any of the following entity types:
- ACCOUNT
- ENTITLEMENT
- LOOKUP
- TARGETACCOUNT

`<SampleBase>/grc-schema-template/src/main/resources/schema/applications/<YourApplicationName>/TEMPLATE.json`

For an example from the sample implementation see[Schema Output](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm#rest-schema-output).

GRC-REQUEST-TEMPLATE
Item Description
Input
- Orchestrated System name
- Operation name
- Entity name
Configuration

List of configured custom REST identity aware systems:`<SampleBase>/grc-request-template/src/main/resources/request/config.yaml`
For example, from the sample implementation:
```

```

List of Orchestrated Systems linked to custom REST identity aware system:`<SampleBase>/grc-request-template/src/main/resources/request/applications/<YourApplicationName>/config.yaml`
For example, from the sample implementation:
```

```

Output

JSON Request template document, for defined entities and operations:
Entities
- ACCOUNT
- ENTITLEMENT
- LOOKUP
- TARGETACCOUNT
Operations
- CREATE
- GET
- SEARCH
- DELETE
- UPDATE
- ADD_CHILD_DATA
- REMOVE_CHILD_DATA
- ENABLE
- DISABLE

`<SampleBase>/grc-schema-template/src/main/resources/request/applications/<YourApplicationName>/<EntityName>/<Operation>_TEMPLATE.json`

For an example from the sample implementation see[Request Output](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm#rest-request-output).

GRC-RESPONSE-TEMPLATE
Item Description
Input
- Orchestrated System name
- Operation name
- Entity name
Configuration

List of configured custom REST identity aware systems:`<SampleBase>/grc-response-template/src/main/resources/response/config.yaml`
For example, from the sample implementation:
```

```

List of Orchestrated Systems linked to custom REST identity aware system:`<SampleBase>/grc-response-template/src/main/resources/response/applications/<YourApplicationName>/config.yaml`
For example, from the sample implementation:
```

```

Output

JSON Response template document, for defined entities and operations:
Entities
- ACCOUNT
- ENTITLEMENT
- LOOKUP
- TARGETACCOUNT
Operations
- CREATE
- GET
- SEARCH
- DELETE
- UPDATE
- ADD_CHILD_DATA
- REMOVE_CHILD_DATA
- ENABLE
- DISABLE

`<SampleBase>/grc-response-template/src/main/resources/response/applications/<YourApplicationName>/<EntityName>/<Operation>_TEMPLATE.json`

For an example from the sample implementation see[Response Output](https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference.htm#rest-response-output).

GRC-TEST-TEMPLATE
Item Description
Input Orchestrated System name
Configuration

List of configured custom REST identity aware systems:`<SampleBase>/grc-test-template/src/main/resources/test/config.yaml`
For example, from the sample implementation:
```

```

List of Orchestrated Systems linked to custom REST identity aware application:`<SampleBase>/grc-test-template/src/main/resources/test/applications/<YourApplicationName>/config.yaml`
For example, from the sample implementation:
```

```

Output

JSON Test Request template document:`<SampleBase>/grc-test-template/src/main/resources/test/applications/<YourApplicationName>/TEMPLATE.json`
For example, from the sample implementation:
```

```

### Test Infra Module Guide

Request and Response templates are complex and errors can occur during development. It is crucial to identify and validate all configured Request and Response templates for correctness during the build time itself.

To address this challenge, the grc-test-infra module has been introduced. This module includes tests corresponding to each configured Request and Response template. These tests aim to verify the requests made to the target application's REST API and the responses received. To achieve this, the tests utilize a utility, such as a generic Request and Response processor, capable of handling any REST API call developed within the module. Essentially, it internally interacts with the target application's endpoints and validates the responses based on the configured response templates.
To effectively identify and validate all configured GRC Request and Response templates for correctness during the build time, follow these steps:
- Develop tests following the example outlined below:
grc-test-infra sample test
```

```

- The first line inside the test is to get the configured Request template by passing the connectedSystem Name, entity name, and operation.
- The second line gets the configured Response template using similar parameters.
- Users need to pass the required attributes in the request template by putting them in the attribute map.
- Then, users just need to call the generic utility method processAndValidateRequestAndResponseTemplate, which internally validates both the request and response templates for correctness by invoking the API and mapping its response with the configured response template.
- The test will pass if the configured request and response templates are correctly configured; otherwise, it will fail, allowing users to see the failure reason and correct the templates accordingly.

The example test file can be found in the sample implementation at the following location:`<SampleBase>/grc-test-infra/src/test/java/com/oracle/idm/agcs/grc/fn/test/infra/RequestResponseTemplateValidationTest.java`
- Add the following prerequisites before running the test:
- Update the`<SampleBase>/grc-test-infra/src/test/resources/config`file with the following values for your environment:
```

```

- Update the`<SampleBase>/grc-test-infra/src/test/resources/config.properties`file with the following value for your environment:
```

```

- Add the private SSH key (.pem file) for the API Signing Key to the following location:
```

```

- Execute the developed test and build the function:
- Navigate to the`functions`directory of the sample implementation.
- Compile and package the functions
```

```

### Build and Deploy Your Function
- Build your function.
```

```

- Deploy your function on OCI. The steps should be carried out for each function
- grc-schema-template
- grc-request-template
- grc-response-template
- grc-test-template
```

```
