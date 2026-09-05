# Pushing Images Using the Docker CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrypushingimagesusingthedockercli.htm
- Fetched: 2026-09-05 02:54 CDT

# Pushing Images Using the Docker CLI

Find out how to push images to Container Registry using the Docker CLI.

You use the Docker CLI to push images to Oracle Cloud Infrastructure Registry (also known as Container Registry).

To push an image, you first use the`docker tag`command to create a copy of the local source image as a new image (the new image is actually just a reference to the existing source image). As a name for the new image, you specify the fully qualified path to the target location in Container Registry where you want to push the image, including the name of a repository.

For example, assume you have a local image named`acme-web-app:latest`(the image name comprising the repository name of`acme-web-app`, and the image tag of`latest`). Let's say you want to push this image to Container Registry into a repository called`project01/acme-web-app`with a version identifier of`v2.0.test`, in the Ashburn region of the acme-dev tenancy. When you use the`docker tag`command, you'd name the new image with the fully qualified path to its destination, in the format`<registry-domain>/<tenancy-namespace>/<repo-name>:<version>`. So in this case, you'd name the new image`ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:v2.0.test`. Subsequently, when you use the`docker push`command, the image's name ensures it is pushed to the correct destination.

Your permissions control the images you can push to Container Registry (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can push images to repositories you've created (see[Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm)). You can also push images to repositories that the groups to which you belong have been granted access by appropriate identity policies. If you belong to the Administrators group, you can push images to any repository in the tenancy.

Note that the instructions in this topic assume that the repository to which you want to push images already exists. That will usually be the case, but need not always be so (see[Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm)).
Note  
  

Container Registry is an[Open Container Initiative](https://opencontainers.org/)-compliant registry. As a result, you can store any artifacts that conform to Open Container Initiative specifications, such as Docker images, manifest lists (sometimes known as multi-architecture images), and Helm charts. The instructions in this topic assume you are storing Docker images and using the Docker CLI.

To push images to Container Registry using the Docker CLI:
- 

If you already have an auth token, go to the next step. Otherwise:
- 

In the top-right corner of the Console, open the Profile menu , and then select User settings (or My Profile or your account name) to view the details.
- 

On the Tokens and keys tab, go to the Auth Tokens section and select Generate token .
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

If your tenancy is federated with Oracle Identity Cloud Service, use the format`<tenancy-namespace>/<domain-name>/<username>`. For federated users, the`<domain-name>/<username>`is displayed in the Profile menu in the Console. For example, if the namespace string of your tenancy is`ansh81vru1zp`, and your tenancy is federated with Oracle Identity Cloud Service, and your username is`jdoe@acme.com`, then enter`ansh81vru1zp/oracleidentitycloudservice/jdoe@acme.com`
- 

When prompted for a password, enter the auth token you copied earlier.
- 

Find the image on the client machine that you want to push:
- 

In a terminal window on your client machine, enter`docker images`to list the available images.

For example:

```

```

- 

Find the local image on the client machine that you want to push to Container Registry.

In the output of the`docker images`command, look for the specific image that you want to push. You'll need to uniquely identify this image later, in one of the following ways:
- 

Using its id.
- 

Using its image name (its repository name and image tag separated by a colon).

For example, on the client machine you might have an acme-web-app image. In the output of the`docker images`command, look for the specific acme-web-app image that you want to push. You can uniquely identify that particular image in one of the following ways:
- 

Using its id (for example,`8e0506e14874`).
- 

Using its image name (its repository name and image tag separated by a colon, for example`acme-web-app:latest`).
- 

Use the`docker tag`command to create a copy of the original image as a new image (the new image is actually just a reference to the existing original image). As a name (or tag) for the new image, you specify the fully qualified path to the target location in Container Registry where you want to push the image, by entering:

```

```

where:
- 

`<image-identifier>`uniquely identifies the original image, either using the image's id (for example,`8e0506e14874`), or the image's name (its original repository name and image tag separated by a colon, for example`acme-web-app:latest`).
- 

`<target-tag>`is the fully qualified path to the target location in Container Registry where you want to push the image, in the format`<registry-domain>/<tenancy-namespace>/<repo-name>:<version>`where:
- 

`<registry-domain>`includes the region key or region identifier for the Container Registry region you're using.. For example,`ocir.us-ashburn-1.oci.oraclecloud.com`. See[Terminology Summary](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registryconcepts.htm#Terminology_Summary).
- 

`<tenancy-namespace>`is the auto-generated Object storage namespace string of the tenancy that owns the repository to which you want to push the image (as shown on the Tenancy General Information page). For example, the namespace of the acme-dev tenancy might be`ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example,`acme-dev`). Note also that your user must have access to the tenancy.
- 

`<repo-name>`is the name of the target repository to which you want to push the image (for example,`project01/acme-web-app`). Note that you'll usually specify a repository that already exists, but that need not always be the case (see[Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm)).
- 

`<version>`is a version identifier you want to give the image in Container Registry (for example,`v2.0.test`).

For example, combining the previous examples, you might enter:

```

```

- 

Confirm that the Docker image has been correctly tagged on the client machine by entering`docker images`and verifying that the list of images includes an image with the tag you specified.

For example:

```

```

- 

Push the Docker image from the client machine to Container Registry by entering:

```

```

where`<target-tag>`is in the format`<registry-domain>/<tenancy-namespace>/<repo-name>:<version>`where:
- 

`<registry-domain>`includes the region key or region identifier for the Container Registry region you're using. For example,`ocir.us-ashburn-1.oci.oraclecloud.com`. See[Terminology Summary](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registryconcepts.htm#Terminology_Summary).
- 

`<tenancy-namespace>`is the auto-generated Object storage namespace string of the tenancy that owns the repository to which you want to push the image (as shown on the Tenancy General Information page). For example, the namespace of the acme-dev tenancy might be`ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example,`acme-dev`). Note also that your user must have access to the tenancy.
- 

`<repo-name>`is the name of the target repository to which you want to push the image (for example,`project01/acme-web-app`). Note that you'll usually specify a repository that already exists, but that need not always be the case (see[Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm)).
- 

`<version>`is the version identifier you want to give the image in Container Registry (for example,`v2.0.test`).

For example:

```

```
