Description
===========

Indigo-dc python-synchrepos is under active development taking as groundwork the project
Openstack python-cinderclient and Stackops python-automationclient, therefore to
recreate the current project you need to clone this one throught the command 
``https://github.com/indigo-dc/python-syncrepos`` in your OpenStack and/or OpenNebula 
platforms and then follow the guide ``How to test``:


How to test
===========

Enviroment
----------

This project has been tested under the next environment

1. Ubuntu 14.04
2. vagrant ONE 4.12 -  docker driver ``https://github.com/indigo-dc/onedock/tree/master/vagrant`` 
3. devstack OpenStack - docker driver ``https://wiki.openstack.org/wiki/Docker#Configure_DevStack_to_use_Nova-Docker``

Docker Hub repository and Webhooks
----------------------------------

Be sure you have a Docker Hub repository, just log in ``https://hub.docker.com/`` click in
``Create Repository`` button, enter the information required, at the end your new repository
should look like as ``ouruser/namerepo``, once created click your new repository and create a 
``Webhook``, set the ``Webhook Name`` and ``Webhook URL``, this url/endpoint should be pointing to 
the current OpenNebula and/or OpenStack installation where the python-synchrepos is going to be 
installed in the form ``http://url_server:port_server/synch``

For more information ``https://docs.docker.com/docker-hub/repos/#webhooks``

Install APP in OpenStack/OpenNebula Platforms
---------------------------------------------

Install the app along your OpenNebula and/or OpenStack platforms, be sure you have the 
package ``python-virtualenv`` in your platforms, otherwise just procced to install it

  ``apt-get install python-virtualenv``

Be sure you have the docker credentials configured correctly and log into the Docker Hub
from the command line

  ``docker login --username=yourhubusername --email=youremail@company.com``

Finally do this few steps once cloned the code:

1. Go to the directory ``python-syncrepos``
2. Once on the directory run the command ``python tools/install_venv.py`` to create a virtual environment
   to work on it
3. Activate the virtual environment with the command ``source .venv/bin/activate``
4. In the file ~/python-syncrepos/reposynch/reposynch.cfg set ``api_endpoint`` and ``api_port`` 
5. Install the python-synchrepos throught the command ``python setup.py install``

That's all!! The app is runnig on OpenStack/OpenNebula platforms, just start to contribute to the API 
or test it as follow

Testing the app
---------------

In path ~/python-syncrepos/reposynch/tests do:

  ``docker build -t ouruser/namerepo .``

``Push`` the new image to your new repos ``docker push ``ouruser/namerepo````, once the image is pushed to your
repository the ``Webhook`` created previously will be fired to our python-synchrepos app to update the 
OpenStack and/or OpenNebula images datastores.
