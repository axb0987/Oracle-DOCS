# Functions QuickStart on Local Host
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm
- Fetched: 2026-09-05 02:09 CDT

# Functions QuickStart on Local Host

Find out how to get set up and running quickly on a local host using this OCI Functions QuickStart.

## A. Set up your tenancy

[1. Create groups and users](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

If suitable users and groups don't exist already:
- Sign in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select a domain, and select the User management tab.
- Create a new group by selecting Create group in the Groups section.
- Create a new user by selecting Create in the Users section.
- Add a user to a group by selecting the name of the group, and then Assign user to group on the Users tab.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatinggroupsusers.htm)for more information.

[2. Create compartment](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

If a suitable compartment in which to create network resources and OCI Functions resources doesn't exist already:
- Sign in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments .
- Select Create Compartment .

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingcompartment.htm)for more information.

[3. Create VCN and subnets](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

If a suitable VCN in which to create network resources doesn't exist already:

- Sign in to the Console as a tenancy administrator.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select Start VCN Wizard from the Actions menu to create a new VCN.
- In the Start VCN Wizard panel, select Create VCN with Internet Connectivity and select Start VCN Wizard .
- Enter a name for the new VCN, select Next , and then select Create to create the VCN along with the related network resources.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingvcn.htm)for more information.

[4. Create policy for group and service](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

If one or more OCI Functions users is not a tenancy administrator:
- Sign in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .
- 

Select Create Policy , specify a name and description for the new policy, and select the tenancy's root compartment.
- 

Use the Policy Builder to create the policy. Select Functions from the list of Policy use cases , and base the policy on the policy template Let users create, deploy, and manage functions and applications .

The policy template includes the following policy statements:
- `Allow group <group-name> to use cloud-shell in tenancy`
- `Allow group <group-name> to manage repos in tenancy`
- `Allow group <group-name> to read objectstorage-namespaces in tenancy`
- `Allow group <group-name> to manage logging-family in tenancy`
- `Allow group <group-name> to read metrics in tenancy`
- `Allow group <group-name> to manage functions-family in tenancy`
- `Allow group <group-name> to use virtual-network-family in tenancy`
- `Allow group <group-name> to use apm-domains in tenancy`
- `Allow group <group-name> to read vaults in tenancy`
- `Allow group <group-name> to use keys in tenancy`
- `Allow service faas to use apm-domains in tenancy`
- `Allow service faas to {KEY_READ} in tenancy where request.operation='GetKeyVersion'`

If necessary, you can restrict these policy statements by compartment.

If the function and its image or encryption key are in different tenancies, use cross-tenancy resource principal policies.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingpolicies.htm)for more information.

## B. Create application

[1. Create your first application](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

- Sign in to the Console as a functions developer.
- Open the navigation menu and select Developer Services . Under Functions , select Applications .
- Select the region you're using with OCI Functions.
- Select Create application .
- Specify:
- helloworld-app as the name for the new application. You'll deploy your first function in this application, and specify this application when invoking the function.
- The VCN and subnet in which to run the function. Note that a public subnet requires an internet gateway in the VCN, and a private subnet requires a service gateway in the VCN.
- Select Create .

See[detailed instructions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingapps.htm)for more information.

## C. Set up your local host dev environment

[1. Install and start Docker](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

In a terminal window in your development environment:
- Confirm that Docker is installed by entering:

```

```

If you see an error message indicating that Docker is not installed, you have to install Docker before proceeding. See the[Docker documentation](https://docs.docker.com/)for your platform (for Oracle Linux, see[here](https://docs.oracle.com/cd/E52668_01/E87205/html/docker_install_upgrade.html)).

Assuming Docker is installed, go to the[Prerequisites section of the Fn Project home page on GitHub](https://github.com/fnproject/fn#pre-requisites)and confirm that the installed version of Docker is at least the minimum version specified there. If not, re-install Docker before proceeding.
- Launch the standard hello-world Docker image as a container to confirm that Docker is running by entering:

```

```

If you see an error message indicating that Docker is not running, you have to start the Docker daemon before proceeding. See the[Docker documentation](https://docs.docker.com/).

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsstartdocker.htm)for more information.

[2. Set up API signing key and OCI profile](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

- Sign in to the Console as a functions developer.
- In the navigation menu , select the Profile menu and then select User settings .
- Select the Tokens and keys tab, go to the API keys section, and select Add API key .
- Select Generate API key pair in the Add API key panel.
- Select Download private key and save the private key file (as a .pem file) in the`~/.oci`directory. (If the`~/.oci`directory doesn't already exist, create it now).
- Select Add to add the new API signing key to your user settings.

The Configuration File Preview dialog is displayed, containing a configuration file snippet with basic authentication information for a profile named`DEFAULT`(including the fingerprint of the API signing key you just created).
- Copy the configuration file snippet shown in the text box, and close the Configuration File Preview dialog.
- In a text editor, open the`~/.oci/config`file and paste the snippet into the file. (If the`~/.oci/config`file doesn't already exist, create it now).
- In the text editor, change the profile in the snippet you've just pasted, as follows:
- Change the name of the profile from`[DEFAULT]`to a name of your choosing (for example,`[functions-developer-profile]`). Note that the`~/.oci/config`file cannot contain two profiles with the same name.
- Change the value of the`key_file`parameter of the profile to specify the path of the private key file (the .pem file) you downloaded earlier.
- In the text editor, save the changes you've made to the`~/.oci/config`file, and close the text editor.
- In a terminal window, change permissions on the private key file (the .pem file) to ensure that only you can read it, by entering:

```

```

See Configuration Notes for more information about[setting up an API signing key](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssetupapikey.htm)and[creating a profile](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm).

[3. Install Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

In a terminal window in your development environment:
- Install the Fn Project CLI using the appropriate instructions below for your environment:
- Linux or MacOS: Enter:

```

```

- MacOS using Homebrew: Enter:

```

```

- Windows: Follow the[Install Fn Client instructions on GitHub](https://github.com/fnproject/docs/blob/master/fn/develop/running-fn-client-windows.md#install-fn-client).
- Linux, MacOS, or Windows: Download and run the binary from the[Fn Project Releases page on GitHub](https://github.com/fnproject/cli/releases).
- Confirm that the Fn Project CLI has been installed by entering:

```

```

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstallfncli.htm)for more information.

[4. Set up Fn Project CLI context provider --oracle](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

In a terminal window in your development environment:
- Create a new Fn Project CLI context by entering:

```

```

Note that you specify`--provider oracle`to enable authentication and authorization using Oracle Cloud Infrastructure request signing, private keys, user groups, and policies that grant permissions to those user groups.
- Specify that the Fn Project CLI is to use the new context by entering:

```

```

- Configure the new Fn Project CLI context with the name of the OCI profile you've created for use with OCI Functions (for example,`[functions-developer-profile]`), by entering:

```

```

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)for more information.

[5. Complete Fn Project CLI context configuration](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

In a terminal window in your development environment:
- Configure the new Fn Project CLI context with the OCID of the compartment you want to own deployed functions

```

```

- Configure the new context with the api-url endpoint to use when calling the OCI API by entering:

```

```

where`<api-endpoint>`is one of the endpoints in the list of Functions endpoints in the[Functions API](https://docs.oracle.com/iaas/api/#/en/functions/latest/), in the format`https://functions.<region-identifier>.oci.oraclecloud.com`. For example:

```

```

- 

Configure the Fn Project CLI context with the Oracle Cloud Infrastructure Registry address in the current region and tenancy that you want to use with OCI Functions:
```

```

where`<tenancy-namespace>`is the tenancy's auto-generated Object Storage namespace, and`<repo-name-prefix>`is a prefix of your choosing for the Oracle Cloud Infrastructure Registry repository in which to store images for the function (see[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)for more information). For example:
```

```

- 

Configure the Fn Project CLI context with the OCID of the compartment for repositories to and from which you want OCI Functions to push and pull function images, by entering:
```

```

For example:
```

```

If you do not specify a value for`oracle.image-compartment-id`, OCI Functions pushes and pulls images to and from repositories in the root compartment.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)for more information.

[6. Generate auth token](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

- Sign in to the Console as a functions developer.
- In the navigation menu , select the Profile menu and then select User settings .
- Select the Tokens and keys tab, go to the Auth Tokens section, and select Generate token .
- Enter a meaningful description for the auth token in the Generate token dialog, and select Generate token . The new auth token is displayed.
- Copy the auth token immediately to a secure location from where you can retrieve it later, because you won't see the auth token again in the Console.
- Close the Generate token dialog.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsgenerateauthtokens.htm)for more information.

[7. Log in to Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

On the Local setup panel in the Console:
- 

Copy the following command:
```

```

where`<tenancy-namespace>`is the tenancy's auto-generated Object Storage namespace (see[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionslogintoocir.htm)for more information). For example:
```

```

If your tenancy is federated with Oracle Identity Cloud Service, the format will be slightly different. For example:
```

```

- In the terminal window, paste the command you just copied and run it.
- 

When prompted for a password, enter the Oracle Cloud Infrastructure auth token that you created and copied earlier. For example,`6aN...6MqX`

You're now ready to start creating, deploying, and invoking functions.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionslogintoocir.htm)for more information.

## D. Create, deploy, and invoke your function

[1. Create your first function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

In the terminal window:
- 

Create a helloworld java function by entering:
```

```

A directory called hello-java is created, containing:
- a function definition file called func.yaml
- a /src directory containing source files and directories for the helloworld function
- a Maven configuration file called pom.xml that specifies the dependencies required to compile the function

Java is just one of several supported languages.

See[detailed instructions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingfirst.htm)for more information.

[2. Deploy your first function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

In the terminal window:
- Change directory to the hello-java directory created in the previous step:
```

```

- Enter the following single Fn Project command to build the function and its dependencies as a Docker image called hello-java, push the image to the specified Docker registry, and deploy the function to OCI Functions in the helloworld-app application that you created earlier:
```

```

- (Optional) Confirm that the function has been deployed to OCI Functions by selecting the Functions tab (on the details page for the helloworld-app application) and noting that the hello-java function now appears.

See[detailed instructions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingfirst.htm)for more information.

[3. Invoke your first function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

In the terminal window:
- 

Invoke the hello-java function by entering:
```

```

The 'Hello world!' message is displayed.
- 

Invoke the hello-java function with the parameter`'John'`by entering:
```

```

The 'Hello John!' message is displayed.

Congratulations! You've just created, deployed, and invoked your first function using OCI Functions!

See[detailed instructions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingfirst.htm)for more information.

[4. Next steps](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#)

Now that you've created, deployed, and invoked a function, learn how to:
- view function logs in the Oracle Cloud Infrastructure Logging service, or by configuring a syslog URL (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionsexportingfunctionlogfiles.htm)
- explore OCI Functions using samples on GitHub (see[Oracle Functions Samples](https://github.com/oracle/oracle-functions-samples))
- invoke a function using SDKs (see[Using SDKs to Invoke Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionsinvokingfunctions.htm#usingsdks))
