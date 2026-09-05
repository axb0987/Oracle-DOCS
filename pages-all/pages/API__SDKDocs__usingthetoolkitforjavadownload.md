# Using the Toolkit for Java Download
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/usingthetoolkitforjavadownload.htm
- Fetched: 2026-09-05 01:37 CDT

# Using the Toolkit for Java Download

This topic shows how to use the Toolkit for Java Download to install an Oracle Java release in Oracle Cloud Shell.

## Before You Begin

To use the toolkit, ensure that:
- You're signed in to your Oracle Cloud Infrastructure (OCI) account.
- You have launched Cloud Shell in the OCI Console.

## Step 1: Run the Toolkit Script
In your Cloud Shell session, run the toolkit script:
```

```

Example output:
```

```

## Step 2: Select a Java Version
You can:
- Select a current release, or
- Choose the option labelled "Show Archived Versions" to view older releases.
Note  
  
The option number for archived versions might vary depending on how many current versions are listed.

Selecting a Current Release

If the Java version you want to install is listed in the current releases, enter its corresponding number. This will proceed the process to Step 3: Token Management.
Viewing Archived Versions
Note  
  
The non-current releases in Archived releases table are provided to help developers debug issues in older systems. They aren’t updated with the latest security patches and aren’t recommended for use in production.
If you choose "Show Archived Versions", the toolkit will list available major Java versions with archived releases:
```

```

Choose the JDK major version you are interested in.
```

```

## Step 3: Token Management

Each Java download through the toolkit must be associated with a valid token managed by the Java Download feature in JMS.
- If a valid token already exists, it can be reused.
- If no suitable token is found, the toolkit helps you create a new one during the installation process.

Case 1: Active Token Exists
If one or more valid tokens already exist, the toolkit will prompt you to reuse an existing token or create a new one:
```

```

Case 2: Create New Token or No Active Token Exists

The example shows JDK 24.0.1, which falls under[Oracle No-Fee Terms and Conditions (NFTC)](https://java.com/freeuselicense):
```

```

Note  
  
If the selected release is distributed under[Oracle Technology Network License Agreement for Oracle Java SE (OTN) License](https://java.com/otnlicense), you’ll be prompted to accept the license terms before a token can be created and the download initiated.

Once a token is selected or created, the download begins automatically.

## Step 4: Download and Complete Installation

If your Cloud Shell instance already has an Oracle Java installation, the toolkit detects it and prompts whether to remove existing JDK directories:
```

```

Once confirmed (or skipped), the download begins:
```

```

At successful installation, the toolkit automatically updates your environment variables and exits execution.
```

```

This completes the installation process in Oracle Cloud Shell. You can now begin using the installed Java version immediately.

To verify the installation, run:
```

```
