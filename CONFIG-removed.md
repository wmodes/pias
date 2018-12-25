## Install python 3.6 on Raspberry Pi

Ref: https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f

NOTE: Don't do this. Use Raspbian's default python3.5

1. Install the required build-tools (some might already be installed on your system).

        sudo apt-get update
        sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev

    If one of the packages cannot be found, try a newer version number (e.g. libdb5.4-dev instead of libdb5.3-dev).

2. Download and install Python 3.6. When downloading the source code, select the most recent release of Python 3.6, available on the official site. Adjust the file names accordingly.

        wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
        tar xf Python-3.6.5.tar.xz
        cd Python-3.6.5
        ./configure
        make
        sudo make altinstall

3. Optionally: Delete the source code and uninstall the previously installed packages. When uninstalling the packages, make sure you only remove those that were not previously installed on your system. Also, remember to adjust version numbers if necesarry.

        sudo rm -r Python-3.6.5
        rm Python-3.6.5.tar.xz
        sudo apt-get --purge remove build-essential tk-dev
        sudo apt-get --purge remove libncurses5-dev libncursesw5-dev libreadline6-dev
        sudo apt-get --purge remove libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev
        sudo apt-get --purge remove libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
        sudo apt-get autoremove
        sudo apt-get clean

## Setup default python

Let's figure out what version you are running as your default python and pip.

    $ python --version
    Python 2.7.13
    $ pip2.7 --version
    pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)

And let's find out where some things are located:

    $ ls -l python* pip*
    -rwxr-xr-x 1 root root     292 Feb 26  2018 pip
    -rwxr-xr-x 1 root root     292 Feb 26  2018 pip2
    -rwxr-xr-x 1 root root     293 Feb 26  2018 pip3
    -rwxr-xr-x 1 root root   34760 Sep 27 05:07 pipanel
    lrwxrwxrwx 1 root root       9 Jan 24  2017 python -> python2.7
    lrwxrwxrwx 1 root root       9 Jan 24  2017 python2 -> python2.7
    -rwxr-xr-x 1 root root 3166320 Sep 26 10:42 python2.7
    lrwxrwxrwx 1 root root       9 Jan 20  2017 python3 -> python3.5
    -rwxr-xr-x 2 root root 3976256 Sep 27 09:25 python3.5
    -rwxr-xr-x 2 root root 3976256 Sep 27 09:25 python3.5m
    lrwxrwxrwx 1 root root      10 Jan 20  2017 python3m -> python3.5m

Okay, so we need to move pip and then relink both to the 3.6 versions.

    sudo mv /usr/bin/pip /usr/bin/pip2.7
    sudo mv /usr/bin/pip3 /usr/bin/pip3.5
    sudo ln -sf python3.5 python
    sudo ln -sf python3.5 python3
    sudo ln -sf pip3.5 pip
    sudo ln -sf pip3.5 pip3

And then check our work:

    $ python --version
    Python 3.5.3
    $ pip --version
    pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.5)

Arguably, we could have setup a venv instead, but since we expect the pi to run headlessly, this will simplify things.