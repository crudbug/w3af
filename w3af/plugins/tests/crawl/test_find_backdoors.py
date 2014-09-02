"""
test_find_backdoor.py

Copyright 2012 Andres Riancho

This file is part of w3af, http://w3af.org/ .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from w3af.plugins.tests.helper import PluginTest, PluginConfig, MockResponse


class TestFindBackdoor(PluginTest):

    target_url = 'http://httpretty-mock/'

    MOCK_RESPONSES = [MockResponse('/', 'Hello world'),
                      MockResponse('/c99shell.php', 'cmd shell')]

    _run_configs = {
        'cfg': {
            'target': target_url,
            'plugins': {'crawl': (PluginConfig('find_backdoors'),)}
        }
    }

    def test_find_backdoor(self):
        cfg = self._run_configs['cfg']
        self._scan(cfg['target'], cfg['plugins'])

        vulns = self.kb.get('find_backdoors', 'backdoors')

        self.assertEqual(len(vulns), 1, vulns)

        vuln = vulns[0]

        vulnerable_url = self.target_url + 'c99shell.php'
        self.assertEqual(vuln.get_url().url_string, vulnerable_url)
        self.assertEqual(vuln.get_name(), 'Potential web backdoor')