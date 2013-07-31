# encoding: utf-8
"""
http://wiki.apache.org/hadoop/Hbase/Stargate
"""
import requests


class HBaseConnection(object):
    def __init__(self, host="http://localhost", port="9300"):
        self.url = '{host}:{port}'.format(host=host, port=port)

    def get_version(self):
        """
        Returns server, rest, os, jvm versions.
        """
        target = "{url}/version".format(url=self.url)
        headers = {"Accept": "application/json"}
        response = requests.get(target, headers=headers)
        return response.json()

    def get_cluster_version(self):
        """
        Returns HBase cluster version (0.90.5)
        """
        target = "{url}/version/cluster".format(url=self.url)
        headers = {"Accept": "application/json"}
        response = requests.get(target, headers=headers)
        return response.json()

    def get_cluster_status(self):
        """
        Returns cluster status
        """
        target = "{url}/status/cluster".format(url=self.url)
        headers = {"Accept": "application/json"}
        response = requests.get(target, headers=headers)
        return response.json()

    def get_table_list(self):
        """
        Returns the table list.
        @return table names list

        Example output:
        ['AccessLog', 'webpage']
        """
        target = "{url}/".format(url=self.url)
        headers = {"Accept": "application/json"}
        response = requests.get(target, headers=headers)
        result = response.json()
        tables = [table['name'] for table in result['table']]
        return tables

    def create_table(self):
        """
        Creates a HBase table.
        """
        raise NotImplementedError

    def get_table_schema(self, table_name):
        """
        Returns table schema.
        @return schema dict
        {u'IS_ROOT': u'false', u'ColumnSchema': [{u'BLOCKCACHE': u'true',
        u'COMPRESSION': u'NONE', u'VERSIONS': u'3', u'BLOCKSIZE': u'65536',
        u'REPLICATION_SCOPE': u'0', u'TTL': u'2147483647',
        u'IN_MEMORY': u'false', u'BLOOMFILTER': u'NONE', u'name': u'common'},
        {u'BLOCKCACHE': u'true', u'COMPRESSION': u'NONE', u'VERSIONS': u'3',
        u'BLOCKSIZE': u'65536', u'REPLICATION_SCOPE': u'0',
        u'TTL': u'2147483647', u'IN_MEMORY': u'false',
        u'BLOOMFILTER': u'NONE', u'name': u'http'},
        {u'BLOCKCACHE': u'true', u'COMPRESSION': u'NONE', u'VERSIONS': u'3',
        u'BLOCKSIZE': u'65536', u'REPLICATION_SCOPE': u'0',
        u'TTL': u'2147483647', u'IN_MEMORY': u'false', u'BLOOMFILTER': u'NONE',
        u'name': u'misc'}], u'name': u'AccessLog', u'IS_META': u'false'}
        """
        target = "{url}/{table_name}/schema".format(url=self.url,
                                                    table_name=table_name)
        headers = {"Accept": "application/json"}
        response = requests.get(target, headers=headers)
        return response.json()

    def replace_table_schema(self, table_name, new_schema):
        """
        PUT /<table>/schema
        """
        pass

    def modify_table_schema(self, table_name, modifications):
        """
        POST /<table>/schema
        """
        pass

    def query_table_metadata(self, table_name):
        """
        GET /<table>/regions
        """

        target = "{url}/{table_name}/regions".format(url=self.url,
                                                     table_name=table_name)
        headers = {"Accept": "application/json"}
        response = requests.get(target, headers=headers)
        return response.json()

    def delete_table(self, table_name):
        """
        Deletes given table.
        DELETE /<table>/schema
        """
        target = "{url}/{table_name}/schema".format(url=self.url,
                                                    table_name=table_name)
        headers = {"Accept": "application/json"}
        response = requests.delete(target, headers=headers)
        return response.json()