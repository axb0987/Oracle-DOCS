# Using the Oracle Developer Tools for Visual Studio
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/visualstudio_using.htm
- Fetched: 2026-09-05 01:37 CDT

# Using the Oracle Developer Tools for Visual Studio

This topic shows how to use the Oracle Developer Tools for Visual Studio's Deployment wizard to deploy a web application to Oracle Cloud Infrastructure Kubernetes Engine.

This topic shows how to use the Oracle Developer Tools for Visual Studio's Deployment wizard to deploy a web application to Oracle Cloud Infrastructure Kubernetes Engine.
Note  
  
The Oracle Developer Tools for Visual Studio has additional functionality that is not covered in this document. For more information, see[Oracle Developer Tools for Visual Studio](https://www.oracle.com/database/technologies/developer-tools/visual-studio/).

## Prerequisites

This topic assumes a working knowledge of OCI Kubernetes Engine. The tutorials below will help understand some of the technologies and backend framework used by the wizard for deployment.
- [Pushing an Image to Oracle Cloud Infrastructure Registry](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/registry/index.html)
- [Creating a Cluster with Oracle Cloud Infrastructure Container Engine for Kubernetes](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-full/index.html)
- [Deploying an Application to OKE](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-and-registry/index.html)

## Overview

Using the Oracle Developer Tools for Visual Studio assumes you've already created a docker image for your application. This workflow generally looks like this:
- Build your web application.
- Build a docker image for your application locally. For more information, see the[Docker documentation](https://docs.docker.com/engine/reference/commandline/build/).
- Push the docker image of the web application to the Oracle Cloud Infrastructure Registry. For more information on pushing a docker image to OCIR, see[Push an Image to Oracle Cloud Infrastructure Registry](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/registry/index.html).
- Create a cluster in Oracle Cloud using Oracle Cloud Infrastructure Kubernetes Engine. See[Create a Cluster with Oracle Cloud Infrastructure Container Engine for Kubernetes](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-full/index.html)and download the resulting`kubeconfig`file.
- Create a named secret containing OCI credentials to be used for Kubernetes deployment. For more information, see[Pull an Image from Oracle Cloud Infrastructure Registry when Deploying a Load-Balanced Application to a Cluster.](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-and-registry/index.html#CreateaSecretfortheTutorial)

## Deploy an Application Using the Oracle Deployment Wizard

- From the Visual Studio Extensions menu, select Oracle Cloud App Deployment -&gt; Deploy to Oracle Cloud . The Oracle Deployment Wizard displays.
- Click Next .
- Select an[Authentication Profile](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm)(make sure that this profile matches the OCI CLI profile) and click Next .
- Select a deployment option:
- Redeploy using an existing deployment configuration: This deployment choice should be used for re-deployment of a web application when there are no deployment configuration changes. If the developer needs to make changes only to his/her web application and then re-deploy, they can do so using this option. This option allows developers to do quick deployment in a few clicks with no new information asked for.
- Redeploy with a different deployment configuration: This deployment choice should be used for re-deployment of a web application when there are deployment configuration changes. Scenarios where this is an appropriate choice include deploying on a different cluster, using a different Docker image, or a change in the Kubernetes configuration.
Note  
  
If selecting a different cluster during re-deployment, delete the Kubernetes resources for your previous deployment using the "kubectl delete" command.
- Create a new deployment: Use this option when deploying your web application for the first time using this wizard. The name for this deployment should be unique, must be no longer than 63 characters, must start and end with a lowercase letter or number, and may contain lowercase letters, numbers, and hyphens.
- 

On the Select A Cluster panel, select an existing Kubernetes cluster from any of the compartments in your tenancy (the wizard does not support creating a cluster, so you should create a cluster using the console first). Click Next .
- On the Specify Deployment Details panel, you can modify existing deployment details.
Note  
  
The deployment file created by the wizard can be modified in any editor and used for re-deployments using the wizard.
- 

Select a Docker image from the drop-down list.
- Select a Kubernetes Secret Name from the drop-down list.
- Click Next .
- Verify your deployment details, and then click Deploy .The window will actively update with the deployment status as it progresses. You can dismiss this dialog and check the deployment status later by selecting Oracle Cloud App Deployment -&gt; Check Deployment Status from the Visual Studio menu.

## Deleting A Deployment

The wizard doesn't support deleting a deployment using the Visual Studio IDE. To delete a deployment:
- Delete the deployment from the OKE cluster using the following command:`kubectl delete -f <path-to-deployment-file> --kubeconfig <path-to-kubeconfig-file>`If the deployment file is not present, you can use the following command:`kubectl delete deploy/<deployment_name> svc/<service_name>`
- 

Delete the folder in`~/.oci/visualstudiowebapps/<your-application-deployment-name>`
