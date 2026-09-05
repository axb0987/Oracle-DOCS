# Using a Template to Create a Function with Code Editor
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfromtemplateusingcodeeditor.htm
- Fetched: 2026-09-05 02:08 CDT

# Using a Template to Create a Function with Code Editor

Find out how to use Code Editor to create a new function in OCI Functions based on a template function.

You can use Code Editor to create a new function in OCI Functions based on a template function. Oracle provides a number of helloworld template functions written in different languages. Having created a template function func.yaml and source code files in an unversioned directory, you use Code Editor to convert the directory into a local Git repository that you can then push to a remote Git repository. With the files in the remote Git repository, you can then use Code Editor to deploy the function to OCI Functions, and then to invoke the function.

When using Code Editor to create and update functions, note the following:
- The remote Git repository must contain a valid func.yaml file at the top level.
- The name of a function you create using Code Editor must match the function name specified in the func.yaml file in the remote code repository. If the names are different, you will be unable to invoke the function.
- When you deploy a function to OCI Functions, you are fetching the latest commit from the remote Git repository. Uncommitted changes, and commits in the local repository, are ignored. Therefore, before you can deploy a new or updated function to OCI Functions, you must always commit new and modified files to the local Git repository, and then push the changes to the remote Git repository.

This topic explains how to use Code Editor to:
- create a new function from a template function
- convert the unversioned directory containing the function's func.yaml and source code files into a local Git repository that you can then push to a remote Git repository
- deploy the function to OCI Functions
- invoke the function
- optionally, update the function, re-deploy it, and invoke it again

Before you start:
- You must have completed the steps in the[Functions QuickStart on Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm).
- To follow the steps in this topic, you must have access to an empty remote Git repository (for example, in GitHub), or be able to create such a repository.
- For convenience and simplicity, the examples in this topic assume you create a function from a Java template. If you create a function from a different template, some of the instructions do not apply.

For more information about Code Editor features and functionality, see[Code Editor](https://docs.oracle.com/iaas/Content/API/Concepts/code_editor_intro.htm).

## Creating a Helloworld Function From a Template Using Code Editor

To use Code Editor to create a new function in OCI Functions based on a template function:
- Confirm that you have completed the steps in the[Functions QuickStart on Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm)to:
- [Set up your tenancy](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#functionsquickstart_cloudshell_topic_setup_your_tenancy)with groups and users, create a compartment in which to create OCI Functions resources, create a VCN and subnets, and create an IAM policy.
- [Set up your Cloud Shell dev environment](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#functionsquickstartcloudshell_topic_setup_CloudShell_dev_env)with the Fn Project CLI context, obtain an auth token, and log in to the Docker registry specified for the Fn Project CLI context.
- Sign in to the Console as a functions developer.
- 

Use the Console to create a new application in OCI Functions:
- Open the navigation menu and select Developer Services . Under Functions , select Applications .
- Select the region you intend to use for OCI Functions.

We recommend that you use the same region as the Docker registry specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).
- 

Select the compartment specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).

The Applications page shows the applications already defined in the compartment.
- 

Select Create Application and specify:
- A name for the new application. For example,`helloworld-java-app`
- 

The VCN and subnet (or subnets, up to a maximum of three) in which to run the function. We recommend that subnets are in the same region as the Docker registry specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).

For more information about the other application creation options, see[Creating an Application](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingapps-task.htm).
- Select Create to create the application.
- 

Start Code Editor in either of the following ways:
- On the Applications list page, select the application in which you want to create the function. On the application details page, select Functions . On the Functions tab, select Create in code editor . This method opens Code Editor at the application you just created.
- Select the Code Editor option from the Developer Tools button in the Console's toolbar.
- Create a new function from a template:
- In the Code Editor Oracle Cloud Infrastructure panel, navigate to the application you just created in the compartment specified in the Fn Project CLI context. For example,`helloworld-java-app`.
- With the application name highlighted, select Create Function... from the right mouse button menu.
- Select the Create from a template creation method in the entry field in the Code Editor menu bar.
- Select a language from the language list and press Enter. For example, select Java .
- Enter a name for the new helloworld function in the entry field in the Code Editor menu bar and press Enter. For example,`helloworld-func-java`.
- Select OK to acknowledge the dialog informing you that changes have to be committed and pushed to a remote branch before the function can be deployed.

A directory named after the function is created in the`/home/<username>/oci-ide-plugins/faas-artifacts/<app-ocid>/`directory. For example, in`/home/jdoe/oci-ide-plugins/faas-artifacts/ocid1.fnapp.oc1.iad.aaaaaa______76nf/helloworld-func-java`,

If you have based the new function on the Java template function, the directory contains:
- func.yaml
- pom.xml
- a /src directory
- Save the function in a local Git repository:
- Open a Code Editor terminal window by selecting New Terminal from the Terminal window in the Code Editor menu bar.
- In the Code Editor terminal window, change directory to the newly created directory containing the func.yaml file and the function source files by entering:
```

```

For example:
```

```

- Convert the unversioned directory (for example, named`helloworld-func-java`) into a local Git repository by entering:
```

```

- Add the files in the directory to the staging area by entering:
```

```

- Store the contents of the staging area in the local Git repository by entering:
```

```

- When prompted, enter a commit message:
- Press the i key on your keyboard to insert text.
- Enter a commit message. For example:
```

```

- Press the Esc key, then type : w q and then press Enter.
- Create a new remote Git repository. For example, in GitHub as`https://github.com/jdoe/template-java-helloworld-repo`.
- Push the function to the remote Git repository:
- In the Code Editor terminal window, in the directory containing the func.yaml file and the function source files,connect the local Git repository to the remote Git repository you just created by entering:
```

```

For example:
```

```

- Create a new branch named main in the local Git repository by entering:
```

```

- Push files to the`main`branch in the remote Git repository by entering:
```

```

- If prompted, enter the Git username and password for the remote Git repository.

In the case of GitHub, note that the password is the GitHub Personal Access Token.
- Deploy the function to OCI Functions:
- 

In the Code Editor terminal window, in the directory containing the func.yaml file and the function source files, log in to the Docker registry specified in the Fn Project CLI context. Assuming the Docker registry is Oracle Cloud Infrastructure Registry, use the following command:
```

```

For example:
```

```

- When prompted for a password, enter your OCI auth token.
- In the Code Editor terminal window, deploy the function to OCI Functions by running:
```

```

For example:
```

```

- Invoke the function you've just deployed:
- In the Code Editor terminal window, in the directory containing the func.yaml file and the function source files, invoke the function by running:
```

```

For example:
```

```

If a message is returned showing the function is not found, one likely cause is a mismatch between the name of the function you created in Code Editor, and the name of the function specified in the func.yaml. Repeat the previous steps to create a function in Code Editor that has the same name as specified in the func.yaml file in the remote Git repository.

If you have based the new function on the Java template function, the following message is displayed:
```

```

- 

(Optional) If you have based the new function on a template Java function named`helloworld-func-java`in the previous steps, this optional step describes how to change the text of the message that is displayed when the function is invoked. You update the message text in the local Git repository, push the update to the remote Git repository, and then deploy and invoke the function.
- In the Code Editor Oracle Cloud Infrastructure panel, under the`helloworld-func-java`function that you just created:
- Cick on the`/src/main/java/com/example/fn/HelloFunction.java`file and change the line:
```

```

to read:
```

```

- Select on the`/test/java/com/example/fn/HelloFunctionTest.java`file and change the line:
```

```

to read:
```

```

- In the Code Editor navigator, select the Source Control panel, select the More Actions button, and select Commit from the Commit menu.
- When prompted to stage changes, select Yes .
- Enter a commit message (for example,`Changes-Hello-to-Hi`) and press Enter .
- Select the More Actions button, and select Push from the Pull, Push menu
- If prompted, enter the Git username and password for the remote Git repository.

In the case of GitHub, note that the password is the GitHub Personal Access Token.
- If a dialog is displayed with the message "Would you like Code Editor to periodically run 'git fetch'?", select Ask Me Later .
- 

In the Code Editor terminal window, in the directory containing the func.yaml file and the function source files, deploy the function to OCI Functions by entering:
```

```

For example:
```

```

- 

In the Code Editor terminal window, invoke the function by entering:
```

```

For example:
```

```

The following message is displayed:
```

```
