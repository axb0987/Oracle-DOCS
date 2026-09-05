# Functions QuickStart on Cloud Shell
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm
- Fetched: 2026-09-05 02:09 CDT

# Functions QuickStart on Cloud Shell

Find out how to get set up and running quickly on Cloud Shell using this OCI Functions QuickStart.

## A. Set up your tenancy

[1. Create groups and users](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

If suitable users and groups don't exist already:
- Sign in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select a domain, and select the User management tab.
- Create a new group by selecting Create group in the Groups section.
- Create a new user by selecting Create in the Users section.
- Add a user to a group by selecting the name of the group, and then Assign user to group on the Users tab.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatinggroupsusers.htm)for more information.

[2. Create compartment](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

If a suitable compartment in which to create network resources and OCI Functions resources doesn't exist already:
- Sign in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments .
- Select Create Compartment .

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingcompartment.htm)for more information.

[3. Create VCN and subnets](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

If a suitable VCN in which to create network resources doesn't exist already:

- Sign in to the Console as a tenancy administrator.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select Start VCN Wizard from the Actions menu to create a new VCN.
- In the Start VCN Wizard panel, select Create VCN with Internet Connectivity and select Start VCN Wizard .
- Enter a name for the new VCN, select Next , and then select Create to create the VCN along with the related network resources.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingvcn.htm)for more information.

[4. Create policy for group and service](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

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

[1. Create your first application](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

- Sign in to the Console as a functions developer.
- Open the navigation menu and select Developer Services . Under Functions , select Applications .
- Select the region you're using with OCI Functions.
- Select Create application .
- Specify:
- helloworld-app as the name for the new application. You'll deploy your first function in this application, and specify this application when invoking the function.
- The VCN and subnet in which to run the function. Note that a public subnet requires an internet gateway in the VCN, and a private subnet requires a service gateway in the VCN.
- Select Create .

See[detailed instructions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingapps.htm)for more information.

## C. Set up your Cloud Shell dev environment

[1. Display the Cloud shell setup panel and the Cloud Shell window](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

On the Applications list page in the Console:
- Select the helloworld-app application you just created to display the application details page.
- 

Go to the Getting Started section, and then select View Guide beside Cloud Shell Setup .

Tip: The Cloud shell setup panel now displays commands tailored specifically for you. You copy and paste these commands to configure your Cloud Shell environment for functions development.
- Select Launch cloud shell to display the Cloud Shell terminal window.
- In the Cloud Shell terminal window, select Architecture from the Actions menu, and select the X86_64 option as your preferred architecture.

[2. Set up Fn Project CLI context](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

Copy and paste commands from the Cloud shell setup panel into the Cloud Shell terminal window to configure your environment, as follows:
- 

Find the name of the pre-created Fn Project context for the current region in which you created the application:
```

```

At least two Fn Project contexts are returned, a default context and a context for the current region (for example, named us-phoenix-1). Although not required, you can, if you prefer, create your own context for use with Cloud Shell by entering the command`fn create context <my-context> --provider oracle-cs`, and specify that context in subsequent commands.
- 

Set the Fn Project context to use the region context:
```

```

where`<region-context>`is the context for the current region. For example:
```

```

- 

Configure the Fn Project context with the OCID of the current compartment that will own deployed functions:
```

```

For example:
```

```

- 

Configure the Fn Project context with the Oracle Cloud Infrastructure Registry address in the current region and tenancy that you want to use with OCI Functions:
```

```

where`<tenancy-namespace>`is the tenancy's auto-generated Object Storage namespace, and`<repo-name-prefix>`is a prefix of your choosing for the Oracle Cloud Infrastructure Registry repository in which to store images for the function (see[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)for more information). For example:
```

```

- 

Configure the Fn Project context with the OCID of the compartment for repositories to and from which you want OCI Functions to push and pull function images, by entering:
```

```

For example:
```

```

If you do not specify a value for`oracle.image-compartment-id`, OCI Functions pushes and pulls images to and from repositories in the root compartment.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)for more information.

[3. Generate auth token](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

On the Cloud shell setup panel in the Console:
- Select Generate an auth token to display the Auth Tokens page, and select Generate Token .
- Enter a meaningful description for the auth token in the Generate Token dialog, and select Generate Token . The new auth token is displayed (for example, 6aN...6MqX).
- Copy the auth token immediately to a secure location from where you can retrieve it later, because you won't see the auth token again in the Console.
- Close the Generate Token dialog.

See[Configuration Notes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsgenerateauthtokens.htm)for more information.

[4. Log in to Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

On the Cloud shell setup panel in the Console:
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

[1. Create your first function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

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

[2. Deploy your first function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

In the terminal window:
- Change directory to the hello-java directory created in the previous step:
```

```

- Enter the following single Fn Project command to build the function and its dependencies as a Docker image called hello-java, push the image to the specified Docker registry, and deploy the function to OCI Functions in the helloworld-app application that you created earlier:
```

```

- (Optional) Confirm that the function has been deployed to OCI Functions by selecting the Functions tab (on the details page for the helloworld-app application) and noting that the hello-java function now appears.

See[detailed instructions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionscreatingfirst.htm)for more information.

[3. Invoke your first function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

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

[4. Next steps](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#)

Now that you've created, deployed, and invoked a function, learn how to:
- view function logs in the Oracle Cloud Infrastructure Logging service, or by configuring a syslog URL (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionsexportingfunctionlogfiles.htm)
- explore OCI Functions using samples on GitHub (see[Oracle Functions Samples](https://github.com/oracle/oracle-functions-samples))
- invoke a function using SDKs (see[Using SDKs to Invoke Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../shared/../Tasks/functionsinvokingfunctions.htm#usingsdks))
