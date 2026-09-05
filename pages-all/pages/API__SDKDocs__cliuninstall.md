# Uninstalling the CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliuninstall.htm
- Fetched: 2026-09-05 01:36 CDT

# Uninstalling the CLI

## For Manual Installations

If you manually installed the CLI using pip, run the following command:

```

```

If you manually installed the CLI in a virtual environment, run the following command:

```

```

## For Script Installations

If you used the install script and the default installation location, you should delete the following directories.

On Windows:
- %USERPROFILE%/lib/oracle-cli
- %USERPROFILE%/bin/oci
- %USERPROFILE%/bin/oci-cli-scripts

On Mac:
- $HOME/lib/oracle-cli
- $HOME/bin/oci
- $HOME/bin/oci-cli-scripts

If you used the install script, but installed to a custom location, you should delete the directories at that location.

## Uninstalling Python

The script also installs Python as a dependency if it was not already installed. In Windows 10, you can uninstall Python in Control Panel or at the command line.

### Using Control Panel

To uninstall Python in Control Panel, select Programs and Features . Right-click Python and select Uninstall .

For more information, see[Repair or remove programs in Windows 10](https://support.microsoft.com/help/4028054/windows-10-repair-or-remove-programs).

### Using the Command Line

To uninstall Python at the command line, run the following command:
```

```

If you do not have the MSI file, you can also use the package or product code. For more information, see[Using the Windows Installer](https://www.python.org/download/releases/2.4/msi/).

## Uninstalling the CLI on Mac OS X with Homebrew

To unsinstall the CLI from Mac OS X using[Homebew](https://docs.brew.sh/Installation):

```

```
