#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Testing module for TRE
"""

import tre as re

def test_search():
    """Tests searching for matches in a bytestring"""
    pattern = re.compile('a([0-9])a')
    m = pattern.search('bcda7aefga8ah')
    assert m.groups() == ('7',)
    assert m.group(0) == 'a7a'
    assert m.group(1) == '7'

def test_search_unicode():
    """Tests searching for matches in a unicode string"""
    pattern = re.compile(u'ä([0-9])ö')
    m = pattern.search(u'bcdä7öefga8ah')
    assert m.groups() == (u'7',)
    assert m.group(0) == u'ä7ö'
    assert m.group(1) == u'7'

def test_search_approx():
    """Test approximate search"""
    pattern = re.compile(u'abc([0-9])abc')
    m = pattern.approx(u'asdfabc5acbasdfsd', cost_subst=1, max_costs=10, max_subst=10, max=10)
    assert m is not None
    assert m.groups() == ('5',)
    assert m.group(0) == 'abc5acb'
    assert m.cost == 2
    assert m.num == (0, 0, 2)