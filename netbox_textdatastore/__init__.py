from extras.plugins import PluginConfig


class NetBoxTextDataStoreConfig(PluginConfig):
    name = 'netbox_textdatastore'
    verbose_name = ' NetBox Text Data Store'
    description = 'Store raw text files for devices, like configuration files, unparsed command output or test results'
    version = '0.0.1'
    base_url = 'textdata'


config = NetBoxTextDataStoreConfig
