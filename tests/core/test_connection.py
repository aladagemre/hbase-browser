from hbase_browser.core.connection import HBaseConnection

__author__ = 'emre'

import unittest


class ConnectionTestCase(unittest.TestCase):
    def setUp(self):
        self.con = HBaseConnection("http://localhost", 9300)

    def test_constructor(self):
        hc = HBaseConnection("http://127.0.0.1", 8000)
        self.assertEqual(hc.url, "http://127.0.0.1:8000")

        hc = HBaseConnection()
        self.assertEqual(hc.url, "http://localhost:9300")

    def test_get_version(self):
        actual = self.con.get_version()
        self.assertIn("Server", actual)
        self.assertIn("OS", actual)
        self.assertIn("JVM", actual)

    def test_get_cluster_version(self):
        actual = self.con.get_cluster_version()
        self.assertIn('.', actual)
        dot_count = actual.count('.')
        self.assertEquals(dot_count, 2)

    def test_get_cluster_status(self):
        actual = self.con.get_cluster_status()
        self.assertIn("LiveNodes", actual)

    def test_get_table_list(self):
        actual = self.con.get_table_list()
        self.assertIn("AccessLog", actual)

    def test_create_table(self):
        pass

    def test_get_table_schema(self):
        actual = self.con.get_table_schema('AccessLog')
        self.assertIn("name", actual)
        self.assertEqual(actual["name"], "AccessLog")

    def test_replace_table_schema(self):
        pass

    def test_query_table_metadata(self):
        actual = self.con.query_table_metadata('AccessLog')
        self.assertIn("name", actual)
        self.assertEqual(actual["name"], "AccessLog")

    def test_delete_table(self):
        # TODO: Create a temp table at the setUp
        pass





if __name__ == '__main__':
    unittest.main()
