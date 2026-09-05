# Openswan
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/openswanCPE.htm
- Fetched: 2026-09-05 02:42 CDT

# Openswan

To use Openswan to create Site-to-Site VPN to Oracle Cloud Infrastructure, see[Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm).

## How Openswan and Libreswan Are Related

[Openswan](https://www.openswan.org/)is a common IPSec implementation for Linux. It began as a fork of the now-defunct[FreeS/WAN project](https://www.freeswan.org/)in 2003. Unlike the FreeS/WAN project, it didn't solely target the GNU/Linux operation system, but expanded its use to other OSs. In 2012, FreeS/WAN renamed itself to the[Libreswan](https://libreswan.org/)Project because of a lawsuit over a trademark of the name openswan .

As a result, when you try to install or query the Openswan package on Oracle Linux, by default the Libreswan package is installed or shown instead. The following yum search query command illustrates this behavior:
```

```

Libreswan is maintained by The Libreswan Project and has been under active development for over 15 years, going back to the FreeS/WAN Project. For more information, see the[project's history](https://libreswan.org/wiki/History)
