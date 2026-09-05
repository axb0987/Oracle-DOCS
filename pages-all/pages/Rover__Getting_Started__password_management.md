# Managing Serial Console Sign-In Attempts
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/password_management.htm
- Fetched: 2026-09-05 02:59 CDT

# Managing Serial Console Sign-In Attempts

By default, serial console sign-in attempts is set to 10. If an incorrect password is entered 11 times, the unlock key is shredded, preventing any further access to the serial console menu. You can change the number of incorrect password attempts that are allowed on the device.
When you attempt to sign in and provide an incorrect password, a message similar to the following is displayed:
```

```

If you reach your final attempt before you exceed the number of attempts allowed, a message similar to the following appears:
```

```

Note  
  
If the device unlock key is shredded, you can recover the device using the recovery key. See[Managing Roving Edge Infrastructure Device Master Keys](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../master_key_management.htm#MasterKeyManagement).
- 

Using terminal emulation to display the serial console, select the Advanced Menu &gt; Network Management menu option. The following option appears:

No. of attempts before key is shredded (Default:10)
- 

Select this option. The following option appears:

Enter number of unlock attempt allowed (between 3 and 100)
- Enter the number of attempts the user can try to unlock the device before they are prevented from any further tries. The number of attempts can be between 3 and 100. If you don't provide a value, the default number 10 is used.
Note
