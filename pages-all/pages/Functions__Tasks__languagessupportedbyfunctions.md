# Languages Supported by OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/languagessupportedbyfunctions.htm
- Fetched: 2026-09-05 02:09 CDT

# Languages Supported by OCI Functions

Find out which languages and language versions are currently supported by the Function Development Kits (FDKs) used by OCI Functions.

[Function Development Kits (FDKs)](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssupportedlanguageversions.htm)are specific to particular versions of a given language. FDK updates are regularly published for supported languages (for example, to issue a patch, or to support a newly released version of the language).

Existing functions built using old FDK base images will continue to work. However, Oracle recommends you upgrade functions to a supported language version wherever possible.
The following table shows:
- FDK Language: The languages for which FDKs are currently available.
- Default: The default language version for an FDK (usually the latest language version).
- Supported: The language versions for which FDK updates are regularly published.
- Deprecated: Language versions for which FDK updates are no longer published.

FDK Language Default Supported Deprecated
Java 21 21, 17, 11, 8 n/a
Python 3.12 3.12, 3.11 3.9, 3.8, 3.7, 3.6
Ruby 3.3 3.3 3.1, 2.7, 2.5
Go 1.24 1.24, 1.23 1.20, 1.19, 1.18, 1.15, 1.11
Node.js 24 24, 22 20, 18, 16, 14, 11
C# (.NET) 9.0 9.0, 8.0 see Note 1 6.0, 3.1

Note 1: The dotnet FDK version determines the architectures on which C# (.NET) version 8.0 is supported, as follows:
- For dotnet FDK versions 1.0.49 and earlier, C# (.NET) version 8.0 is only supported on x86 architectures.
-
