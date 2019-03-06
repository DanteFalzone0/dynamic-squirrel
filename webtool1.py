"""
Copyright (C) 2019 Dante Falzone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import requests
import bs4
from bs4 import UnicodeDammit

r = requests.get("https://xkcd.com/rss.xml")
q = r.text
soup = bs4.BeautifulSoup(q, 'lxml')
xqf = str(soup.item.description)
unicode_dammit = (((xqf.partition('alt="')[2])[:-21]).replace("&amp;quot;", '"'))
print(unicode_dammit)
