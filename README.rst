YoLog !
=======
.. image:: https://badge.fury.io/py/yolog.png
  :target: https://badge.fury.io/py/yolog

Beautify your git logs !

Here is how default git logs look like:

.. image:: http://raw.githubusercontent.com/karandesai-96/yolog/master/docs/original.png

Yolog wraps over standard git log and represents commit message history in a compact 
manner. It provides a visualization of commit graph, and shows refs, tags and unmerged 
branches altogether. A yolog powered git log looks like this:

.. image:: http://raw.githubusercontent.com/karandesai-96/yolog/master/docs/yolog-powered.png

Installation
------------
Obtain stable release from PyPI
::
  pip install yolog

Perform this manual configuration for the first time, by opening python command line:

.. code-block:: python

  import yolog
  yolog.configure()

For turning it off/ uninstalling, open python command line and unconfigure in same manner:

.. code-block:: python

  import yolog
  yolog.unconfigure()


Usage
-----

To view yolog powered git log, simply execute ``git yolog`` in terminal.

It also accepts arguments which are used to filter output. 
These arguments are same as those accepted by standard git log, for example:
::
  git yolog -11                     // show recent eleven commits
  git yolog --skip=11               // skip recent eleven commits
  git yolog --since="3 weeks ago"
  git yolog --after="28 Nov 2016"
  git yolog --author="Karan Desai"

... and many more, refer `git-log documentation <https://git-scm.com/docs/git-log>`_ 
for more info about these arguments.

Features
--------

- Tabulated commit history with shortened hashes, author, date and commit message (refs included if peresnt).
- Colored fields for better readability, with visualization of commit graph.
- Vertical as well as horizontol pagination for longer commit history / smaller terminal window.
