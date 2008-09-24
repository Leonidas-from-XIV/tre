#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Testing module for TRE
"""

from nose.tools import assert_raises
import tre as re

def test_search():
    """Test searching for matches in a bytestring"""
    pattern = re.compile('a([0-9])a')
    m = pattern.search('bcda7aefga8ah')
    assert m.groups() == ('7',)
    assert m.group(0) == 'a7a'
    assert m.group(1) == '7'

def test_search_unicode():
    """Test searching for matches in a unicode string"""
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

def test_finditer():
    """Test whether finditer() returns the proper matches"""
    pattern = re.compile('[0-9]')
    results = pattern.finditer('d3t4 ru7e5!')
    # check for each one and for the exception, not by using list(results)
    assert results.next() == '3'
    assert results.next() == '4'
    assert results.next() == '7'
    assert results.next() == '5'
    assert_raises(StopIteration, results.next)

def test_findall():
    """Test whether findall() returns the proper list of matches"""
    pattern = re.compile('[0-9]')
    results = pattern.findall('d3t4 ru7e5!')
    assert results == ['3', '4', '7', '5']

