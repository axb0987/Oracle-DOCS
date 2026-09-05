# Starting Docker
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsstartdocker.htm
- Fetched: 2026-09-05 02:09 CDT

# Starting Docker

Find out how to start Docker for use with OCI Functions.

Before using OCI Functions, Docker must be running in your development environment. If it is not running, you must start Docker before proceeding.

If you are using Cloud Shell as your development environment, Docker has already been started for you.

The instructions in this topic assume:
- you are not using Cloud Shell as your development environment
- you are using Linux
- you have already completed the steps in[Generating an Auth Token to Enable Login to Oracle Cloud Infrastructure Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsgenerateauthtokens.htm)

To verify that Docker is running:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, launch the standard hello-world Docker image as a container to confirm that Docker is running by entering:

```

```

- 

Do one of the following, depending on the message you see:
- 

If you see an error message indicating that Docker is not running, you have to start the Docker daemon before proceeding. See the[Docker documentation](https://docs.docker.com/)for information about starting Docker on your platform.
- If you see an error message indicating that the network timed out while trying to connect and advising you to check your internet connection or whether you are behind a proxy, your development environment might be behind a corporate proxy server or firewall. In which case, you will probably need to set the http_proxy, https_proxy, and no_proxy environment variables. Ask your network administrator for advice.
- 

If you see a message like the one shown below, Docker is already running and you can proceed:
```

```

When you have completed the steps in this topic, go on to[Logging in to Oracle Cloud Infrastructure Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionslogintoocir.htm)
