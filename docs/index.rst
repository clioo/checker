How to run this project
===========================================
Create a local settings configuration
*************************************
You need to create a local_settings.py so you can automate your check in 
and check out, see an example::

   USERS = {
    'joe': ['you_user@softtek.com', 'your_softtek_password']
   }
   DEBUG = False

See the first item in the list is your **email** and your second item is your 
**password**. It is intended to be run by a pipeline, one user per pipeline 
so you can add your coworkers to this local settings file.

Is that all?
************
Yes, the next step is simply to run this script within docker container, 
see a nice example below::

   docker build -t clioo/checker .
   docker run -e TZ=America/Tijuana --rm clioo/checker bash -c "cd app && python checker.py check_in joe"

Add it to a pipeline
********************

Add this to a pipeline is out of scope, you can use Cron, Jenkins or whatever
CI/CD tool you want to use, you just have to specify in that pipeline, the 
timezone and user target, see this example:

Check in
----------

::

   docker run -e TZ=America/Tijuana --rm clioo/checker bash -c "cd app && python checker.py check_in joe"

Check out
-----------

::

   docker run -e TZ=America/Tijuana --rm clioo/checker bash -c "cd app && python checker.py check_out joe"

.. automodule:: app.checker
   :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:
