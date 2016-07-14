YoLog !
=======
.. image:: https://badge.fury.io/py/yolog.png
  :target: https://badge.fury.io/py/yolog

Beautify your git logs !

Here is how default git logs look like:

.. image:: https://raw.githubusercontent.com/karandesai-96/yolog/master/docs/ordinary.png

Yolog wraps over standard git log and represents commit message history in a compact manner. It provides a
visualization of commit graph, and shows refs, tags and unmerged branches altogether. A yolog powered git log looks
like this:

.. image:: https://raw.githubusercontent.com/karandesai-96/yolog/master/docs/yolog-powered.png


Installation
------------
Obtain stable release from PyPI
::
  pip install yolog

Alternatively, to obtain the bleeding edge version, clone the repo and build it from source:
::
  git clone https://www.github.com/karandesai-96/yolog
  cd yolog && python setup.py install


Usage
-----

* To view yolog powered git log, simply execute ``yolog`` in terminal.

* For brief instructions, execute ``yolog -h`` or ``yolog --help`` in terminal.

* For changing color of any attribute, execute command of format ``yolog config attribute COLOR``.

  - Alternatively, ``-c`` or ``--config`` work as well.
  - ``attribute`` can be one of: ``author, date, description, hash, refs``
  - ``COLOR`` can be one of: ``RED, GREEN, YELLOW, BLUE, CYAN, PURPLE, BLACK, WHITE``
  - Arguments ``attribute`` and ``COLOR`` are case insensitive.

.. image:: https://raw.githubusercontent.com/karandesai-96/yolog/master/docs/color-changing.png

* It also accepts arguments which are used to filter output. These arguments are same as those accepted by standard
git log.

Here are the most common used ones:

+-------------------------------------+---------------------------------------------------------+
|          Command Example            |                      Description                        |
+=====================================+=========================================================+
| ``yolog -n N``                      | Display recent ``N`` commits.                           |
+-------------------------------------+---------------------------------------------------------+
| ``yolog --skip N``                  | Skip recent ``N`` commits and display further.          |
+-------------------------------------+---------------------------------------------------------+
| ``yolog --author "john\ doe"``      | Filter commits according to author.                     |
|                                     | Part of name / whole will be accepted.                  |
+-------------------------------------+---------------------------------------------------------+
| ``yolog --before dd-mmm-yyyy``      | Display commits before this date.                       |
|                                     |                                                         |
| ``yolog --until dd/mmm/yyyy``       | Hyphen (-) or slash (/) can be used interchangeably.    |
+-------------------------------------+---------------------------------------------------------+
| ``yolog --after dd/mmm/yyyy``       | Display commits after this date.                        |
|                                     |                                                         |
| ``yolog --since dd-mmm-yyyy``       | Hyphen (-) or slash (/) can be used interchangeably.    |
+-------------------------------------+---------------------------------------------------------+
| ``yolog --grep "foo\ bar"``         | Display commits with "foo bar" in their description.    |
+-------------------------------------+---------------------------------------------------------+

* Any of these can be combined together and used.
* ``=`` can be optionally used in args as: ``yolog --skip=10``
* Regular expressions are also accepted in ``grep`` and ``author``.
* Use inverted commas and escape character if using whitespace: ``yolog --grep "fixes\ bug"``

Features
--------

- Tabulated commit history with shortened hashes, author, date and commit message (refs included if present).
- Colored fields for better readability, with visualization of commit graph.
- Vertical as well as horizontol pagination for longer commit history / smaller terminal window.
- Flexibility to change color of any part of log by a single command.

Contributing
------------

Feel free to file bugs, ask questions and suggest enhancements through Issues and Pull Requests !

License
-------

Yolog is released under MIT 2016 License.
