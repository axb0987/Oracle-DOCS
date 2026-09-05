# Set Up Terminal Emulation
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/setting-up-terminal-emulation.htm
- Fetched: 2026-09-05 03:02 CDT

# Set Up Terminal Emulation

Your initial communication with the Roving Edge Device is made through the serial console that's connected to your controlling host computer, such a laptop. The controlling host must have a USB-to-serial port driver and terminal emulation software that's configured as described in this section.
- 

Based on your host OS and hardware, use the appropriate method to ensure that a USB serial port driver is installed. The driver is required for connectivity to the Roving Edge Device serial port.
- 

Linux

The USB serial port driver is preinstalled on Oracle Linux Unbreakable Enterprise Kernel. The following command shows that the USB driver is present (driver version numbers vary):
```

```

- Microsoft Windows

USB serial ports are listed in the Device Manager under Ports (COM &amp; LPT) . The following example shows the common serial ports:
```

```

If a serial device isn't displayed, you might need to install or update the USB serial port drivers. Go to the Microsoft Windows store to obtain and install the driver.
- macOS

Example of listing USB serial ports in a terminal window:
```

```

If a serial device isn't displayed, you might need to install or update the USB serial port drivers. Go to the Apple store to obtain and install the driver.
- 

Install and configure a terminal emulator.

We recommend the following terminal emulation software based on your host OS:

Linux: PuTTY, Minicom, or screen

Microsoft Windows: PuTTY

macOS ZOC or screen

Configure the terminal emulator software settings as follows:
- Terminal Type: VT100+
- Bits per second: 115200
- Data Bits: 8
- Stop Bits: 1
- Parity: None
- Flow Control: None
Note  
  

With PuTTY, you can't configure all these settings individually. However, you can configure the PuTTY default settings by selecting the Serial connection type and specifying 115200 for the Serial Line baud speed. This configuration is sufficient to use PuTTY as a terminal emulator for the device.
- 

Connect the terminal window to the port:
- Linux example:
```

```

- 

Microsoft Windows: In PuTTY, under Connection , select Serial , then enter the following attributes:
- Serial line to connect to : COM n (replace n with the appropriate COM number)
- Speed (baud) : 115200
- Data Bits : 8
- Stop Bits : 1
- Parity : None
- Flow Control : None

Select Open .
- 

macOS example:
```

```

Serial console output is displayed after the device is powered on.

What's next?

[Power On the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/power-on-device.htm#unlock-the-device)
