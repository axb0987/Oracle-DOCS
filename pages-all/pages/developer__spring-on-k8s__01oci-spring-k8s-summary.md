# Kubernetes: Deploy a Spring Boot Application
- Source: https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm
- Fetched: 2026-09-05 03:31 CDT

# Kubernetes: Deploy a Spring Boot Application

In this tutorial, you use an Oracle Cloud Infrastructure account to set up a Kubernetes cluster. Then, you deploy a Spring Boot application to your cluster.

Key tasks include how to:
- Set up a Kubernetes cluster on OCI.
- Set up OCI CLI to access your cluster.
- Build a Spring Boot application and Docker image.
- Push the image to OCI Container Registry.
- Deploy the Docker application to your cluster.
- Connect to your application from the internet.

For additional information, see:
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [OCI Kubernetes Engine](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengoverview.htm)
- [OCI Container Registry](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryoverview.htm)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[Requirements](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- For Container Registry, Kubernetes and Load Balancers:
- A paid Oracle Cloud Infrastructure account.
- See[Signing Up for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- For building applications and Docker images:
- One of the following local environments:
- A MacOS or Linux machine.
- A Windows machine with Linux support. For example:
- [Windows Subsystem for Linux](https://docs.microsoft.com/windows/wsl/install-win10)
- [Oracle Virtual Box](https://www.virtualbox.org/)
- The following applications on your local environment:
- JDK 11 and set JAVA_HOME in .bashrc.
- Python 3.6.8+ and pip installer for Python 3
- Kubernetes Client 1.11.9+
- Apache Maven 3.0+
- Docker 19.0.3+
- Git 1.8+

#### Get the Applications

If you want to use an OCI Free Tier Linux compute instance to manage your deployment, the following sections provide information to get the required software installed.

[Install a Linux Instance](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Install a Linux VM with an Always Free compute shape, on Oracle Cloud Infrastructure. You will need a machine with`ssh`support to connect to your Linux instance.
- [Install an Oracle Linux VM](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/../common/install/../../apache-on-oracle-linux/01-summary.htm)
- Follow sections 2 and 3.
- If you have a paid account, for section 2, choose your compute options based on your offerings.
- To connect to your instance, in section 4, follow steps 1-5.
- Skip the Apache instructions.
- Install an Ubuntu VM

[Install JDK](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Verify your current installation:

```

```

- To install JDK 11, run the following commands:
- Oracle Linux:

```

```

```

```

```

```

- Ubuntu:

```

```

```

```

- Verify the installation.

```

```

- Set`JAVA_HOME`in`.bashrc`.

Update the file:

```

```

In the file, append the following text and save the file:

```

```

Examples:

```

```

```

```

- Activate the preceding command in the current window.

```

```

[Install Python 3 and Pip 3](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Verify your current installation.

```

```

- For Python 3, run the following commands:
- Oracle Linux:

```

```

```

```

- Ubuntu:

```

```

```

```

- Verify the pip installation for Python3.

```

```

Example output if pip for Python3 is installed:
```

```

- To install pip for Python 3, run the following commands:
- Oracle Linux:

```

```

```

```

- Ubuntu:

```

```

```

```

- Verify the pip for Python 3 installation.

```

```

[Install Kubernetes Client](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Verify your current installation:

```

```

If you have Kubernetes, then the version is`<major-version>.<minor-version>`. For example, for version 1.20, you get the following:
```

```

- To install he`kubectl`client, refer to the following links:
- [Install Kubernetes client on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux)
- [Install Kubernetes client on MacOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
- Verify the installation.

```

```

[Install Apache Maven](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Verify your current installation.

```

```

- To install Apache Maven, refer to the following links:
- [Download Apache Maven](https://maven.apache.org/download.cgi)
- [Install Apache Maven](https://maven.apache.org/install.html)
- Verify the installation.

```

```

[Install Docker](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Verify your current installation:

```

```

- Oracle Linux

To install Docker on Oracle Linux, run the following commands.

```

```

```

```

```

```

Note: The last command enables Docker to start on reboots.
- Ubuntu Linux

To install Docker on Ubuntu Linux, refer to the following link:[Get Docker](https://docs.docker.com/get-docker/)
- Verify the installation.

```

```

## 1. Prepare

Prepare your environment to create and deploy your application.

[Check your Service Limits](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Log in to the Oracle Cloud Infrastructure Console .
- Open the navigation menu, and click Governance and Administration . Under Governance , click Limits, Quotas and Usage .
- Find your service limit for Regions :
- Filter for the following options:
- Service: Regions
- Scope: Tenancy
- Resource: Subscribed region count
- Compartment:`<tenancy-name>`(root)
- Find service limit:
- Limit Name:`subscribed-region-count`
- Service Limit: minimum 2
- Find your available Compute core count for the VM.Standard.E3.Flex shape:
- Filter for the following options:
- Service: Compute
- Scope:`<first-availability-domain>`. Example:`EMlr:US-ASHBURN-AD-1`
- Resource: Cores for Standard.E3.Flex and BM.Standard.E3.128 Instances
- Compartment:`<tenancy-name>`(root)
- Find available core count:
- Limit Name:`standard-e3-core-ad-count`
- Available: minimum 1
- Repeat for Scope:`<second-availability-domain>`and`<third-availability-domain>`. Each region must have at least one core available for this shape.
- Find out if you have 50 GB of Block Volume available:
- Filter for the following options:
- Service: Block Volume
- Scope:`<first-availability-domain>`. Example:`EMlr:US-ASHBURN-AD-1`
- Resource Volume Size (GB)
- Compartment:`<tenancy-name>`(root)
- Find available block volume storage:
- Limit Name:`total-storage-gb`
- Available: minimum 50
- Repeat for Scope:`<second-availability-domain>`and`<third-availability-domain>`. Each region must have at least 50 GB of block volume available.
- Find out how many Flexible Load Balancers you have available:
- Filter for the following options:
- Service: LbaaS
- Scope:`<your-region>`. Example:`us-ashburn-1`
- Resource:`<blank>`
- Compartment:`<tenancy-name>`(root)
- Find the number of available flexible load balancers:
- Limit Name:`lb-flexible-count`
- Available: minimum 1
Note  
  
This tutorial creates three compute instances with a VM.Standard.E3.Flex shape for the cluster nodes. To use another shape, filter for its core count . For example, for VM.Standard2.4 , filter for Cores for Standard2 based VM and BM Instances and get the count .

For a list of all shapes, see[VM Standard Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#vmshapes__vm-standard).
Note  
  

This tutorial uses a 'Quick Create' workflow to create a cluster with a public regional subnet that hosts a flexible load balancer. To use a different load balancer, you can use a custom workflow to explicitly specify which existing network resources to use, including the existing subnets in which to create the load balancers.

To use another bandwidth for the load balancer, filter for its count , for example 100-Mbps bandwidth or 400-Mbps bandwidth .

[Create an Authorization Token](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- In the navigation menu , select the Profile menu and then select User settings .
- Click Auth Tokens .
- Click Generate Token .
- Give it a description.
- Click Generate Token .
- Copy the token and save it.
- Click Close .

Note  
  
Ensure that you save your token right after you create it. You have no access to it later.

[Gather Required Information](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Collect the following credential information from the Oracle Cloud Infrastructure Console .

- Tenancy name:`<tenancy-name>`
- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- Tenancy namespace:`<tenancy-namespace>`
- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- Copy the value for Object Storage Namespace .
Note  
  
For some accounts, tenancy name and namespace differ. Ensure that you use namespace in this tutorial.
- Tenancy OCID:`<tenancy-ocid>`
- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- Copy OCID.
- Username:`<user-name>`
- In the navigation menu , select the Profile menu and then select User settings .
- User OCID:`<user-ocid>`
- In the navigation menu , select the Profile menu and then select User settings .
- Copy OCID.
- Find your region information.

- Region:`<region-identifier>`
- In the Console's top navigation bar, find your region. Example: US East (Ashburn) .
- Find your Region Identifier from the table in[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- Example:`us-ashburn-1`.
- Region Key:`<region-key>`
- Find your Region Key from the table in[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- Example:`iad`
- Copy your authentication token from Create an Authentication Token section.

- Auth Token:`<auth-token>`

[Set up OCI Command Line Interface](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

[Install a Python Virtual Environment and Wrapper](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

The Python`virtualenv`creates a folder that contains all the executables and libraries for your project.

The`virtualenvwrapper`is an extension to`virtualenv`. It provides a set of commands, which makes working with virtual environments much more pleasant. It also places all your virtual environments in one place. The`virtualenvwrapper`provides tab-completion on environment names.
- Install`virtualenv`.

```

```

- Install`virtualenvwrapper`.

```

```

- Find the location of the`virtualenvwrapper.sh`script.

```

```

Example paths:
- Linux example:`/home/ubuntu/.local/bin/virtualenvwrapper.sh`
- MacOS example:`/usr/local/bin/virtualenvwrapper.sh`
- Configure the virtual environment wrapper in`.bashrc`.

```

```

Append the following text.

```

```

Replace`<path-to-virtualenvwrapper.sh>`with its value.

Based on the location of Python3 binaries in your environment, update`/usr/bin/python3`to its correct location.

Save the file.
- Activate the commands in the current window.

```

```

Example output:
```

```

[Install OCI CLI](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Start a virtual environment.

```

```

- Confirm that the name of your virtual environment,`cli-app`appears in the left of your command prompt.

Example:`(cli-app) ubuntu@<ubuntu-instance-name>:~$`
- Install OCI CLI.

```

```

- Test the installation:

```

```

If everything is set up correctly, you get the version.

```

```

[Configure the OCI CLI](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Enter the following command in your virtual environment :

```

```

- Enter your answers from the Gather Required Information section:
- Location for your config [$HOME/.oci/config]:`<take-default>`
- User OCID:`<user-ocid>`
- Tenancy OCID:`<tenancy-ocid>`
- Region (e.g. us-ashburn-1):`<region-identifier>`
- Enter the following information to set up your OpenSSL API encryption keys:
- Generate a new API Signing RSA key pair? [Y/n]: Y
- Directory for your keys [$HOME/.oci]:`<take-default>`
- Name for your key [oci_api_key]`<take-default>`
- Deactivate the virtual environment:

```

```

The`(cli-app)`prefix in your environment is not displayed anymore.
Note  
  
Your private key is`oci_api_key.pem`and your public key is`oci_api_key_public.pem`.

[Add the Public Key to Your User Account.](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Activate the`cli-app`environment:

```

```

- Display the public key.

```

```

- Copy the public key.
- Add the public key to your user account:

- Go to the Console.
- In the navigation menu , select the Profile menu and then select User settings .
- Click API Keys .
- Click Add API Key .
- Click Paste Public Key .
- Paste value from previous step, including the lines with`BEGIN PUBLIC KEY`and`END PUBLIC KEY`.
- Click Add .
Note  
  

- Whenever you want to use the OCI CLI, activate it with:`workon cli-app`
- When you change project names,`workon`deactivates your current working environment. This way, you can quickly switch between environments.

## 2. Set Up a Cluster

Install and configure management options for your Kubernetes cluster. Later, deploy your application to this cluster.

[Add Compartment Policy](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

If your username is in the Administrators group, then skip this section. Otherwise, have your administrator add the following policy to your tenancy:

```

```

With this privilege, you can create a compartment for all the resources in your tutorial.

[Steps to Add the Policy](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- In the navigation menu , select the Profile menu and then select User settings .
- In the left pane, click Groups .
- In a notepad, copy the Group Name that your username belongs.
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Policies .
- Select your compartment from the Compartment drop-down.
- Click Create Policy .
- Fill in the following information:

- Name:`manage-compartments`
- Description:`Allow the group <the-group-your-username-belongs> to list, create, update, delete and recover compartments in the tenancy.`
- Compartment:`<your-tenancy> (root)`
- For Policy Builder , click Show manual editor .
- Paste in the following policy:

```

```

- Click Create .

Reference: The`compartments`resource-type in[Verbs + Resource-Type Combinations for IAM](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm#Identity)

[Create a Compartment](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

Create a compartment for the resources that you create in this tutorial.
- Sign in to the Oracle Cloud Infrastructure Console .
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Compartments .
- Click Create Compartment .
- Fill in the following information:
- Name:`<your-compartment-name>`
- Description:`Compartment for <your-description> .`
- Parent Compartment:`<your-tenancy> (root)`
- Click Create Compartment .

Reference:[Create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To)

[Add Resource Policy](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

If your username is in the Administrators group, then skip this section. Otherwise, have your administrator add the following policy to your tenancy:

```

```

With this privilege, you can manage all resources in your compartment , essentially giving you administrative rights in that compartment.

[Steps to Add the Policy](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Open the navigation menu and click Identity &amp; Security . Under Identity , click Policies .
- Select your compartment from the Compartment drop-down.
- Click Create Policy .
- Fill in the following information:

- Name:`manage- <your-compartment-name> -resources`
- Description:`Allow users to list, create, update, and delete resources in <your-compartment-name>.`
- Compartment:`<your-tenancy> (root)`
- For Policy Builder , select the following choices:

- Policy use cases:`Compartment Management`
- Common policy templates:`Let compartment admins manage the compartment`
- Groups:`<the-group-your-username-belongs>`
- Location:`<your-tenancy> (root)`
- Click Create .

Reference:[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)

[Create a Cluster with 'Quick Create'](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

Create a cluster with default settings and new network resources through the 'Quick Create' workflow.

- Sign in to the Oracle Cloud Infrastructure Console .
- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Kubernetes Clusters (OKE) .
- Click Create Cluster .
- Select Quick Create .
- Click Launch Workflow .

The Quick Create Cluster dialog is displayed.
- Fill in the following information.

- Name:`<your-cluster-name>`
- Compartment:`<your-compartment-name>`
- Kubernetes Version:`<take-default>`
- Kubernetes API Endpoint: Public Endpoint

The Kubernetes cluster is hosted in a public subnet with an auto-assigned public IP address.
- Kubernetes Worker Nodes: Private Workers

The Kubernetes worker nodes are hosted in a private subnet.
- Shape:`VM.Standard.E3.Flex`
- Select the number of OCPUs: 1
- Amount of Memory (GB): 16
- Number of Nodes: 3
- Click Show Advanced Options .

Keep the defaults.
- Specify a custom boot volume size: Clear the check box.
- Image Verification: Clear the check box.
- Add an SSH key: No SSH key
- Click Next .

All your choices are displayed. Review them to ensure that everything is configured correctly.
- Click Create Cluster .

The services set up for your cluster are displayed.
- Click Close .
- Get a cup of coffee. It takes a few minutes for the cluster to be created.
You have successfully created a Kubernetes cluster.

[Set Up Local Access to Your Cluster](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

After you create a Kubernetes cluster, set up your local system to access the cluster.

- Sign in to the Oracle Cloud Infrastructure Console .
- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Kubernetes Clusters (OKE) .
- Click the link to`<your-cluster>`.

The information about your cluster is displayed.
- Click Access Cluster .
- Click Local Access .
- Follow the steps provided in the dialog. They are reprinted here for your reference.

Note  
  
If you are not in your virtual environment, enter:`workon cli-app`before you run`kubectl`commands.

Check your`oci`CLI version.

```

```

Make your`.kube`directory if it doesn't exist.

```

```

Create a kubeconfig file for your setup. Use the information from Access Your Cluster dialog.
```

```

Export the`KUBECONFIG`environment variable.

```

```

Note  
  
If you want to have the environment variable start in a new shell, then add`export KUBECONFIG=$HOME/.kube/config`to your`~/.bashrc`file.
- Test your cluster configuration with the following commands.

List clusters:

```

```

Get deployment details:

```

```

Get pods:

```

```

Note  
  
Since no application is deployed, the last two commands produce: "No resources found in default namespace."
Note  
  
To look at a different cluster, specify a different config file on the command line. Example:

```

```

With your cluster access set up, you are now ready to prepare your application for deployment.

## 3. Build a Local Application

Build a local application and a Docker image for the application.

[Create a Local Application](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Make a copy of the Spring Boot Docker guide with Git:

```

```

- Change into the`gs-spring-boot-docker/initial`directory.

```

```

- Change into the Java source directory:`src/main/java/hello`.

```

```

- Update`Application.java`with the following code:

```

```

- Save the file.

[Run the Local Application](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Change into the`gs-spring-boot-docker/initial`directory.
- Package the app:

```

```

Example output:
```

```

- Run the app:

```

```

Example output:
```

```

- Keep the code running and test the app in one of the following ways:

- In a new terminal connected to your instance, enter the following code:

```

```

Output:
```

```

- Load the following address in a browser:

```

```

You can use the second option, only if your environment is local.
- Stop the running application. Example:`Ctrl + C`

[Build a Docker Image](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

A Docker image holds an application, its dependencies, and instructions to run the application.
Note  
  
For MacOS, you can remove the`sudo`in the`docker`commands.

- Change into the`gs-spring-boot-docker/initial`directory.
- Create a file named`Dockerfile`.

```

```

- Build the Docker image:

```

```

Example output:
```

```

- Run the Docker image:

```

```

You get the same result as running the local app.
- Stop the running application.
Congratulations! You have successfully created a Spring Boot Docker image.
References:
- [Spring Boot with Docker guide on GitHub](https://github.com/spring-guides/gs-spring-boot-docker)
- [Spring Boot Docker tutorial](https://spring.io/guides/gs/spring-boot-docker/)

## 4. Deploy Your Docker Image

Push your Spring Boot Docker image to OCI Container Registry. Then use the image to deploy your application.

[Create a Docker Repository](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Container Registry .
- In the left navigation, select`<your-compartment-name>`.
- Click Create Repository .
- Create a private repository with your choice of repo name:

```

```

Example:`spring-projects/spring-boot-hello`
You are now ready to push your local image to Container Registry.
Note  
  
Before you push an image into a compartment, you must create a repository in that compartment .
Note  
  
The slash in a repository name does not represent a hierarchical directory structure . The optional`<repo-prefix>`helps organize your repositories.

[Push Your Local Image](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

Note  
  
For MacOS, you can remove the`sudo`in the`docker`commands.

- Open a terminal window.
- Log in to OCI Container Registry:

```

```

You are prompted for your login name and password.
- Username:`<tenancy-namespace>/<user-name>`
- Password:`<auth-token>`
- List your local Docker images:

```

```

The Docker images on your system are displayed. Identify the image you created in the last section:`spring-boot-hello`
- Tag your local image with the URL for the registry plus the repo name , so you can push it to that repo.

```

```

- Replace`<repo-url>/<repo-name>`with:
```

```

- Replace`<repo-name>`with:

`<repo-prefix>/<image-name>`from the Create a Docker Repository section.
- Example:
```

```

In this example, the components are:
- `<repo-url>:``iad.ocir.io/my-namespace/`
- `<repo-name>:``spring-projects/spring-boot-hello`
Note  
  
OCI Container Registry now supports creating a registry repo in any compartment rather than only in the root compartment (tenancy). To push the image to the repo you created, combine the registry URL with the exact repo name. OCI Container Registry matches the unique repo name and pushes your image.
- Check your Docker images to see if the image is tagged .

```

```

- The tagged image points to your local image and has the same image ID as your local image.
- The tagged image name is:
```

```

- Push the image to Container Registry.

```

```

Example:
```

```

- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Container Registry .
- Find your image in Container Registry after the push command is complete.

Note  
  
You can only push images that include the registry URL in their name.

[Deploy the Image](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

With your image in Container Registry, you can now deploy your image and app.

- Create a registry secret for your application. This secret authenticates your image when you deploy it to your cluster.

To create your secret, fill in the information in this template .

```

```

After the command runs, you get a message similar to:`secret/ocirsecret created`.
- Verify that the secret is created. Issue the following command:

```

```

The output includes information about your secret in the yaml format.
- Determine the host URL to your registry image using the following template:

```

```

Example:
```

```

- On your system, create a file called`sb-app.yaml`with the following text:

Replace the following place holders:
- `<your-image-url>`
- `<your-secret-name>`

```

```

- Deploy your application with the following command.

```

```

Output:
```

```

Note  
  
In the`sb-app.yaml`file, the code after the dashes adds a load balancer.

[Test Your App](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-k8s/01oci-spring-k8s-summary.htm#)

After you deploy your app, it might take the load balancer a few seconds to load.

- Check if the load balancer is live:

```

```

Repeat the command until load balancer is assigned a public IP address.
- Use the load balancer IP address to connect to your app in a browser:

```

```

The browser displays:`Spring Boot Hello World!`
- (Optional) To undeploy your application from the cluster, run the following command:

```

```

Output:
```

```

Your application is now removed from your cluster.

## What's Next

Congratulations! You have successfully created a Hello World application, deployed it to a Kubernetes cluster, and made it accessible on the internet, using the Spring Boot framework.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
