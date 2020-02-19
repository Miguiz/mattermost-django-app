Mattermost Django apps made for Nadine Co-Working github project
================================================================

| This is a simple Mattermost Django apps for adding user, removing user and changing the password of one user on your Mattermost server.
| This apps works with the Mattermost API (see `Users Mattermost API`_).

.. _Users Mattermost API: https://api.mattermost.com/#tag/users

Requirements
~~~~~~~~~~~~

* Python 3.6
* One Django site
* Postgresql
* Mattermost Server

.. inclusion-stop

Quick install in your project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download the Mattermost App source code from Gitlab:

::

   $ git clone https://github.com/Miguiz/mattermost-django-app.git

Copy the Mattermost App to your Django site:

::

   $ cd mattermost-django-app
   $ cp mattermost path/to/your/django/site

Install all the requirements:

::

   $ pwd
   .../my-django-site
   $ cd mattermost
   $ pip3 install -r requirements.txt

Then use your favorite text editor to fill the settings:

- Add and fill Mattermost constants (see back) in the Django site settings:

::

   $ pwd
   .../my-django-site
   $ nano settings.py

- or set it directely in the Mattermost App settings:

::

   $ pwd
   .../my-django-site/mattermost
   $ nano settings.py


+--------------------------+---------------------------------+---------------------------------------------------------------------------------+
| Key                      | Default Value                   | Description                                                                     |
+==========================+=================================+=================================================================================+
| MATTERMOST_HOST          | your-mattermost-url.com         | Set with the mattermost server domain                                           |
+--------------------------+---------------------------------+---------------------------------------------------------------------------------+
| MATTERMOST_PORT          | 8065                            | Set with the mattermost server port (in digit, no characters)                   |
+--------------------------+---------------------------------+---------------------------------------------------------------------------------+
| MATTERMOST_ADMIN         | admin                           | Set with the mattermost user with admin right (needed if no token key)          |
+--------------------------+---------------------------------+---------------------------------------------------------------------------------+
| MATTERMOST_PASSWORD      | password                        | Set with the mattermost admin password (needed if no token key)                 |
+--------------------------+---------------------------------+---------------------------------------------------------------------------------+
| MATTERMOST_TOKEN         | None                            | Set with the mattermost admin token connection (set None if no token)           |
+--------------------------+---------------------------------+---------------------------------------------------------------------------------+
| MATTERMOST_USE_HTTPS     | True                            | Set False if your mattermost serveur only use HTTP                              |
+--------------------------+---------------------------------+---------------------------------------------------------------------------------+
| MATTERMOST_SSL_IS_SIGNED | True                            | Set False if your ssl certificate is not certified                              |
+--------------------------+---------------------------------+---------------------------------------------------------------------------------+
| MATTERMOST_USER_TEAM     | None                            | Set the Team name where user need to be registered (set None if no Team name)   |
+--------------------------+---------------------------------+---------------------------------------------------------------------------------+

- You can change to use your own Alerts Manager in the Mattermost App settings:

::

   .../my-django-site/mattermost/settings.py
   ..
   line 3: from .models.alerts import new_membership, ending_membership, changing_membership_password
   ..

- And change the signal name if needed:

::

   .../my-django-site/mattermost/signals.py
   ..
   line 22: @receiver(new_membership)
   line 60: @receiver(ending_membership)
   line 87: @receiver(changing_membership_password)
   ..

Note
----

This app use the `mattermostdriver`_ library.

.. _mattermostdriver: https://vaelor.github.io/python-mattermost-driver/

Authors
-------

-  **Corentin M.** - *Developer* - `Gitlab Profile`_

.. _Gitlab Profile: https://gitlab.beezim.fr/corentin
