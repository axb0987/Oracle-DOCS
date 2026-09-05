# Using Fn Server to Develop Functions Locally
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfnserverlocally.htm
- Fetched: 2026-09-05 02:09 CDT

# Using Fn Server to Develop Functions Locally

Find out how to develop functions in a local environment by using the Fn Server component in Fn Project.

OCI Functions is powered by the Fn Project open source engine. The Fn Server is a core component of Fn Project and is responsible for managing functions, handling HTTP requests, and running function containers. You can run the Fn Server locally to provide an environment where you can deploy, invoke, and manage serverless functions. Running Fn Server locally enables you to test and troubleshoot function code before deploying it to Oracle Cloud Infrastructure, streamlining the development workflow while reducing round-trip times for code changes.

Although developing functions locally accelerates development, be aware of the following limitations:
- 

Infrastructure Validation: You cannot fully validate OCI-specific infrastructure locally. Networking, security policies, and some infrastructure features can only be tested after deploying to OCI.
- 

Resource Principal Authentication: You cannot test resource principal authentication mechanisms locally. Resource principals only work when functions run on OCI infrastructure. Instead, use a user principal (API key) to call OCI services (see[Example: Using User Principals (API Keys) Locally](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfnserverlocally.htm#Using-User-Principals-Locally)), or stub or mock any code that calls OCI services.

The Fn Server provides additional options, such as starting Fn Server with a syslog container for centralized log collection. For more information about the Fn Server, see:
- [Fn Project Tutorials](https://fnproject.io/tutorials/)
- [Fn Project Documentation](https://github.com/fnproject/docs#-project-documentation)

The examples in this topic describe:
- How to create an example "Hello World" Python function, build and deploy the function locally, and then invoke the function. See[Example: Developing and Testing Functions Locally](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfnserverlocally.htm#Developing-and-Testing-Functions-Locally).
- How to use a user API signing key to enable a function to list storage buckets in a compartment. See[Example: Using User Principals (API Keys) Locally](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfnserverlocally.htm#Using-User-Principals-Locally).

## Example: Developing and Testing Functions Locally

In this example, you create a "Hello World" Python function, build and deploy the function locally, and then invoke the function.
- Log in to your local environment.
- Install and start Docker by following the instructions in[1. Install and start Docker](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost_topic_install_docker)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost).

A local container engine is required to build and run functions locally. If your environment uses a Docker-compatible alternative (such as Podman Desktop or Rancher Desktop), you can use that instead.
- Install the Fn Project CLI by following the instructions in[3. Install Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost_topic_install_fn_cli)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost).
- In a terminal window, start the Fn Server locally by entering:
```

```

The command starts the Fn Server in a container on your system. You see a message indicating the Fn Server is listening on`localhost:8080`
- Initialize a new Python function named`myfunc`by entering:
```

```

The command creates the`myfunc`directory with sample code and configuration files. The content of the`myfunc`directory is as follows:
```

```

- 

Change directory to the newly created function directory (`myfunc`) by entering:
```

```

- Create an application named`myapp`to group functions by entering:
```

```

- In the`myfunc`directory, build and deploy the function locally by entering:
```

```

- Invoke the function using the Fn CLI by entering:
```

```

The function runs in a container and returns the following response:
```

```

- (Optional) To help troubleshoot issues, restart the Fn Server with debug logging enabled by entering:
```

```

Detailed log messages are shown directly in the terminal, including logs from the function code. For example:
```

```

## Example: Using User Principals (API Keys) Locally

This example extends[Example: Developing and Testing Functions Locally](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfnserverlocally.htm#Developing-and-Testing-Functions-Locally).

In this example, you use a user API signing key to enable a Python function to list storage buckets in a compartment.
- Follow the instructions in[Example: Developing and Testing Functions Locally](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfnserverlocally.htm#Developing-and-Testing-Functions-Locally)to create, build, deploy, and invoke a Python function named`myfunc`in an application named`myapp`.
- Create an OCI user, create an OCI group, and assign the user to the group (see[1. Create groups and users](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartcloudshell_topic_setup_your_tenancy_create_groups_users)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost)).
- Create a policy to enable the group to read storage buckets in a particular compartment, in the format:
```

```

See[4. Create policy for group and service](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartcloudshell_topic_setup_your_tenancy_create_group_policy)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost).
- Set up an API signing key and OCI profile for the OCI user by following the instructions in[2. Set up API signing key and OCI profile](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhosts_topic_set_up_signing_key)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost)to create an`~/.oci/config`file and a private key file (a`.pem`file).
- Make sure the`~/.oci/config`file contains a`DEFAULT`section with user, fingerprint, tenancy, region, and key_file fields, in the following format:
```

```

- 

Change directory to the`myfunc`directory by entering:
```

```

- Create a new directory named`.oci`in the`myfunc`directory by entering:
```

```

- Copy the`~/.oci/config`file and the`~/.oci/<private-key-file-name>.pem`file into the`.oci`directory. The content of the`myfunc`directory is as follows:
```

```

- Edit the`func.py`file in your preferred development environment, and replace the contents of the`func.py`file with the following code to list the buckets in the compartment:
```

```

- In the`myfunc`directory, build and deploy the function locally by entering:
```

```

- Invoke the function using the Fn CLI by entering:
```

```

The function runs in a container and returns a response similar to the following:
```

```
