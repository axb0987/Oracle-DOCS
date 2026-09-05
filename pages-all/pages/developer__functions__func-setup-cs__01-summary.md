# Functions: Get Started using Cloud Shell
- Source: https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm
- Fetched: 2026-09-05 03:31 CDT

# Functions: Get Started using Cloud Shell

In this tutorial, you use an Oracle Cloud Infrastructure account to set up Oracle Functions development using Cloud Shell. Then, you create a function application and a function.

Key tasks include how to:
- Set up an authentication token.
- Gather required information.
- Set up a VCN.
- Log in to OCI Registry (OCIR).
- Configure Cloud Shell to deploy functions.
- Configure your Fn context.
- Create an app for your Oracle function.
- Create a function.
- Deploy your function.
- Test your function.

For additional information, see:
- [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)
- [Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm)
- [Oracle Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)
- [OCI Container Registry](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryoverview.htm)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[Requirements](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

- A paid Oracle Cloud Infrastructure account. See[Signing Up for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- Your OCI account configured to support Oracle Functions development. See[Oracle Functions on Cloud Shell Quickstart](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm).
- OCI Cloud Shell which is included with your account and includes:
- OCI CLI
- Docker
- Python 3.6+
- Java 1.8+
- Node.js 10+

## 1. Gather Required Information

Collect all the information needed to complete the tutorial.

[Gather Region and Registry Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

Prepare the information you need from the OCI Console .
- Find your region identifier and region key from[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

Example:`us-ashburn-1`and`iad`for Ashburn.
- Create a registry project name to store your function images in OCI Registry (OCIR).

When you publish a function, a Docker image is created in OCIR. Your OCIR project name is prepended to your function images to make them easy to find. For example, given:
- Registry project name:`my-func-prj`
- Function name:`node-func`

Your function image would be stored on OCIR under:`my-func-prj/node-func`

[Create or Select a Compartment](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

To create a compartment see[Create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To). After your compartment is created, save the compartment OCID.

To get the compartment OCID from an existing compartment:

- Open the navigation menu and click Identity &amp; Security . Under Identity , click Compartments .
- Select your compartment.
- Click the Copy link for the OCID field.

[Create an Authorization Token](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

You create an authorization token to log in to the OCI Registry. To create an authorization token:

- In the navigation menu , select the Profile menu and then select User settings .
- Click Auth Tokens .
- Click Generate Token .
- Give it a description.
- Click Generate Token .
- Copy the token and save it.

Note  
  
Ensure that you save your token right after you create it. You do not have access to it later.

[Collect your Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

Collect all the information needed to complete the tutorial. Copy the following information into your notepad.

- Region:`<region-identifier>`

Example:`us-ashburn-1`.
- Region Key:`<region-key>`

Example:`iad`.
- Registry Project Name:`<your-project-name>`

Example:`my-func-prj`.
- Compartment ID:`<compartment-id>`

Example:`ocid1.compartment.oc1.aaaaaaa...`
- Auth Token:`<auth-token>`

Example:`ABC.1aBC...`
- Tenancy name:`<tenancy-name>`

From your user avatar, example:`mytenancyname`
- Tenancy OCID:`<tenancy-ocid>`

From your user avatar, go to Tenancy: &lt;your-tenancy&gt; and copy OCID, example:`ocid1.tenancy.oc1.aaaaaaa...`
- Username:`<user-name>`

From your user avatar.

## 2. Create your Virtual Cloud Network (VCN)

Set up a VCN to connect your Linux instance to the internet.

[Configure your VCN](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

To configure virtual cloud network, perform the following steps.

- Click the Oracle Cloud icon to go to the main landing page.

- Scroll down to Launch Resources .
- Select Set up a network with a wizard .
- In the Start VCN Wizard workflow, select Create VCN with Internet Connectivity and then click Start VCN Wizard .
- In the configuration dialog, fill in the VCN Name for your VCN. Your Compartment is already set to the last compartment you were working in, or if it's your first time, to its default value of`<your-tenancy> (root)`.
- In the Configure VCN and Subnets section, keep the default values for the CIDR blocks:

- VCN CIDR BLOCK: 10.0.0.0/16
- PUBLIC SUBNET CIDR BLOCK: 10.0.0.0/24
- PRIVATE SUBNET CIDR BLOCK: 10.0.1.0/24
Note  
  
Notice the public and private subnets have different network addresses.
- For DNS Resolution, uncheck Use DNS hostnames in this VCN.
- Click Next .

The Create a VCN with Internet Connectivity configuration dialog is displayed (not shown here) confirming all the values you just entered.
- Click Create to create your VCN.

The Creating Resources dialog is displayed (not shown here) showing all VCN components being created.
- Click View Virtual Cloud Network to view your new VCN.

Your new VCN is displayed. Now you need to add a security rule to allow HTTP connections on port 80, the default port for your applications.
- With your new VCN displayed, click your Public subnet link.

The public subnet information is displayed with the Security Lists at the bottom of the page. There should be a link to the Default Security List for your VCN.
- Click the Default Security List link.

The default Ingress Rules for your VCN are displayed.
- Click Add Ingress Rules .

An Add Ingress Rules dialog is displayed.
- Fill in the ingress rule with the following information. Once all the data is entered, click Add Ingress Rules .

Fill in the ingress rule as follows:
- Stateless: Checked
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: (leave-blank)
- Destination Port Range: 80
- Description: VCN for applications

Once you click Add Ingress Rules , HTTP connections are allowed to your public subnet .

Note  
  
To open a different port, replace 80 in the last step with the port number. You have successfully created a VCN that makes your applications available from the internet.

## 3. Log into the OCI Registry

Next, you log Docker into the OCI Registry (OCIR).

[Log Docker into OCIR](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

- Get the information you gathered earlier.
- Open a terminal window.
- Log in to OCIR:

```

```

You are prompted for your login name and password.
- Username:`<tenancy-name>/<user-name>`
- Password:`<auth-token>`

You have logged your instance into OCIR.

## 4. Configure Functions

To use Oracle Functions, you must configure the Fn application context. The context stores the values needed to connect to the Oracle Functions service. Fn client commands are used to add the required configuration data.

[Configure the Fn Context for the Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

You need the information you gathered from earlier on. Use Fn client commands to configure Fn.

- Open your Cloud Shell instance.
- Get a list of Fn contexts.

`fn list context`

You see contexts for`default`and`<your-region-identifier>`.
- Select the context named with`<your-region-identifier>`.

For example:`fn use context us-phoenix-1`
- List the Fn contexts to ensure`<your-region-identifier>`is selected. (Has a star next to it.)
- Set the compartment for Oracle Functions.

Example:`fn update context oracle.compartment-id ocid1.compartment.oc1..aaaaaaaarvdfa72n...`
- Set the URL for your Registry repository.

Sample command:`fn update context registry <region-key>.ocir.io/<tenancy-namespace>/<registry-project-name>`

Example:`fn update context registry phx.ocir.io/my-tenancy/my-func-prj`

Note  
  

View/Edit your Context

Your Fn context files are in the`~/.fn/contexts`directory. Each context is stored in a`.yaml`file. For example, your`us-phoenix-1.yaml`file might look similar to:
```

```

You can edit the file directly with an editor if necessary.

For a detailed explanation of each step, see:[Oracle Functions on Cloud Shell Quickstart](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm)

You have now setup the Fn context for your instance.

## 5. Create and Deploy a Function

With your configuration complete, create and deploy a function.

[Create an Application](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

An Application is the main storage container for functions. Each function must have an application for deployment. To create application, follow these steps.
- Open the navigation menu and click Developer Services . Under Functions , click Applications .
- Click Create Application .

Fill in the form data.
- Name: &lt;your-app-name&gt;
- VCN: &lt;your-VCN&gt;
- Subnets: &lt;your-public-subnet&gt; or &lt;your-private-subnet&gt;
Note  
  
A public or private subnet can be used, select one.
- Click Create .

Your app is created.

### Choose a Language

Select one of the following languages to create and deploy a function. If you want, you can do all three.

[Create and Deploy a Java Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

With your application created, deploy a Java function. Follow these steps to create a Java "Hello World" function.
Note  
  
Ensure Java 8+ is installed to perform these steps.

- Open Cloud Shell.
- Create a directory to store your functions and change into that directory.

```

```

- Create a Java "Hello World" function with Fn.

```

```

This command creates a directory named`my-func-name`with several files in it.
- `func.yaml`- Function configuration file.
- `pom.xml`- Maven build file.
- `src/main/java/com/example/fn/HelloFunction.java`- The actual function file.
- Change into the directory.
- Deploy the function.

```

```

Various messages are displayed as the docker images are built, pushed to OCIR, and eventually deployed to Oracle Functions.
- Invoke the function.

```

```

Returns:`Hello, world!`
- Invoke the function with a parameter.

```

```

Returns:`Hello, Bob!`
- If you want to connect to your function from the net, you need to get the function's invoke endpoint. To find your invoke endpoint use the`inspect`command.

```

```

- Examine the results of the`inspect`command. Notice the invoke endpoint URL is included in the`annotations`section of the returned JSON data.

```

```

- Use the URL returned from`inspect`to invoke the function. Because functions require requests to be digitally signed, the`oci raw-request`command is used for this example.

```

```

The command returns:
```

```

Note  
  
You can connect to a Functions endpoint using tools like`curl`. However, because of security considerations, the script is complex. As an alternative, use the OCI CLI`raw-request`command. See[Invoking Functions: Sending a Signed Request to a Function with raw-request](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#rawrequestinvoke).

You have successfully deployed and tested a Java function.

[Create and Deploy a Python Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

With your application created, deploy a Python function. Follow these steps to create a Python "Hello World" function.

- Open Cloud Shell.
- Create a directory to store your functions and change into that directory.

```

```

- Create a Python "Hello World" function with Fn.

```

```

This command creates a directory named`my-func-name`with several files in it.
- `func.yaml`- Function configuration file.
- `requirements.txt`- List of required Python libraries.
- `func.py`- The actual function file.
- Change into the directory.
- Deploy the function.

```

```

Various messages are displayed as the docker images are built, pushed to OCIR, and eventually deployed to Oracle Functions.
- Invoke the function.

```

```

Returns:`{"message": "Hello World"}`
- Invoke the function with a parameter.

```

```

Returns:`{"message": "Hello Bob"}`
- If you want to connect to your function from the net, you need to get the function's invoke endpoint. To find your invoke endpoint use the`inspect`command.

```

```

- Examine the results of the`inspect`command. Notice the invoke endpoint URL is included in the`annotations`section of the returned JSON data.

```

```

- Use the URL returned from`inspect`to invoke the function. Because functions require requests to be digitally signed, the`oci raw-request`command is used for this example.

```

```

The command returns:
```

```

Note  
  
You can connect to a Functions endpoint using tools like`curl`. However, because of security considerations, the script is complex. As an alternative, use the OCI CLI`raw-request`command. See[Invoking Functions: Sending a Signed Request to a Function with raw-request](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#rawrequestinvoke).

You have successfully deployed and tested a Python function.

[Create and Deploy a Node Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

With your application created, deploy a Node function. Follow these steps to create a Node "Hello World" function.
Note  
  
Ensure Node.js 10+ is installed to perform these steps.

- Open Cloud Shell.
- Create a directory to store your functions and change into that directory.

```

```

- Create a Node "Hello World" function with Fn.

```

```

This command creates a directory named`my-func-name`with several files in it.
- `func.yaml`- Function configuration file.
- `package.json`- NPM build file.
- `func.js`- The actual function file.
- Change into the directory.
- Deploy the function.

```

```

Various messages are displayed as the docker images are built, pushed to OCIR, and eventually deployed to Oracle Functions.
- Invoke the function.

```

```

Returns:`{"message":"Hello World"}`
- Invoke the function with a parameter.

```

```

Returns:`{"message":"Hello Bob"}`
- If you want to connect to your function from the net, you need to get the function's invoke endpoint. To find your invoke endpoint use the`inspect`command.

```

```

- Examine the results of the`inspect`command. Notice the invoke endpoint URL is included in the`annotations`section of the returned JSON data.

```

```

- Use the URL returned from`inspect`to invoke the function. Because functions require requests to be digitally signed, the`oci raw-request`command is used for this example.

```

```

The command returns:
```

```

Note  
  
You can connect to a Functions endpoint using tools like`curl`. However, because of security considerations, the script is complex. As an alternative, use the OCI CLI`raw-request`command. See[Invoking Functions: Sending a Signed Request to a Function with raw-request](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#rawrequestinvoke).

You have successfully deployed and tested a Node function.

## 6. Review Function Information

After your functions run, information about your functions is available in the OCI Console.

[View Function Images in OCIR](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

When you deploy, the function is uploaded and stored in OCIR. You can navigate to OCIR and examine the function images.
- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Container Registry .
- Search for the`<your-repository-project-name>`.
- Under your project name, you see an entry for each function you deployed.
- Click the link of each image you want to see information about.

[View Function Execution Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

After you run a function, you can display metrics for that function.
- Open the navigation menu and click Developer Services . Under Functions , click Applications . Your applications are listed on the page.
- Click the link to the application you created.
- Click the link to the function you want to examine.

Metric information about your function is displayed.

[Enable and View Logging Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cs/01-summary.htm#)

To enable logging for an application, follow these steps.
- Open the navigation menu and click Developer Services . Under Functions , click Applications . Your applications are listed on the page.
- Click the link to the application you created.
- On the left side of the application page, click the Logs link.
- Click Disabled to enable logging for your application.
- The Enable Log dialog is displayed. Fill in the following information:
- Compartment: &lt;your-compartment-name&gt;
- Log Group: Take the default value`Auto-Create a Default Log Group`
- Log name:`<take-default>`
- Log Retention:`<take-default>`
- Click Enable Log

Wait a moment for your log to be created.

To view your log, click the log name link created by the preceding steps.

## What's Next

You have successfully created a function and deployed it to Oracle Functions.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
- [Oracle Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)
