# dellemc_idrac_export_scp
Export Server Configuration Profile (SCP) to remote network share or a local path

  * [Synopsis](#Synopsis)
  * [Options](#Options)
  * [Examples](#Examples)

## <a name="Synopsis"></a>Synopsis
 Export Server Configuration Profile to a given remote network share (CIFS, NFS) or a local directory path on Ansible controller

## <a name="Options"></a>Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| idrac_ip  |   yes  |  | |  iDRAC IP Address  |
| idrac_user  |   yes  |  | |  iDRAC user name  |
| idrac_pwd  |   yes  |  | |  iDRAC user password  |
| idrac_port  |   no  |  443  | |  iDRAC port  |
| share_name  |   yes  |  | |  Remote CIFS or NFS Network share or local directory path on Ansible controller |
| share_user  |   no  |  | |  Network share user in the format 'user@domain' if user is part of a domain else 'user'  |
| share_pwd  |   no  |  | |  Network share user password  |
| scp_components  |   no  |  ALL  | <ul> <li>ALL</li>  <li>IDRAC</li>  <li>BIOS</li>  <li>NIC</li>  <li>RAID</li> </ul> |  <ul><li>if C(ALL), will export all components configurations in SCP file</li><li>if C(IDRAC), will export iDRAC configuration in SCP file</li><li>if C(BIOS), will export BIOS configuration in SCP file</li><li>if C(NIC), will export NIC configuration in SCP file</li><li>if C(RAID), will export RAID configuration in SCP file</li></ul>  |
| export_format |  no  |  XML  |  <ul><li>XML</li><li>JSON</li></ul> | <ul><li>if C(XML), will export the SCP file in XML format</li><li>if C(JSON), will export the SCP file in JSON format</li></ul> |
| export_use |  no  |  Default  |  <ul><li>Default</li><li>Clone</li><li>Replace</li></ul>  | <ul><li>if C(Default>, will export the SCP using the Default mode. SCP files exported using Default mode has non-destructive settings and actions that will not cause disruption to a target system if applied.</li><li>if C(Clone), will export the SCP using the Clone mode. Usually, Clone method should be used when you want to duplicate settings from a golden source server to a target server with an identical hardware configuration.</li><li>if C(Replace), will export SCP using the Replace mode. SCP exported using Replace mode will have uncommented authentical attributes, storage actions, and I/O identity properties for NICs and Fibre Channels. You will want to use this export method when you want to retire a server from datacenter and replace it with another, or restore the server to a known baseline.</li></ul>
| job_wait  |   no  |  True  | |  <ul><li>if C(True), will wait for the SCP export job to finish and return the job completion status</li><li>if C(False), will return immediately with a JOB ID after queueing the SCP export jon in LC job queue</li></ul>  |

## <a name="Examples"></a>Examples

```
# Export SCP to local directory
- name: Export Server Configuration Profile (SCP)
  dellemc_idrac_export_scp:
    idrac_ip:       "192.168.1.1"
    idrac_user:     "root"
    idrac_pwd:      "calvin"
    share_name:     "/home/user"
    scp_components: "ALL"
    export_format:  "JSON"
    export_use:     "Default"
    job_wait:       True
```

```
# Export SCP to a CIFS network share
- name: Export Server Configuration Profile (SCP)
  dellemc_idrac_export_scp:
    idrac_ip:       "192.168.1.1"
    idrac_user:     "root"
    idrac_pwd:      "calvin"
    share_name:     "\\192.168.10.10\share"
    share_user:     "user1"
    share_pwd:      "password"
    scp_components: "ALL"
    export_format:  "JSON"
    export_use:     "Default"
    job_wait:       True
```

```
# Export SCP to a NFS network share
- name: Export Server Configuration Profile (SCP)
  dellemc_idrac_export_scp:
    idrac_ip:   "192.168.1.1"
    idrac_user: "root"
    idrac_pwd:  "calvin"
    share_name: "192.168.10.10:/share"
    share_user: "user1"
    share_pwd:  "password"
    scp_components: "ALL"
    export_format:  "JSON"
    export_use:     "Default"
    job_wait:       True
```

---

Copyright © 2018 Dell Inc. or its subsidiaries. All rights reserved. Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.
