==============
TRE for Python
==============

This project does not really have a name yet, but will provide a
pure Python binding (via ctypes) to TRE_.

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
test, you can also run the unit tests, see the Testing_.

::

  >>> import tre as re
  >>> # use re just as usual

From here you can use TRE just as you would use the normal Python
regular expression engine. You can use ``dir(tre)`` to look what
this binding provides as well as you can call ``help()`` on the
objects to get their on-line help.

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
planned.

--------------------------
Building the documentation
--------------------------

The documentation of this binding is written in reStructuredText_ and
can be read in any text editor. Additionally, it can also be converted
into a number of formats, including HTML, by installing the docutils_
package.

To create the HTML version of this document::

  $ rst2html readme.rst > readme.html

This will create a plain HTML file which can be viewed by any browser.

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

To send your changes upstream, either contact the autors to give you
push privileges in the tre Repository or send the patches via mail;
Mercurial contains a Patchbomb_ extension which can send these patches
automatically.

.. _TRE: http://laurikari.net/tre/
.. _nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Mercurial: http://selenic.com/mercurial/
.. _Bitbucket: http://www.bitbucket.org/
.. _Subversion: http://subversion.tigris.org/
.. _Patchbomb: http://www.selenic.com/mercurial/wiki/index.cgi/PatchbombExtension
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _docutils: http://docutils.sourceforge.net/
