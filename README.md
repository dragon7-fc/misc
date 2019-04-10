# misc

A playground to note something.

## Tool

* ipmitool

    - How to make in Ubuntu

        ```bash
        apt-get install automake libtool
        ./bootstrap
        ./configure
        make
        ```

    - How to make in Windows
      
        - install Cygwin (32/64) with following package

            ```
            gcc-core
            make
            openssl-devel
            diff
            autoconf
            automake
            m4
            libtool
            libncurses-devel
            libreadline-devel
            perl
            ```

        - Cygwin build

            ```
            ./bootstrap
            ./configure
            make
            ```

        - Create ipmitool package
        
            ```
            .\src\.libs\ipmitool.exe
            C:\cygwin64\bin\cygcrypto-1.0.0.dll
            C:\cygwin64\bin\cyggcc_s-1.dll
            C:\cygwin64\bin\cygncursesw-10.dll
            C:\cygwin64\bin\cygreadline7.dll
            C:\cygwin64\bin\cygwin1.dll
            C:\cygwin64\bin\cygz.dll
            ```
        
    - [Computer Cheese](https://computercheese.blogspot.com/)

* Docker

    - [Docker Cheat Sheet](https://github.com/wsargent/docker-cheat-sheet)

* Beyond Compare

    - __Linux__:
    
        ```bash
        docker run --rm \
        -v $HOME/.Xauthority:/root/.Xauthority \
        -e DISPLAY=:10.0 --net=host \
        --name bcompare \
        -v $HOME/:/home/user \
        zeitgeist/docker-bcompare
        ```

    - __Mac__:
    
        ```
        socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" &
        docker run --rm \
        -e DISPLAY=[HOST_IP]:0 -v "$HOME":"/home/user" \
        zeitgeist/docker-bcompare
        ```

* putty

    - X11 Forwarding

        ```
        Connection -> SSH -> X11 -> Enable X11 Forwarding
        Connection -> SSH -> X11 -> X display location -> localhost:0.0
        ```

* Tmux

    - [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm)

        - [tmux-yank](https://github.com/tmux-plugins/tmux-yank)
        - [Tmux Themepack](https://github.com/jimeh/tmux-themepack)
        - [Tmux Resurrect](https://github.com/tmux-plugins/tmux-resurrect)
        - [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum)

    - [Tmux Cheat Sheet & Quick Reference](https://tmuxcheatsheet.com/)

    - [.tmux.conf](.tmux.conf)

    - [Renew environment variables in tmux](https://babushk.in/posts/renew-environment-tmux.html)

* Minicom

    - Start

        ```bash
        sudo minicom -b [BAUD_RATE] -D /dev/ttyUSB[N] -w
        ```

        |                    | Key                        |
        |--------------------|----------------------------|
        | exit               | `CTRL a, x`                |
        | help menu          | `CTRL a, z`                |
        | current parameters | `CTRL a, p`                |
        | save log           | `minicom -C [LOG_FILE]`    |
        | save log (live)    | `CTRL a, L` -> `CTRL a, L` |

    - Setup

        ```bash
        sudo minicom -s
        ```

* VcSrv

    - clipboard share

        Un-check: `XLaunch -> Extra settings -> Clipboard -> Primary Selection`

* VSCode

    - __Mac__:

        - X11 forwarding for keyboard

            `"keyboard.dispatch": "keyCode"`

* vi

    - [Vi Cheat Sheet](http://www.lagmonster.org/docs/vi2.html)

    |             | command                                                               |
    |-------------|-----------------------------------------------------------------------|
    | edit binary | `vi -b [FILE] ` -> `:%!xxd` -> edit binary... -> `:%!xxd -r` -> `:wq` |


* U-Boot

    - TFTP flash

        `setenv ipaddr [HOST_IP]; setenv serverip [SERVER_IP]; protect off all; erase all; tftpboot [FLASH_MEM_ADDR] [SERVER_IP]:[FOM_FILE]`

        __NOTE__: [FLASH_MEM_ADDR]
        
            AST2500: 20000000

* linux

    - CONFIG_IPMI_PANIC_EVENT

        `Device Drivers > Character devices > IPMI top-level message handler > Generate a panic event to all BMCs on a panic`

    - Rebuild kernel

        - Download linux kernle (ex. linux-x.xx.xx.tar.gz)
        - Untar

            `tar Jxvf linux-x.xx.xx.tar.gz`
        - Configuration

            ```bash
            mv linux-x.xx.xx /usr/src/kernels
            cd /usr/src/kernels/linux-x.xx.xx
            cp /boot/config-xxx .config
            make menuconfig
            ```
        - Build kernel and modules

            ```bash
            make -j N bzImage (N threads)
            make -j N modules (N threads)
            ll arch/x86_64/boot/bzImage
            ```
        - Install modules

            ```bash
            make modules_install
            ll /lib/modules/
            ```
        - install kernel
            
            `make install`
        - (Optional) Generate GRUB boot menu

            `grub2-mkconfig -o /boot/grub2/grub.cfg`

        - reboot
        - `unaame -r` to see new kernel version

    - sysctl

        - kernel parameters
            
            `/proc/sys`
        
        - register/unregister
        
            `include/linux/sysctl.h`

            ```c
            /* A sysctl table is an array of struct ctl_table: */
            struct ctl_table 
            {
                const char *procname;		/* Text ID for /proc/sys, or zero */
                void *data;
                int maxlen;
                umode_t mode;
                struct ctl_table *child;	/* Deprecated */
                proc_handler *proc_handler;	/* Callback for text formatting */
                struct ctl_table_poll *poll;
                void *extra1;
                void *extra2;
            };

            struct ctl_table_header *register_sysctl_table(struct ctl_table * table);

            void unregister_sysctl_table(struct ctl_table_header * table);
            ```

    - init

        `/etc/inittab`

- i2c-tools

    |                    | command                                         |
    |--------------------|-------------------------------------------------|
    | scan bus           | `i2cdetect -l`                                  |
    | scan slave address | `i2cdetect -y [BUS]`                            |
    | dump register      | `i2cdump -y [BUS] [SLAVE_ADDRESS]`              |
    | write register     | `i2cset -f -y [BUS] [SLAVE_ADDRESS] [REGISTER]` |
    | read register      | `i2cget -y [BUS] [SLAVE_ADDRESS] [REGISTER]`    |

* BSOD/Kernel Panic

    - [Cause a Linux Kernel Panic or a Windows BSOD](https://technodrone.blogspot.com/2012/03/cause-linux-kernel-panic-or-windows.html)

        - Windows BSOD

            1. Start Registry Editor.
            1. Locate and then click the following registry subkey:
                `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\kbdhid\Parameters`
            1. On the Edit menu, click Add Value, and then add the following registry entry.
                ```
                Name : CrashOnCtrlScroll 
                Data Type : REG_DWORD 
                Value : 1
                ```
            1. Exit Registry Editor.
            1. Restart the computer. (On a computer that uses a USB keyboard, you do not have to restart the computer. Unplugging the keyboard and plugging it back again is sufficient. After that, the Memory dump file can be generated.)
        
        - Linux Kernel Panic

            `echo c > /proc/sysrq-trigger`

* Git

    - GitHub & Collaboration

        - Pull Request

            - Fork [UPSTREAM_REPO]

            - create a [XXX-BUG-BRANCH] to do something
        
                - `git clone [ORIGIN_REPO_URL]`
                - `git checkout -b [XXX-BUG-BRANCH]`
                - commit changes
                - create Pull Request for [XXX-BUG-BRANCH]
            
        - Sync local, [UPSTREAM_REPO] and [ORIGIN_REPO]

            ```bash
            git remote add upstream [UPSTREAM_REPO_URL]
            git checkout master
            git pull upstream master
            git push origin master
            ```

    - [Git Cheat Sheets](https://services.github.com/on-demand/resources/cheatsheets/)

    |                   | command                      |
    |-------------------|------------------------------|
    | Get older version | `git checkout [COMMIT_HASH]` |

* SVN

    - Create branch

        `svn copy [SRC_REPO] [DEST_REPO] -m '[MSG]'`

* Gitlab

    - Run the image

        ```bash
        sudo docker run --detach \
        --hostname gitlab.example.com \
        --publish 443:443 --publish 80:80 --publish 22:22 \
        --name gitlab \
        --restart always \
        --volume /srv/gitlab/config:/etc/gitlab \
        --volume /srv/gitlab/logs:/var/log/gitlab \
        --volume /srv/gitlab/data:/var/opt/gitlab \
        gitlab/gitlab-ce:latest
        ```

    - Where is the data stored?

        | Local location       | Container location | Usage                                      |
        |----------------------|--------------------|--------------------------------------------|
        | `/srv/gitlab/data`   | `/var/opt/gitlab`  | For storing application data               |
        | `/srv/gitlab/logs`   | `/var/log/gitlab`  | For storing logs                           |
        | `/srv/gitlab/config` | `/etc/gitlab`      | For storing the GitLab configuration files |

* RamDisk

    ```bash
    mkdir /tmp/ramdisk
    chmod 777 /tmp/ramdisk

    mount -t tmpfs -o size=100G tmpfs /tmp/ramdisk/
    ```

* sudo

    ```bash
    visudo

    ##+++>
    XXX      ALL=(ALL) NOPASSWD:ALL
    ##+++<
    ```

* ssh

    ```bash
    sudo apt-get install openssh-server
    ```

* Samba

    ```bash
    sudo apt-get install samba
    sudo apt-get install winbind
    sudo get install libnss-winbind

    ## sudo smbpasswd -a XXX

    sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
    sudo nano /etc/samba/smb.conf

    ##+++>
    [MyShare]
    path =/
    available = yes
    browsealbe = yes
    public = yes
    writable = yes
    ##+++<

    sudo testparm
    sudo service smbd restart
    sudo smbstatus
    ```

* TFTP

    - Server

        ```bash
        sudo apt-get install tftpd-hpa

        sudo nano /etc/default/tftpd-hpa

        ##+++>
        TFTP_USERNAME="tftp"
        TFTP_DIRECTORY="/path/to/tftproot"
        TFTP_ADDRESS="0.0.0.0:69"
        TFTP_OPTIONS="--secure --create"
        RUN_DAEMON="yes"
        ##+++<

        chmod 777 /path/to/tftproot
        chown nobody:nogroup -R /path/to/tftproot
        sudo service tftpd-hpa restart
        ```

    - Client

        |     | command                              |
        |-----|--------------------------------------|
        | put | `tftp -p -l [FILE] [TFTP_SERVER_IP]` |
        | get | `tftp -g -r [FILE] [TFTP_SERVER_IP]` |

* NFS

    - Server

        ```bash
        sudo apt-get install nfs-kernel-server 

        sudo nano /etc/exports

        ##+++>
        /path/to/nfsroot *(rw,no_root_squash)
        ##+++<

        sudo service nfs-kernel-server restart
        ```

    - Client

        `mount -t nfs -o tcp,nolock [NFS_SERVER_IP]:/path/to/nfsroot /path/to/mount`

* Wireshark

    - [How to Decrypt SSL and TLS Traffic Using Wireshark](https://support.citrix.com/article/CTX116557)

        1. Start Wireshark and open the network capture.
        1. From the menu, go to `Edit > Preferences`.
        1. Expand `Protocols` in the `Preferences` window.
        1. Scroll down and select `SSL`.

            - `SSL debug file`: Type a location and file name for a debug file in the SSL debug file field.
            - `RSA keys list`: In the RSA keys list field click `Edit > New` and add the following information:
            
                - `IP address`: is the IP Address of the server/appliance with the private key.
                - `Port`: is usually 443 for SSL/TLS.
                - `Protocol`: is usually HTTP.
                - `Key FIle`: is the location and file name of the private key. This is the key used in the certificate key pair of SSL virtual server for which you are trying to decrypt the traffic. All the SSL key and certificates are saved on NetScaler appliance in config/ssl directory. To use the key to decrypt the traffic it should be saved to the local disk and this path should be specified while decrypting the traffic.
                - `Password`: enter the password that you assigned while exporting the server certificate.

        1. Decrypt the SSL traffic

* VirtualBox

    |          | command                                  |
    |----------|------------------------------------------|
    | start vm | `vboxmanage startvm XXX --type headless` |
    | stop vm  | `vboxmanage controlvm XXX poweroff`      |

* RU

    - [RU.EXE + RU.EFI](http://ruexe.blogspot.com/)

* RWEverything

    - [RWEverything](http://rweverything.com/)

* Proxy setup

    - APT

        ```bash
        touch /etc/apt/apt.conf
        nano /etc/apt/apt.conf

        ##+++>
        Acquire::http::Proxy "http://[PROXY_IP]:[PROXY_PORT]";
        Acquire::https::Proxy "https://[PROXY_IP]:[PROXY_PORT]";
        ##+++<
        ```

    - Bashrc

        ```bash
        nano ~/.bashrc

        ##+++>
        export http_proxy=http://[PROXY_IP]:[PROXY_PORT]
        export https_proxy=http://[PROXY_IP]:[PROXY_PORT]
        export ftp_proxy=ftp://[PROXY_IP]:[PROXY_PORT]
        ##+++<

        source ~/.bashrc
        ```

    - Docker

        ```bash
        nano /etc/systemd/system/docker.service.d/http-proxy.conf

        ##+++>
        [Service]
        Environment="HTTP_PROXY=http://10.32.2.109:3128"
        Environment="HTTPS_PROXY=http://10.32.2.109:3128"
        ##+++<
        ```

        ```bash
        docker build --no-cache --build-arg HTTP_PROXY=$http_proxy \
        --build-arg HTTPS_PROXY=$http_proxy --build-arg NO_PROXY=$no_proxy \
        --build-arg http_proxy=$http_proxy --build-arg https_proxy=$http_proxy \
        --build-arg no_proxy=$no_proxy -t XXX /path/to/Dockerfile/directory
        ```

* Conda

    - Environment Management

        |        | command                   |
        |--------|---------------------------|
        | list   | `conda list`              |
        | create | `conda create -n XXX`     |
        | enter  | `source activate XXX`     |
        | exit   | `source deactivate`       |
        | remove | `conda env remove -n XXX` |

    - Package Management (support pip)

        |         | command 1            | command 2           |
        |---------|----------------------|---------------------|
        | install | `conda install XXX`  | `pip install XXX`   |
        | remove  | `condata remove XXX` | `pip remove XXX`    |

* IPython

    - [Ipython-quick-ref-sheets](https://damontallen.github.io/IPython-quick-ref-sheets/)

    |                | command                                           |
    |----------------|---------------------------------------------------|
    | install kernel | `python -m ipykernel install --user --name [CONDA_ENV] --display-name "XXX"` |
    | remote open    | `jupyter lab --allow-root --ip='' --no-browser &` |
    | list           | `jupyter notebook list`                           |
    | stop           | `jupyter notebook stop [PORT]`                    |

* ROS

    - [ROS Wiki](http://wiki.ros.org/)
    - [ROS Answers](http://answers.ros.org/)
    - [ROS Cheat Sheet](https://github.com/ros/cheatsheet/releases/download/0.0.1/ROScheatsheet_catkin.pdf)
    - [A gentle Introduction to ROS](https://cse.sc.edu/~jokane/agitr/)

## Language

* Shell

    - [An A-Z Index of the Linux command line](https://ss64.com/bash/)
    - [Terminal Cheatsheet for Mac (Basics)](https://github.com/0nn0/terminal-mac-cheatsheet)
    - [.bashrc PS1 generator](http://bashrcgenerator.com/)
    - [Bash Beginners Guide](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
    - [Bash Programming HOWTO](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)
    - [Regexr — Learn Regular Expressions](http://regexr.com/)
    - [Bash scripting cheatsheet](https://devhints.io/bash)

    |             | command 1         | command 2   | command 3           | command 4        |
    |-------------|-------------------|-------------|---------------------|----------------- |
    | view binary | `xxd -g 1 [FILE]` | `hd [FILE]` | `hexdump -C [FILE]` | `od -t x1 [FILE]`|

* Python

    - [The Python Tutorial ](https://docs.python.org/3/tutorial/)
    - [The Python Language and Library References](https://docs.python.org/3/index.html)
    - [Third-Party Library Documentation](https://readthedocs.org/)
    - [Doug Hellmann](https://doughellmann.com/blog/)
    - [Eli Bendersky](http://eli.thegreenplace.net/)
    - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
    - [A summary of python code style conventions](https://development.robinwinslow.uk/2014/01/05/summary-of-python-code-style-conventions/)
    - Numpy

        - [NumPy Manual](https://docs.scipy.org/doc/numpy-1.13.0/contents.html)
        - [NumPy User Guide](https://docs.scipy.org/doc/numpy-1.13.0/user/index.html)
        - [NumPy Reference](https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html#reference)
        - [Scipy Lectures](http://www.scipy-lectures.org/intro/numpy/index.html)

    - Pandas

        - [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

* C++

    - [Modern C++ Coding Guidelines](https://github.com/Microsoft/AirSim/blob/master/docs/coding_guidelines.md)
    - [Google C++ Style Guideline](https://google.github.io/styleguide/cppguide.html)

* Tensorflow

    - [TensorFlow-Tutorials](https://github.com/Hvass-Labs/TensorFlow-Tutorials)
    - [TensorFlow.js Examples](https://github.com/tensorflow/tfjs-examples)
    - [Machine Learning Notebooks](https://github.com/ageron/handson-ml)

* Database

    - [SQLite vs MySQL vs PostgreSQL: A Comparison Of Relational Database Management Systems](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems)

## Article
- [Quick Guide to Build a Recommendation Engine in Python](https://www.analyticsvidhya.com/blog/2016/06/quick-guide-build-recommendation-engine-python/)
- [Probability and Statistics - 假設檢定：基本流程總整理 Process of Hypothesis Testing Statistics](http://mropengate.blogspot.com/2015/03/hypothesis-testing-p-value.html)
- [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)
- [Data Science Tutorials](https://www.topcoder.com/community/data-science/data-science-tutorials/)

## Interview
- [LeetCode](https://leetcode.com/): The World's Leading Online Programming Learning Platform
- [Grammarly](https://www.grammarly.com/): Free Writing Assistant
- [Hemingway App](http://www.hemingwayapp.com/): Makes your writing bold and clear.
- [Sejda](https://www.sejda.com/sign-pdf): Fill and Sign PDF Online Free