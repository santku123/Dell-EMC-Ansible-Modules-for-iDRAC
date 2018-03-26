# dellemc_idrac_import_scp
Import Server Configuration Profile (SCP) from a remote network share or a local path

  * [Synopsis](#Synopsis)
  * [Options](#Options)
  * [Examples](#Examples)

## <a name="Synopsis"></a>Synopsis
 Import a given Server Configuration Profile (SCP) file from a network share (CIFS, NFS) or a local path on the Ansible controller

## <a name="Options"></a>Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| idrac_ip  |   yes  |  | |  iDRAC IP Address  |
| idrac_user  |   yes  |  | |  iDRAC user name  |
| idrac_pwd  |   yes  |  | |  iDRAC user password  |
| idrac_port  |   no  |  443  | |  iDRAC port  |
| share_name  |   yes  |  | |  Local directory path or a Remote Network file share (either CIFS or NFS)  |
| share_user  |   No  |  | |  Network share user in the format 'user@domain' if user is part of a domain, else 'user'  |
| share_pwd  |   No  |  | |  Network share user password  |
| share_mnt  |   No  |  | |  Local mount path of the network file share specified in I(share_name) with read-write permission for ansible user  |
| scp_file  |   yes  |    | |  Server Configuration Profile file name relative to I(share_name) |
| scp_components  |   no  |  ALL  | <ul> <li>ALL</li>  <li>IDRAC</li>  <li>BIOS</li>  <li>NIC</li>  <li>RAID</li> </ul> |  <ul><li>if C(ALL), will import all components configurations from SCP file</li><li>if C(IDRAC), will import iDRAC comfiguration from SCP file</li><li>if C(BIOS), will import BIOS configuration from SCP file</li><li>if C(NIC), will import NIC configuration from SCP file</li><li>if C(RAID), will import RAID configuration from SCP file</li><ul>  |
| end_hos_power_state |   no  |  On  | <ul><li>On</li><li>Off</li></ul> |  Host's power state after importing the SCP; Default is 'On'  |
| shutdown_type |  no  |  Graceful  | <ul><li>Graceful</li><li>Forced</li><li>NoReboot</li></ul> | <ul><li>if C(Graceful), will gracefully shut down the server</li><li>if C(Forced), will do a forced shutdown of the server</li><li>if C(NoReboot), will not reboot the server</li><ul> |
| job_wait  |   no  |  True  | |  <ul><li>if C(True), wait for the import scp job to be completed and return the status</li><li>if C(False), return immediately after creating a import scp job</li></ul>  |

## <a name="Examples"></a>Examples

```
# Import Server Configuration Profile from a local path
# Following play will import a SCP file named 'scp_file.xml' from the local path
# '/home/user' by sending the contents of the file in the https message to iDRAC

- name: Import Server Configuration Profile
    dellemc_idrac_import_scp:
      idrac_ip:              "192.168.1.1"
      idrac_user:            "root"
      idrac_pwd:             "calvin"
      share_name:            "/home/user"
      scp_file:              "scp_file.xml"
      scp_components:        "ALL"
      end_host_power_state:  "On"
      shutdown_type:         "Graceful"
      job_wait:              True

```

# Import Server Configuration Profile from a CIFS Network Share

- name: Import Server Configuration Profile
    dellemc_idrac_import_scp:
      idrac_ip:              "192.168.1.1"
      idrac_user:            "root"
      idrac_pwd:             "calvin"
      share_name:            "\\192.168.10.10\share"
      share_user:            "user1"
      share_pwd:             "password"
      share_mnt:             "/mnt/share"
      scp_file:              "scp_file.xml"
      scp_components:        "ALL"
      end_host_power_state:  False
      shutdown_type:         "Graceful"
      job_wait:              True
```

```
# Import Server Configuration Profile from a NFS Network Share

- name: Import Server Configuration Profile
    dellemc_idrac_import_scp:
      idrac_ip:   "192.168.1.1"
      idrac_user: "root"
      idrac_pwd:  "calvin"
      share_name: "192.168.10.10:/share"
      share_user: "user1"
      share_pwd:  "password"
      share_mnt:  "/mnt/share"
      scp_file:   "scp_file.xml"
      scp_components: "ALL"
      end_host_power_state:  False
      shutdown_type:         "Graceful"
      job_wait:              True

```

---

Copyright © 2018 Dell Inc. or its subsidiaries. All rights reserved. Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.
