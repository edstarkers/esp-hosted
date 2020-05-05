# Copyright 2015-2020 Espressif Systems (Shanghai) PTE LTD
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from host_commands import slave_comm
failure = 'failure'
# get mac address

# 1 : station
# 2 : softAP
'''
x = slave_comm.get_mac(2)
print("sta mac "+str(x))

# 0: null Mode, Wi-Fi mode not set
# 1: station mode
# 2: softAP mode
# 3: softAP+station mode
# or Failure

x = slave_comm.get_wifi_mode()
print("wifi mode is "+str(x))

x = slave_comm.set_wifi_mode(2)
print("connected mode is "+str(x))

x = slave_comm.wifi_set_ap_config('xyz','xyz123456','0')
print(x)

x = slave_comm.wifi_get_ap_config()
print(x)

x = slave_comm.wifi_disconnect_ap()
print(x)

x = slave_comm.wifi_set_softap_config('ESP12','0',4,0,5,0,1)
print(x)

x = slave_comm.wifi_get_softap_config()
print(x)

# output is list of Aplist class instances
x = slave_comm.wifi_ap_scan_list()
print(x)
if (x == failure):
    print(failure)
else:
    for obj in x:
        print(obj.ssid,obj.chnl,obj.rssi,obj.bssid,obj.ecn)


# output is list of Stationlist class instances
x = slave_comm.wifi_connected_stations_list()
print(x)
if (x == failure):
    print(failure)
else :
    for obj in x:
        print(obj.mac)
'''