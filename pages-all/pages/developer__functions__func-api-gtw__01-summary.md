# Functions: Call a Function using API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm
- Fetched: 2026-09-05 03:31 CDT

# Functions: Call a Function using API Gateway

In this tutorial, you use Oracle Functions to process data passed from Oracle API Gateway. You create a Python function that uses the runtime context to extract HTTP information passed in a request.

Key tasks include how to:
- Gather required information.
- Create an application for your function.
- Create a "Hello World!" function.
- Convert your function to process runtime context data.
- Deploy and test your function.
- Create an API Gateway for your function
- Call your function from the internet using your API Gateway.

For additional information, see:
- [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)
- [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm)
- [Oracle Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)
- [Oracle API Gateway](https://docs.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayoverview.htm)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[OCI Account Requirements](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

- A paid Oracle Cloud Infrastructure account. See[Signing Up for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- Your OCI account configured to support Oracle Functions development. See[Oracle Functions on Cloud Shell Quickstart](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm).
- Completion of one of the two Oracle Functions introduction tutorials.
- [Functions: Get Started using Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/../func-setup-cs/01-summary.htm)
- [Functions: Get Started using the CLI](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/../func-setup-cli/01-summary.htm)
- Completing one of the two tutorials results in:
- Oracle Functions is set up and configured to create applications and deploy functions.
- Oracle Registry is set up to store function images.
- Docker is logged into the Oracle Registry.
- The required VCN and required resources needed for Oracle Functions.
- An API key pair and an auth token.

[Software Requirements](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

Oracle CLI
- Python 3.6+ and pip3.
- Docker Engine: A Linux computer or Linux VM. See[Docker engine requirements](https://docs.docker.com/engine/install/)for versions, and distros supported.
- Docker Desktop: Available for MacOS or Windows 10.
- Windows 10: Windows 10 update 2004 with WSL 2 and Ubuntu or other distro installed.
- See[Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
- [Install Docker Desktop for Windows 10.](https://docs.docker.com/docker-for-windows/install/)
Note  
  
Docker includes special Linux support for WSL 2 on Windows 10 update 2004.
- MacOS: See[Install Docker Desktop for MacOS.](https://docs.docker.com/docker-for-mac/install/)

Oracle Cloud Shell
- If you use Cloud Shell, the preceding list of software is already installed.

## 1. Gather Required Information

Collect all the information you need to complete the tutorial. Copy the following information into your notepad.

[Get Compartment Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

To create a compartment see[Create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To). After your compartment is created, save the compartment OCID and name.

To get the compartment OCID from an existing compartment:
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Compartments .
- Select your compartment.
- Click the Copy link for the OCID field.

Save the compartment OCID and name.

[Collected Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

Ensure you have the following information written down for the tutorial.
- Compartment Name:`<your-compartment-name>`

Example:`my-compartment`
- Compartment ID:`<your-compartment-OCID>`

Example:`ocid1.compartment.oc1.aaaaaaa...`
- VCN Name:`<your-vcn-name>`

Example:`my-vcn`

Open the navigation menu and click Networking , and then click Virtual Cloud Networks . From the list of networks, select your VCN.
- VCN Public Subnet Name:`<Public-Subnet-your-vcn-name>`

Example:`Public-Subnet-my-vcn`

Open the navigation menu and click Networking , and then click Virtual Cloud Networks . From the list of networks, select your VCN.

## 2. Perform Required Configuration

Perform all the configuration you need for the tutorial.

[Create Functions Application](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

To create application, follow these steps.
- Open the navigation menu and click Developer Services . Under Functions , click Applications .
- Select your compartment from the Compartment drop-down.
- Click Create Application .
- Fill in the form data.
- Name:`<your-app-name>`
- VCN:`<your-vcn-name>`
- Subnets:`<Public-Subnet-your-vcn-name>`
- Click Create .

Your app is created.

[Setup Ingress Rule for HTTPS](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

- Open the navigation menu and click Networking , and then click Virtual Cloud Networks .
- Click the name of the VCN you used to for your Oracle Functions application.
- With your new VCN displayed, click your Public subnet link.

The public subnet information is displayed with the Security Lists at the bottom of the page.
- Click the Default Security List link or appropriate security list link.

The default Ingress Rules for your VCN are displayed.
- Click Add Ingress Rules .

An Add Ingress Rules dialog is displayed.
- Fill in the ingress rule with the following information. After all the data is entered, click Add Ingress Rules

Fill in the ingress rule as follows:
- Stateless: Checked
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source port range: (leave-blank)
- Destination Port Range: 443
- Description: VCN for applications

After you click Add Ingress Rule , HTTPS connections are allowed to your public subnet .

[Setup Policy for API Gateway Access to Functions](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

Next, setup a policy which allows API Gateway to invoke functions.

First, create a Dynamic Group for API Gateway.
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Dynamic Groups .
- Click Create Dynamic Group .
- Fill in the following information to define your dynamic group.
- Name:`<name-for-your-dynamic-group>`
- Under Matching Rules use Rule 1:`<the-rule-text>`

Here is sample name and the rule you need to fill out. Replace`<your-compartment-OCID>`with its value.
- Name: api-gtw-func-dynamic-group
- Under Matching Rules use Rule 1:`ALL {resource.type = 'ApiGateway', resource.compartment.id = '<your-compartment-OCID>'}`
- Click Create .

Now create the policy for API Gateway.
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Policies .
- Click Create Policy .
- To define your policy, fill in the following information.
- Name:`<name-for-your-policy>`
- Description:`<description-for policy>`
- Compartment:`<name-of-functions-compartment>`

For the Policy Builder section:
- Click Show manual editor .
- Enter your policy in the text box, for example:

```

```

Note  
  
The last parameter is the compartment name , not the compartment OCID.
- Click Create .

You have created a policy to allow API Gateway to use Functions.

[Create "Hello World" Python Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

- Open a terminal.
- Create a directory to store your functions and change into that directory.

```

```

- Create a Python "Hello World" function with Fn.

```

```

This command creates a directory named`my-func-name`with the function and configuration files in it.
- Change into the directory.
- Deploy the function.

```

```

Various messages are displayed as the Docker images are built, pushed to OCIR, and eventually deployed to Oracle Functions.
- Invoke the function.

```

```

Returns:`{"message": "Hello World"}`
- Invoke the function with a parameter.

```

```

Returns:`{"message": "Hello Bob"}`

## 3. Create an API Gateway

To call your function, create an API Gateway.

[Create the API Gateway](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

To create an API Gateway:
- Open the navigation menu and click Developer Services . Under API Management , click Gateways .
- Select your compartment from the Compartment drop-down.
- Click Create Gateway
- Fill in the following information to define your API Gateway.
- Name:`<your-gateway-name>`
- Type:`<Public>`
- Compartment:`<your-compartment-name>`
- Virtual Cloud Network in &lt;your-vcn-name&gt;:`<select-your-vcn>`
- Subnet in &lt;your-compartment-name:`<your-public-subnet-name>`
- Click Create . Wait a few minutes for your API Gateway to e created.

[Create an API Deployment for your Gateway](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

Next, create a deployment for your API Gateway.
- Click Deployments in Resources section on the left side of the screen.
- Click Create Deployment .
- Ensure that From Scratch is selected for the deployment type.
- To define your deployment, fill in the Basic Information section.
- Name:`<your-deployment-name>`
- Path Prefix (example):`/v1`
- Compartment:`<your-compartment-name>`
- API Request Policies: Take default values
- API Logging Policies: Take default value of Information
- Click Next . The Routes dialog appears with Route 1 selected.
- To define your route, fill in the Route 1 section.
- Path:`<your-route-path>`

Example:`/http-info`
- Methods:`GET POST`
- Type: Oracle Functions
- Application in`<your-compartment-name>`: Select the Functions application you created.
- Function Name: Select the function you created in the configuration section.
- Click Next . The Review dialog is displayed summarizing the choices you have made.
- Click Create . Your deployment is created.
- Click the Deployments link for your gateway. Copy the base end point for the deployment you created.

For example:`https://aaaaa.apigateway.us-ashburn-X.oci.customer-oic.com/v1`

[Test your API Gateway](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

With your API Gateway and deployment created, you can now test you installation. Create a simple script for the`curl`command. To create the URL for`curl`, add your deployment path to your endpoint.
- Create the script file:`touch gtw01.sh && chmod 755 gtw01.sh`
- Add the command curl command to the script file:

```

```

- The command returns:`{"message":"Hello World"}`

You have connected your API Gateway to a boiler plate Python function. Next, you update your Python function to display information passed in an HTTP request.

## 4. Update Function to Access HTTP and Function Data

Next, modify the boiler plate Python function to access the runtime context and display HTTP information.

[Review Starting Python Code](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

If you look at the boiler plate function, your Python function looks something like this.

```

```

Using this code as a starting point, the sections that follow convert the function into a Python function that returns HTTP and configuration data.

[Update Required Packages](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

First, update the function for required packages.
- Update the`requirements.txt`file for the`oci`package.

```

```

- Update the`import`statements in`func.py`for required packages for the HTTP features:

```

```

The`oci`package is required for some of the context requests. The`urlparse, parse_qs`packages are used for parsing.

[Add HTTP Request Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

First, remove the main body of the function. The`response`method and related code are added back as we go.

```

```

Next add code to display HTTP information in the response. Here is the code with comments following.

```

```

- The`handler`function receives system information about the current request through the`ctx`and`data`parameters.
- All the data is added to the`resp`dictionary which is eventually returned in the response.
- Notice the function runtime context (`ctx`) contains much of the HTTP data passed from a request including: headers, request URL, and method.
- The`data`parameter returns the body of the request.

[Add the Function-related Data to the Response](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

Next, retrieve Oracle Functions related data from the context and then return a response. Comments follow.

```

```

Notice all the Functions-related data is retrieved from the`ctx`object including:`AppID`,`FnID`, and`Format`.

[Review Final Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

Here is the final function code.

```

```

You are now ready to retest you function and see the results.

[Create Functions Configuration Variables](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

Oracle Functions allows you to store configuration data in your context that is available in your request. Configuration data can be stored in an application or a function. The following commands store database information in the application context.
- `fn config app <your-app-name> DB-NAME your-db-name`
- `fn config app <your-app-name> DB-USER your-user-name`

For more information, see[Fn Project's tutorial on runtime context](https://fnproject.io/tutorials/basics/UsingRuntimeContext/).

[Test your Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm#)

- Redeploy the updated function.
- Invoke the function to ensure that the function is working.
- Run your script again. To get formatted JSON output, use the`jq`utility which is included with the cloud shell. If you are using the CLI, install`jq`on your local machine.

```

```

The data returned is similar to:

```

```

Notice all the Functions data returned in the second half of the response including:`AppID`,`FnID`, and`Format`. In addition, in the`Configuration`section you see the Functions-generated environment variables like`FN_FORMAT`and the configuration variables:`DB-NAME`and`DB-USER`.
- Update your script to pass headers and`POST`data to the script.

```

```

The output from the script looks similar to:

```

```

Note the header data and the request body data. The key/value JSON data is listed under the "Request Body" section. You can download the complete source code for the function from the[Oracle Function Samples site here](https://github.com/oracle/oracle-functions-samples/tree/master/samples/oci-apigw-display-httprequest-info-python).

Congratulations, you have converted the boiler plate Python function into a new function that returns HTTP and Oracle Function data. The function demonstrates how data can be passed to API Gateway and processed in a function.

## What's Next

You have successfully created an API Gateway and called a function from it. You updated the function to display HTTP and Oracle Function data.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
- [Oracle Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)
- [Oracle API Gateway](https://docs.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayoverview.htm)
