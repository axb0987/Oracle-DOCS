# Add Component Package to a Skill
- Source: https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#dcoc-content-body)

# Add Component Package to a Skill

You add a component package to a skill by creating a component service.

For component packages that you host on an external server, Oracle Cloud Infrastructure Functions, or on Oracle Mobile Hub, a component service is an active connection from the skill to host server. Alternatively, you can upload the component package and host it from your Oracle Digital Assistant instance. This is referred to as an embedded component service.

A component service has two functions:
- 

It queries the component to get the package metadata, including the names of the components, their properties, and allowed actions for each one. After a service is added to the skill, you can see this information in the Components tab, which you access by clicking Components in the left navbar. You can reference this page to get the component names, properties, and actions, which you will need to use the components in your dialog flow.
- 

It allows the skill to invoke the components.

The JSON payload of the call made by the Dialog Engine to the components includes input parameters, variable values, user-level context, and the user’s message text. The component returns the results by changing the values of existing variables or adding new ones (or both). The Dialog Engine parses the returned payload and proceeds.

To add a custom component package to a skill, go to the skill's Components tab and click Add Service , which opens a dialog for configuring the service.

How you configure the service depends on where you are hosting the component package. These topics provide instructions for each type:
- 

[Add Embedded Component Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-C169BC34-7401-4E73-8F33-C8B84E039A96)
- 

[Add Oracle Function Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-EA235282-37B8-4493-8168-A6830EB21EA6)
- 

[Add External Component Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-D7A0D052-810C-4DE3-B75A-BE93D2CA6ACE)
- 

[Add Mobile Hub Component Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-D851A943-CDFC-47A3-B382-43AF7B28834B)

After you create the service, you can invoke the custom components from your dialog flow as described in[Custom Components](https://docs.oracle.com/iaas/digital-assistant/doc/components.html#GUID-D4DB30EC-D089-4809-A845-31FAAE1794AA).

When you upload a package to the embedded container, Digital Assistant verifies that the package is valid, and can reject the package for these reasons:
- 

There are JavaScript errors.
- 

The package doesn't contain all the node module dependencies.
- 

A component name has more than 100 characters, begins with`System.`, or contains other than alphanumeric characters and underscores, then the service creation fails.
- 

Your instance already has the maximum number of embedded component services.
- 

The TGZ file is too large. This typically happens when the`.npmignore`file doesn't contain a`*.tgz`entry and therefore, every time you pack the files, a nested copy of the existing TGZ is added.

See[Add Embedded Component Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-C169BC34-7401-4E73-8F33-C8B84E039A96)for more information about these verification checks.

### Add Embedded Component Service

If you want to host the custom component package from your Oracle Digital Assistant instance, complete these steps:
- 

[Prepare the Package for an Embedded Container Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-E5DB88FF-083E-4F58-9781-0E6F43756D7D).
- 

[Upload Package to Create an Embedded Component Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-1C435C7C-BCBD-4EDD-9ADA-2D503C28842F).

#### Prepare the Package for an Embedded Container Service

If you want to host the custom component package from Oracle Digital Assistant as an embedded component service, you must first pack the custom components into a TGZ file. Then, when you create the embedded component service, you upload this file.

This TGZ file, which you package using`bots-node-sdk pack`, must contain the assets and structure described in[Implement Custom Components](https://docs.oracle.com/iaas/digital-assistant/doc/implement-custom-components.html#GUID-268C35B3-57B3-4E52-BEEC-1DEE7CA0ACFB). It also must contain all the node modules that it depends on (the`bots-node-sdk pack`does that for you).
Note  
  
There's a limit to how many embedded custom component services an instance can have. If you don't know the limit, ask your service administrator to get the`embedded-custom-component-service-count`for you as described in[View Service Limits in the Infrastructure Console](https://docs.oracle.com/iaas/digital-assistant/doc/order-service-provision-instance.html#GUID-F2F7161E-AD06-48E3-A227-C9911020F75B). If you try to add a component service after you meet that limit, then the service creation fails.

To prepare a package for uploading to the embedded container service:
- 

Ensure that you have the latest version of the Bots Node.js command line tools.

The embedded container requires that the TGZ file includes all`dependencies`. Earlier versions did not bundle the`dependencies`into the file. Now, the command that you'll use to create the TGZ file ensures that your`package.json`file contains a`bundledDependencies`node that lists all the dependent modules that need to be included in the TGZ file.
- 

In the directory that contains the`main.js`file, run the following command for each of the modules that your package depends on. You don't need to do this for`devDependencies`, such as the Bots Node SDK.

This command adds the module to the`node_modules`folder and adds it as a dependency in`package.json`.
```

```

If your`package.json`already names all the dependencies, then you can run`npm install`instead.
- 

Ensure that the top-level folder contains an`.npmignore`file that has a`*.tgz`entry. For example:
```

```

Otherwise, when you pack the files into a TGZ file, you include the TGZ file that already exists in the top-level folder, and your TGZ file will double in size. After you pack the files a few times, the TGZ file will be to large to upload into the container.
- 

Run this command:
```

```

This command validates the component package, updates it to include`devDependencies`if necessary, and then creates a TGZ file, which you'll upload when you create an embedded component service from the skill’s Components tab. Note that the files you've listed as`dependencies`are included as`bundledDependencies`, with the exception of the Bots Node SDK and Express, which are`devDependencies`.

Your package should be compatible with Node 14.17.0.

For more information about the`pack`command, see[`https://github.com/oracle/bots-node-sdk/blob/master/bin/CLI.md`](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/digital-assistant/use-chatbot&id=github-node-cli).

#### Upload Package to Create an Embedded Component Service

After you pack a custom component package into a TGZ file, you can upload it to create an embedded component service from the skill's Components tab.

To learn how to create the TGZ file, see[Prepare the Package for an Embedded Container Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-E5DB88FF-083E-4F58-9781-0E6F43756D7D).
Note  
  
When you upload the package to the embedded component service, it's deployed to Oracle Functions Service. If your instance is provisioned on the Oracle Cloud Platform (as all version 19.4.1 instances are), then the service is instead deployed within the Digital Assistant instance.

To create the embedded component service:
- 

From the skill, click Components .
- 

Click .
- 

Select Embedded Container .
- 

Click Upload a component package file and point to the TGZ file to upload, or drag the file to the Package File box.
- 

(Optional) If you want to send custom component`context.logger()`statements to the service's log, then switch Enable Component Logging to On. This switch is available only in instances of Oracle Digital Assistant that were provisioned on Oracle Cloud Infrastructure (sometimes referred to as the Generation 2 cloud infrastructure).

You can see the log from the Components tab by clicking Diagnostics &gt; View Logs .
Note  
  
The skill keeps a log entry for two days. When you delete an embedded custom component service, the skill's log entries for that service are deleted.
- 

Click Create .

Digital Assistant uploads the TGZ file and creates the embedded component service. During the upload, Digital Assistant verifies that the package is valid, and can reject the package for the reasons that are described later in this section.

After you upload the TGZ file, the custom component service is built and its components are deployed. If the Components page displays an awaiting deployment message after you upload the TGZ file, it means that the service has been created, but is not yet available. When the service becomes available, the deployment metadata displays in place of the awaiting deployment message.
- 

Ensure that Service Enabled is switched to On.

During the upload, Digital Assistant might reject the package. Here are reasons for rejection and ways to resolve the issues.
- 

JavaScript contains syntax errors: If a component's JavaScript has syntax errors, then that component is not added to the container, which results in this error message:
```

```

View the component files in an editor that detects syntax errors. Also, try hosting the package on a local server that sends error messages to a console log.

Another reason for this message might be that the package doesn't contain all the node module dependencies. See the next item in this list.
- 

Missing node modules: If the package doesn't contain all the node module dependencies, then you'll get the same error message as above:
```

```

To learn how to include node module dependencies, see[Prepare the Package for an Embedded Container Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#GUID-E5DB88FF-083E-4F58-9781-0E6F43756D7D).
- 

Component name is too long: If a component name has more than 100 characters, begins with`System.`, or contains other than alphanumeric characters and underscores, then the service creation fails.

Change the name in the component's JavaScript, repackage, and upload again.
- 

Exceeded component service limit: If your instance already has the maximum number of embedded custom component services, then the service creation fails. Ask your service administrator for the`embedded-custom-component-service-count`limit as described in[View Service Limits in the Infrastructure Console](https://docs.oracle.com/iaas/digital-assistant/doc/order-service-provision-instance.html#GUID-F2F7161E-AD06-48E3-A227-C9911020F75B).

If you need to raise the limit, you can request an increase. See[Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#three).
- 

TGZ file is too large: This typically happens when the`.npmignore`file doesn't contain a`*.tgz`entry and therefore, every time you pack the files, a nested copy of the existing TGZ is added.

When the top-level folder contains an`.npmignore`file with`*.tgz`, the previous version of the TGZ file isn't included when you update the package.

If you want to send custom component`context.logger()`statements to the service's log, then switch Enable Component Logging to On. This switch is available only in instances of Oracle Digital Assistant that were provisioned on Oracle Cloud Infrastructure (sometimes referred to as the Generation 2 cloud infrastructure).

When Enable Component Logging is switched to On, you can click the Diagnostics button for the service to access view logs and crash reports to diagnose the problem.
- Select View Logs to view messages that the custom component sends to`context.logger()`. This feature is available only in instances of Oracle Digital Assistant that were provisioned on Oracle Cloud Infrastructure (sometimes referred to as the Generation 2 cloud infrastructure). The Enable Component Logging switch must be On for the log to contain these messages.
- Select View Crash Report to view details about what may have caused the container to crash.

After you create the service, you can invoke the custom components from your dialog flow as described in[Custom Components](https://docs.oracle.com/iaas/digital-assistant/doc/components.html#GUID-D4DB30EC-D089-4809-A845-31FAAE1794AA).

### Add Oracle Function Service

You can deploy your custom components to Oracle Cloud Infrastructure Functions and add them to a skill as an Oracle Function service.

To add an Oracle Function service:
- 

You'll need to know the function's URL. A user with function development privileges can get the URL from the Integration Console for you.
- Sign in to the Integration Console.
- 

Click on the top left to open the navigation menu, click Developer Services &gt; Functions , and then select the compartment that's been set up for function development.
- 

Click the application.
- 

In the Functions section, click the More icon for your function and click Copy Invoke Endpoint . Skill developers need this value to add the custom component package as a component service in a skill.
- 

A skill developer adds the component service to a skill in Oracle Digital Assistant. Sign into Oracle Digital Assistant, open the skill and click Components .
- 

Click .
- 

Provide a name and description for the service.
- 

Select Oracle Function .
- 

In the URL text box, enter the invoke endpoint URL that you copied from the Developer Services &gt; Functions page in the Infrastructure Console while completing the steps in[Set Up Your User Account for Oracle Functions](https://docs.oracle.com/iaas/digital-assistant/doc/deploy-component-package-service.html#GUID-B46CB272-DEB9-464A-B8A4-70826A50EE74).
- 

Click Create .

If you get a "Can't Create the Service" error, go to Developer Services &gt; Functions in the Infrastructure Console, select the compartment, click the application, and click Logs in the Resources menu. Then enable the log for the function, retry the deployment, and check the logs (click the log name to see the log). To learn more about logs, see[Storing and Viewing Function Logs](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm)in Oracle Cloud Infrastructure Documentation .

If you see an error like this, it's because the folder doesn't have the right permissions. On your local machine, use`chmod 775`to change the folder's permissions, then redeploy:
```

```

If you see an error like this then, on your local machine, delete`node_modules`, run`npm install`and redeploy.
```

```

- 

Ensure that Service Enabled is switched to On.

After you create the service, you can invoke the custom components from your dialog flow as described in[Custom Components](https://docs.oracle.com/iaas/digital-assistant/doc/components.html#GUID-D4DB30EC-D089-4809-A845-31FAAE1794AA).

### Add External Component Service

You can host your custom components on your own Node.js server and add them to a skill as an external component service.

Tip: You can use the external service option during development, as described in[Run the Component Service in a Development Environment](https://docs.oracle.com/iaas/digital-assistant/doc/implement-custom-components.html#GUID-71C6D280-3BE8-4D74-BD28-C33E8475C662).

To add an external component service:
- 

From the skill, click Components .
- 

Click .
- 

Select External .
- 

In the Metadata URL text box, enter the The URL that points to the GET endpoint that returns the list of components.
- 

Enter the service's user name and password.
- 

Click Create .
- 

Ensure that Service Enabled is switched to On.

After you create the service, you can invoke the custom components from your dialog flow as described in[Custom Components](https://docs.oracle.com/iaas/digital-assistant/doc/components.html#GUID-D4DB30EC-D089-4809-A845-31FAAE1794AA).

### Add Mobile Hub Component Service

You can host your custom components from Oracle Mobile Hub, and add them to a skill as an Oracle Mobile Cloud component service. Custom components that are hosted on Mobile Hub can integrate with remote services using connectors that are controlled by a Mobile Hub backend and they have access to the Mobile Hub platform APIs.

Because the backend that hosts the custom code handles the authentication for the custom components, you need to refer to the backend’s Settings page to get the information that you need to complete the configuration.

To add a component service for the Mobile Hub backend:
- 

From the skill, click Components .
- 

Click .
- 

Select Oracle Mobile Cloud .
- 

Enter the unique identifier assigned to the Mobile Hub backend in the Backend ID field. This ID is passed in the REST header of every call from the skill.
- 

In the MetadataURL field, enter the`/components`endpoint from the custom code API. For example,`http://<server>:<port>/mobile/custom/ccPackage/components`.
- 

Choose Use Anonymous Access if the service allows anonymous login. If you choose this option, enter the anonymous key, which is a unique string that allows your app to access anonymous APIs without sending an encoded user name and password. The anonymous key is passed in their place. You can find the anonymous key on the backend's Settings page in Mobile Hub. (You may need to click Show .)

If the component service requires a login (meaning no anonymous access), then enter the user name and password.
- 

If the service requires specific parameters, click Add HTTP Header and then define the key-value pairs for the headers.
- 

Click Create .
- 

Ensure that Service Enabled is switched to On.

After you create the service, you can invoke the custom components from your dialog flow as described in[Custom Components](https://docs.oracle.com/iaas/digital-assistant/doc/components.html#GUID-D4DB30EC-D089-4809-A845-31FAAE1794AA).

- [Add Component Package to a Skill](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#DACUA-GUID-A93D7DAB-DCCE-42CD-8E6B-A06FB9BEE90D)
- [Add Embedded Component Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#DACUA-GUID-C169BC34-7401-4E73-8F33-C8B84E039A96)
- [Add Oracle Function Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#DACUA-GUID-EA235282-37B8-4493-8168-A6830EB21EA6)
- [Add External Component Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#DACUA-GUID-D7A0D052-810C-4DE3-B75A-BE93D2CA6ACE)
- [Add Mobile Hub Component Service](https://docs.oracle.com/iaas/digital-assistant/doc/add-component-package-skill.html#DACUA-GUID-D851A943-CDFC-47A3-B382-43AF7B28834B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
