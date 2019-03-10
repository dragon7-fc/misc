# misc

A playground to note something.

## Tool

* ipmitool

    - How to make in Ubuntu

        ```
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

* Beyond Compare

    - __Linux__:
    
        ```
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

* Tmux

    - [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm)

        - [tmux-yank](https://github.com/tmux-plugins/tmux-yank)
        - [Tmux Themepack](https://github.com/jimeh/tmux-themepack)
        - [Tmux Resurrect](https://github.com/tmux-plugins/tmux-resurrect)
        - [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum)

    - [Tmux Cheat Sheet & Quick Reference](https://tmuxcheatsheet.com/)

    * [.tmux.conf](.tmux.conf)

* VcSrv

    - clipboard share

        Un-check: `XLaunch -> Extra settings -> Clipboard -> Primary Selection`

* VSCode

    - __Mac__:

        - X11 forwarding for keyboard

            `"keyboard.dispatch": "keyCode"`

* linux

    - CONFIG_IPMI_PANIC_EVENT

        `Device Drivers > Character devices > IPMI top-level message handler > Generate a panic event to all BMCs on a panic`

* BSOD/Kernel Panic

    - [Cause a Linux Kernel Panic or a Windows BSOD](https://technodrone.blogspot.com/2012/03/cause-linux-kernel-panic-or-windows.html)

        - Windows BSOD

            1. Start Registry Editor.
            2. Locate and then click the following registry subkey:
                `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\kbdhid\Parameters`
            3. On the Edit menu, click Add Value, and then add the following registry entry.
                ```
                Name : CrashOnCtrlScroll 
                Data Type : REG_DWORD 
                Value : 1
                ```
            4. Exit Registry Editor.
            5. Restart the computer. (On a computer that uses a USB keyboard, you do not have to restart the computer. Unplugging the keyboard and plugging it back again is sufficient. After that, the Memory dump file can be generated.)
        
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

            ```
            git remote add upstream [UPSTREAM_REPO_URL]
            git checkout master
            git pull upstream master
            git push origin master
            ```

    - [Git Cheat Sheets](https://services.github.com/on-demand/resources/cheatsheets/)

* SVN

    - Create branch

        `svn copy [SRC_REPO] [DEST_REPO] -m '[MSG]'`

* Gitlab

    - Run the image

        ```
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

    ```
    mkdir /tmp/ramdisk
    chmod 777 /tmp/ramdisk

    mount -t tmpfs -o size=100G tmpfs /tmp/ramdisk/
    ```

* sudo

    ```
    visudo

    ##+++>
    XXX      ALL=(ALL) NOPASSWD:ALL
    ##+++<
    ```

* ssh

    ```
    sudo apt-get install openssh-server
    ```

* Samba

    ```
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

        ```
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

        - put

            `tftp -p -l [FILE] [TFTP_SERVER_IP]`

        - get

            `tftp -g -r [FILE] [TFTP_SERVER_IP]`

* NFS

    - Server

        ```
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
        2. From the menu, go to `Edit > Preferences`.
        3. Expand `Protocols` in the `Preferences` window.
        4. Scroll down and select `SSL`.

            - `SSL debug file`: Type a location and file name for a debug file in the SSL debug file field.
            - `RSA keys list`: In the RSA keys list field click `Edit > New` and add the following information:
            
                - `IP address`: is the IP Address of the server/appliance with the private key.
                - `Port`: is usually 443 for SSL/TLS.
                - `Protocol`: is usually HTTP.
                - `Key FIle`: is the location and file name of the private key. This is the key used in the certificate key pair of SSL virtual server for which you are trying to decrypt the traffic. All the SSL key and certificates are saved on NetScaler appliance in config/ssl directory. To use the key to decrypt the traffic it should be saved to the local disk and this path should be specified while decrypting the traffic.
                - `Password`: enter the password that you assigned while exporting the server certificate.

        5. Decrypt the SSL traffic

* VirtualBox

    - Start VM

        `vboxmanage startvm XXX --type headless`

    - Stop VM

        `vboxmanage controlvm XXX poweroff`

* RU

    - [RU.EXE + RU.EFI](http://ruexe.blogspot.com/)

* RWEverything

    - [RWEverything](http://rweverything.com/)

* Proxy setup

    - APT

        ```
        touch /etc/apt/apt.conf
        nano /etc/apt/apt.conf

        ##+++>
        Acquire::http::Proxy "http://[PROXY_IP]:[PROXY_PORT]";
        Acquire::https::Proxy "https://[PROXY_IP]:[PROXY_PORT]";
        ##+++<
        ```

    - Bashrc

        ```
        nano ~/.bashrc

        ##+++>
        export http_proxy=http://[PROXY_IP]:[PROXY_PORT]
        export https_proxy=http://[PROXY_IP]:[PROXY_PORT]
        export ftp_proxy=ftp://[PROXY_IP]:[PROXY_PORT]
        ##+++<

        source ~/.bashrc
        ```

    - Docker

        ```
        nano /etc/systemd/system/docker.service.d/http-proxy.conf

        ##+++>
        [Service]
        Environment="HTTP_PROXY=http://10.32.2.109:3128"
        Environment="HTTPS_PROXY=http://10.32.2.109:3128"
        ##+++<
        ```

        ```
        docker build --no-cache --build-arg HTTP_PROXY=$http_proxy \
        --build-arg HTTPS_PROXY=$http_proxy --build-arg NO_PROXY=$no_proxy \
        --build-arg http_proxy=$http_proxy --build-arg https_proxy=$http_proxy \
        --build-arg no_proxy=$no_proxy -t XXX /path/to/Dockerfile/directory
        ```

* Conda

    - Environment Management

        - List

            `conda list`
        
        - Create

        `conda create -n XXX`

        - Enter

            `source activate XXX`

        - Exit

            `source deactivate`

        - Remove

            `conda env remove -n XXX`

    - Package Management (support pip)

        - Install

            `conda install XXX`

            `pip install XXX`

        - remove

            `condata remove XXX`

            `pip remove XXX`

* IPython

    - Install kernel

        `python -m ipykernel install --user --name [CONDA ENV] --display-name "XXX"`

    - Remote Open

        `jupyter lab --allow-root --ip='' --no-browser &`

    - List

        `jupyter notebook list`

    - Stop

        `jupyter notebook stop [PORT]`

* ROS

    - [ROS Wiki](http://wiki.ros.org/)
    - [ROS Answers](http://answers.ros.org/)
    - [ROS Cheat Sheet](https://github.com/ros/cheatsheet/releases/download/0.0.1/ROScheatsheet_catkin.pdf)
    - [A gentle Introduction to ROS](https://cse.sc.edu/~jokane/agitr/)

## GitHub
- [TensorFlow-Tutorials](https://github.com/Hvass-Labs/TensorFlow-Tutorials)
- [Machine Learning Notebooks](https://github.com/ageron/handson-ml)
- [TensorFlow.js Examples](https://github.com/tensorflow/tfjs-examples)

## Article
- [Quick Guide to Build a Recommendation Engine in Python](https://www.analyticsvidhya.com/blog/2016/06/quick-guide-build-recommendation-engine-python/)
- [Probability and Statistics - 假設檢定：基本流程總整理 Process of Hypothesis Testing Statistics](http://mropengate.blogspot.com/2015/03/hypothesis-testing-p-value.html)
- [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)
- [Data Science Tutorials](https://www.topcoder.com/community/data-science/data-science-tutorials/)
- [A summary of python code style conventions](https://development.robinwinslow.uk/2014/01/05/summary-of-python-code-style-conventions/)

## Interview
- [LeetCode](https://leetcode.com/): The World's Leading Online Programming Learning Platform
- [Grammarly](https://www.grammarly.com/): Free Writing Assistant
- [Hemingway App](http://www.hemingwayapp.com/): Makes your writing bold and clear.
- [Sejda](https://www.sejda.com/sign-pdf): Fill and Sign PDF Online Free