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

To obtain the bleeding edge version, clone the repo and build it from source:
::
  git clone https://www.github.com/karandesai-96/yolog
  cd yolog && python setup.py build


Usage
-----

* To view yolog powered git log, simply execute ``yolog`` in terminal.

* For brief instructions, execute ``yolog -h`` or ``yolog --help`` in terminal.

It also accepts arguments which are used to filter output. 
These arguments are same as those accepted by standard git log.
Here are the most common used ones:

+-----------------------------------+---------------------------------------------------------+
|          Command Example          |                      Description                        |
+===================================+=========================================================+
| ``yolog -n``                      | Display recent ``n`` commits.                           |
+-----------------------------------+---------------------------------------------------------+
| ``yolog --skip=n``                | Skip recent ``n`` commits and display further.          |
+-----------------------------------+---------------------------------------------------------+
| ``yolog --author=karan``          | Filter commits according to author. Part of name / whole|
|                                   | will be accepted.                                       |
+-----------------------------------+---------------------------------------------------------+
| ``yolog --before=dd-mmm-yyyy``    | Display commits before this date.                       |
+-----------------------------------+                                                         |
| ``yolog --until=dd/mmm/yyyy``     |                                                         |
+-----------------------------------+---------------------------------------------------------+
| ``yolog --after=dd/mmm/yyyy``     | Display commits after this date.                        |
+-----------------------------------+                                                         |
| ``yolog --since=dd-mmm-yyyy``     |                                                         |
+-----------------------------------+---------------------------------------------------------+
| ``yolog --grep="foo\ bar"``       | Display commits with "foo bar" in their description.    |
+-----------------------------------+---------------------------------------------------------+

* Any of these can be combined together and used.
* Regular expressions are also accepted in ``grep`` and ``author``.
* Use escape character if using whitespace: ``yolog --grep="fixes\ bug"``

Features
--------

- Tabulated commit history with shortened hashes, author, date and commit message (refs included if present).
- Colored fields for better readability, with visualization of commit graph.
- Vertical as well as horizontol pagination for longer commit history / smaller terminal window.

Contributing
------------

Feel free to file bugs, ask questions and suggest enhancements through Issues and Pull Requests !

License
-------

Yolog is released under MIT 2016 License.
