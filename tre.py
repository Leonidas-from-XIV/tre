#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
A module which creates a binding for the TRE regular expression engine.
You can find the home page of TRE at http://laurikari.net/tre/

Don't be surprised about many very easy and obvious documentation comments
as this module is also intended as a documentation on how to wrap C
libraries with ctypes. ctypes was put into the stdlib for Python 2.5 so it
does not count as external dependency anymore.
"""

# import important ctypes functions
from ctypes import cdll, Structure, POINTER, byref
# inport the built-in C datatypes
from ctypes import c_int, c_size_t, c_void_p, c_char, c_char_p, c_wchar
# get the constants that are defined in sre_constants
import sre_constants

# the constants defined in TRE's regex.h
# 
# unfortunately, it is also possible that tre will use some of the
# constants in the system's regex.h - this has to be handled in some smart
# way. Further analyzing the system's regex.h is neccessary
# 
# not all of them are needed, it doesn't hurt to be as complete as possible

# POSIX regcomp() flags
# enable extended regular expressions - that's the default in tre.py
# as opposed to TRE itself, which uses basic regular expressions
REG_EXTENDED = 1
# ignore case
REG_ICASE = REG_EXTENDED << 1
# special handling of newline character
REG_NEWLINE = REG_ICASE << 1
# do not report submatches. The submatch array won't be filled
REG_NOSUB = REG_NEWLINE << 1

# extra, nonstandard flags
# basic regular expression - this is the default, anyway
REG_BASIC = 0
# all characters of the input string are considered ordinary
REG_NOSPEC = REG_LITERAL = REG_NOSUB << 1
# by default the concatenation is left associative in TRE
REG_RIGHT_ASSOC = REG_LITERAL << 1
REG_UNGREEDY = REG_RIGHT_ASSOC << 1

# POSIX regexec() flags
REG_NOTBOL = 1
REG_NOTEOL = REG_NOTBOL << 1

# extra regexec() flags
REG_APPROX_MATCHER = 0x1000
REG_BACKTRACKING_MATCHER = REG_APPROX_MATCHER << 1

# error constants
reg_errcode_t = [
    # no error
    'REG_OK',
    # no match
    'REG_NOMATCH',
    # invalid regular expression
    'REG_BADPAT',
    # unknown collating element
    'REG_ECOLLATE',
    # unknown charater class name
    'REG_ECTYPE',
    # trailing backslash
    'REG_EESCAPE',
    # invalid back reference
    'REG_ESUBREG',
    # [ and ] parenthesis imbalance
    'REG_EBRACK',
    # ( and ) parenthesis imbalance
    'REG_EPAREN',
    # { and } parenthesis imbalance
    'REG_EBRACE',
    # invalid content of {}
    'REG_BADBR',
    # invalid use of range operator
    'REG_ERANGE',
    # out of memory
    # when this occurs it's almost certain a bug in this file
    'REG_ESPACE',
    # invalid use of repetition operator
    # according to the documentation TRE never returns this error code
    'REG_BADRPT',
]

try:
    # first try to import the library by it's unixish soname
    libtre = cdll.LoadLibrary('libtre.so.4')
except (WindowsError, OSError):
    # the unix lib is not available,
    # try the windows one
    libtre = cdll.LoadLibrary('tre4.dll')

# create the custom types needed for TRE
# not all types are really custom, TRE uses a lot of standard C types
# but gives them only new names

# a regoff_t is just an ordinary c_int
regoff_t = c_int

class regex_t(Structure):
    """This is the regex_t structure as defined by TRE.
    The exact field information was taken from the header files
    of TRE - it was found in regex.h"""
    _fields_ = [
        ('re_nsub', c_size_t),
        ('value', c_void_p),
    ]

# define a pointer type to regex_t structure
regex_p = POINTER(regex_t)

class regmatch_t(Structure):
    """A regmatch_t structure"""
    _fields_ = [
        ('rm_so', regoff_t),
        ('rm_eo', regoff_t),
    ]

# a pointer type to the regmatch_t structure. This ist just the
# same thing as needed for the regex_p type
regmatch_p = POINTER(regmatch_t)

class regaparams_t(Structure):
    """A regaparams_t structure used for approximate matching
    functions.

    This class is internal and not part of the API and should
    therefore not be used.
    """
    _fields_ = [
        ('cost_ins', c_int),
        ('cost_del', c_int),
        ('cost_subst', c_int),
        ('max_cost', c_int),
        ('max_ins', c_int),
        ('max_del', c_int),
        ('max_subst', c_int),
        ('max_err', c_int)
   ]

regaparams_p = POINTER(regaparams_t)

class regamatch_t(Structure):
    """
        A regamatch_t structure
        used for approximate matching functions
    """
    _fields_ = [
        ('nmatch',c_size_t),
        ('pmatch', regmatch_p),
        ('cost', c_int),
        ('num_ins', c_int),
        ('num_del', c_int),
        ('num_subst', c_int)
   ]

regamatch_p = POINTER(regamatch_t)

# function definitions

# the regcomp() functions
libtre.regncomp.argtypes = [regex_p, POINTER(c_char), c_size_t, c_int]
libtre.regwncomp.argtypes = [regex_p, POINTER(c_wchar), c_size_t, c_int]

libtre.regfree.restype = None
libtre.regfree.argtypes = [regex_p]

# regexec() functions
libtre.regnexec.argtypes = [regex_p, POINTER(c_char), c_size_t, c_size_t, POINTER(regmatch_t), c_int]
libtre.regwnexec.argtypes = [regex_p, POINTER(c_wchar), c_size_t, c_size_t, POINTER(regmatch_t), c_int]

# tre_version()
libtre.tre_version.argtypes = []
libtre.tre_version.restype = c_char_p

# approximate matching functions
libtre.reganexec.argtypes = [regex_p, POINTER(c_char), c_size_t,
                             regamatch_p, regaparams_t, c_int]
libtre.regawnexec.argtypes = [regex_p, POINTER(c_wchar), c_size_t,
                              regamatch_p, regaparams_t, c_int]

def _get_specialization(string):
    """Returns tuple of (string_type, reg_function) that is used
    to match the strings.
    This is because TRE can match both char and wchar and
    we need to decide which to use."""
    if isinstance(string, unicode):
        return c_wchar, libtre.regwnexec
    else:
        return c_char, libtre.regnexec

class Match(object):
    def __init__(self, match, cost=None, num_ins=None, num_del=None, num_subst=None):
        self.match = match
        if cost is not None:
            self.cost = cost
            self.num = (num_ins, num_del, num_subst)

    def groups(self):
        return self.match[1:]

    def group(self, index):
        return self.match[index]

class TREPattern(object):
    """This class represents a compiled regular expression"""
    def __init__(self, pattern, flags=0):
        """
        Constructor - see, the signature is the same as of re.compile
        that can be very useful to retain API compatibility.
        Note, the flags aren't yet implemented - REG_EXTENDED is used
        for everything instead.
        """
        if isinstance(pattern, str):
            string_type = c_char
            reg_function = libtre.regncomp
        elif isinstance(pattern, unicode):
            string_type = c_wchar
            reg_function = libtre.regwncomp
        else:
            raise TypeError("first argument must be string or unicode")

        # the real compiled regex - a regex_t instance
        self.preg = byref(regex_t())

        pattern_buffer = (string_type * len(pattern))()
        pattern_buffer.value = pattern
        result = reg_function(self.preg, pattern_buffer, len(pattern),
                              REG_EXTENDED)

        if reg_errcode_t[result] != 'REG_OK':
            if reg_errcode_t[result] in ('REG_EBRACK', 'REG_EPAREN',
                    'REG_EBRACE'):
                raise sre_constants.error("unbalanced parenthesis")
            else:
                raise sre_constants.error('Parse error, symbol %s code %d' %
                        (reg_errcode_t[result], result))

        # how much memory to reserve
        # refer to the re_nsub field of the regex_t
        self.match_buffers = self.preg._obj.re_nsub + 1

    def search(self, string, pos=None, endpos=None):
        """
        Finds the first match of the pattern
        """
        pmatch = (regmatch_t * self.match_buffers)()
        nmatch = c_size_t(self.match_buffers)
        if endpos:
            string = string[:endpos]
        if pos:
            string = string[pos:]

        string_type = c_char
        reg_function = libtre.regnexec
        if type(string) == unicode:
            string_type = c_wchar
            reg_function = libtre.regwnexec

        string_buffer = (string_type*len(string))()
        string_buffer.value = string

        result = reg_function(self.preg, string_buffer, len(string),
                                 nmatch, pmatch, 0)

        if reg_errcode_t[result] != 'REG_OK':
            if result == REG_NOMATCH:
                return None
            else:
                raise Exception('Exec error, status %s' % result)

        matches = list()
        for match in pmatch:
            match_offsets = (match.rm_so, match.rm_eo)
            chunk = string[match.rm_so:match.rm_eo]
            matches.append(chunk)
        return Match(tuple(matches))

    def approx(self, string, pos=None, endpos=None, cost_ins=0,
               cost_del=0, cost_subst=0, max_costs=0,
               max_ins=0, max_del=0, max_subst=0, max=0):
        """
            Like search but returns an approximate match
        """
        if endpos:
            string = string[:endpos]
        if pos:
            string = string[pos:]

        params = regaparams_t()
        params.cost_ins = cost_ins
        params.cost_del = cost_del
        params.cost_subst = cost_subst
        params.max_cost = max_costs
        params.max_ins = max_ins
        params.max_del = max_del
        params.max_subst = max_subst
        params.max_err = max
        pmatch = (regmatch_t * self.match_buffers)()
        amatch = regamatch_t()
        amatch.nmatch = c_size_t(self.match_buffers)
        amatch.pmatch = pmatch
        string_type = c_char
        reg_function = libtre.reganexec
        if type(string) == unicode:
            string_type = c_wchar
            reg_function = libtre.regawnexec
        string_buffer = (string_type*len(string))()
        string_buffer.value = string

        result = reg_function(self.preg, string_buffer, len(string),
                                  byref(amatch), params, 0)

        if reg_errcode_t[result] != 'REG_OK':
            if result == REG_NOMATCH:
                return None
            else:
                raise Exception('Exec error, status %s' % result)

        matches = list()
        for match in pmatch:
            chunk = string[match.rm_so:match.rm_eo]
            matches.append(chunk)
        return Match(tuple(matches), amatch.cost, amatch.num_ins,
                     amatch.num_del, amatch.num_subst)

    def finditer(self, string):
        """Returns an iterator with all matches"""
        pmatch = (regmatch_t * self.match_buffers)()
        nmatch = c_size_t(self.match_buffers)
        # get the proper types and functions for the string
        string_type, reg_function = _get_specialization(string)

        string_buffer = (string_type * len(string))()
        string_buffer.value = string

        # loop until no matches are found (REG_NOMATCH)
        while True:
            result = reg_function(self.preg, string_buffer, len(string),
                    nmatch, pmatch, 0)

            if reg_errcode_t[result] == 'REG_NOMATCH':
                raise StopIteration
            elif reg_errcode_t[result] != 'REG_OK':
                raise sre_constants.error('Exec error')

            for match in pmatch:
                yield string[match.rm_so:match.rm_eo]
                # move string offset
                string = string[match.rm_eo:]
                string_buffer = (string_type * len(string))()
                string_buffer.value = string

    def findall(self, string):
        """Returns all matches in a list"""
        return list(self.finditer(string))

    def __del__(self):
        """Free any allocated preg structures"""
        if hasattr(self, 'preg'):
            libtre.regfree(self.preg)

def compile(*args, **kwargs):
    """Returns a compiled pattern.
    Compiled patterns passed to this function are
    returned without changes"""
    pattern = args[0]
    if isinstance(pattern, TREPattern):
        return pattern
    return TREPattern(*args, **kwargs)

if __name__ == '__main__':
    # this module is not meant to run stand-alone, so just display
    # the version of TRE it uses.
    # This can also be seen as a small self-test which shows whether
    # TRE can be called at all
    print libtre.tre_version()
