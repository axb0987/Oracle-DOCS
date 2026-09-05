# Pulling Images Using the Docker CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrypullingimagesusingthedockercli.htm
- Fetched: 2026-09-05 02:54 CDT

# Pulling Images Using the Docker CLI

Find out how to pull images from Container Registry using the Docker CLI.

You use the Docker CLI to pull images from Oracle Cloud Infrastructure Registry (also known as Container Registry).

Your permissions control the images you can pull from Container Registry (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can pull images from repositories you've created, from public repositories, and from repositories that the groups to which you belong have been granted access by identity policies. If you belong to the Administrators group, you can pull images from any repository in the tenancy.
Note  
  

Container Registry is an[Open Container Initiative](https://opencontainers.org/)-compliant registry. As a result, you can store any artifacts that conform to Open Container Initiative specifications, such as Docker images, manifest lists (sometimes known as multi-architecture images), and Helm charts. The instructions in this topic assume you are storing Docker images and using the Docker CLI.

To pull images from Container Registry using the Docker CLI:
- 

If you already have an auth token, go to the next step. Otherwise:
- 

In the top-right corner of the Console, open the Profile menu , and then select User settings (or My Profile or your account name) to view the details.
- 

On the Tokens and keys tab, go to the Auth tokens section and select Generate token .
- 

Enter a friendly description for the auth token. Avoid entering confidential information.
- 

Select Generate token . The new auth token is displayed.
- 

Copy the auth token immediately to a secure location from where you can retrieve it later, because you won't see the auth token again in the Console.
- 

Close the Generate token dialog.
- 

In a terminal window on the client machine running Docker, log in to Container Registry by entering`docker login <registry-domain>`, where`<registry-domain>`includes a region key or region identifier for the Container Registry region you're using. For example,`docker login ocir.us-ashburn-1.oci.oraclecloud.com`. See[Availability by Region](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registryprerequisites.htm#regional-availability).
- 

When prompted for a username, enter your username in the format`<tenancy-namespace>/<username>`, where`<tenancy-namespace>`is the auto-generated Object storage namespace string of your tenancy (as shown on the Tenancy General Information page). For example,`ansh81vru1zp/jdoe@acme.com`.

If your tenancy is federated with Oracle Identity Cloud Service, use the format`<tenancy-namespace>/<domain-name>/<username>`. For federated users, the`<domain-name>/<username>`is displayed in the Profile menu in the Console. For example, if the namespace string of your tenancy is`ansh81vru1zp`, and your tenancy is federated with Oracle Identity Cloud Service, and your username is`jdoe@acme.com`, then enter`ansh81vru1zp/oracleidentitycloudservice/jdoe@acme.com`.
- 

When prompted for a password, enter the auth token you copied earlier.
- 

Pull the Docker image from Container Registry to the client machine by entering:

```

```

where:
- 

`<registry-domain>`includes the region key or region identifier for the Container Registry region you're using. For example,`ocir.us-ashburn-1.oci.oraclecloud.com`. See[Terminology Summary](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registryconcepts.htm#Terminology_Summary).
- 

`<tenancy-namespace>`is the auto-generated Object storage namespace string of the tenancy that owns the repository from which you want to pull the image (as shown on the Tenancy General Information page). For example, the namespace of the acme-dev tenancy might be`ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example,`acme-dev`). Note also that your user must have access to the tenancy.
- 

`<repo-name>`is the name of a repository from which you want to pull the image (for example,`project01/acme-web-app`). Note that your user must have access to the repository (see[Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registryconcepts.htm#About_Repositories)).
- 

`<version>`is the version identifier of the image that you want to pull from Container Registry (for example,`v2.0.test`).

For example:

```

```

Note that if you don't specify a`<version>`in the`docker pull`command, Docker pulls the image that has the`latest`version identifier.
- 

Confirm that the image has been pulled from Container Registry by entering`docker images`and verifying that the list of images on the client machine now includes the image you just pulled.

For example:

```

```
