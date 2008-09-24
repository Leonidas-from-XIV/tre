#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Tests the compatibility with `re` module.
"""

from nose.tools import assert_raises
import tre

def test_valid_compile():
    """Tests for compilation of patterns which should be ok"""
    pattern = tre.compile("a")
    # worked ok, so pass

def test_bad_compile_type():
    """Tests for TypeErrors that should be rised on invalid input"""
    assert_raises(TypeError, tre.compile, 2)

def test_compile_twice():
    """Tests whether a pattern can be compiled twice"""
    old = tre.compile("a")
    new = tre.compile(old)
    assert old is new
