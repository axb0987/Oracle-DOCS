# Using Interactive Mode
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing_topic-Using_Interactive_Mode.htm
- Fetched: 2026-09-05 01:36 CDT

# Using Interactive Mode

This topic describes how to use the CLI's Interactive Mode to guide you through command usage.

You can use the CLI's Interactive Mode to guide you through command usage.

To enter the CLI's Interactive Mode:
```

```

Note  
  
You can enable interactive mode by default by setting the environment variable OCI_CLI_AUTO_PROMPT=True. For example:
```

```

Once you've entered Interactive Mode, you will see a full-screen prompt like this:

Auto Completion and Command and Parameter Suggestions

Once in Interactive Mode, you can use the tab key to display a suggested list of valid options for the next part of the command. Scroll through the list of options using the arrow keys, or the TAB and shift-TAB keys, and press the space bar to select that option. To run the command, press the ENTER key.

Command Reference Information

You can use Interactive Mode to scroll through information about a command and its parameters in the interactive mode drop-down menu. The color-coding also helps you distinguish the required versus optional parameters.

For example, to launch a compute instance you can check the required parameters followed by any optional parameters:

Exiting Interactive Mode

You can exit Interactive Mode at any time by pressing`Ctrl-D`
