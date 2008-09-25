=======================
Mat-TRE: TRE for Python
=======================

Mat-TRE (Breton: *Mat-tre!*, for "*Very good!*") is a pure Python binding
to the TRE_ regular expression library which provides, contrary to the
regular expression engine bundled with Python.

Another advantage of this binding is that it does not need any compilation 
and is written completely in Python, which makes deployment and 
installation easier and makes the whole library easier to understand
and extend.

This could be done because of the ctypes_ library which is shipped with
Python 2.5 and is available to older Python versions separately.

.. contents:: **Table of Contents**

------------
Installation
------------

The installation of the library is straightforward as it uses the
standard Python tools for installing, ``distutils``. To install
it from the source, change into the containing directory and call

::

  $ python setup.py install

But ``mat-tre`` can also be installed from the Python Package Index
using easy_install.

::

  $ easy_install mat-tre

This installs the Python part of the binding, and the procedure is
the same for every operating system. In case you don't have Python
2.5 you still need ctypes - but keep in mind that Mat-TRE is developed
on Python 2.5 so backwards compatibility is not guaranteed.

To use the library you also need the TRE library for C, which is
part of many distributions and can be installed on about any system,
check your package manager or the `TRE download page`_. Note that
you *don't* need the ``-dev`` or ``-devel`` package for Mat-TRE to
work.

Building the documentation
==========================

The documentation of this binding is written in reStructuredText_ and
can be read in any text editor. Additionally, it can also be converted
into a number of formats, including HTML, by installing the docutils_
package.

To create the HTML version of this document::

  $ rst2html README > readme.html

This will create a plain HTML file which can be viewed by any browser.

-----
Usage
-----

This binding is meant to be a drop-in replacement for the regular
expression engine included in Python - RE/SRE.

The only thing you need for using this binding is the TRE shared
library. You can donwload it from the TRE_ homepage, but it is also
included in many distributions.

Running ``tre.py`` directly will output the version of TRE, so you
might want to run it to check whether it works. For a more detailed
test, you can also run the unit tests, see the testing_ chapter.

::

  >>> import tre as re
  >>> # use re just as usual

From here you can use TRE just as you would use the normal Python
regular expression engine. You can use ``dir(tre)`` to look what
this binding provides as well as you can call ``help()`` on the
objects to get their on-line help.

You can also take a look at the unit tests (see testing_) to see
how things are done in TRE.

-------
Testing
-------

The unittests can be run via nose_, so you need nose as a
prerequisite. Change to the folder containing the ``tests`` folder
(or directly into the ``tests`` folder, as nose finds both) and
issue the ``nosetests`` command::

  $ nosetests
  ...
  ----------------------------------------------------------------------
  Ran 3 tests in 0.009s

  OK

An output of ``OK`` shows that all tests passed and the binding is ready
to use. Of course three tests is just the current state, more tests are
planned. It should also be mentioned that the binding may be usable already
even if not all tests pass, since development snapshots are not guaranteed
to pass all tests.

----------
Contribute
----------

We use Mercurial_ for managing the source code as it is a Distributed
Version Control system and provides an easy way for others to work
on this project. The hosting is provided by Bitbucket_, but it
doesn't matter much, since everyone can freely copy the repository from
there.

To clone the whole repository you need the Mercurial client, which
is available for nearly all platforms. The command to get the repository
is::

  $ hg clone https://bitbucket.org/leonidas/tre/
  destination directory: tre
  requesting all changes
  adding changesets
  adding manifests
  adding file changes
  added 14 changesets with 19 changes to 3 files
  updating working directory
  3 files updated, 0 files merged, 0 files removed, 0 files unresolved

Now you have a whole copy of the repository and can work on it very much
like with Subversion. For help with Mercurial_ see its home page.

To send your changes upstream, send the patches via mail; Mercurial 
bundles a Patchbomb_ extension which can send these patches
automatically.

.. _TRE: http://laurikari.net/tre/
.. _nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Mercurial: http://selenic.com/mercurial/
.. _Bitbucket: http://www.bitbucket.org/
.. _Subversion: http://subversion.tigris.org/
.. _Patchbomb: http://www.selenic.com/mercurial/wiki/index.cgi/PatchbombExtension
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _docutils: http://docutils.sourceforge.net/
.. _TRE download page: http://laurikari.net/tre/download.html
.. _ctypes: http://starship.python.net/crew/theller/ctypes/
