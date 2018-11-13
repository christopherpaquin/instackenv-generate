# csv-to-instack
Convert a CSV of your Overcloud nodes into the instackenv.json format.

## Usage
```
python csv-to-instack.py --csv=target-csv-file
```

## Example CSV
Always provide the header row. The code ignores the first row, since it assumes it is the header

# name | macaddress | ip address | ipmi user | ipmi password | ipmi driver | vmbc port
```
overcloud-node1,52:54:00:ac:78:ed,10.1.99.112,admin,password,pxe_ipmitool,6231
overcloud-node2,52:54:00:41:b6:74,10.1.99.112,admin,password,pxe_ipmitool,6232
overcloud-node3,52:54:00:ab:3f:7d,10.1.99.112,admin,password,pxe_ipmitool,6233
overcloud-node4,52:54:00:2e:2b:3d,10.1.99.112,admin,password,pxe_ipmitool,6234
overcloud-node5,52:54:00:15:b7:3a,10.1.99.112,admin,password,pxe_ipmitool,6235
```

# Origin
Originaly forked from the now defunct, https://github.com/rthallisey/clapperm


**name** - Name of the node.

**macaddress** - Mac Address of NIC that will PXE.

**ipmi url** - URL to the drac/ilo/vbmc host.

**ipmi user** - Username to login to the drac/ilo/vbmc.

**ipmi password** - Password to login to the drac/ilo/vbmc.

**ipmi tool** - Which tool to use, when in doubt, use pxe_ipmitool.

**vbmc port** - Configured vmbc port

## Example output
```
{
    "nodes": [
        {
            "arch": "x86_64", 
            "cpu": "4", 
            "disk": "40", 
            "mac": [
                "52:54:00:ac:78:ed"
            ], 
            "memory": "6144", 
            "name": "overcloud-node1", 
            "pm_addr": "password", 
            "pm_password": "admin", 
            "pm_port": "6231", 
            "pm_type": "pxe_ipmitool", 
            "pm_user": "admin"
        }, 
        {
            "arch": "x86_64", 
            "cpu": "4", 
            "disk": "40", 
            "mac": [
                "52:54:00:41:b6:74"
            ], 
            "memory": "6144", 
            "name": "overcloud-node2", 
            "pm_addr": "password", 
            "pm_password": "admin", 
            "pm_port": "6232", 
            "pm_type": "pxe_ipmitool", 
            "pm_user": "admin"
        }, 
        {
            "arch": "x86_64", 
            "cpu": "4", 
            "disk": "40", 
            "mac": [
                "52:54:00:ab:3f:7d"
            ], 
            "memory": "6144", 
            "name": "overcloud-node3", 
            "pm_addr": "password", 
            "pm_password": "admin", 
            "pm_port": "6233", 
            "pm_type": "pxe_ipmitool", 
            "pm_user": "admin"
        }, 
        {
            "arch": "x86_64", 
            "cpu": "4", 
            "disk": "40", 
            "mac": [
                "52:54:00:2e:2b:3d"
            ], 
            "memory": "6144", 
            "name": "overcloud-node4", 
            "pm_addr": "password", 
            "pm_password": "admin", 
            "pm_port": "6234", 
            "pm_type": "pxe_ipmitool", 
            "pm_user": "admin"
        }, 
        {
            "arch": "x86_64", 
            "cpu": "4", 
            "disk": "40", 
            "mac": [
                "52:54:00:15:b7:3a"
            ], 
            "memory": "6144", 
            "name": "overcloud-node5", 
            "pm_addr": "password", 
            "pm_password": "admin", 
            "pm_port": "6235", 
            "pm_type": "pxe_ipmitool", 
            "pm_user": "admin"
        }
    ]
}

```
