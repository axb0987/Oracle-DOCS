# Freeing Up Cloud Shell Storage By Removing Unused Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscloudshellcleanup.htm
- Fetched: 2026-09-05 02:07 CDT

# Freeing Up Cloud Shell Storage By Removing Unused Images

Find out about Cloud Shell storage limitations and how to safely free up space by removing unused images when using OCI Functions.

Cloud Shell allocates 5GB for each user’s home directory. This limit cannot be increased or mounted to external storage. For more information, see[Cloud Shell Limitations](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm#Cloud_Shell_Limitations).

You are responsible for keeping your Cloud Shell home directory below the 5GB limit. For example, by regularly removing unused images.
Caution  
  
Removing images can affect running applications or your environment’s state. Only proceed if you are certain the data can be deleted.

Always use the appropriate Docker or Podman command (such as`docker rmi`or`podman rmi`) to safely remove unused images.

Do not attempt to free up space by manually deleting directories such as`~/.local`. These directories might contain application data and configuration files for tools you use. In particular, for Podman users, the`~/.local`directory is critical because it contains Podman-managed image storage and configuration data. Deleting the`~/.local`directory might corrupt the Podman installation or cause unexpected issues.

Follow these steps to safely free up space by removing unused images:
- Verify available storage by entering:
```

```

- Identify which images are consuming space, by entering:
- Docker:`docker images`
- Podman:`podman images`

Images are listed, including their image id, and repository/tag.
- (recommended) Before deleting images, make sure they are not in use by containers. List all containers (including stopped containers) and the images they are using, by entering:
- Docker:`docker ps -a`
- Podman:`podman ps -a`

Note which images are in use by checking the`IMAGE`column in the output. Any image appearing here is in use by at least one container (even if stopped).
- Delete unused images, by specifying the image id or repository/tag.
- To delete images by specifying the image id, enter:
- Docker:`docker rmi <image-id>`
- Podman:`podman rmi <image-id>`
- To delete images by specifying the repository/tag, enter:
- Docker:`docker rmi <repository>:<tag>`
- Podman:`podman rmi <repository>:<tag>`
- (optional) To attempt to delete all images not currently used by any containers, enter:
- Docker:`docker rmi $(docker images -q)`
- Podman:`podman rmi $(podman images -q)`

This command attempts to remove every image. However, images that are still used by containers (including stopped containers) cause an error and are not deleted.
- (optional) If you are certain that you no longer need an image (nor any of the containers using it), you can force delete the image by entering:
- Docker:`docker rmi -f <image_id>`
- Podman:`podman rmi -f <image_id>`
Caution  
  
Only force delete an image when you are certain that you no longer need any container using it.
- Verify available storage again by entering:
```

```
