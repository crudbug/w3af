'''
test_invalid_url.py

Copyright 2013 Andres Riancho

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
'''
import os

from core.ui.tests.wrappers.xpresser_unittest import XpresserUnittest


class TestInvalidURL(XpresserUnittest):
    
    IMAGES = os.path.join('core', 'ui', 'tests', 'gui', 'invalid_target_url', 'images')
    
    def test_invalid_url(self):
        self.click('insert_target_url_here')
        self.type('http:', False)
        self.type(['<Enter>',], False)
        # For some reason this moves the mouse pointer to the right location
        # but then it doesn't seem to click on it
        #self.click('scan_start')
        
        self.find('invalid_url')
        self.click('ok')

        
        
        