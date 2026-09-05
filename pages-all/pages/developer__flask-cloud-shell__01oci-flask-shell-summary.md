# Kubernetes Using Cloud Shell: Deploy a Python Flask Application
- Source: https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm
- Fetched: 2026-09-05 03:31 CDT

# Kubernetes Using Cloud Shell: Deploy a Python Flask Application

In this tutorial, you use an Oracle Cloud Infrastructure account to set up a Kubernetes cluster. Then, you create a Python application with a Flask framework. Finally, you deploy your application to your cluster using Cloud Shell.

Key tasks include how to:
- Create a Compartment.
- Set up a Kubernetes cluster on OCI.
- Build a Python application in a Flask framework.
- Create a Docker image.
- Push your image to OCI Container Registry.
- Use Cloud Shell to deploy your Docker application to your cluster.
- Connect to your application from the internet.

For additional information, see:
- [More on Kubernetes](https://kubernetes.io/docs/home/)
- [OCI Kubernetes Engine](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengoverview.htm)
- [OCI Container Registry](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryoverview.htm)
- [Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[Requirements](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

- A paid Oracle Cloud Infrastructure account. See[Signing Up for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- Cloud Shell provides the following applications:
- JDK 8+
- Python 3.6.8+
- Kubectl 1.18.10+
- Apache Maven 3.5+
- Docker 19.0.11+
Note  
  
The advantage of using Cloud Shell is all the required tools to manage your application are already installed and ready to use.

## 1. Prepare

Prepare your environment to create and deploy your application.

[Check your Service Limits](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

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
- Find available core count:
- Limit Name:`total-storage-gb`
- Available: minimum 50
- Repeat for Scope:`<second-availability-domain>`and`<third-availability-domain>`. Each region must have at least 50 GB of block volume available.
- Find out how many Flexible Load Balancers you have available:
- Filter for the following options:
- Service: LbaaS
- Scope:`<your-region>`. Example:`us-ashburn-1`
- Resource:`<blank>`
- Compartment:`<tenancy-name>`(root)
- Find the count for the following shapes
- Limit Name:`lb-flexible-bandwidth-count`
- Available: minimum 1
Note  
  
This tutorial creates three compute instances with a VM.Standard.E2.1 shape for the cluster nodes. To use another shape, filter for its core count . For example, for VM.Standard2.4 , filter for Cores for Standard2 based VM and BM Instances and get the count .

For a list of all shapes, see[VM Standard Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#vmshapes__vm-standard).
Note  
  
This tutorial creates three compute instances with a VM.Standard.E3.Flex shape for the cluster nodes. To use another shape, filter for its core count . For example, for VM.Standard2.4 , filter for Cores for Standard2 based VM and BM Instances and get the count .

For a list of all shapes, see[VM Standard Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#vmshapes__vm-standard).
Note  
  

This tutorial uses a 'Quick Create' workflow to create a cluster with a public regional subnet that hosts a flexible load balancer. To use a different load balancer, you can use a custom workflow to explicitly specify which existing network resources to use, including the existing subnets in which to create the load balancers.

To use another bandwidth for the load balancer, filter for its count , for example 100-Mbps bandwidth or 400-Mbps bandwidth .

[Create an Authorization Token](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

- In the navigation menu , select the Profile menu and then select User settings .
- Click Auth Tokens .
- Click Generate Token .
- Give it a description.
- Click Generate Token .
- Copy the token and save it.
- Click Close .

Note  
  
Ensure that you save your token right after you create it. You have no access to it later.

[Gather Required Information](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

- Collect the following credential information from the Oracle Cloud Infrastructure Console .

- Tenancy name:`<tenancy-name>`
- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- Tenancy namespace:`<tenancy-namespace>`
- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- Copy the value for Object Storage Namespace .
Note  
  
For some accounts, tenancy name and namespace differ. Ensure that you use namespace in this tutorial.
- Tenancy OCID:`<tenancy-ocid>`
- In the navigation menu , select the Profile menu and then select User settings .
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

## 2. Set Up a Cluster

Install and configure management options for your Kubernetes cluster. Later, deploy your application to this cluster.

[Add Compartment Policy](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

If your username is in the Administrators group, then skip this section. Otherwise, have your administrator add the following policy to your tenancy:

```

```

With this privilege, you can create a compartment for all the resources in your tutorial.

[Steps to Add the Policy](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

- In the navigation menu , select the Profile menu and then select User settings .
- In the left pane, click Groups .
- In a notepad, copy the Group Name that your username belongs.
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Policies .
- Click Create Policy .
- Fill in the following information:

- Name:`manage-compartments`
- Description:`Allow the group <the-group-your-username-belongs> to list, create, update, delete and recover compartments in the tenancy.`
- Compartment:`<your-tenancy>(root)`
- For Policy Builder , click Show manual editor .
- Paste in the following policy:

```

```

- Click Create .

Reference

The`compartments`resource-type in[Verbs + Resource-Type Combinations for IAM](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm#Identity)

[Create a Compartment](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

Create a compartment for the resources that you create in this tutorial.
- Log in to the Oracle Cloud Infrastructure Console .
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Compartments .
- Click Create Compartment .
- Fill in the following information:
- Name:`<your-compartment-name>`
- Description:`Compartment for <your-description>.`
- Parent Compartment:`<your-tenancy>(root)`
- Click Create Compartment .

Reference:[Create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To)

[Add Resource Policy](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

If your username is in the Administrators group, then skip this section. Otherwise, have your administrator add the following policy to your tenancy:

```

```

With this privilege, you can manage all the resources in your compartment , essentially giving you administrative rights in that compartment.

[Steps to Add the Policy](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

- Open the navigation menu and click Identity &amp; Security . Under Identity , click Policies .
- Select your compartment from the Compartment list.
- Click Create Policy .
- Fill in the following information:

- Name:`manage-<your-compartment-name>-resources`
- Description:`Allow users to list, create, update, and delete resources in <your-compartment-name>.`
- Compartment:`<your-tenancy>(root)`
- For Policy Builder , select the following choices:

- Policy use cases:`Compartment Management`
- Common policy templates:`Let compartment admins manage the compartment`
- Groups:`<the-group-your-username-belongs>`
- Location:`<your-tenancy>(root)`
- Click Create .

Reference

[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)

[Create a Cluster with 'Quick Create'](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

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
- Network Bandwidth: 1.0 (This value is calculated by OCPU count.)
- Max Total VNICs: 2 (This value is calculated by OCPU count.)
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

[Configure Cloud Shell to Access to Your Cluster](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

After you create a Kubernetes cluster, set up Cloud Shell to access the cluster.

- Sign in to the Oracle Cloud Infrastructure Console .
- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Kubernetes Clusters (OKE) .
- Click the link to`<your-cluster>`.

The information about your cluster is displayed.
- Click Access Cluster .
- Click Cloud Shell Access . Follow the steps in the dialog. The following steps are provided for your reference.
- Click Launch Cloud Shell . Alternatively, from the main menu, you can click the Cloud Shell icon ( ) and start a session.
- Check your`oci`CLI version and verify that Cloud Shell is working.

```

```

- Create kubeconfig file for your setup. Use the information from Access Your Cluster dialog.

```

```

You get a message that:
```

```

Note  
  
If the`config`file is not stored in its default location (`~/.kube/config`, you must export the`KUBECONFIG`environment variable to point to the location.

```

```

Note  
  
When working with more than one cluster, you specify a specific config file on the command line. Example:

```

```

- Test your cluster configuration with the following command.

List clusters:

```

```

With your cluster access setup, you are now ready to prepare your application for deployment.

## 3. Build your Docker Application

Next, set up the Flask framework on Cloud Shell. Then, create and run a Python application.

[Create a Local Application](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

Create your Flask application.

- Install Flask.

```

```

- Create a directory for your application.

```

```

- Change to the`python-hello-app`directory.

```

```

- Create a "Hello, World!" application.

Create the file:

```

```

In the file, input the following text:

```

```

- Save the file.

[Run the Local Application](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

Run your Flask application.

- Run the Python program.

```

```

Produces the following output:
```

```

- Move the app to the background.

- Hit Ctrl z .
- Enter the following command:`bg`
- Test the app using`curl`.

In Cloud Shell terminal, enter the following code:

```

```

Output:
```

```

- Stop the running application.

- When you are done testing, get the process ID for your application.

```

```

- Stop the process.

```

```

You have successfully created a local Python application with the Flask framework.

References:

For more information on Flask, see[Flask Documentation](https://flask.palletsprojects.com/en/stable/).

[Build a Docker Image](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

Next, create a Docker image for your Flask application.

- First, ensure you are in the`python-hello-app`directory.
- Create a file named`Dockerfile`:

Create the file:

```

```

In the file, input the following text and save the file:

```

```

- Build a Docker image:

```

```

You get a success message.
```

```

- Run the Docker image:

```

```

- Test the application using the`curl`command:

```

```

If you get`<h1>Hello World from Flask!</h1>`, then the Docker image is running. Now you can push the image to Container Registry.
- Stop the running application.

- When you are done testing, get the process ID for your application.

```

```

- Stop the process.

```

```

Congratulations! You have successfully created a Python Flask Docker image.

## 4. Deploy Your Docker Image

With your Python image created, now you can deploy it.

[Create a Docker Repository](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Container Registry .
- In the left navigation, select`<your-compartment-name>`.
- Click Create Repository .
- Create a private repository with your choice of repo name:

```

```

Example:`flask-apps/python-hello-app`
You are now ready to push your local image to Container Registry.
Note  
  
Before you can push a Docker image into a registry repository, the repository must exist in your compartment . If the repository does not exist, the Docker push command does not work correctly.
Note  
  
The slash in a repository name does not represent a hierarchical directory structure . The optional`<image-path-name>`helps to organize your repositories.

[Push Your Local Image](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

With your local Docker image created, push the image to the Container Registry.

Follow these steps.

- Open a terminal window.
- Log in to Container Registry:

```

```

You are prompted for your login name and password.
- Username:`<tenancy-namespace>/<user-name>`
- Password:`<auth-token>`
- List your local Docker images:

```

```

The Docker images on your system are displayed. Identify the image you created in the last section:`python-hello-app`
- Tag your local image with the URL for the registry plus the repo name , so you can push it to that repo.

```

```

- Replace`<repo-url>`with:
```

```

- Replace`<repo-name>`with:

`<image-folder-name>/<image-name>`from the Create a Docker Repository section.
- Here is an example after combining both:
```

```

In this example, the components are:
- Repo URL:`iad.ocir.io/my-namespace/`
- Repo name:`flask-apps/python-hello-app`
Note  
  
OCI Container Registry now supports creating a registry repo in any compartment rather than only in the root compartment (tenancy). To push the image to the repo you created, combine the registry URL with the exact repo name. OCI Container Registry matches the unique repo name and pushes your image.
- Check your Docker images to see if the image is copied .

```

```

- The tagged or the copied image has the same image ID as your local image.
- The copied image name is:
```

```

- Push the image to Container Registry.

```

```

Example:
```

```

- Open the navigation menu and click Developer Services . Under Containers &amp; Artifacts , click Container Registry .

Find your image in Container Registry after the push command is complete.

[Deploy the Image](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

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

- On your system, create a file called`app.yaml`with the following text:

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
  
In the`app.yaml`file, the code after the dashes adds a flexible load balancer.

[Test Your App](https://docs.oracle.com/en-us/iaas/Content/developer/flask-cloud-shell/01oci-flask-shell-summary.htm#)

After you deploy your app, it might take the load balancer a few seconds to load.

- Check if the load balancer is live:

```

```

Repeat the command until load balancer is assigned an IP address.
Note  
  
While waiting for the load balancer to deploy, you can check the status of your cluster with these commands:
- Get each pods status:`kubectl get pods`
- Get app status:`kubectl get deployment`
- Use the load balancer IP address to connect to your app in a browser:

```

```

The browser displays:`<h1>Hello World from Flask!</h1>`
- Undeploy your application from the cluster. (Optional) To remove your application run this command:

```

```

Output:
```

```

Your application is now removed from your cluster.

## What's Next

You have successfully created a Hello World Python application, deployed it to a Kubernetes cluster and made it accessible on the internet, using the Flask framework.

Check out these sites to explore more information about development with Oracle products:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
