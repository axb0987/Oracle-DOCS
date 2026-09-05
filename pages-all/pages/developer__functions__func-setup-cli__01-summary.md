# Functions: Get Started using the CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm
- Fetched: 2026-09-05 03:31 CDT

# Functions: Get Started using the CLI

In this tutorial, you use an Oracle Cloud Infrastructure account to set up Oracle Functions development. Then, you create a function application and a function.

Key tasks include how to:
- Set up an authentication token.
- Gather required information.
- Set up a VCN.
- Set up the OCI Registry (OCIR).
- Set up the CLI to deploy functions
- Configure your Fn context.
- Create an app for your Oracle function.
- Create a function.
- Deploy your function.
- Test your function.

For additional information, see:
- [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)
- [Launching Your First Linux Instance](https://docs.oracle.com/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
- [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm)
- [Oracle Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)
- [OCI Container Registry](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryoverview.htm)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[OCI Account Requirements](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

- A paid Oracle Cloud Infrastructure account. See[Signing Up for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- Your OCI account configured to support Oracle Functions development. See[Set up your tenancy](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#functionsquickstart_cloudshell_topic_setup_your_tenancy).

[Software Requirements](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

- Python 3.6+ and pip3.
- Docker Engine: A Linux computer or Linux VM. See[Docker engine requirements](https://docs.docker.com/engine/install/)for versions, and distros supported.
- Docker Desktop: Available for MacOS or Windows 10.
- Windows 10: Windows 10 update 2004 with WSL 2 and Ubuntu or other distro installed.
- See[Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
- [Install Docker Desktop for Windows 10.](https://docs.docker.com/docker-for-windows/install/)
Note  
  
Docker includes special Linux support for WSL 2 on Windows 10 update 2004.
- MacOS: See[Install Docker Desktop for MacOS.](https://docs.docker.com/docker-for-mac/install/)

## 1. Gather Required Information

Collect all the information you need to complete the tutorial.

[Gather Region and Registry Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

Prepare the information you need from the OCI Console.
- Find your region identifier and region key from[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

Example:`us-ashburn-1`and`iad`for Ashburn.
- Create a registry project name to store your function images in OCI Registry (OCIR).

When you publish a function, a Docker image is created in OCIR. Your OCIR project name is prepended to your function images to make them easy to find. For example, given:
- Registry project name:`my-func-prj`
- Function name:`node-func`

Your function image would be stored on OCIR under:`my-func-prj/node-func`

[Create or Select a Compartment](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

To create a compartment see[Create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To). After your compartment is created, save the compartment OCID.

To get the compartment OCID from an existing compartment:

- Open the navigation menu and click Identity &amp; Security . Under Identity , click Compartments .
- Select your compartment.
- Click the Copy link for the OCID field.

[Create an Authorization Token](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

You create an authorization token to log in to the OCI Registry. To create an authorization token:

- In the navigation menu , select the Profile menu and then select User settings .
- Click Auth Tokens .
- Click Generate Token .
- Give it a description.
- Click Generate Token .
- Copy the token and save it.

Note  
  
Ensure that you save your token right after you create it. You do not have access to it later.

[Collect your Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

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

Set up a VCN to connect your Linux instance to the internet. You configure all the components needed to create your virtual network.

[Run the VCN Wizard](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

- Click the Oracle Cloud icon to go to the main landing page.
- Scroll down to Launch Resources .
- Select Set up a network with a wizard .
- In the Start VCN Wizard workflow, select Create VCN with Internet Connectivity and then click Start VCN Wizard .
- In the configuration dialog, fill in the VCN Name for your VCN. Your Compartment is already set to the last compartment you were working in, or defaults to your`<your-tenancy> (root)`.
- In the Configure VCN and Subnets section, keep the default values for the CIDR blocks:
- VCN CIDR BLOCK: 10.0.0.0/16
- PUBLIC SUBNET CIDR BLOCK: 10.0.0.0/24
- PRIVATE SUBNET CIDR BLOCK: 10.0.1.0/24
Note  
  
Notice the public and private subnets have different network addresses.
- For DNS Resolution, uncheck Use DNS hostnames in this VCN.
- Click Next .

The Create a VCN with Internet Connectivity configuration dialog is displayed (not shown here) confirming all the values you just entered.
- To create your VCN, click Create .

The Creating Resources dialog is displayed (not shown here) showing all VCN components being created.

[Add a Security Rule to your VCN](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

- Click View Virtual Cloud Network to view your new VCN.

Your new VCN is displayed. Now you need to add a security rule to allow HTTP connections on port 80, the default port for your applications.
- With your new VCN displayed, click your Public subnet link.

The public subnet information is displayed with the Security Lists at the bottom of the page. A link to the Default Security List for your VCN is displayed.
- Click the Default Security List link.

The default Ingress Rules for your VCN are displayed.
- Click Add Ingress Rules .

An Add Ingress Rules dialog is displayed.
- Fill in the ingress rule with the following information. After all the data is entered, click Add Ingress Rules

Fill in the ingress rule as follows:
- Stateless: Checked
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: (leave-blank)
- Destination Port Range: 80
- Description: VCN for applications

After you click Add Ingress Rule , HTTP connections are allowed to your public subnet .
Note  
  
To open a different port, replace 80 in the last step with the port number.

You have successfully created a VCN that makes your applications available from the internet.

## 3. Set up OCI Command Line Interface

To develop functions on your local machine, you must set up the OCI Command Line Interface (CLI). This section assumes you have already installed Docker and Python 3.6+ and`pip3`.

Complete the following three sections to enable Oracle Functions development on your local machine with the CLI. For a detailed explanation of each step, see[Set up Oracle Functions in a Local Dev Environment](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost_topic_start_setting_up_local_dev_environment).

[Set up CLI with Python](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

Setting up the CLI allows you to deploy your functions and function application to OCI Registry from your machine. First, install the CLI using Python's virtual environment feature.

- Install`virtualenv`:

With a virtual environment, you can manage dependencies for your project. Every project can be in its own virtual environment to host independent groups of Python libraries. You install`virtualenv`and`virtualenvwrapper`.
- Ubuntu:

```

```

- Oracle Linux: If you are using an OCI Oracle Linux 7.8 image, Python 3.6 and pip3 are included by default. In case you are using a different Oracle Linux image, the commands to install the Oracle Linux developer repo along with Python 3.6 follow. If your image already has Python 3.6 installed, skip the first two commands down to the pip3 command.

```

```

- MacOS: When you install Python 3 for MacOS, pip3 is installed, so you are ready to install modules with pip3.

```

```

Note  
  
You might need to type "y" a few times to accept the packages that are installed to the VM.
- Create a directory to store your virtual environments. For example,`mkdir ~/envs`creates an`envs`directory under your home directory.
- Set up your virtual environment wrapper in`.bashrc`.

Update the file:

```

```

Note  
  
The path to the Python executable and`virtualwrapper.sh`could be different depending on the Linux distro or operating system. Ensure you use the correct path with the`which`command.

In the file, append the following text and save the file:

```

```

Activate the preceding commands in the current window.

```

```

- Start a virtual environment.

```

```

You see something similar to:`(cli-app) ubuntu@<ubuntu-instance-name>:~$`
- Install the CLI.

```

```

[Set up CLI Connection](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

Set up the CLI so it can connect to OCI services.

- Set up the CLI config file.

```

```

Enter basic information: (Get the answers from "Gather Required Information" step.)
- Location for your config [$HOME/.oci/config]:`<take-default>`
- User OCID:`<user-ocid>`
- Tenancy OCID:`<tenancy-ocid>`
- Region (for example, us-ashburn-1):`<region-identifier>`

Set up your OpenSSL API encryption keys:
- Generate a new API Signing RSA key pair? [Y/n]:`Y`
- Directory for your keys [$HOME/.oci]:`<take-default>`
- Name for your key [oci_api_key]`<take-default>`
Note  
  
Your private key is`oci_api_key.pem`and your public key is`oci_api_key_public.pem`.
- Copy the public key.
In the terminal, enter:

```

```

- Add the public key to your user account.

- In the navigation menu , select the Profile menu and then select User settings .
- From your User Settings page, under Resources , click API Keys .
- Click Add Public Key .
- Select Paste Public Keys .
- Paste value from previous step, including the lines with`BEGIN PUBLIC KEY`and`END PUBLIC KEY`
- Click Add .
You have now set up the CLI to connect to your tenancy with your user account.
- Test the installation:

```

```

If everything is set up correctly, your namespace is displayed.
- Deactivate the virtual environment:

```

```

The`(cli-app)`prefix in your environment is not be displayed anymore.
Note  
  

- Whenever you want to use the CLI, activate it with:`workon cli-app`
- If you change project names,`workon`deactivates the environment you are currently in. This way, you can quickly switch between environments.

[Set up the Fn Client](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

To do function development on your local machine, you need to install the Fn client. Fn allows you to create functions, create applications, and deploy functions to the OCI Registry.

- Install the Fn client.

The Fn client is used to create, manage, and deploy Oracle Functions. To install the client:

Command line option for Linux, MacOS, and Windows 10 Update 2004 (WSL 2.0):

Enter:

```

```

Note  
  
Regularly, rerun the installation command to upgrade to the latest version of Fn.

MacOS using Homebrew:

Enter:

```

```

Note  
  
Fn is updated as part of normal Homebrew upgrades:`brew upgrade`.
- Test your Fn installation.

Enter:`fn version`

The command returns text similar to:

```

```

Note  
  
The response indicates you have installed the current version and do not have the Fn Project server running on your local machine.

## 4. Prepare the OCI Registry for Functions

Next, you log Docker into the OCI Registry (OCIR).

[Log your Docker into OCIR](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

- Get the information you gathered earlier.
- Open a terminal window.
- Log in to OCIR:

```

```

You are prompted for your login name and password.
- Username:`<tenancy-name>/<user-name>`
- Password:`<auth-token>`

You have logged your instance into OCIR.

## 5. Configure Functions

To use Oracle Functions, you must configure the Fn application context. The context stores the values needed to connect to the Oracle Functions service.

[Configure the Fn Context](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

Use the information you gathered previously for your configuration values.

- Open a terminal instance.
- Get a list of Fn contexts.

`fn list context`

You see the`default`context selected.
- Create a Fn context for Oracle Functions. Your`<region-identifier>`is a good name for your context.

Sample command:`fn create context <region-identifier> --provider oracle`

Example:`fn create context us-phoenix-1 --provider oracle`
- Use the context you created.

Example:`fn use context us-phoenix-1`
- Set the compartment for Oracle Functions.

Example:`fn update context oracle.compartment-id ocid1.compartment.oc1..aaaaaa...`
- Set the API URL for your Oracle Functions region.

Example:`fn update context api-url https://functions.us-phoenix-1.oci.oraclecloud.com`
Note  
  
You can find the API endpoints here:[Oracle Functions API Endpoints](https://docs.oracle.com/iaas/api/#/en/functions/latest/)
- Set the URL for your Registry repository.

Sample command:`fn update context registry <region-key>.ocir.io/<tenancy-namespace>/<repo-name>`

Example:`fn update context registry phx.ocir.io/my-tenancy/myproject/repo`

Note  
  

If you use multiple profiles for the CLI, you need to set a`oracle.profile`value.

Example:`fn update context oracle.profile <profile-name>`

You have configured Fn to connect to the Oracle Functions service.
Note  
  

View/Edit your Context

Your Fn context files are in the`~/.fn/contexts`directory. Each context is stored in a`.yaml`file. For example, your`us-phoenix-1.yaml`file might look similar to:
```

```

You can edit the file directly with an editor if necessary.

For a detailed explanation of each step, see[Functions QuickStart on Local Host](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm).

## 6. Create and Deploy a Function

With your configuration complete, create and deploy a function.

[Create an Application](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

An Application is the main storage container for functions. Each function must have an application for deployment. To create application, follow these steps.
- Open the navigation menu and click Developer Services . Under Functions , click Applications .
- Click Create Application .

Fill in the form data.
- Name:`<your-app-name>`
- VCN:`<your-VCN>`
- Subnets:`<your-public-subnet>`or`<your-private-subnet>`
Note  
  
A public or private subnet may be used, select one.
- Click Create .

Your app is created.

[Create and Deploy your Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

Select one of the following languages to create and deploy a function. If you want, you can do all three.

[Create and Deploy a Java Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

With your application created, deploy a Java function. Follow these steps to create a Java "Hello World" function.
Note  
  
Ensure Java 8+ is installed to perform these steps.

- Open a terminal.
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

Various messages are displayed as the Docker images are built, pushed to OCIR, and eventually deployed to Oracle Functions.
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

[Create and Deploy a Python Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

With your application created, deploy a Python function. Follow these steps to create a Python "Hello World" function.

- Open a terminal.
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

Various messages are displayed as the Docker images are built, pushed to OCIR, and eventually deployed to Oracle Functions.
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

[Create and Deploy a Node Function](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

With your application created, deploy a Node function. Follow these steps to create a Node "Hello World" function.
Note  
  
Ensure Node.js 10+ is installed to perform these steps.

- Open a terminal.
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

Various messages are displayed as the Docker images are built, pushed to OCIR, and eventually deployed to Oracle Functions.
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

## 7. Review Function Information

After your functions run, information about your functions is available in the OCI Console.

[View Function Images in OCIR](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

When you deploy, the function is uploaded and stored in OCIR. You can navigate to OCIR and examine the function images.
- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Container Registry .
- Search for the`<your-repository-project-name>`.
- Under your project name, you see an entry for each function you deployed.
- Click the link of each image you want to see information about.

[View Function Execution Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

After you run a function, you can display metrics for that function.
- Open the navigation menu and click Developer Services . Under Functions , click Applications .

Your applications are listed on the page.
- Click the link to the application you created.
- Click the link to the function you want to examine.

Metric information about your function is displayed.

[Enable and View Logging Information](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-setup-cli/01-summary.htm#)

To enable, logging for an application, follow these steps.
- Open the navigation menu and click Developer Services . Under Functions , click Applications .
- Click the link to the application you created.
- On the left side of the application page, click the Logs link.
- Click Disabled to enable logging for your application.
- The Enable Log dialog is displayed. Fill in the following information:
- Compartment: &lt;your-compartment-name&gt;
- Log Group: Take the default value`Auto-Create a Default Log Group`
- Log name: &lt;take-default&gt;
- Log Retention: &lt;take-default&gt;
- Click Enable Log

Wait a moment for your log to be created.

To view your log, click the log name link created by the preceding steps.

## What's Next

You have successfully created a function and deployed it to Oracle Functions.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
- [Oracle Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)
