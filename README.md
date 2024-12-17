# netbox_textdatastore
Store raw text files for devices, like configuration files, unparsed command output or test results
*Use version 0.0.5 for netbox 3.6* 

TextData Object:
'''
{
    "id": Int,                # unique id
    "name": String,           # Object Name, eg "device config"
    'device': Device ID,      # Device ID from Netbox
    'hash': String,           # Hash of your Text Data
    'data': String,           # Your text data, eg Device Configfile
}
'''


# Example:
## extend python-netbox
*https://github.com/jagter/python-netbox*

'''
from netbox import NetBox as NetBoxOrig

class textdata(object):

    def __init__(self, netbox_con):
        self.netbox_con = netbox_con

    def get_data(self, **kwargs):
        return self.netbox_con.get('/plugins/textdata/data/', **kwargs)

    def add_data(self, device, name, hash, data,  **kwargs):
        required_fields = {
            "name": name,
            'device': device,
            'hash': hash,
            'data': data,
            }
        print(required_fields)

        return self.netbox_con.post(
            '/plugins/textdata/data/',
            required_fields,
            **kwargs
        )

    def update_data_id(self, pk, **kwargs):
        return self.netbox_con.patch(
            '/plugins/textdata/data/',
            pk,
            **kwargs
        )


class NetBox(NetBoxOrig):


    def __init__(self, host, **kwargs):
        super().__init__(host, **kwargs)
        self.textdata = textdata(self.connection)
'''

## use it in napalm

'''
def store_config(task, obj, content):
    """store config to netbox"""

    hasher = md5()
    hasher.update(content.encode('utf-8'))
    hash = hasher.hexdigest()
    device_id = task.host.data["id"]
    res = obj.netbox.textdata.get_data(
        device_id=device_id,
        name="device config"
    )
    if(len(res) > 0):
        res = res[0]
        if(res["hash"] == hash):
            print("No change")
            return
        print(obj.netbox.textdata.update_data_id(
            pk=res["pk"],
            data=content,
            hash=hash
        ))
        return
    print(obj.netbox.textdata.add_data(
        device=device_id,
        name="device config",
        hash=hash,
        data=content
    ))

def backup_config(task, obj):
    """ get config from devices"""

    from nornir_napalm.plugins.tasks import napalm_get
    device_config = task.run(task=napalm_get, getters=["config"])
    task.run(
        task=store_config,
        obj=obj,
        content=device_config.result["config"]["running"]
    )
'''