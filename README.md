# misc

A playground to note something.

## Tool

* ipmitool

    - Build

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
                
        - How to built-in OpenSSL 1.0.0 static library
        
            ```bash
            gie clone https://github.com/openssl/openssl
            cd openssl
            git checkout OpenSSL_1_0_0
            ./configure
            make    -> generate ./libcrypto.a
            cd ..
            
            cd ipmitool
            ./configure LIBS='[/path/to/openssl]/libcrypto.a -ldl' --enable-intf-usb
            ldd src/ipmitool    -> check libcrypto.a NOT in the dependency list
            ```
    - [Computer Cheese](https://computercheese.blogspot.com/)
    
    - SOL
        - BIOS
            
            `Advanced -> Serial Port Console Redirection -> Console Redirection Settings`
        - BMC
            1. Get SOL Configuration Parameters
            
                `ipmitool -H <BMC_IP> -U <IPMI_USER> -P <IPMI_PASSWORD> sol info`
            1. Get COM Port Baud Rate from BIOS (Default is 57.6K)
            1. Set SOL volatile-bit-rate
            
                `ipmitool -I lanplus -H <BMC_IP> -U <IPMI_USER> -P <IPMI_PASSWORD> sol set volatile-bit-rate xx.x`
            1. Activate IPMI SOL
            
                `ipmitool -I lanplus -H <BMC_IP> -U <IPMI_USER> -P <IPMI_PASSWORD> sol activate nokeepalive`
            1. Terminate connection
            
                `~.` or `ipmitool -I lanplus -H <BMC_IP> -U <IPMI_USER> -P <IPMI_PASSWORD> sol deactivate`

* Docker

    - [Docker Cheat Sheet](https://github.com/wsargent/docker-cheat-sheet)

    - How do I change the Docker image installation directory?
    
        - Stop docker: `service docker stop`. Verify no docker process is running `ps faux`
        - Double check docker really isn’t running. Take a look at the current docker directory: `ls /var/lib/docker/`
            - Make a backup - `tar -zcC /var/lib docker > /mnt/pd0/var_lib_docker-backup-$(date +%s).tar.gz`
        - Move the `/var/lib/docker` directory to your new partition: `mv /var/lib/docker /new/path/to/docker`
        - Make a symlink: `ln -s /new/path/to/docker /var/lib/docker`
        - Take a peek at the directory structure to make sure it looks like it did before the mv: `ls /var/lib/docker/` (note the trailing slash to resolve the symlink)
        - Start docker back up service `docker start`
        - restart your containers
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
    - xterm 256 color

        ```
        Window -> Colours -> Allow terminal to specify xterm 256-colour mode
        ```

        ```bash
        nano ~/.bashrc

        export TERM=xterm-256color
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
    - Update the DISPLAY environment variable

        `export DISPLAY="`tmux show-env | sed -n 's/^DISPLAY=//p'`"`

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

    - Disable Hardware Flow Control

        `sudo minicom -s` -> `Serial Port Setup` -> `Hardware Flow Control` -> `No`
        
    - [Serial Transfer](http://www.armadeus.org/wiki/index.php?title=Serial_Transfer)
* VcSrv

    - clipboard share

        Un-check: `XLaunch -> Extra settings -> Clipboard -> Primary Selection`

* VSCode

    - __Mac__:

        - X11 forwarding for keyboard

            `"keyboard.dispatch": "keyCode"`

* vi

    - [Vi Cheat Sheet](http://www.lagmonster.org/docs/vi2.html)
    - [VI (Linux Terminal) Help Sheet](https://www.gosquared.com/blog/vi-linux-terminal-help-sheet)

    |             | command                                                               |
    |-------------|-----------------------------------------------------------------------|
    | edit binary | `vi -b [FILE] ` -> `:%!xxd` -> edit binary... -> `:%!xxd -r` -> `:wq` |

* Vim

    - [Vim Cheatsheet](https://alejandrodev.com/vim)
    - [Vim Cheat Sheet](https://vim.rtorr.com/)
    - [VIM Cheat Sheet for Programmers](http://michael.peopleofhonoronly.com/vim/)
    - [Vim Cheat Sheet](vim_cheat_sheet.png)
    - [Graphical vi-vim Cheat Sheet and Tutorial](http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html)
    - [Vimdiff cheatsheet](https://devhints.io/vim-diff)
    - [Learn Vim Progressively](https://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)
    - [Use Vim like an IDE](https://vim.fandom.com/wiki/Use_Vim_like_an_IDE)
    - [Vim Awesome](https://vimawesome.com/)'
    - [Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/)
    - [Vundle, the plug-in manager for Vim](https://github.com/VundleVim/Vundle.vim)
    - ack-vim

        ```bash
        export LC_CTYPE=en_US.UTF-8
        export LC_ALL=en_US.UTF-8
        ```
* U-Boot

    - TFTP flash

        `setenv ipaddr [HOST_IP]; setenv serverip [SERVER_IP]; protect off all; erase all; tftpboot [FLASH_MEM_ADDR] [SERVER_IP]:[ROM_FILE]`

        __NOTE__: [FLASH_MEM_ADDR]
        
            AST2500: 20000000

* linux

    - [UNIX Toolbox](http://cb.vu/unixtoolbox.pdf)
    - [LINUX Administrator’s Quick Reference Card](http://www.cheat-sheets.org/saved-copy/linux_quickref.pdf)
    - [Practical Linux Command Line Reference](http://www.pixelbeat.org/cmdline.html)
    - [Linux Quick Reference Guide](https://perso.crans.org/~raffo/docs/linux-guide.pdf)
    - [Inter Process Communication Tutorial](https://www.tutorialspoint.com/inter_process_communication/index.htm)
    - [Systemd Cheatsheet](https://linux020.nl/l20/Howto/SystemdCheatsheet)
    - [D-Bus Specification](https://dbus.freedesktop.org/doc/dbus-specification.html#type-system)
    - [The new sd-bus API of systemd](http://0pointer.net/blog/the-new-sd-bus-api-of-systemd.html)
    - [Using the DBUS C API](http://www.matthew.ath.cx/misc/dbus)
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
    - [Ubuntu – How to resize root to increase home partition size in ubuntu 16.04 with gparted](https://itectec.com/ubuntu/ubuntu-how-to-resize-root-to-increase-home-partition-size-in-ubuntu-16-04-with-gparted-duplicate/)

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
    - [Git Cheatsheet](https://blog.programster.org/git-cheatsheet)
    - Clone 100 repositories of 1 page of one GitHub organization
    
        `GHUSER=[CHANGEME]; curl "https://api.github.com/orgs/$GHUSER/repos?page=1&per_page=100" | grep -w clone_url | grep -o '[^"]\+://.\+.git' | xargs -L1 git clone`

    |                   | command                      |
    |-------------------|------------------------------|
    | Get older version | `git checkout [COMMIT_HASH]` |

* SVN

    - Create branch

        `svn copy [SRC_REPO] [DEST_REPO] -m '[MSG]'`
    - [Migrating to Git from SVN](https://blog.axosoft.com/migrating-git-svn/)
* Tig

    - [Tig cheatsheet](https://devhints.io/tig)

* Gitlab

    - Install

        ```bash
        sudo docker run --detach \
        --hostname gitlab.example.com \
        --publish 443:443 --publish 80:80 \
        -p 3000:22 -e "GITLAB_SHELL_SSH_PORT=3000" \
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
        
    - Clone Repository
        
        `git clone ssh://git@[GITLAB_IP]:3000/OOO/XXX.git`
        
        __NOTE__: Copy SSH public key from Jenkins.
* Jenkins

    - Install
    
        ```bash
         sudo docker run --name jenkins \
         -d -u root --restart always \
         -p 8080:8080 \
         -v /path/to/jenkins/jenkins-data:/var/jenkins_home \
         -v /var/run/docker.sock:/var/run/docker.sock \
         jenkinsci/blueocean
        ```
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

    - [SSH Cheatsheet](https://cheatsheet.dennyzhang.com/cheatsheet-ssh-a4)
    - SSH login without password
        
        ```bash
        a@A:~> ssh-keygen -t rsa
        
        a@A:~> ssh b@B mkdir -p .ssh
        b@B's password:
        
        a@A:~> cat .ssh/id_rsa.pub | ssh b@B `cat >> .ssh/authorized_keys`
        b@B's password:
        
        a@A:~> ssh b@B
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

        sudo vim /etc/default/tftpd-hpa

        + TFTP_USERNAME="tftp"
        + TFTP_DIRECTORY="/path/to/tftproot"
        + TFTP_ADDRESS="0.0.0.0:69"
        + TFTP_OPTIONS="--secure --create"
        + RUN_DAEMON="yes"

        chmod 777 /path/to/tftproot
        chown nobody:nogroup -R /path/to/tftproot
        sudo service tftpd-hpa restart
        
        # power on auto start
        sudo vim /etc/rc.local
        
        + sleep 30
        + service tftpd-hpa restart
        
        exit 0
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

- FTP

     - Server
         ```
         # Install
         sudo apt update
         sudo apt install vsftpd
         sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.orig

         # Firwall rules
         sudo ufw allow ftp-data
         sudo ufw allow ftp
         sudo ufw status

         # Preparing Space for Files
         sudo mkdir -p /var/ftp
         sudo chown nobody:nogroup /var/ftp
         echo "vsftpd test file" | sudo tee /var/ftp/test.log
         sudo mkdir /var/ftp/pub
         sudo chmod a+rwx /var/ftp/pub

         # enable anonymous write & read
         sudo nano /etc/vsftpd.conf

         ##+++>
         anonymous_enable=YES
         write_enable=YES
         anon_upload_enable=YES
         anon_mkdir_write_enable=YES
         anon_umask=022
         anon_other_write_enable=YES
         anon_root=/var/ftp
         no_anon_password=YES
         hide_ids=YES
         pasv_min_port=40000
         pasv_max_port=50000
         ##+++<
         ```
    - Client

    ```ftp -p [FTP_SERVER_IP]```
* DHCP

    - Server
    
        - install dnsmasq
            
            ```bash
            # setup static ip address
            IF = "eth[x]"  # bind DPCP server interface
            IF_IP = "x.x.x.x/x"  # ip/mask
            
            echo "interface $(IF)" >> /etc/dhcpcd.conf
            echo "static ip_address=$(IF_IP" >> /etc/dhcpcd.conf     
            
            # install dnsmasq
            sudo apt-get install dnsmasq
            
            # setup dnsmasq
            IP_START="x.x.x.x"
            IP_END="x.x.x.x"
            NETMASK="x.x.x.x"
            BMCx_MAC="xx:xx:xx:xx:xx:xx"
            BMCx_IP="x.x.x.x"
            sudo echo "dhcp-range=$(IF),$(IP_START),$(IP_END),$(NETMASK)" >> /etc/dnsmasq.conf
            sudo echo "dhcp-host=$(BMCx_MAC),$(BMCx_IP)" >> /etc/dnsmasq.conf
            
            # start/enable service
            sudo systemctl start dnsmasq
            sudo systemctl enable dnsmasq
            
            # test
            cat /var/lib/misc/dnsmasq.leases
            ```
        - [dnsmasq - ArchWiki](https://wiki.archlinux.org/index.php/dnsmasq)
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

* nmap

    - [Nmap Cheat Sheet](https://www.stationx.net/nmap-cheat-sheet/)
    - To see the SSL/TLS algorithms a server supports

        `nmap --script ssl-enum-ciphers -p 443 [TARGET|IP]`

* curl

    - [CURL CHEATSHEET](https://cheatsheet.dennyzhang.com/cheatsheet-curl-a4)

- iperf

    - [Iperf cheat sheet](https://www.jamescoyle.net/cheat-sheets/581-iperf-cheat-sheet)

- iptables

    - NAT Server
    
        - environment
        
            - ---> eth0 -> eth1 -> BMCx
        
                - eth0(internet): 10.32.4.40
                - eth1(intranet): 192.168.2.2 (ssh user: sysadmin)
        - Setup
        
            ```bash
            BMCx_IP = "x.x.x.x"
            
            # Activate IP-forwarding in the kernel!
            # cat /proc/sys/net/ipv4/ip_forward -> 1
            # echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
            echo 1 > /proc/sys/net/ipv4/ip_forward

            # clear filter table
            sudo iptables -F
            sudo iptables -X
            sudo iptables -Z
            # clear nat table
            sudo iptables -t nat -F
            sudo iptables -t nat -X
            sudo iptables -t nat -Z

            # Connect a private subnet to the internet using NAT
            sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

            # Running a HTTPS Server behind a NAT-router
            sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 \
            -j DNAT --to-destination ${BMCx_IP}:443
            
            # IPMI server
            sudo iptables -t nat -A PREROUTING -i eth0 -p udp --dport 623 \
            -j DNAT --to-destination ${BMCx_IP}:623
            
            # SSH server (ssh -p 2222 sysadmin@10.32.4.40)
            sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 2222 \
            -j DNAT --to-destination ${BMCx_IP}:22
            
            # show filter table
            sudo iptables -L -n -v
            # show nat table
            sudo iptables -t nat -L -n -v
            ```
            
            __NOTE__: can write ot `/etc/rc.local`
* VirtualBox

    |          | command                                  |
    |----------|------------------------------------------|
    | start vm | `vboxmanage startvm XXX --type headless` |
    | stop vm  | `vboxmanage controlvm XXX poweroff`      |
    | list vm  | `VBoxManage list vms`                    |
    | list vm (running) | `VBoxManage list runningvms`    |
* QEMU

    - [QEMU Cheat Sheet](https://gist.github.com/bradfa/3721697)
* Raspbian

    - configuration

        `raspi-config`

    - [Setting up a Raspberry Pi as an access point in a standalone network (NAT)](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)

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

        - CentOS

        ```bash
        nano /etc/systemd/system/docker.service.d/http-proxy.conf

        ##+++>
        [Service]
        Environment="HTTP_PROXY=http://[PROXY_IP]:[PROXY_PORT]"
        Environment="HTTPS_PROXY=http://[PROXY_IP]:[PROXY_PORT]"
        ##+++<
        ```

        - Ubuntu

        ```bash
        nano /etc/default/docker
        
        ##+++>
        export http_proxy="http://[PROXY_IP]:[PROXY_PORT]"
        ##+++<
        
        service docker restart
        ```

        - command

        ```bash
        docker build --no-cache --build-arg HTTP_PROXY=$http_proxy \
        --build-arg HTTPS_PROXY=$http_proxy --build-arg NO_PROXY=$no_proxy \
        --build-arg http_proxy=$http_proxy --build-arg https_proxy=$http_proxy \
        --build-arg no_proxy=$no_proxy -t XXX /path/to/Dockerfile/directory
        ```
    - npm

        ```bash
        npm config set proxy http://[PROXY_IP]:[PROXY_PORT]
        npm config set https-proxy http://[PROXY_IP]:[PROXY_PORT]
        npm set strict-ssl=false
        ```
        
    - Yocto
    
        - [Working Behind a Network Proxy](https://wiki.yoctoproject.org/wiki/Working_Behind_a_Network_Proxy)
        
* Conda

    - Environment Management

        |        | command                   |
        |--------|---------------------------|
        | list   | `conda list`              |
        | create | `conda create -n XXX`     |
        | enter  | `conda activate XXX`     |
        | exit   | `conda deactivate`       |
        | remove | `conda env remove -n XXX` |

    - Package Management (support pip)

        |         | command 1            | command 2           |
        |---------|----------------------|---------------------|
        | install | `conda install XXX`  | `pip install XXX`   |
        | remove  | `condata remove XXX` | `pip remove XXX`    |

* zsh

    - install zsh
    
        `sudo apt-get install zsh`
    - install Oh My Zsh
    
        `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
        
    - install Font: DejaVu Sans Mono for Powerline
    
        - [https://github.com/powerline/fonts/tree/master/DejaVuSansMono](https://github.com/powerline/fonts/tree/master/DejaVuSansMono)
        - download and install `DejaVu Sans Mono for Powerline.ttf`
    - setup putty
    
        - right click -> `Change Settings` -> `Appearance` -> `Font Settings` -> `Change` -> `DejaVu Sans Mono font`
        - right click -> `Change Settings` -> `Appearance` -> `Font Settings` -> `Clear Type`
        - right click -> `Change Settings` -> `Translation` -> `UTF8`
        
    - install powerline
    
        `sudo -E pip install powerline-status`
        
    - configure powerline
    
        ```bash
        mkdir -p ~/.config/powerline/themes/shell
        cp /usr/local/lib/python2.7/dist-packages/powerline/config_files/themes/shell/default.json ~/.config/powerline/themes/shell
        
        nano ~/.config/powerline/themes/shell/default.json
        
        ##--->
                        {
                                "function": "powerline.segments.common.net.hostname",
                                "priority": 10
                        },
                        {
                                "function": "powerline.segments.common.env.user",
                                "priority": 30
                        },
        ##---<
        ##+++>
                        {
                                "function": "powerline.segments.common.time.date",
                                "args": {
                                    "format": "%H:%M:%S"
                                },
                                "priority": 10
                        }
        ##+++<
        ```
    - install plugins

        - zsh-syntax-highlighting
        
            `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`
        - zsh-autosuggestions
        
            `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`
        - zsh-completions
        
            `git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions`
    - configure .zshrc
    
        ```bash
        ##+++>
        # ZSH_THEME="robbyrussell"
        ZSH_THEME="agnoster"
        ##+++<
        
        ##+++>
        # plugins=(git)
        plugins=(git zsh-completions zsh-autosuggestions zsh-syntax-highlighting)
        ##+++<
    
        ##+++>
        export TERM=xterm-256color
        if [[ -r /usr/local/lib/python2.7/dist-packages/powerline/bindings/zsh/powerline.zsh  ]]; then
            source /usr/local/lib/python2.7/dist-packages/powerline/bindings/zsh/powerline.zsh
        fi
        ##+++<
        ```
    - finish
    
        `source ~/.zshrc`      
* Midnight Commander

    - [Cheetsheet for Midnight Commander](http://www.softpanorama.org/OFM/MC/cheetsheet.shtml)

* IPython

    - [Ipython-quick-ref-sheets](https://damontallen.github.io/IPython-quick-ref-sheets/)

    |                | command                                           |
    |----------------|---------------------------------------------------|
    | install kernel | `python -m ipykernel install --user --name [CONDA_ENV] --display-name "XXX"` |
    | remote open    | `jupyter-lab --allow-root --ip=0.0.0.0 --no-browser &` |
    | list           | `jupyter notebook list`                           |
    | stop           | `jupyter notebook stop [PORT]`                    |

* ROS

    - [ROS Wiki](http://wiki.ros.org/)
    - [ROS Answers](http://answers.ros.org/)
    - [ROS Cheat Sheet](https://github.com/ros/cheatsheet/releases/download/0.0.1/ROScheatsheet_catkin.pdf)
    - [A gentle Introduction to ROS](https://cse.sc.edu/~jokane/agitr/)

* Autotools

    - [GNU autotools cheatsheet](https://home.fnal.gov/~neilsen/notebook/autotools/autotools.html)
* CMake

    - [BOTTOM-UP CMAKE INTRODUCTION](https://lowlevelbits.org/bottom-up-cmake-introduction/)
    - [CMake by Example](https://mirkokiefer.com/cmake-by-example-f95eb47d45b1)
* Yocto

    - [Yocto Project Reference Manual](https://www.yoctoproject.org/docs/3.1/ref-manual/ref-manual.html#var-FILES)
    - [Yocto Project Cheatsheet](https://github.com/LetoThe2nd/yoctoproject-cheatsheet)
    - [Quick start guide to kas - best tool for setting up the Yocto projects](https://blog.3mdeb.com/2019/2019-02-07-kas/)
    - Docker

        - Poky Container
    
        ```bash
        sudo docker run --name yocto --rm -it -v /path/to/workdir:/workdir -v /path/to/downloads:/downloads -v /path/to/sstate_cache:/sstate_cache --workdir=/workdir crops/poky
        ```
* OpenBMC
    
    - [OpenBMC cheatsheet](https://github.com/openbmc/docs/blob/master/cheatsheet.md)

## Language

* Shell

    - [An A-Z Index of the Linux command line](https://ss64.com/bash/)
    - [Terminal Cheatsheet for Mac (Basics)](https://github.com/0nn0/terminal-mac-cheatsheet)
    - Bash
        - [.bashrc PS1 generator](http://bashrcgenerator.com/)
        - [Bash Reference Manual](https://tiswww.case.edu/php/chet/bash/bashref.html#Command-Substitution)
        - [Bash scripting cheatsheet](https://devhints.io/bash)
        - Misc

            **Brackets**
            ```
            if [ CONDITION ]    Test construct
            if [[ CONDITION ]]  Extended test construct
            Array[1]=element1   Array initialization
            [a-z]               Range of characters within a Regular Expression
            $[ expression ]     A non-standard & obsolete version of $(( expression  )) [1]
            ```
            [1] http://wiki.bash-hackers.org/scripting/obsolete

            **Curly Braces**
            ```
            ${variable}                             Parameter substitution
            ${!variable}                            Indirect variable reference
            { command1; command2; . . . commandN; } Block of code
            {string1,string2,string3,...}           Brace expansion
            {a..z}                                  Extended brace expansion
            {}                                      Text replacement, after find and xargs
            ```

            **Parentheses**
            ```
            ( command1; command2 )             Command group executed within a subshell
            Array=(element1 element2 element3) Array initialization
            result=$(COMMAND)                  Command substitution, new style
            >(COMMAND)                         Process substitution
            <(COMMAND)                         Process substitution
            ```

            **Double Parentheses**
            ```
            (( var = 78  ))            Integer arithmetic
            var=$(( 20 + 5  ))         Integer arithmetic, with variable assignment
            (( var++  ))               C-style variable increment
            (( var--  ))               C-style variable decrement
            (( var0 = var1<98?9:21  )) C-style ternary operation
            ```
    - [Linux ip Command Networking Cheat Sheet](https://www.linuxtrainingacademy.com/linux-ip-command-networking-cheat-sheet/)
    - [SS – Socket Statistics Commands Cheatsheet](https://neverendingsecurity.wordpress.com/2015/04/13/ss-socket-statistics-commands-cheatsheet/)
    - [7 Linux lspci Command Examples to Get PCI Bus Hardware Device Info](https://www.thegeekstuff.com/2014/04/lspci-examples/)

    |             | command     |
    |-------------|-------------------------------------------------------------------------|
    | read binary | `xxd -g 1 [FILE]` |
    |  | `hd [FILE]`|
    |  | `hexdump -C [FILE]` |
    |  | `od -t x1 [FILE]`|
    | write binary | `echo -n -e \\xHH\\xHH\\xHH > XXX` |
    |  | `printf '\xHH' > XXX` |
    | convert ascii to hex string | `echo "<ASCII_STRING>" \| xxd -ps -c 200 \| tr -d '\n'` |
    |  | `a=<ASCII_STRING>; for ((i=0;i<${#a};i++));do printf %02X \'${a:$i:1};done` |
    |  | `a=<ASCII_STRING>; for letter in $(echo "$a" \| sed "s/\(.\)/'\1 /g");do printf '%x' "$letter";done` |
    | convert hex to ascii string | `echo "<HEX_STRING>" \| xxd -ps -r` |
    | compare binary | `diff <(xxd -g1 OOO.bin) <(xxd -g1 XXX.bin)`   |

* Regular Expression

    - [Regexr — Learn Regular Expressions](http://regexr.com/)
    - [Regexp Syntax Summary](http://www.greenend.org.uk/rjk/tech/regexp.html)
    - [Regex cheatsheet](https://remram44.github.io/regex-cheatsheet/regex.html)
    - [grep (english) Cheat Sheet by TME520](https://www.cheatography.com/tme520/cheat-sheets/grep-english/)
    - [Sed - An Introduction and Tutorial by Bruce Barnett](http://www.grymoire.com/Unix/Sed.html)
    - [AWK Cheat Sheet](https://www.shortcutfoo.com/app/dojos/awk/cheatsheet)
    - [awk (english) Cheat Sheet by TME520](https://www.cheatography.com/tme520/cheat-sheets/awk-english/)
    - [ag - The Silver Searcher, a better UNIX search tool](https://blog.dnsimple.com/2017/07/ag-a-better-unix-search-tool/)
    
    |                                       | command  |
    |---------------------------------------|----------|
    | replace [BRE1] in [PATH]/OOO.XXX file | `find [PATH] -type f -name "OOO.XXX" -print0 \| xargs -0 sed -i 's/[BRE1]/[BRE2]/g'` |

* Batch

    - [List of DOS commands](https://en.wikipedia.org/wiki/List_of_DOS_commands#IF)
    - [A Comparison of Common DOS and Linux Commands](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/4/html/Step_by_Step_Guide/ap-doslinux.html)

* Python

    - [The Python Tutorial ](https://docs.python.org/3/tutorial/)
    - [The Python Language and Library References](https://docs.python.org/3/index.html)
    - [Third-Party Library Documentation](https://readthedocs.org/)
    - [general decorators tutorial](https://realpython.com/primer-on-python-decorators/)
    - Python’s pass-by-assignment scheme isn’t the same as C++’s reference parameters, but it turns out to be very similar to C’s in practice:
        - Immutable arguments act like C’s “by value” mode
        Objects such as integers and strings are passed by object reference (assignment), but since you can’t change immutable objects in place anyhow, the effect is much like making a copy.

        - Mutable arguments act like C’s “by pointer” mode
Objects such as lists and dictionaries are passed by object reference too, which is similar to the way C passes arrays as pointers—mutable objects can be changed in place in the function, much like C arrays.
    - Copy list
        
        - list.copy()
        
            ```python
            new_list = old_list.copy()
            ```
        - list slicing
        
            ```python
            new_list = old_list[:]
            ```
        - list()
        
            ```python
            new_list = list(old_list)
            ```
        - copy.copy()
        
            ```python
            import copy
            new_list = copy.copy(old_list)
            ```
        - list objects
         
            ```python
            import copy
            new_list = copy.deepcopy(old_list)
            ```
    - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
    - [A summary of python code style conventions](https://development.robinwinslow.uk/2014/01/05/summary-of-python-code-style-conventions/)
    - [Python For Data Science Cheat Sheet - Python Basics](https://datacamp-community-prod.s3.amazonaws.com/e30fbcd9-f595-4a9f-803d-05ca5bf84612)
    - [Python For Data Science Cheat Sheet - Importing Data](https://datacamp-community-prod.s3.amazonaws.com/50d31142-3de0-4159-89b9-18b718a728ef)
    - SciPy
    
        - Linear Algebra

            - [Python For Data Science Cheat Sheet - SciPy - Linear Algebra](https://datacamp-community-prod.s3.amazonaws.com/5710caa7-94d4-4248-be94-d23dea9e668f)

        - Numpy

            - [NumPy Manual](https://docs.scipy.org/doc/numpy-1.13.0/contents.html)
            - [NumPy User Guide](https://docs.scipy.org/doc/numpy-1.13.0/user/index.html)
            - [NumPy Reference](https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html#reference)
            - [Scipy Lectures](http://www.scipy-lectures.org/intro/numpy/index.html)
            - [Python For Data Science Cheat Sheet - NumPy Basics](https://datacamp-community-prod.s3.amazonaws.com/e9f83f72-a81b-42c7-af44-4e35b48b20b7)

        - Pandas

            - [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
            - [Python For Data Science Cheat Sheet - Pandas](https://datacamp-community-prod.s3.amazonaws.com/9f0f2ae1-8bd8-4302-a67b-e17f3059d9e8)
            - [Python For Data Science Cheat Sheet - Pandas Basics](https://datacamp-community-prod.s3.amazonaws.com/fbc502d0-46b2-4e1b-b6b0-5402ff273251)

        - Matplotlib

            - [Python For Data Science Cheat Sheet - Matplotlib](https://datacamp-community-prod.s3.amazonaws.com/28b8210c-60cc-4f13-b0b4-5b4f2ad4790b)

    - Seaborn

        - [Python For Data Science Cheat Sheet - Seaborn](https://datacamp-community-prod.s3.amazonaws.com/f9f06e72-519a-4722-9912-b5de742dbac4)
        - [seaborn cheat sheet - Interactive Chaos](https://www.interactivechaos.com/sites/default/files/data/seaborn_cheat_sheet.pdf)

    - Scikit-learn

        - [Python For Data Science Cheat Sheet - Scikit-Learn](https://datacamp-community-prod.s3.amazonaws.com/5433fa18-9f43-44cc-b228-74672efcd116)

    - NLTK

        - [Text Analytics for Beginners using NLTK](https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk)

    - spaCy

        - [spaCy Cheat Sheet: Advanced NLP in Python](https://www.datacamp.com/community/blog/spacy-cheatsheet) 

    - keras

        - [Python For Data Science Cheat Sheet - Keras](https://datacamp-community-prod.s3.amazonaws.com/94fc681d-5422-40cb-a129-2218e9522f17)

    - Flask

        - [how @app.route works](https://ains.co/blog/things-which-arent-magic-flask-part-1.html)
        - [Tutorial - Using Databases with Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
        - [SQL Alchemy](http://docs.sqlalchemy.org/en/latest/) - a Python toolkit for working with SQL
        - [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - a Flask library for using SQLAlchemy with Flask
        - [Flask: The Cheat Sheet](http://flask-cheat-sheet.herokuapp.com/)
 
     - Jinja
     
        - [Jinja Cheat Sheet](https://lzone.de/cheat-sheet/Jinja)

    - [Cheat Sheets for AI, Neural Networks, Machine Learning, Deep Learning & Big Data](https://becominghuman.ai/cheat-sheets-for-ai-neural-networks-machine-learning-deep-learning-big-data-678c51b4b463)

* C/C++

    - [The GNU C Reference Manual - GNU.org](https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html)
    - [Cprogramming.com: Learn C and C++ Programming](https://www.cprogramming.com/)
    - [C++ reference](https://en.cppreference.com/w/)
    - [cplusplus.com - The C++ Resources Network](http://www.cplusplus.com/)
    - [C Reference Cheat Sheet by Ashlyn Black](https://www.cheatography.com/ashlyn-black/cheat-sheets/c-reference/)
    - [Modern C++ Coding Guidelines](https://github.com/Microsoft/AirSim/blob/master/docs/coding_guidelines.md)
    - [Google C++ Style Guideline](https://google.github.io/styleguide/cppguide.html)
    - [GCC Command-Line Options](http://tigcc.ticalc.org/doc/comopts.html)
    - [Make Refcard](https://web.archive.org/web/20171218110823/http://www.schacherer.de/frank/technology/tools/make.html)
    - [GNU GDB Debugger Command Cheat Sheet](http://www.yolinux.com/TUTORIALS/GDB-Commands.html)
    - [Static, Shared Dynamic and Loadable Linux Libraries](http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html)
    - Function Pointer
        
        A function pointer is a variable that stores the address of a function that can later be called through that function pointer. This is useful because functions encapsulate behavior.
    - volatile
    
        `volatile` tells the compiler that the variable is explicitly changeable, and seemingly useless accesses of the variable (for instance, via pointers) should not be optimized away. You might use volatile variables to store data that is updated via callback functions or signal handlers.
        
    - Static Functions
    
        You can define a function to be static if you want it to be callable only within the source file where it is defined:
* Java

    - [Java + OOP concept Cheat Sheet by son9912](https://www.cheatography.com/son9912/cheat-sheets/java-oop-concept/)
    - [C++ and Java Syntax Differences Cheat Sheet](https://www.cprogramming.com/tutorial/java/syntax-differences-java-c++.html)

* Tensorflow

    - [TensorFlow-Tutorials](https://github.com/Hvass-Labs/TensorFlow-Tutorials)
    - [TensorFlow.js Examples](https://github.com/tensorflow/tfjs-examples)
    - [Machine Learning Notebooks](https://github.com/ageron/handson-ml)

* HTML

    - [HTML Element Reference](https://www.w3schools.com/tags/default.asp)
    - [Online Interactive HTML Cheat Sheet](https://htmlcheatsheet.com/)
    - The __difference__ between span and div is that a __span__ element is in-line and usually used for a small chunk of HTML inside a line (such as inside a paragraph) whereas a __div__ (division) element is block-line (which is basically equivalent to having a line-break before and after it) and used to group larger chunks of code.

* CSS

    - [Online Interactive CSS CheatSheet](https://htmlcheatsheet.com/css/)

* Javascript

    - [Online Interactive JavaScript (JS) Cheat Sheet](https://htmlcheatsheet.com/js/)
    - [Online jQuery Cheat Sheet](https://htmlcheatsheet.com/jquery/)
    - [Backbone.js cheatsheet](https://devhints.io/backbone)
    - [Bootstrap 4 Cheat Sheet](https://hackerthemes.com/bootstrap-cheatsheet/)
    - [Plotly Javascript Open Source Graphing Library](https://plot.ly/javascript/)

* Lua

    - [Lua Scripting 5.1 Cheat Sheet by SrGMC](https://www.cheatography.com/srgmc/cheat-sheets/lua-scripting-5-1/)

* SQL

    - [SQL Cheat Sheet](http://www.sql-tutorial.net/sql-cheat-sheet.pdf)
    - [Welcome to the SQL Tutorial](https://mode.com/sql-tutorial/)
    - [SQLite vs MySQL vs PostgreSQL: A Comparison Of Relational Database Management Systems](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems)

* Markdown

    - [The Printable Markdown Cheat Sheet for Beginners and Experts](https://www.makeuseof.com/tag/printable-markdown-cheat-sheet/)

* LaTeX

    - [How To Write Mathematical Equations, Expressions, and Symbols with LaTeX: A cheatsheet](https://www.authorea.com/users/77723/articles/110898-how-to-write-mathematical-equations-expressions-and-symbols-with-latex-a-cheatsheet)

* General

    - [Tutorialspoint](https://www.tutorialspoint.com/index.htm)
    - [w3schools](https://www.w3schools.com/)
    - [GeeksforGeeks](https://www.geeksforgeeks.org/)

## Theorem

* Statistics
    - [Statistics Cheat Sheet - MIT](http://web.mit.edu/~csvoss/Public/usabo/stats_handout.pdf)

* Probability
    - [Probability Basics  Cheat Sheet](https://www.sas.upenn.edu/~astocker/lab/teaching-files/PSYC739-2016/probability_cheatsheet.pdf)
    - [Probability cheat sheet for distribution](http://www.cs.elte.hu/~mesti/valszam/kepletek)

* Algorithm
    - [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
    - [Algorithms and Data Structures Cheatsheet](https://algs4.cs.princeton.edu/cheatsheet/)

## Article
* [Performance Metrics for Classification problems in Machine Learning](https://medium.com/thalus-ai/performance-metrics-for-classification-problems-in-machine-learning-part-i-b085d432082b)
- [Bayes' Theorem - Math is Fun](https://www.mathsisfun.com/data/bayes-theorem.html)
* [Quick Guide to Build a Recommendation Engine in Python](https://www.analyticsvidhya.com/blog/2016/06/quick-guide-build-recommendation-engine-python/)
* [Probability and Statistics - 假設檢定：基本流程總整理 Process of Hypothesis Testing Statistics](http://mropengate.blogspot.com/2015/03/hypothesis-testing-p-value.html)
* [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)
* [Data Science Tutorials](https://www.topcoder.com/community/data-science/data-science-tutorials/)
* [Top 28 Cheat Sheets for Machine Learning, Data Science, Probability, SQL & Big Data](https://www.analyticsvidhya.com/blog/2017/02/top-28-cheat-sheets-for-machine-learning-data-science-probability-sql-big-data/)

## Interview
* [LeetCode](https://leetcode.com/): The World's Leading Online Programming Learning Platform
* [Grammarly](https://www.grammarly.com/): Free Writing Assistant
* [Hemingway App](http://www.hemingwayapp.com/): Makes your writing bold and clear.
* [Sejda](https://www.sejda.com/sign-pdf): Fill and Sign PDF Online Free
export PS1="\[\033[38;5;21m\]\u\[$(tput sgr0)\]\[\033[38;5;15m\]@\[$(tput sgr0)\]\[\033[38;5;2m\]\w\[$(tput sgr0)\]"
* [Technical Interview Preparation - Data Structures and Algorithms
](https://hackmd.io/@nesquena/SJIV-n7B?type=view)
