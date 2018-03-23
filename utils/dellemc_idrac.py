#! /usr/bin/python
# _*_ coding: utf-8 _*_

#
# Copyright (c) 2017 Dell Inc.
#
# Version: BETA
#
# Copyright © 2018 Dell Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# All rights reserved. Dell, EMC, and other trademarks are trademarks of
# Dell Inc. or its subsidiaries.
# Other trademarks may be trademarks of their respective owners.
#


try:
    from omsdk.sdkinfra import sdkinfra
    from omsdk.sdkcreds import UserCredentials
    from omsdk.sdkfile import FileOnShare, file_share_manager
    HAS_OMSDK = True
except ImportError:
    HAS_OMSDK = False

class iDRACConnection():

    def __init__(self, module):
        if not HAS_OMSDK:
            results = {}
            results['msg']="Dell EMC OpenManage Python SDK is required for this module"
            module.fail_json(**results)

        self.module = module
        self.handle = None

    def connect(self):
        results = {}

        ansible_module_params = self.module.params

        idrac = ansible_module_params.get('idrac')
        idrac_ip = ansible_module_params.get('idrac_ip')
        idrac_user = ansible_module_params.get('idrac_user')
        idrac_pwd = ansible_module_params.get('idrac_pwd')
        idrac_port = ansible_module_params.get('idrac_port')

        if idrac:
            return idrac

        try:
            sd = sdkinfra()
            sd.importPath()
        except Exception as e:
            results['msg'] = "Could not initialize drivers"
            results['exception'] = str(e)
            self.module.fail_json(**results)

        # Connect to iDRAC
        if idrac_ip == '' or idrac_user == '' or idrac_pwd == '':
            results['msg'] = "hostname, username and password required"
            self.module.fail_json(**results)
        else:
            creds = UserCredentials(idrac_user, idrac_pwd)
            idrac = sd.get_driver(sd.driver_enum.iDRAC, idrac_ip, creds)

            if idrac is None:
                results['msg'] = "Could not find device driver for iDRAC with IP Address: " + idrac_ip
                self.module.fail_json(**results)

        self.handle = idrac
        return idrac

    def disconnect(self):
        idrac = self.module.params.get('idrac')

        if idrac:
            # pre-existing handle from a task
            return False

        if self.handle:
            self.handle.disconnect()
            return True

        return True

    def setup_nw_share_mount(self):
        results = {}
        try:
            share_name = self.module.params.get('share_name')
            share_user = self.module.params.get('share_user')
            share_pwd  = self.module.params.get('share_pwd')
            share_mnt  = self.module.params.get('share_mnt')

            if share_name: 
                if not share_mnt:
                    file_share = file_share_manager.create_share_obj(
                                    share_path=share_name,
                                    creds=UserCredentials(share_user, share_pwd),
                                    isFolder=True)
                else:
                    file_share = FileOnShare(remote=share_name,
                                    mount_point=share_mnt,
                                    isFolder=True,
                                    creds=UserCredentials(share_user, share_pwd))

                if file_share:
                    return self.handle.config_mgr.set_liason_share(file_share)

        except Exception as e:
            results['msg'] = "Error: %s" % str(e)
            self.module.fail_json(**results)

        return False
