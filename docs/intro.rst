Introduction
============

Welcome to Jaskier's documentation.

Basic Concepts
--------------

Jaskier is a simple ``logging`` handler that adds a rich output.

.. code-block:: python

    import logging
    from jaskier import JaskierHandler

    logger = logging.getLogger('my-logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(JaskierHandler())

    logger.debug('Some debug message')
    logger.info('And another info message')
    # etc.
