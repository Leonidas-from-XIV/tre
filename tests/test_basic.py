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

def test_search_nomatch():
    """Test whether a string with no match returns None"""
    pattern = re.compile("Doesn't exist")
    assert pattern.search('In this text') is None

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

def test_match():
    """Test matching"""
    pattern = re.compile('zat')
    m = pattern.match('zatazata')
    assert m is not None
    assert m.groups() == tuple()
    assert m.group() == 'zat'
    assert m.group(0) == 'zat'

def test_match_groups():
    pattern = re.compile('a([0-9])')
    m = pattern.match('a4ra6')
    assert m is not None
    assert m.groups() == (4,)
    assert m.group() == 'a4'
    assert m.group(0) == 'a4'
    assert m.group(1) == '4'

def test_match_nomatch():
    """Test matching with strings that don't match"""
    pattern = re.compile('a')
    m = pattern.match('zzzzaaaa')
    assert m is None

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

def test_module_search():
    """Tests whether tre.search() finds the same as a compiled regex"""
    regex = r'a([0-9])a'
    text = 'a3abda6ama7ada'
    m1 = re.compile(regex).search(text)
    m2 = re.search(regex, text)
    assert m1.groups() == m2.groups()
    assert m1.group(0) == m2.group(0)
    assert m1.group(1) == m2.group(1)

def test_module_match():
    """Tests whether tre.match() finds the same as a compiled regex"""
    regex = r'a([0-9])a'
    text = 'a3abda6ama7ada'
    m1 = re.compile(regex).match(text)
    m2 = re.match(regex, text)
    assert m1.groups() == m2.groups()
    assert m1.group(0) == m2.group(0)
    assert m1.group(1) == m2.group(1)
