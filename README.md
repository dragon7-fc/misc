f# misc

A playground to note something.

## Tool

* ipmitool

    - Build

        - How to make in Ubuntu

            ```bash
            apt-get install automake libtool
            apt-get install libssl-dev
            # yum install openssl-devel
            
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
    - Build with proxy
    
        `sudo docker build --build-arg http_proxy="$http_proxy" --build-arg https_proxy="$https_proxy" -t XXX .`
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

* minicom

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
    | edit binary | `vi -b [FILE] ` -> `:%!xxd -g1` -> edit binary... -> `:%!xxd -r` -> `:wq` |
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
    - [Use vim with ctags](https://kulkarniamit.github.io/whatwhyhow/howto/use-vim-ctags.html)
    - file revision compare
    
        `vimdiff <( git show [REVISION_1]:[XXX_FI|LE] ) <( git show [REVISION_2]:[XXX_FI|LE] )`
    - [Vim configuration for Linux kernel development](https://stackoverflow.com/questions/33676829/vim-configuration-for-linux-kernel-development)
        
        - index kernel source for aspeed platform
    
            ```bash
            sudo aptitude install cscope exuberant-ctags
            cd [LINUX]
            make O=. ARCH=arm SUBARCH=aspeed cscope tags
            ```
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
    - [systemd](https://wiki.archlinux.org/index.php/systemd)
    - [How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)
    - [Terry : systemd](https://terry.im/wiki/terry/systemd.html)
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
    - [How To Upgrade Linux Kernel In CentOS 7](https://phoenixnap.com/kb/how-to-upgrade-kernel-centos)
    - [Ubuntu – How to resize root to increase home partition size in ubuntu 16.04 with gparted](https://itectec.com/ubuntu/ubuntu-how-to-resize-root-to-increase-home-partition-size-in-ubuntu-16-04-with-gparted-duplicate/)
    - [Linux Package Management Cheatsheet](https://danilodellaquila.com/en/blog/linux-package-management-cheatsheet)
    - [Command-Line Printing and Options](https://www.cups.org/doc/options.html)
    - Discovering Open Ports
    
        - sudo netstat -ltunpe | grep [PORT]
        - sudo fuser -vn tcp [PORT]
        - lsof -i@[IP]:[PORT]
    - [IPv6 Explained for Beginners](http://www.steves-internet-guide.com/ipv6-guide/)
    
        __NOTE__: link local address: fe80::/10
    - [File locking in Linux](https://gavv.github.io/articles/file-locks/#command-line-tools)
- i2c-tools

    |                    | command                                         |
    |--------------------|-------------------------------------------------|
    | scan bus           | `i2cdetect -l`                                  |
    | scan slave address | `i2cdetect -y [BUS]`                            |
    | dump register      | `i2cdump -y [BUS] [SLAVE_ADDRESS]`              |
    | write register     | `i2cset -f -y [BUS] [SLAVE_ADDRESS] [REGISTER]` |
    | read register      | `i2cget -y [BUS] [SLAVE_ADDRESS] [REGISTER]`    |
- BSOD/Kernel Panic

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
         -v [/PAT|H/TO/JENKINS]/jenkins-data:/var/jenkins_home \
         -v /var/run/docker.sock:/var/run/docker.sock \
         jenkinsci/blueocean
        ```
* Kubernetes

    - [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
    - Weave Net Addon
    
        - IPALLOC_RANGE
        
            - the range of IP addresses used by Weave Net and the subnet they are placed in (CIDR format; default 10.32.0.0/12)
            - ex. change to 10.244.0.0/24
            
                `kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')&env.IPALLOC_RANGE=10.244.0.0/16"`
    - Inter-pod anti-affinity
    
        ```bash
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          creationTimestamp: null
          labels:
            id: very-important                  # change
          name: deploy-important
          namespace: project-tiger              # important
        spec:
          replicas: 3                           # change
          selector:
            matchLabels:
              id: very-important                # change
          strategy: {}
          template:
            metadata:
              creationTimestamp: null
              labels:
                id: very-important              # change
            spec:
              containers:
              - image: nginx:1.17.6-alpine
                name: container1                # change
                resources: {}
              - image: kubernetes/pause         # add
                name: container2                # add
              affinity:                                             # add
                podAntiAffinity:                                    # add
                  requiredDuringSchedulingIgnoredDuringExecution:   # add
                  - labelSelector:                                  # add
                      matchExpressions:                             # add
                      - key: id                                     # add
                        operator: In                                # add
                        values:                                     # add
                        - very-important                            # add
                    topologyKey: kubernetes.io/hostname             # add
        ```
    - Pod
    
        ```
        kind: Pod
        ...
        spec:
          nodeName: foo-node # schedule pod to specific node
          # node affinity
          nodeSelector:
            # <LABEL-NAME>: <LABEL-VALUE>
            node-role.kubernetes.io/master: ""
          # toleration
          tolerations:
          - effect: NoSchedule
            key: node-role.kubernetes.io/master
          schedulerName: my-shiny-scheduler     # customized scheduler
          containers:
          - c1
            # Expose Pod Information to Containers Through Environment Variables
            env:
              - name: MY_NODE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: spec.nodeName
        ```
    - Cluster Setup

        - Kubernetes Dashboard

            - install

               `kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.1.0/aio/deploy/recommended.yaml`
        
            - Secure Kubernetes Dashboard
           
                ```bash
                ➜ k -n kubernetes-dashboard edit deploy kubernetes-dashboard
               
                template:
                  spec:
                    containers:
                    - args:
                      - --namespace=kubernetes-dashboard  
                      - --authentication-mode=token        # Enforce authentication using a token (with possibility to use RBAC)
                      - --auto-generate-certificates       # Add the --auto-generate-certificates argument
                      #- --enable-skip-login=true          # Deny users to "skip login"
                      #- --enable-insecure-login           # Deny insecure access, enforce HTTPS (self signed certificates are ok for now)
                      image: kubernetesui/dashboard:v2.0.3
                      imagePullPolicy: Always
                      name: kubernetes-dashboard
                
                # Allow only cluster internal access
                ➜ k -n kubernetes-dashboard edit svc kubernetes-dashboard
               
                spec:
                  clusterIP: 10.107.176.19
                  externalTrafficPolicy: Cluster
                  ports:
                  - name: http
                    nodePort: 32513  # delete
                    port: 9090
                    protocol: TCP
                    targetPort: 9090
                  - name: https
                    nodePort: 32441  # delete
                    port: 443
                    protocol: TCP
                    targetPort: 8443
                  selector:
                    k8s-app: kubernetes-dashboard
                  sessionAffinity: None
                  type: ClusterIP          # change or delete
                status:
                  loadBalancer: {}
                ```
        - CIS benchmark

            - [kube-bench](https://github.com/aquasecurity/kube-bench)
                
                ```bash
                kube-bench master
                kube-bench node
                ```
    - Cluster Hardening

        - RBAC
        
            - combinations
            
                1. Role + RoleBinding (available in single Namespace, applied in single Namespace)
                1. ClusterRole + ClusterRoleBinding (available cluster-wide, applied cluster-wide)
                1. ClusterRole + RoleBinding (available cluster-wide, applied in single Namespace)
                1. Role + ClusterRoleBinding (**NOT POSSIBLE**: available in single Namespace, applied cluster-wide)
            - Users and CertificateSigningRequests

                ```bash
                #
                # add user `60099@internal.users`
                #
                
                # 1. Create KEY
                #
                ➜ openssl genrsa -out 60099.key 2048

                # 2. Create CSR
                #
                ➜ openssl req -new -key 60099.key -out 60099.csr
                # set Common Name = 60099@internal.users

                # 3. Manual signing
                #
                ➜ find /etc/kubernetes/pki | grep ca
                ➜ openssl x509 -req -in 60099.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out 60099.crt -days 500

                # 4. Signing via API
                #
                # csr.yaml

                apiVersion: certificates.k8s.io/v1
                kind: CertificateSigningRequest
                metadata:
                  name: 60099@internal.users # ADD
                spec:
                  groups:
                  - system:authenticated
                  request: {{BASE_64_ENCODED_CSR}} # ADD
                  signerName: kubernetes.io/kube-apiserver-client
                  usages:
                  - client auth

                # Note: 
                #   BASE_64_ENCODED_CSR: cat 60099.csr | base64 -w 0

                # Create the resource, check its status and approve
                ➜ k -f csr.yaml create
                ➜ k certificate approve 60099@internal.users

                # Now download the CRT
                ➜ k get csr 60099@internal.users -ojsonpath="{.status.certificate}" | base64 -d > 60099.crt

                # 5. Use it to connect to K8s API
                #
                ➜ k config set-credentials 60099@internal.users --client-key=60099.key --client-certificate=60099.crt
                ➜ k config set-context 60099@internal.users --cluster=kubernetes --user=60099@internal.users
                ➜ k config get-contexts
                ➜ k config use-context 60099@internal.users
                ```
        - Service Account
        
            - add service account (sa -> role -> rolebinding)

                ```bash
                kubectl -n project-hamster create sa processor

                kubectl -n project-hamster create role processor \
                  --verb=create \
                  --resource=secret \
                  --resource=configmap

                kubectl -n project-hamster create rolebinding processor \
                  --role processor \
                  --serviceaccount project-hamster:processor

                kubectl -n project-hamster auth can-i create secret \
                  --as system:serviceaccount:project-hamster:processor

                kubectl -n project-hamster auth can-i create configmap \
                  --as system:serviceaccount:project-hamster:processor
                ```
            - add service account (sa -> clusterrole -> clusterrolebinding)
                
                ```bash
                kubectl create serviceaccount pvviewer
                kubectl create clusterrole pvviewer-role --resource=persistentvolumes --verb=list
                kubectl create clusterrolebinding pvviewer-role-binding --clusterrole=pvviewer-role --serviceaccount=default:pvviewer

                # XXX-pod.yaml
                    
                kind: pod
                ...
                spec:
                  serviceAccountName: pvviewer
                ```
               - We can see all necessary information to contact the apiserver manually
               
                   ```bash
                   / # curl https://kubernetes.default/api/v1/namespaces/restricted/secrets -H "Authorization: Bearer $(cat /run/secrets/kubernetes.io/serviceaccount/token)" -k
                   ...
                       {
                         "metadata": {
                           "name": "secret3",
                           "namespace": "restricted",
                   ...
                             }
                           ]
                         },
                         "data": {
                           "password": "cEVuRXRSYVRpT24tdEVzVGVSCg=="
                         },
                         "type": "Opaque"
                       }
                   ...
                   
                   ➜ echo cEVuRXRSYVRpT24tdEVzVGVSCg== | base64 -d
                   pEnEtRaTiOn-tEsTeR
                   ```
        - Change kube-apiserver service type from `NodePort` to `ClusterIP`
        
           ```bash
           # /etc/kubernetes/manifests/kube-apiserver.yaml
           
           - command:
            - kube-apiserver
            - --advertise-address=192.168.100.11
            - --allow-privileged=true
            - --authorization-mode=Node,RBAC
            - --client-ca-file=/etc/kubernetes/pki/ca.crt
            - --enable-admission-plugins=NodeRestriction
            - --enable-bootstrap-token-auth=true
            - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
            - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
            - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
            - --etcd-servers=https://127.0.0.1:2379
            - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
            - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
            - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
            - --kubernetes-service-node-port=31000   # delete or set to 0
            - --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt
            - --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key
            
           ➜ kubectl delete svc kubernetes
           ➜ kubectl get svc
           ```
        - check certificate
            
            - ex. check apiserver expiration: `kubeadm certs check-expiration | grep apiserver`
            - ex. renew the apiserver server certificate: `kubeadm certs renew apiserver`
        - check kubelet certificate directory
            
            - `/var/lib/kubelet/pki`: default of `kubelet --cert-dir`
        - customized kubelet manifests directory
        
            - `--pod-manifest-path`
        - service cidr
        
            - parameter: `--service-cluster-ip-range`
            
                - `/etc/kubernetes/manifests/kube-apiserver.yaml`
                - `/etc/kubernetes/manifests/kube-controller-manager.yaml`
        - upgrade (ex. 1.18.0 -> 1.19.0)
            
            ```bash
            # On Master Node

            kubectl drain controlplane --ignore-daemonsets
            apt-get install kubeadm=1.19.0-00
            kubeadm  upgrade plan
            kubeadm  upgrade apply v1.19.0
            apt-get install kubelet=1.19.0-00
            systemctl daemon-reload
            systemctl restart kubelet
            kubectl uncordon controlplane
            kubectl drain node01 --ignore-daemonsets


            # On Worker Node

            apt-get install kubeadm=1.19.0-00
            kubeadm upgrade node
            apt-get install kubelet=1.19.0-00
            systemctl daemon-reload
            systemctl restart kubelet     

            # Back on Master Nodess

            kubectl uncordon node01
            ```
    - System Hardening

        - AppArmor profile
        
            ```bash
            # /opt/course/9/profile 

            #include <tunables/global>
              
            profile very-secure flags=(attach_disconnected) {
              #include <abstractions/base>

              file,

              # Deny all file writes.
              deny /** w,
            }

            # Install the AppArmor profile on Node cluster1-worker1
            ➜ scp /opt/course/9/profile cluster1-worker1:~/
            ➜ ssh cluster1-worker1
            
            # Install the AppArmor profile on Node cluster1-worker1
            ➜ apparmor_parser -q ./profile
            
            # verify
            ➜ apparmor_status
           
            # Add label security=apparmor to the Node
            ➜ k label node cluster1-worker1 security=apparmor
           
            # create the Deployment which uses the profile
            ➜ k create deploy apparmor --image=nginx:1.19.2 $do > 9_deploy.yaml
           
            # 9_deploy.yaml
           
            template:
              metadata:
                creationTimestamp: null
                labels:
                  app: apparmor
                annotations:                                                                 # add
                  container.apparmor.security.beta.kubernetes.io/c1: localhost/very-secure   # add (Single container named c1 with the AppArmor profile very-secure enabled)
              spec:
                nodeSelector:                    # add
                  security: apparmor             # add
                containers:
                - image: nginx:1.19.2
                  name: c1                       # change
                  resources: {}
           
            ➜ k -f 9_deploy.yaml create
           
            # This looks alright, the Pod is running on cluster1-worker1 because of the nodeSelector. 
            ➜ k get pod -owide | grep apparmor
           
            # The AppArmor profile simply denies all filesystem writes, but Nginx needs to write into some locations to run, hence the errors.
            ➜ k logs apparmor-85c65645dc-w852p
           
            /docker-entrypoint.sh: No files found in /docker-entrypoint.d/, skipping configuration
            /docker-entrypoint.sh: 13: /docker-entrypoint.sh: cannot create /dev/null: Permission denied
            2020/09/26 18:14:11 [emerg] 1#1: mkdir() "/var/cache/nginx/client_temp" failed (13: Permission denied)
            nginx: [emerg] mkdir() "/var/cache/nginx/client_temp" failed (13: Permission denied)
           
            ➜ ssh cluster1-worker1
            ➜ docker ps -a | grep apparmor
           
            # the container is using our AppArmor profile.
            ➜ docker inspect 41f014a9e7a8 | grep -i profile
                    "AppArmorProfile": "very-secure",
            ```
    - Monitoring, Logging and Runtime Security
    
        - falco
    
            - Falco uses system calls to secure and monitor a system, by:

                - Parsing the Linux system calls from the kernel at runtime
                - Asserting the stream against a powerful rules engine
                - Alerting when a rule is violated
            - install falco on worker node
                
                ```bash
                curl -s https://falco.org/repo/falcosecurity-3672BA8F.asc | apt-key add -
                echo "deb https://download.falco.org/packages/deb stable main" | tee -a /etc/apt/sources.list.d/falcosecurity.list
                apt-get update -y
                apt-get -y install linux-headers-$(uname -r)
                apt-get install -y falco=0.26.1
                ```
            - Usage
            
                - service
                
                    ```bash
                    systemctl start falco
                    
                    # view log
                    cat /var/log/syslog | grep falco
                    ```
                - command line
                
                    ```bash
                    systemctl stop falco && falco
                    
                    # view log
                    falco
                    ```
            - Configuration
            
                ```bash
                # /etc/falco/falco.yaml
                
                ...
                # Where security notifications should go.
                # Multiple outputs can be enabled.

                syslog_output:
                  enabled: trues
                ...
                ```
            - Create logs in correct format (ex. chnge Package management process launched message formate to time,container-id,container-name,user-name)
            
                ```bash
                cd /etc/falco
                grep -r "Package management process launched" .
                
                # falco_rules.yaml
                
                # Container is supposed to be immutable. Package management should be done in building the image.
                - rule: Launch Package Management Process in Container
                  desc: Package management process ran inside container
                  condition: >
                    spawned_process
                    and container
                    and user.name != "_apt"
                    and package_mgmt_procs
                    and not package_mgmt_ancestor_procs
                    and not user_known_package_manager_in_container
                  output: >
                    Package management process launched in container (user=%user.name user_loginuid=%user.loginuid command=%proc.cmdline container_id=%container.id container_name=%container.name     ## remove
                    Package management process launched in container %evt.time,%container.id,%container.name,%user.name     ## add
                  priority: ERROR
                  tags: [process, mitre_persistence]

                # test
                #
                falco | grep "Package management"

                20:23:14.395725592: Error Package management process launched in container 20:23:14.395725592,fd6a98d42973,k8s_nginx_webapi-5fcb69b746-gtx8q_team-blue_d5e9178c-60fb-43e5-af89-3b8a579614ef_0,root
                ```
                
                __NOTE__: move custimized settings to /etc/falco/falco_rules.local.yaml

                __NOTE__: [Supported Fields for Conditions and Outputs](https://falco.org/docs/rules/supported-fields)
        - Audit Log Policy
        
            ```bash
            # enable audit log in kube-apiserver
            #
            # /etc/kubernetes/manifests/kube-apiserver.yaml 

            apiVersion: v1
            kind: Pod
            metadata:
              annotations:
                kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 192.168.100.21:6443
              creationTimestamp: null
              labels:
                component: kube-apiserver
                tier: control-plane
              name: kube-apiserver
              namespace: kube-system
            spec:
              containers:
              - command:
                - kube-apiserver
                - --audit-policy-file=/etc/kubernetes/audit/policy.yaml  # add
                - --audit-log-path=/etc/kubernetes/audit/logs/audit.log  # add
                - --audit-log-maxsize=5                                  # add
                - --audit-log-maxbackup=1                                # only one backup of the logs is stored

                - --advertise-address=192.168.100.21
                - --allow-privileged=true
            ...

            # create audit policy
            #
            # /etc/kubernetes/audit/policy.yaml

            apiVersion: audit.k8s.io/v1
            kind: Policy
            rules:
            
            # log Secret resources audits, level Metadata
            - level: Metadata
              resources:
              - group: ""
                resources: ["secrets"]
            
            # log node related audits, level RequestResponse
            - level: RequestResponse
              userGroups: ["system:nodes"]
            
            # for everything else don't log anything
            - level: None

            # restart apiserver
            #
            ➜ cd /etc/kubernetes/manifests/
            ➜ mv kube-apiserver.yaml ..
            ➜ truncate -s 0 /etc/kubernetes/audit/logs/audit.log

            # check log
            #
            # /etc/kubernetes/audit/logs/audit.log

            {
              "kind": "Event",
              "apiVersion": "audit.k8s.io/v1",
              "level": "RequestResponse",
              "auditID": "c90e53ed-b0cf-4cc4-889a-f1204dd39267",
              "stage": "ResponseComplete",
              "requestURI": "...",
              "verb": "list",
              "user": {
                "username": "system:node:cluster2-master1",
                "groups": [
                  "system:nodes",
                  "system:authenticated"
                ]
              },
              "sourceIPs": [
                "192.168.100.21"
              ],
              "userAgent": "kubelet/v1.19.1 (linux/amd64) kubernetes/206bcad",
              "objectRef": {
                "resource": "configmaps",
                "namespace": "kube-system",
                "name": "kube-proxy",
                "apiVersion": "v1"
              },
              "responseStatus": {
                "metadata": {},
                "code": 200
              },
              "responseObject": {
                "kind": "ConfigMapList",
                "apiVersion": "v1",
                "metadata": {
                  "selfLink": "/api/v1/namespaces/kube-system/configmaps",
                  "resourceVersion": "83409"
                },
                "items": [
                  {
                    "metadata": {
                      "name": "kube-proxy",
                      "namespace": "kube-system",
                      "selfLink": "/api/v1/namespaces/kube-system/configmaps/kube-proxy",
                      "uid": "0f1c3950-430a-4543-83e4-3f9c87a478b8",
                      "resourceVersion": "232",
                      "creationTimestamp": "2020-09-26T20:59:50Z",
                      "labels": {
                        "app": "kube-proxy"
                      },
                      "annotations": {
                        "kubeadm.kubernetes.io/component-config.hash": "..."
                      },
                      "managedFields": [
                        {
            ...
                        }
                      ]
                    },
            ...
                  }
                ]
              },
              "requestReceivedTimestamp": "2020-09-27T20:01:36.223781Z",
              "stageTimestamp": "2020-09-27T20:01:36.225470Z",
              "annotations": {
                "authorization.k8s.io/decision": "allow",
                "authorization.k8s.io/reason": ""
              }
            }

            # shows Secret entries
            ➜ cat audit.log | grep '"resource":"secrets"' | wc -l
            
            # confirms Secret entries are only of level Metadata
            ➜ cat audit.log | grep '"resource":"secrets"' | grep -v '"level":"Metadata"' | wc -l
            
            # shows RequestResponse level entries
            ➜ cat audit.log | grep -v '"level":"RequestResponse"' | wc -l
            
            # shows RequestResponse level entries are only for system:nodes
            ➜ cat audit.log | grep '"level":"RequestResponse"' | grep -v "system:nodes" | wc -l
            ```
    - Microservice Vulnerabilities

        - ETCD:
        
            - Backing up an etcd cluster
                
                ```bash
                ➜ ETCDCTL_API='3' etcdctl snapshot save --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key /PATH/TO/BACKUP.XX
                ```
            - Restore an etcd cluster
            
                ```bash
                ➜ ETCDCTL_API=3 etcdctl snapshot restore /tmp/etcd-backup.db --data-dir /var/lib/etcd-backup

                # /etc/kubernetes/manifests/etcd.yaml

                spec:
                  ...
                  volumes:
                  ...
                  - hostPath:
                      path: /var/lib/etcd-backup                # change
                      type: DirectoryOrCreate
                    name: etcd-data
                ```
            - Verifying that data is encrypted
            
                ```bash
                # read secret out of etcd
                ➜ ETCDCTL_API=3 etcdctl \
                --cert /etc/kubernetes/pki/apiserver-etcd-client.crt \
                --key /etc/kubernetes/pki/apiserver-etcd-client.key \
                --cacert /etc/kubernetes/pki/etcd/ca.crt get /registry/secrets/team-green/database-access  # ETCD in Kubernetes stores data under /registry/{type}/{namespace}/{name}
                
                k8s


                v1Secret

                database-access
                team-green"*$3e0acd78-709d-4f07-bdac-d5193d0f2aa32bB
                0kubectl.kubernetes.io/last-applied-configuration{"apiVersion":"v1","data":{"pass":"Y29uZmlkZW50aWFs"},"kind":"Secret","metadata":{"annotations":{},"name":"database-access","namespace":"team-green"}}
                z
                kubectl-client-side-applyUpdatevFieldsV1:
                {"f:data":{".":{},"f:pass":{}},"f:metadata":{"f:annotations":{".":{},"f:kubectl.kubernetes.io/last-applied-configuration":{}}},"f:type":{}}
                pass
                    confidentialOpaque"
                    
                ➜ echo Y29uZmlkZW50aWFs | base64 -d
                ```
        - Container Runtime Sandbox gVisor
        
            - check if containerd and runsc are installed and configured

                ```bash
                ➜ root@cluster1-worker2:~# runsc --version
                runsc version release-20201130.0
                spec: 1.0.1-dev
                
                ➜ root@cluster1-worker2:~# service containerd status
                ● containerd.service - containerd container runtime
                   Loaded: loaded (/lib/systemd/system/containerd.service; enabled; vendor preset: enabled)
                   Active: active (running) since Thu 2020-09-03 15:58:22 UTC; 2min 36s ago
                   ...
                
                ➜ root@cluster1-worker2:~# cat /etc/containerd/config.toml
                disabled_plugins = ["restart"]
                [plugins.linux]
                  shim_debug = true
                [plugins.cri.containerd.runtimes.runsc]
                  runtime_type = "io.containerd.runsc.v1"
                ```
            - arguments the kubelet has been configured with to use containerd
            
                ```bash
                # /etc/default/kubelet
                KUBELET_EXTRA_ARGS="--container-runtime remote --container-runtime-endpoint unix:///run/containerd/containerd.sock"
                ```
            - Create a RuntimeClass named gvisor with handler runsc.
            
                ```bash
                # 10_rtc.yaml

                apiVersion: node.k8s.io/v1
                kind: RuntimeClass
                metadata:
                  name: gvisor
                handler: runsc
                ```
            - Create a Pod that uses the RuntimeClass. The Pod should be in Namespace `team-purple`, named `gvisor-test` and of image `nginx:1.19.2`. Make sure the Pod runs on `cluster1-worker2`.
            
                ```bash
                ➜ k -n team-purple run gvisor-test --image=nginx:1.19.2 $do > 10_pod.yaml

                # 10_pod.yaml

                apiVersion: v1
                kind: Pod
                metadata:
                  creationTimestamp: null
                  labels:
                    run: gvisor-test
                  name: gvisor-test
                  namespace: team-purple
                spec:
                  nodeName: cluster1-worker2 # add
                  runtimeClassName: gvisor   # add
                  containers:
                  - image: nginx:1.19.2
                    name: gvisor-test
                    resources: {}
                  dnsPolicy: ClusterFirst
                  restartPolicy: Always
                status: {}
                
                ➜ k -f 10_pod.yaml create
                ➜ k -n team-purple exec gvisor-test -- dmesg
                [    0.000000] Starting gVisor...
                [    0.417740] Checking naughty and nice process list...
                [    0.623721] Waiting for children...
                [    0.902192] Gathering forks...
                [    1.258087] Committing treasure map to memory...
                [    1.653149] Generating random numbers by fair dice roll...
                [    1.918386] Creating cloned children...
                [    2.137450] Digging up root...
                [    2.369841] Forking spaghetti code...
                [    2.840216] Rewriting operating system in Javascript...
                [    2.956226] Creating bureaucratic processes...
                [    3.329981] Ready!
                ```
        - Open Policy Agent

            - install

               ```bash 
               # /etc/kubernetes/manifests/kube-apiserver.yaml 
               
               - --enable-admission-plugins=NodeRestriction      # change
               
               ➜ kubectl create -f https://raw.githubusercontent.com/killer-sh/cks-course-environment/master/course-content/opa/gatekeeper.yaml

               # test
               ➜ k -n gatekeeper-system get pod,svc
               NAME                                                 READY   STATUS    RESTARTS   AGE
               pod/gatekeeper-audit-6ffc8f5544-ng89x                1/1     Running   0          14m
               pod/gatekeeper-controller-manager-6f9c99b4d7-bbdwj   1/1     Running   0          14m

               NAME                                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
               service/gatekeeper-webhook-service   ClusterIP   10.109.101.207   <none>        443/TCP   14m
               ```
           
            - Alter the existing constraint and/or template to also blacklist images from `very-bad-registry.com`.
               
                ```bash
                ➜ k get crd
                NAME                                                 CREATED AT
                blacklistimages.constraints.gatekeeper.sh            2020-09-14T19:29:31Z
                configs.config.gatekeeper.sh                         2020-09-14T19:29:04Z
                constraintpodstatuses.status.gatekeeper.sh           2020-09-14T19:29:05Z
                constrainttemplatepodstatuses.status.gatekeeper.sh   2020-09-14T19:29:05Z
                constrainttemplates.templates.gatekeeper.sh          2020-09-14T19:29:05Z
                requiredlabels.constraints.gatekeeper.sh             2020-09-14T19:29:31Z
               
                ➜ k get constraint
                NAME                                                           AGE
                blacklistimages.constraints.gatekeeper.sh/pod-trusted-images   10m
                
                NAME                                                                  AGE
                requiredlabels.constraints.gatekeeper.sh/namespace-mandatory-labels   10m
               
                ➜ k edit blacklistimages pod-trusted-images
               
                ➜ k edit constrainttemplates blacklistimages
               
                apiVersion: templates.gatekeeper.sh/v1beta1
                kind: ConstraintTemplate
                metadata:
                ...
                spec:
                  crd:
                    spec:
                      names:
                        kind: BlacklistImages
                  targets:
                  - rego: |
                      package k8strustedimages

                      images {
                        image := input.review.object.spec.containers[_].image
                        not startswith(image, "docker-fake.io/")
                        not startswith(image, "google-gcr-fake.com/")
                        not startswith(image, "very-bad-registry.com/") # ADD THIS LINE
                      }

                      violation[{"msg": msg}] {
                        not images
                        msg := "not trusted image!"
                      }
                    target: admission.k8s.gatekeeper.sh
                   
                # test
                ➜ k run opa-test --image=very-bad-registry.com/image

                Error from server ([denied by pod-trusted-images] not trusted image!): admission webhook "validation.gatekeeper.sh" denied the request: [denied by pod-trusted-images] not trusted image!

                ➜ k describe blacklistimages pod-trusted-images
                ...
                  Total Violations:  1
                  Violations:
                    Enforcement Action:  deny
                    Kind:                Pod
                    Message:             not trusted image!
                    Name:                untrusted-68c4944d48-2hgt9
                    Namespace:           default
                Events:                  <none>
                ```
        - Pod Security Policies
   
            - Cluster-level resources. Controls under which security conditions a Pod has to run.
           
            - Enable Admission Plugin for PodSecurityPolicy
           
                ```bash
                # /etc/kubernetes/manifests/kube-apiserver.yaml 
               
                - --enable-admission-plugins=NodeRestriction,PodSecurityPolicy      # change
                ```
            - Create new PodSecurityPolicy
           
                ```bash
                # Creating a PodSecurityPolicy named psp-mount which allows hostPath volumes only for directory /tmp
                # psp.yaml
               
                apiVersion: policy/v1beta1
                kind: PodSecurityPolicy
                metadata:
                  name: psp-mount
                spec:
                  privileged: true  # allow privileged pods!
                  seLinux:
                    rule: RunAsAny
                  supplementalGroups:
                    rule: RunAsAny
                  runAsUser:
                    rule: RunAsAny
                  fsGroup:
                    rule: RunAsAny
                  volumes:
                  - '*'
                  allowedHostPaths:             # allows hostPath volumes only for directory /tmp
                    - pathPrefix: "/tmp"        #
               
                ➜ k create -f psp.yaml
               
                # Creating a ClusterRole named psp-mount which allows to use the new PSP
                ➜ k -n team-red create clusterrole psp-mount --verb=use \
                    --resource=podsecuritypolicies --resource-name=psp-mount
               
                # Creating a RoleBinding named psp-mount in Namespace team-red which binds the new ClusterRole to all ServiceAccounts in the Namespace team-red
                ➜ k -n team-red create rolebinding psp-mount --clusterrole=psp-mount --group system:serviceaccounts
               
                # test with deployment
                ➜ k -n team-red rollout restart deploy docker-log-hacker
                ➜ k -n team-red describe deploy docker-log-hacker

                Name:                   docker-log-hacker
                Namespace:              team-red
                ...
                Replicas:               1 desired | 0 updated | 0 total | 0 available | 2 unavailable
                ...
                Pod Template:
                  Labels:       app=docker-log-hacker
                  Annotations:  kubectl.kubernetes.io/restartedAt: 2020-09-28T11:08:18Z
                  Containers:
                   bash:
                ...
                  Volumes:
                   dockerlogs:
                    Type:          HostPath (bare host directory volume)
                    Path:          /var/lib/docker
                    HostPathType:  
                Conditions:
                  Type             Status  Reason
                  ----             ------  ------
                  Available        False   MinimumReplicasUnavailable
                  ReplicaFailure   True    FailedCreate

                ➜ k -n team-red get events --sort-by='{.metadata.creationTimestamp}'

                docker-log-hacker-6bdfbf8546-" is forbidden: PodSecurityPolicy: unable to admit pod: [spec.volumes[0].hostPath.pathPrefix: Invalid value: "/var/lib/docker": is not allowed to be used]

                ➜ k -n team-red edit deploy docker-log-hacker

                # kubectl -n team-red edit deploy docker-log-hacker

                apiVersion: apps/v1
                kind: Deployment
                metadata:
                ...
                spec:
                ...
                  template:
                    metadata:
                ...
                    spec:
                      containers:
                      - command:
                        - sh
                        - -c
                        - while true; do sleep 1d; done
                        image: bash
                ...
                        volumeMounts:
                        - mountPath: /dockerlogs
                          name: dockerlogs
                ...
                      volumes:
                      - hostPath:
                          path: /tmp                         # change
                          type: ""

                ➜ k -n team-red get pod -l app=docker-log-hacker
                NAME                                 READY   STATUS    RESTARTS   AGE
                docker-log-hacker-5674dbccc9-5lc6q   1/1     Running   0          20s

                ➜ k -n team-red describe pod -l app=docker-log-hacker
                ...
                Annotations:  kubernetes.io/psp: psp-mount
                ```
    - Supply Chain Security

        - ImagePolicyWebhook / AdmissionController

            -  allows a backend webhook to make admission decisions

            ```bash
            # Download existing files
            #
            ➜ git clone https://github.com/killer-sh/cks-challenge-series
            ➜ cp -r cks-challenge-series/challenges/ImagePolicyWebhook /etc/kubernetes/admission

            # Register in apiserver
            #
            ➜ cd /etc/kubernetes/manifests
            # /etc/kubernetes/manifests/kube-apiserver.yaml

            apiVersion: v1
            kind: Pod
            metadata:
            ...
              name: kube-apiserver
              namespace: kube-system
            spec:
              containers:
              - command:
                - kube-apiserver
                - --admission-control-config-file=/etc/kubernetes/admission/admission_config.yaml    # add config file
                - --enable-admission-plugins=NodeRestriction,ImagePolicyWebhook    # add ImagePolicyWebhook admission controller
            ...
                volumeMounts:
                - mountPath: /etc/kubernetes/admission
                  name: admission
                  readOnly: true
            ...
              volumes:
              - hostPath:
                  path: /etc/kubernetes/admission
                  type: DirectoryOrCreate
                name: admission
            ...

            # Create admission_config.yaml
            #
            ➜ cd /etc/kubernetes/admission

            # /etc/kubernetes/admission/admission_config.yaml

            apiVersion: apiserver.config.k8s.io/v1
            kind: AdmissionConfiguration
            plugins:
              - name: ImagePolicyWebhook
                configuration:
                  imagePolicy:
                    kubeConfigFile: /etc/kubernetes/admission/kubeconf
                    allowTTL: 50
                    denyTTL: 50
                    retryBackoff: 500
                    defaultAllow: false # DENY ALL PODS IF SERVICE NOT AVAILABLE

            # /etc/kubernetes/admission/kubeconf

            # clusters refers to the remote service.
            clusters:
            - name: name-of-remote-imagepolicy-service
              cluster:
                certificate-authority: /path/to/ca.pem    # CA for verifying the remote service.
                server: https://images.example.com/policy # URL of remote service to query. Must use 'https'.
            
            # users refers to the API server's webhook configuration.
            users:
            - name: name-of-api-server
              user:
                client-certificate: /path/to/cert.pem # cert for the webhook admission controller to use
                client-key: /path/to/key.pem          # key matching the cert

            # Wait for apiserver to come back by looking for a response
            #
            ➜ mv ./kube-apiserver.yaml ../
            ➜ mv ../kube-apiserver.yaml ./
            ➜ k -n kube-system get pod # just wait for a response

            # test
            #
            ➜ k run test --image=nginx

            Error from server (Forbidden): pods "test" is forbidden: Post "https://external-service:1234/check-image?timeout=30s": dial tcp: lookup external-service on 169.254.169.254:53: no such Hostname
            ```
        - Image Vulnerability Scanning

            - [trivy](https://github.com/aquasecurity/trivy)

                - ex. scan image (nginx:1.16.1-alpine) with vulnerabilities CVE-2020-10878 or CVE-2020-1967 
                
                    `trivy nginx:1.16.1-alpine | grep -E 'CVE-2020-10878|CVE-2020-1967'`
* RamDisk

    - create 100G ramdisk
    
        ```bash
        mkdir /tmp/ramdisk
        chmod 777 /tmp/ramdisk

        mount -t tmpfs -o size=100G tmpfs /tmp/ramdisk/
        ```
    - [Linux: Create RAM Disk Filesystem](https://stackpointer.io/unix/linux-create-ram-disk-filesystem/438/)
* TCP Wrappers

    - support
    
        `ldd /PATH/TO/EXE | grep libwrap`
    - order
    
        - `/etc/hosts.deny` -> `/etc/hosts.deny`
* sudo

    ```bash
    visudo

    ##+++>
    XXX      ALL=(ALL) NOPASSWD:ALL
    ##+++<
    ```
* ssh

    - server
    
        - setup
        
            ```
            sudo yum search openssh | grep -i server
            
            sudo vim /etc/ssh/sshd_config
            
            #PermitRootLogin yes
            X11Forwarding yes
            ```
        - file
        
            - `~/.ssh/authorized_keys`: client public key
        - port
        
            - tcp/22
        - log
        
            - `/var/log/secure.log`: centos
            - `/var/log/auth.log`: debian
    - client
    
        - setup
        
            - file: `/etc/ssh/ssh_config`
            - precedence: 
                
                - ssh command > `~/.ssh/config` > `/etc/ssh/ssh_config`
        - file
        
            - `~/.ssh/known_hosts`: server public key
        - [cheatsheet-ssh-A4](https://github.com/dennyzhang/cheatsheet-ssh-A4)
        - ssh
        
            - [SSH Cheatsheet](https://cheatsheet.dennyzhang.com/cheatsheet-ssh-a4)
            - SSH login without password

                ```bash
                ## can create passphrase
                a@A:~> ssh-keygen -t rsa  # generage ~/.ssh/id_rsa  and ~/.ssh/id_rsa.pub

                a@A:~> ssh b@B mkdir -p .ssh
                b@B's password:

                a@A:~> cat .ssh/id_rsa.pub | ssh b@B 'cat >> .ssh/authorized_keys'
                # or ssh-copy-id -i ~/.ssh/id_rsa.pub b@B
                b@B's password:

                ## can use ssh-agent and ssh-add to keep passhprase
                ## ssh-agent - agent to hold private key for single sign-on
                ## ssh-add - tool to add a key to the agent
                # 
                # ssh-agent /bin/bash
                # ssh-add
                # Enter passphrase for /home/a/.ssh/id_rsa:

                a@A:~> ssh b@B
                
                ## exit from B
                # exit
                #
                ## exit from /bin/bash to release passphrase
                # exit
                ```
            - Local Port Tunnel

                - Local post XXXX tunnel to Remote port YYYY

                  `ssh -L XXXX:localhost:YYYY -Nf yy@yyyy`
                  
                  __NOTE__: localhost: yyyy (remote machine)
            - Remote Port Tunnel

                - Remote post YYYY tunnel to Local port XXXX

                  `ssh -R YYYY:localhost:XXXX -Nf yy@yyyy`
                  
                  __NOTE__: localhost: local machine
        - scp
        
            - [SCP Command Examples to Securely Transfer Files in Linux](https://www.linuxtechi.com/scp-command-examples-in-linux/)
        - sftp
        
            - [SFTP commands and options](https://learn.akamai.com/en-us/webhelp/netstorage/netstorage-user-guide/GUID-E0B5C44E-7618-4C41-B9AB-186CF3E28628.html)
* Samba

    - server
    
        - setup
        
            ```bash
            sudo apt install samba

            sudo smbpasswd -a [XXX_USER]

            sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
            
            sudo vim /etc/samba/smb.conf
            ##+++>
            [MyShare]
            path =/
            read only = no
            valid users = [XXX_USER]
            force user = root
            force group = root
            ##+++<

            sudo testparm
            sudo systemctl enable samba
            sudo systemctl start samba
            
            ## only reload config
            # sudo smbcontrol smbd reload-config
            ```
        - list all smb connections
        
            - `sudo smbstatus`
            - `sudo net status shares`
        - log
        
            - `/var/log/samba`
        - port
        
            - udp/137: nmbd
            - tcp/139, tcp/445: smbd
    - client
    
        - netbios name lookup
            ```bash
            sudo apt install samba-common-bin
            
            nmblookup [NETBIOS_NAME]
            ```
        - not mount
        
            ```bash
            sudo apt install smbclient
            
            smbclient -U [XXX_USER] //[SAMBA_SERVER_IP]/MyShare
            ```
        - mount
        
            `sudo mount //[SAMBA_SERVER_IP]/MyShare [/PATH|/TO/MOUNT-POINT] -o username=[XXX_USER],password=[XXX_USER_PASSWORD]`
        - mount on power on
        
            ```bash
            # vim /etc/fstab
            ##+++>
            //[SAMBA_SERVER_IP]/MyShare [/PATH|/TO/MOUNT-POINT] cifs credentials=/mnt/.smbcredentials 0 0
            ##+++<

            sudo touch /mnt/.smbcredentials
            sudo chmod 600 /mnt/.smbcredentials
            
            # sudo vim /mnt/.smbcredentials
            username=[XXX_USER]
            password=[XXX_USER_PASSWORD]

            sudo mount -a
            ```
* NFS

    - server

        - setup
        
            ```bash
            sudo apt-get install nfs-kernel-server 

            sudo vim /etc/exports
            # format: 
            # <export> <host1>(<options>) <hostN>(<options>)...
            # no_root_squash: map users root client acount to the server root account
            ##+++>
            [/PATH/TO/NFSROOT] [NFS_SERVER_IP|*](rw,no_root_squash)
            ##+++<

            sudo exportfs -a
            sudo service nfs-kernel-server restart
            ```
        - port
        
            - tcp/111, udp/111: rpcbind.portmapper
            - tcp/2049, udp/2049: rpc.nfsd
            - tcp/random, udp/random: rpc.mountd (setup in /etc/sysconfig/nfs)
            - tcp/random, udp/random: rpc.statd (setup in /etc/sysconfig/nfs)
            - tcp/random, udp/random: rpc.lockd (setup in /etc/sysconfig/nfs)
        - view rpc service status for `rpcbind`
        
            `rpcinfo -p`
        - show nfs share
        
            `exportfs` or `showmount -e`
        - reports NFS statistics
        
            `nfsstat`
        - Firewall
        
            ```bash
            # (For CentOS)
            sudo firewall-cmd --permanent --add-service=rpc-bind
            sudo firewall-cmd --permanent --add-service=mountd
            sudo firewall-cmd --permanent --add-port=2049/tcp
            sudo firewall-cmd --permanent --add-port=2049/udp
            sudo firewall-cmd --reload
            ```
    - client

        - mount
            ```
            sudo apt install nfs-common
            mount -t nfs -o tcp,nolock [NFS_SERVER_IP]:[/PATH/TO/NFSROOT] [/PATH/TO/MOUNT]
            ```
        - mount on power on
        
            ```bash
            # vim /etc/fstab
            ##+++>
            # creating an entry to mount our NFS share
            192.168.10.133:/nfsshare    /mnt/nfsmounthere    nfs    hard,bg,timeo=300,rsize=1024,wsize=2048        0 0
            ##+++<
            ```
        - show rpc service status for `rpcbind`
        
            `rpcinfo -p [NFS_SERVER_IP]`
        - ists the available shares at the remote server
        
            - `showmount -e [NFS_SERVER_IP]`
* DHCP

    - server
    
        - ipv4
    
            - isc-dhcp-server

                - setup

                    ```bash
                    ## setup static ip address for DHCP server
                    # vim /etc/network/interfaces
                    ##+++>
                    auto [NETWORK_INTERFACE]
                    iface [NETWORK_INTERFACE] inet static
                    address [DHCP_IP]
                    netmask [DHCP_NETMASK]
                    ##+++<
                    
                    sudo apt install isc-dhcp-server

                    # vim /etc/default/isc-dhcp-server
                    ##***>
                    INTERFACES="[NETWROK_INTERFACE]"
                    ##***<

                    # vim /etc/dhcp/dhcpd.conf
                    ##+++>
                    subnet [NETWORK_IP] netmask [NETMASK] {
                      range [IP_START],[IP_END];
                      option routers [ROUTER_IP];
                    }
                    
                    ### add static IP address
                    # host [name] { [static network information] }
                    host [NAME] {
                      hardware  ethernet [MAC];
                      fixed-address [IP];
                    }
                    ##+++<

                    # check config
                    dhcpd -t -cf /etc/dhcp/dhcpd.conf

                    sudo systemctl restart isc-dhcp-server
                    ```
                - Lease status

                    `cat /var/lib/dhcp/dhclient.leases`
                - Log

                    `czat /var/log/syslog | grep dhcpd`
            - dnsmasq

                - setup

                    ```bash
                    ## setup static ip address for DHCP server
                    # vim /etc/dhcpcd.conf
                    ##+++>
                    interface=[NETWORK_INTERFACE]
                    static ip_address=[NETWORK_INTERFACE]/[NETMASK]
                    # ex.
                    # interface=eth1
                    # static ip_address=192.168.2.2/24
                    ##+++<

                    ## install dnsmasq
                    sudo apt-get install dnsmasq

                    ## setup dnsmasq
                    # vim /etc/dnsmasq.conf
                    ##+++>
                    interface=[NETWROK_INTERFACE]
                    dhcp-range=[IP_START],[IP_END],$[NETMASK]
                    dhcp-host=[BMCx_MAC],[BMCx_IP]
                    # ex.
                    # interface=eth1
                    # dhcp-range=192.168.2.10,192.168.2.50,255.255.255.0
                    # dhcp-host=28:C1:3C:89:FD:5B,192.168.2.10
                    ##+++<

                    # start/enable service
                    sudo systemctl start dnsmasq
                    sudo systemctl enable dnsmasq
                    ```
                - lease status

                    `cat /var/lib/misc/dnsmasq.leases`
                - log

                    `czat /var/log/syslog | grep dnsmasq`
            - port

                - udp/67
            - firewall

                ```bash
                # iptables (CentOS/RHEL 6)
                iptables -A INPUT -p udp -m state --state NEW --dport 67 -j ACCEPT
                service iptables save

                # firewalld (CentOS/RHEL 7)
                firewall-cmd --add-service=dhcp --permanent 
                firewall-cmd --reload

                # uncomplicated firewall (Ubuntu)
                ufw allow  67/udp
                ufw reload
                ufw show
                ```
            - misc

                - [dnsmasq - ArchWiki](https://wiki.archlinux.org/index.php/dnsmasq)
        - ipv6
        
            - isc-dhcp-server (statefull)
            
                - setup
                
                    ```bash
                    # vim /etc/dhcp/dhcpd6.conf
                    ##+++>
                    subnet6 2001:db8:0:1::/64 {
                            range6 2001:db8:0:1::129 2001:db8:0:1::254;
                            option dhcp6.name-servers fec0:0:0:1::1;
                            option dhcp6.domain-search "domain.example";
                    }
                    ##+++<
                    ```
                - port
                
                    - udp/547
            - radvd (stateless)
            
                - setup
                
                    ```bash
                    apt install radvd
                    
                    # setup static ip address
                    # vim /etc/dhcpcd.conf
                    ##+++>
                    interface eth1
                    noipv6rs
                    static ip6_address=fd00:1234:5678:9abc::1/64
                    ##+++<
                    
                    # vim /etc/radvd.conf
                    ##+++>
                    interface eth1
                    {
                                        AdvSendAdvert on;
                                        MinRtrAdvInterval 30;
                                        MaxRtrAdvInterval 100;
                                        prefix fd00:1234:5678:9abc::/64
                                        {
                                                            AdvOnLink on;
                                                            AdvAutonomous on;
                                                            AdvRouterAddr off;
                                        };

                    };
                    ##+++<
                    
                    # check ICMP6 broadcasting
                    tcpdump -i eth1 icmp6
                    ```
    - client
    
        - ipv4
    
            - config

                - CentOS

                    ```bash
                    # vim /etc/sysconfig/network-scripts/ifcfg-eth0
                    DEVICE=eth0
                    BOOTPROTO=dhcp
                    TYPE=Ethernet
                    ONBOOT=yes
                    ```
                - Ubuntu

                    ```bash
                    # vim /etc/network/interfaces
                    auto  eth0
                    iface eth0 inet dhcp
                    ```
            - renew dhcp

                ```bash
                dhclient -r
                dhclient
                ```
            - port

                - udp/68
        - ipv6
        
            - renew dhcp

                ```bash
                dhclient -r
                dhclient
                ```
            - port (statefull)
            
                - udp/546
- TFTP

    - server

        ```bash
        sudo apt-get install tftpd-hpa

        sudo vim /etc/default/tftpd-hpa
        ##+++>
        TFTP_USERNAME="tftp"
        TFTP_DIRECTORY="/path/to/tftproot"
        TFTP_ADDRESS="0.0.0.0:69"
        TFTP_OPTIONS="--secure --create"
        RUN_DAEMON="yes"
        ##+++<

        chmod 777 [/PATH/TO/TFTPROOT]
        chown nobody:nogroup -R [/PATH/TO/TFTPROOT]
        sudo service tftpd-hpa restart
        
        # power on auto start
        sudo vim /etc/rc.local
        
        + sleep 30
        + service tftpd-hpa restart
        
        exit 0
        ```

    - client

        |     | command                              |
        |-----|--------------------------------------|
        | put | `tftp -p -l [FILE] [TFTP_SERVER_IP]` |
        | get | `tftp -g -r [FILE] [TFTP_SERVER_IP]` |
* FTP

     - server
     
         - vsftpd
         
             - setup
             
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
                 sudo vim /etc/vsftpd.conf

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
             - files
             
                 - `/etc/vsftpd/vsftpd.conf`: The configuration file for vsftpd
                 - `/etc/pam.d/vsftpd`:  The Pluggable Authentication Modules (PAM) configuration file for vsftpd
                 - `/etc/vsftpd/ftpusers`: A list of users not allowed to log into vsftpd
                 - `/etc/vsftpd/user_list`: This file can be configured to either deny or allow access to the users listed, depending on whether the userlist_deny directive is set to YES (default) or NO in /etc/vsftpd/vsftpd.conf
         - pureftpd
             
             - setup
             
                 ```
                 # start with anounymous access
                 pure-ftpd -B -S localhost,21 -e
                 
                 # start without anounymous access
                 pure-ftpd -B -S localhost,21 -E
                 
                 # stop
                 killall pure-ftpd
                 ```
         - Proftpd
             
             - setup
             
                 ```
                 sudo apt install proftpd
                 
                 vim /etc/proftpd/proftpd.conf
                 ```
         - port
         
             | | Active FTP | Passive FTP |
             |-|------------|-------------|
             | command | client >1023 -> server 21 | client >1023 -> server 21    |
             | data    | client >1023 <- server 20 | client >1024 -> server >1023 |
         - compare
         
             | advantage | server |
             |--|--|
             | many users | vsftpd |
             | simple, secure | pureftpd |
             | flexible, external modules | Proftpd |
    - client

        - [Summary of FTP Commands](http://www.cryst.bbk.ac.uk/education/Internet/ftp_old/FTP_Summary.html)   
* HTTP

    - server
    
        - apache
        
            - setup
            
                - centOS
            
                    ```bash
                    sudo yum -y  install httpd.x86_64 

                    ## main configuration file 
                    # /etc/httpd/conf/httpd.conf

                    ## Web page
                    # /var/www

                    ## install php module
                    # sudo yum install php

                    ## install perl module
                    # sudo yum install mod_perl

                    ## module file
                    # /etc/httpd/modules/

                    ## module configuration file
                    # /etc/httpd/conf.modules.d
                    
                    ## check mpm
                    # httpd -V | grep -i mpm

                    ## Name Based Virtual Hosting (every domains to Single IP)
                    sudo vim /etc/httpd/conf/httpd.conf
                    ##+++>
                    NameVirtualHost 192.168.10.128:80

                    <VirtualHost 192.168.10.128:80>
                        ServerAdmin webmaster@example1.com
                        DocumentRoot /var/www/html/example1
                        ServerName www.example1.com
                        ErrorLog /var/log/httpd/error_log
                        CustomLog /var/log/httpd/access_log
                    </VirtualHost>
                    <VirtualHost *:80>
                        ServerAdmin webmaster@example2.com
                        DocumentRoot /var/www/html/example2
                        ServerName www.example2.com
                        ErrorLog /var/log/httpd/error_log
                        CustomLog /var/log/httpd/access_log
                    </VirtualHost>
                    ##+++<

                    ## IP Based Virtual Hosting (every domain to specific ip)
                    sudo vim /etc/httpd/conf/httpd.conf
                    ##+++>
                    <VirtualHost 192.168.10.128:80>
                        ServerAdmin webmaster@example1.com
                        DocumentRoot /var/www/html/example1
                        ServerName www.example1.com
                        ErrorLog /var/log/httpd/error_log
                        TransferLog /var/log/httpd/access_log
                    </VirtualHost>
                    <VirtualHost 192.168.10.133:80>
                        ServerAdmin webmaster@example2.com
                        DocumentRoot /var/www/html/example2
                        ServerName www.example2.com
                        ErrorLog /var/log/httpd/error_log
                        TransferLog /var/log/httpd/access_log
                    </VirtualHost>
                    ##+++<
                    ```
                    
                - ubuntu
                
                    ```bash
                    sudo apt install apache2

                    ## main configuration file 
                    # /etc/apache2/apache2.conf

                    ## Web page
                    # /var/www

                    ## install php module
                    # sudo apt-get install libapache2-mod-php

                    ## install perl module
                    # sudo apt-get install libapache2-mod-perl2
                    
                    # vim /etc/apache2/apache2.conf
                    # 
                    # ################ Perl support
                    # Alias /perl /var/www/perl
                    # <Directory /var/www/perl>
                    #     AddHandler perl-script .cgi .pl
                    #     PerlResponseHandler ModPerl::PerlRun
                    #     PerlOptions +ParseHeaders
                    #     Options +ExecCGI
                    # </Directory>

                    ## enabled modules
                    # /etc/apache2/mods-enabled
                    # `a2enmod [module name]` to enable module
                    # `a2dismod [module name]` to disable module

                    ## mpm module configuration
                    # /etc/apache2/mods-enabled/mpm_prefork.conf
                    
                    ## check mpm
                    # apache2ctl -V | grep -i mpm

                    ## enabled sites
                    # /etc/apache2/sites-enabled
                    # `a2ensite [site name]` to enable site
                    # `a2dissite [site name]` to disable site

                    ## user authentication
                    ## Method 1:
                    sudo apt-get install apache2.utils
                    # create user1 authentication and stored in /etc/apache2/webpass
                    sudo htpasswd -c /etc/apache2/webpass user1
                    # add user2
                    sudo htpasswd /etc/apache2/webpass user2

                    sudo vim /etc/apache2/sites-enabled/000-default.conf
                    ##+++>
                    <Directory /var/www/html/XXX>

                        AuthType Basic
                        AuthName "This name will be appeared in dialog box"
                        #Passord file wich we will create using htpasswd tool
                        AuthUserFile /etc/apache2/webpass 
                        #Only user who have valid user nad pass word can access
                        Require valid-user 
                    </Directory>
                    ##+++<

                    ## Method 2: .htaccess file in each proteced folder
                    sudo apt-get install apache2.utils
                    # create user1 authentication and stored in /etc/apache2/webpass
                    sudo htpasswd -c /etc/apache2/webpass user1
                    # add user2
                    sudo htpasswd /etc/apache2/webpass user2

                    cd /var/www/html/XXXX
                    sudo touch .htaccess
                    sudo vim .htaccess
                    ##+++>
                    AuthName "secure folder2"
                    AuthType Basic
                    AuthUserFile /etc/apache2/webpass
                    Require valid-user
                    ##+++<

                    sudo vim /etc/apache2/sites-enabled/000-default.conf
                    ##+++>
                    <Directory /var/www/html/XXXX>
                        AllowOverride AuthConfig
                    </Directory>
                    ##+++<

                    ## Redirection
                    sudo vim /etc/apache2/apache2.conf
                    ##+++>
                    <VirtualHost *:80>

                    #Redirecting form one directory to another directory
                    # Temporary redirect (single page)
                    Redirect /protected /redirected
                    # Temporary redirect (every page)
                    RedirectMatch ^/images/(.*)$ http://XXX/$1

                    # Permanent redirect
                    # Method 1
                    Redirect permanent /oldlocation http://www.example.com/newlocation
                    # Method 2
                    Redirect 301 /oldlocation http://www.example.com/newlocation
                    </VirtualHost>
                    ##+++<

                    ## Name Based Virtual Hosting (every domains to Single IP)
                    sudo touch /etc/apache2/sites-available/example1.conf
                    sudo vim /etc/apache2/sites-available/example1.conf

                    ##+++>
                    <VirtualHost 192.168.10.128:80>
                        ServerAdmin webmaster@example1.com
                        DocumentRoot /var/www/html/example1
                        ServerName www.example1.com
                        ErrorLog ${APACHE_LOG_DIR}/error-example1.log
                        CustomLog ${APACHE_LOG_DIR}/access-example1.log combined

                    </VirtualHost>
                    ##+++<

                    sudo touch /etc/apache2/sites-available/example2.conf
                    sudo vim /etc/apache2/sites-available/example2.conf
                    ##+++>
                    <VirtualHost *:80>
                        ServerAdmin webmaster@example2.com
                        DocumentRoot /var/www/html/example2
                        ServerName www.example2.com
                        ErrorLog ${APACHE_LOG_DIR}/error-example2.log
                        CustomLog ${APACHE_LOG_DIR}/access-example2.log combined

                    </VirtualHost>
                    ##+++<
                    
                    # check config
                    apache2ctl configtest
                    ```
            - setup (HTTPS)
            
                - CentOS
                
                    ```bash
                    ## generating self signed certificates
                    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/httpd/ssl/XXX.key -out /etc/httpd/ssl/XXX.crt
                    
                    ## check public key
                    openssl x509 -in /etc/httpd/ssl/XXX.crt -text
                    
                    ## install apache module mod_ssl
                    yum install mod_ssl
                    
                    sudo vim /etc/httpd/conf.d/ssl.conf
                    
                    ...
                    <VirtualHost _default_:443>
                    ...
                    DocumentRoot "/var/www/html"
                    ...
                    SSLCertificateFile /etc/httpd/ssl/XXX.crt
                    ...
                    SSLCertificateKeyFile /etc/httpd/ssl/XXX.key
                    ...
                    </VirtualHost>
                    
                    ## check configuration
                    httpd -V
                    
                    ## restart httpd
                    sudo systemctl restart httpd
                    
                    ## enable 443 port on firewall
                    sudo firewall-cmd --permanent --zone=public --add-port=443/tcp
                    sudo firewall-cmd --reload
                    sudo firewall-cmd --list-all
                    ```
            - port
            
                - tcp/80, tcp/443
            - log
            
                - centOS
                    ```
                    /var/log/httpd/access_log
                    /var/log/httpd/error_log
                    ```
                - ubuntu
                
                    ```
                    /var/log/apache2/access.log
                    /var/log/apache2/error.log
                    ```
            - [Apache HTTP Server - ArchWiki](https://wiki.archlinux.org/index.php/Apache_HTTP_Server)
            - [How To Configure Apache 2](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Apache_HowToConfigure.html)
* Proxy

    - forward
    
        - server
    
            - squid
        
                - setup
                
                    ```
                    sudo apt install squid -y
                    
                    sudo vim /etc/squid/squid.conf
                    
                    
                    ...
                    #acl localnet src 192.168.0.0/16        # RFC1918 possible internal network
                    acl localnet src X.X.X.X/X  # add X.X.X.X/X as localnet acl
                    ...
                    #http_access allow localnet
                    http_access allow localnet  # allow localnet acl
                    ...                    ...
                    cache_peer [PROXY_IP] parent [PROXY_PORT] 0 no-query default login=[PROXY_USER|]:[PROXY_PASSWORD]  # add another proxy to forward request
                    acl all src 0.0.0.0/0.0.0.0
                    never_direct allow all
                    
                    sudo systemctl restart squid
                    ```
                - setup (Authority)
                
                    ```
                    sudo vim /etc/squid/squid.conf
                    
                    ##auth_param basic program <uncomment and complete this line>
                    ##auth_param basic children 5 startup=5 idle=1
                    ##auth_param basic realm Squid proxy-caching web server
                    ##auth_param basic credentialsttl 2 hours
                    auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwords
                    auth_param basic children 5 startup=5 idle=1
                    auth_param basic realm Squid proxy-caching web server
                    auth_param basic credentialsttl 2 hours
                    acl MYBASICAUTH proxy_auth REQUIRED
                    http_access allow MYBASICAUTH
                    
                    # create password file
                    sudo htpasswd -c /etc/squid/passwords [PROXY_USER]
                    
                    # check password file
                    /usr/lib/squid/basic_ncsa_auth /etc/squid/passwords
                    
                    sudo systemctl restart squid
                    ```
                - port
                
                    - tcp/3128
                - log
                
                    ```
                    /var/log/squid/access.log
                    /var/log/squid/cache.log
                    /var/log/squid/store.log
                    ```
                - [Squid - Arch Wiki](https://wiki.archlinux.org/index.php/squid)
                - [How To Setup Your Own Free Proxy Server Using Squid Proxy](https://comtechies.com/free-proxy-server-setup-squid-proxy.html)
                - [How to Install Squid Proxy Server on Ubuntu 16.04](https://www.liquidweb.com/kb/install-squid-proxy-server-ubuntu-16-04/)
    - reverse
    
        - nginx
    
            - [nginx - ArchWiki](https://wiki.archlinux.org/index.php/nginx)
            - [How to Set up a Reverse Proxy (Step-By-Steps for Nginx and Apache)](https://kinsta.com/blog/reverse-proxy/)
    - client
    
        - Setup environment variable
            
            `export http_proxy=[PROXY_USER]:[PROXY_PASSWORD]@[PROXY_IP]:[PROXY_PORT]`
* DNS

    - server
    
        - setup
        
            ```bash
            sudo apt install bind9 bind9utils
            
            # default: caching DNS server
            sudo vim /etc/bind/named.conf.options
            
            options {
                ...
                recursion yes;
            };
            
            # change to forward DNS server
            sudo vim /etc/bind/named.conf.options
            
            options {
            ...
                ##+++>
                forwarders {
                        X.X.X.X;
                };
                forward only;
                ##+++<
            ...
            };
            
            
            
            # BIND includes a utility called rndc (Remote Name Daemon Control) which allows command line administration of the named daemon from the localhost or a remote host.
            cd /etc/bind
            # generate rndc.key
            sudo rm rndc.key
            sudo rndc-confgen -r /dev/urandom -a
            sudo chown bind.bind rndc.key 
            sudo chmod 640 rndc.key
            
            # add myzone
            cd /etc/named
            wudo vim /etc/bind/named.conf.local
            
            ##+++>
            zone "myzone" {
            type master;
            file "/etc/bind/zonedbfiles/db.myzone";
                };

            zone "YY.XX.WW.in-addr.arpa" {
            type master;
            file "/etc/bind/zonedbfiles/db.YY.XX.WW";
                };
            ##+++<
            
            
            sudo mkdir zonedbfiles
            sudo cp db.local zonedbfiles/db.myzone
            sudo cp db.127 zonedbfiles/db.YY.XX.WW
            
            sudo vim zonedbfiles/db.myzone
            
            ##***>
            ;
            ; BIND data file for local loopback interface
            ;
            $TTL    604800
            @    IN    SOA    myzone. root.myzone. (
                              4        ; Serial
                         604800        ; Refresh
                          86400        ; Retry
                        2419200        ; Expire
                         604800 )    ; Negative Cache TTL
            ;
            @        IN    NS    ns.myzone.
            ns       IN    A     WW.XX.YY.ZZ
            @        IN    A     WW.XX.YY.XX
            host2    IN    A     WW.XX.YY.PP
            ##+++<
            
            sudo vim zonedbfiles/db.YY.XX.WW
            
            ##***>
            ;
            ; BIND reverse data file for local loopback interface
            ;
            $TTL    604800
            @    IN    SOA    myzone. root.myzone. (
                              8        ; Serial
                         604800        ; Refresh
                          86400        ; Retry
                        2419200        ; Expire
                         604800 )    ; Negative Cache TTL
            ;
            @    IN    NS    ns.myzone.
            PP    IN    PTR    host2.myzone.
            ##+++<
            
            # check config
            sudo named-checkzone myzone. db.myzone
            sudo named-checkzone WW.XX.YY.in-addr.arpa db.YY.XX.WW
            sudo named-checkconf
            
            sudo systemctl restart bind9.service
            sudo rndc reload
            
            # check
            dig @localhost myzone
            dig @localhost host2.myzone
            dig @localhost -x WW.XX.YY.ZZ
            ```
        - dnssec
        
            ```bash
            cd /etc/bind
            sudo mkdir dnsseckeys
            cd dnsseckeys
            
            # generate KSK
            sudo dnssec-keygen -a RSASHA256 -b 512 -n ZONE -f KSK myzone.
            
            # generate ZSK
            dnssec-keygen -a RSASHA256 -b 512 -n ZONE myzone.
            
            # sign myzone
            cp ../zonedbfiles/db.myzone .
            dnssec-signzone -o myzone. -S db.myzone
            
            # check
            cat db.myzone.signed
            
            sudo vim /etc/bind/named.conf.options
            
            options {
            ...
            ##+++>
                dnssec-enable yes; 
                dnssec-validation yes; 
                dns-seclookaside auto;
            ##+++<
            ...
            }l
            ```
        - transaction signatures (TSIG)
        
            ```bash
            cd /etc/bind
            sudo mkdir mykeys
            cd mykeys
            
            # generate tsig key
            sudo dnssec-keygen -a HMAC-MD5 -b 128 -n HOST -r /dev/urandom mykey
            
            cat Kmykey.XXX.private
            
            ...
            Key: KKK             <- public key
            ...
            
            # create key file for transaction
            cd /etc/bind
            sudo vim named.conf.tsig
            
            ##+++>
            key "mykey" {
            algorithm HMAC-MD5;
            secret "KKK"              <- public key
            };
            ##+++<
            
            # include key file
            cd /etc/bind
            sudo vim named.conf
            
            ##+++>
            include "/etc/bind/named.conf.tsig";
            ##+++<
            
            # allow zone transfer with with whom has the shared-key
            cd /etc/bind
            sudo vim named.conf
            
            zone "myzone" {
                type master;
                file "/etc/bind/zonedbfiles/db.myzone";
                allow-transfer    { key "mykey"; };       <- key name
            };
            
            sudo rndc reload
            
            # triger zone transfer
            sudo vim /etc/bind/db.myzone
            
            ##***>
                (( XX+1 ))       ; Serial
            ##***<
            
            # check zone transfer
            root@slave:/var/cache/bind# cat /var/log/syslog
            
            # add key to slave server
            root@slave:/etc/bind# vim named.conf.tsig
            
            key "mykey" {
                algorithm HMAC-MD5;
                secret "KKK" ;
                };

            server [MASTER_IP] {
                keys { "mykey" ; };
                };
            
            root@slave:/etc/bind# vim named.conf
            
            ##+++>
            include "/etc/bind/named.conf.tsig";
            ##+++<
            
            root@slave:/etc/bind# rndc reload
            
            # check zone transfer
            root@slave:/etc/bind# cat /var/log/syslog
            ```
        - chroot
        
            ```bash
            sudo yum install bind bind-utils -y
            sudo yum install bind-chroot
            
            cd /var/named/chroot
            ```
        - port
        
            - tcp/53, udp/53
        - log
        
            - /var/log/syslog
    - client
    
        - dig

            - [Linux and Unix dig Command Examples](https://www.cyberciti.biz/faq/linux-unix-dig-command-examples-usage-syntax/)
        - nslookup

            - [How to Use Nslookup Command](https://networkproguide.com/how-to-use-nslookup-command/)
        - host
        
            - [host command in Linux with examples](https://www.geeksforgeeks.org/host-command-in-linux-with-examples/)
* Mail

    - server
    
        - postfix
        
            - setup

                ```
                sudo yum install postfix

                sudo vim /etc/postfix/master.cf
                
                ## enble TLS security
                #  -o smtpd_tls_security_level=encrypt
                
                sudo vim /etc/postfix/main.cf

                # see just customized settings
                postconf -n

                sudo systemctl restart postfix.service

                # send mail
                mail -s "hello root!" root@localhost
                Hi there! I am user1
                .

                # check the mail queue - method 1
                sendmail -bp

                # check the mail queue - method 2
                mailq
                ```
            - /usr/libexec/postfix/master
            
                - main process
            
                - configuration
                
                    `/etc/postfix/master.cf`
            - /etc/postfix/main.cf
            
                - controls mail processing
            - email aliases

                - ex. ssend mail to user3 who doesn't existed

                    ```
                    # change to user1 
                    su user1
                    sudo systemctl stop postfix.service
                    ls -la /etc/aliases.db

                    # add user3 as root aliases
                    sudo echo "user3:    root" >> /etc/aliases

                    # update /etc/aliases.db database
                    sudo newaliases
                    ls -la /etc/aliases.db
                    sudo systemctl start postfix

                    # send mail to root
                    mail -s "From user1 to root" root@localhost
                    Hi my dear friend are you there? 
                    .

                    # change to root
                    su -

                    # receive mail
                    mail
                    ```
            - virtual: redirect e-mail to the virtual destinations

                - ex. deliver user4@localhost to abc@xyz.com

                    ```
                    sudo systemctl stop postfix.service

                    sudo echo "abc@xyz.com        user4" >> /etc/aliases

                    # convert to binary file 
                    sudo postmap /etc/postfix/virtual

                    # update main.cf
                    sudo echo ""#virtual_alias_map = unix:hash:/etc/postfix/virtual" >> /etc/postfix/main.cf

                    sudo systemctl stop postfix.service

                    sudo tail /var/log/maillog
                    ```
            - port

                `tcp/25`

            - queued messages

                `/var/spool/postfix`
            - default mail drop directory

                `/var/spool/mail`
            - log

                `/var/log/maillog`
        - courier-imap
        
            - setup
            
                ```
                sudo apt-get install courier-imap
                
                sudo vim /etc/courier/imapd
                
                ##+++>
                MAILDIRPATH=XXX
                ##+++<
                
                sudo systemctl restart courier-imap.service 
                ```
            - port
            
                - tcp/143
            - storage format
            
                - maildir
        - courier-pop
        
            - setup
            
                ```
                sudo apt-get install courier-pop
                
                sudo vim /etc/courier/pop3d
                
                ##+++>
                MAILDIRPATH=XXX
                ##+++<
                
                sudo systemctl restart courier-pop.service
                ```
            - port
            
                - tcp/110
            - storage format
            
                - maildir
        - dovecot
        
            - setup
            
                ```
                sudo apt-get install dovecot-imapd dovecot-pop3d
                
                
                sudo systemctl restart dovecot
                
                # check status
                lsof -i | grep dovecot
                netstat -tulpen | grep 143
                netstat -tulpen | grep 110
                
                # view mail
                telnet localhost 110
                user XXX
                pass OOO
                list
                retr X
                ...
                quit
                ```
            - tls Configuration
                - setup
                    ```
                    # generate self signed SSL certificate
                    sudo openssl req -new -x509 -days 1000 -nodes -out "/etc/dovecot/private/XXX.pem" -keyout "/etc/dovecot/private/XXX.key"
                    
                    sudo vim /etc/dovecot/conf.d/10-ssl.conf
                    
                    ##+++>
                    # ssl_cert = </etc/dovecot/private/dovecot.pem
                    # ssl_key = </etc/dovecot/private/dovecot.key
                    ssl_cert = </etc/dovecot/private/XXX.pem
                    ssl_cert = </etc/dovecot/private/XXX.key
                    ##+++<
                    
                    # check pop3s connection
                    openssl s_client -connect server1:995
                    
                    # check imaps connection
                    openssl s_client -connect server1:imaps
                    ```
                - port
                
                    - imaps: tcp/993
                    - pop3s: tcp/995
            - doveconf
            
                - reads and parses Dovecot's configuration files and converts them into a simpler format 
                - show only settings with non-default values
                
                    - `doveconf -n`
            - doveadm
            
                - Dovecot administration tool
        - POP3 vs IMAP
        
            | POP3 (Post Office Protocol) | IMAP (Internet Message Access Protocol) |
            |-----------------------------|-----------------------------------------|
            | Downloads e-mails(could be configured to leave a copy on server) | e-mails stay on the server |
            | Mails are stored on the clients | Clients read e-mail remotely |
    - client
    
        - procmail
        
            - Setup
            
                ```
                sudo yum install procmail
                
                sudo vim /etc/postfix/main.cf
                
                ##+++>
                mailbox_command = procmail
                ##+++<
                
                sudo vim /etc/procmailrc
                
                ##+++>
                ### Define where we want to emails be stored
                MAILDIR=$HOME/mail

                ### Defining mail storage Format

                # For mbox format
                DEFAULT=$HOME/mail/inbox
                
                #For maildir format
                #DEFAULT=$HOME/mail/inbox/
                ##+++<
                
                # send email
                su - user1
                mkdir mail
                exit
                
                mail -s "test mbox for user 1" user1@localhost
                Hi this is my first message for testing mbox
                .
                
                mail -s "test mbox for user 1 #2" user1@localhost
                Hi this is my second message for testing mbox 
                .
                
                # view email
                su - user1
                cat mail/inbox
                
                # list email
                mail -f ~/mail/inbox
                ```
            - recipes
            
                - to filter email
                
                - format
                
                    ```
                    :0 [flags] [: lockfile-name ]
                    * [ condition_1_special-condition-character condition_1_regular_expression ]
                    * [ condition_2_special-condition-character condition-2_regular_expression ]
                    * [ condition_N_special-condition-character condition-N_regular_expression ]
                            special-action-character
                            action-to-perform
                    ```
                - ex.
                
                    ```
                    su - user1
                    vim .procmailrc
                    
                    ##+++>
                    :0:
                    * ^Subject:.lpi
                    linuxcert
                    
                    mail -s "lpi" user1@localhost
                    cat mail/linuxcert 
                    ##+++<
                    ```
* LDAP

    - defination
    
        - Object: Sometimes reffered to as a record or an entry, reperesnt a single item in the direstory. This object provides a description based on the structure of the schema.
        - Schema: This is the structure that is built to define the characteristics (or attributes) of an object. It also defines what can be stored in each attributes.
Attribute: This is a part of an object. One or more attributes make up an object, as defined by schema.
        - LDIF: Stands for LDAP Interchange Format. It is used to create objects within the LDAP directory. These values are placed into a file and can be loaded into a directory with the slapadd command.
        - DC: Stands for Domain Component. And that is one of the domain that is reflected in hierarchy.
        - OU: Stands for Organizational Unit.
        - CN: Stands for Common Name and is the name of object(often a username, but not always)
        - DN: Stands for Distinguished Name. Each object in our directory has to have a unique name in order to provide structure. It is build with a CN and one or more DC (example: cn=user,dc=abc,dc=com)
    - server
    
        - setup
        
            ```
            sudo yum install openldap openldap-servers openldap-clients.x86_64
            sudo systemctl start slapd
            firewall-cmd --add-service=ldap 
            
            ###########################
            ## Configuring LDAP Server
            ###########################
            # shows default configurations:
            slapcat -b cn=config
            
            # create a OpenLDAP administrative password
            slappasswd
            
            [{SSHA}XXXXXXXXXXXXXXXX]
            
            # Configure LDAP for domain and add administrative user.
            # create a ldif file
            vim cat mydb.ldif
            
            ##+++>
            dn: olcDatabase={2}hdb,cn=config
            changetype: modify
            replace: olcSuffix
            olcSuffix: dc=example,dc=com

            dn: olcDatabase={2}hdb,cn=config
            changetype: modify
            replace: olcRootDN
            olcRootDN: cn=ldapadm,dc=example,dc=com

            dn: olcDatabase={2}hdb,cn=config
            changetype: modify
            replace: olcRootPW
            olcRootPW: [{SSHA}XXXXXXXXXXXXXXXX]   <- copy from previous step
            ##+++<
            
            # add a ldap entry
            sudo ldapmodify -Y EXTERNAL -H ldapi:/// -f mydb.ldif
            
            # check the suitability of the OpenLDAP slapd.conf file
            sudo slaptest -u -v
            
            # see what we have added
            sudo slapcat -b "cn=config" | tail -n 18
            
            # search ldap entry for everything
            ldapsearch -x -b '' -s base '(objectclass=*)' namingContexts
            
            ##############################
            ## Configuring LDAP Database
            ##############################
            sudo cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
            sudo chown ldap:ldap /var/lib/ldap -R
            
            # create DN an the associated top levels DCs
            vim mydc.ldif
            
            ##+++>
            dn: dc=example,dc=com
            dc: example
            description: creating my dc 
            objectClass: dcObject
            objectClass: organization
            o: example,organization.
            ##+++<
            
            sudo systemctl stop slapd
            sudo slapadd -l mydc.ldif
            sudo systemctl start slapd
            
            # check result
            sudo slapcat
            ```
        - configuration files
        
            `/etc/openldap/slapd.d/`
        - ldap directory database and log
        
            `/var/lib/ldap`
        - port
        
            - tcp/389, tcp8/636
    - client

        - ldapsearch
        
            - opens a connection to an LDAP server, binds, and performs a search using specified parameters
            - ex.
                ```
                ldapsearch -x -b '' -s base '(objectclass=*)' namingContexts
                
                # search uid in managers ou
                ldapsearch -x -b 'ou=managers,dc=example,dc=com' '(objectclass=inetorgperson)' uid
                
                # search user 'Maria Garcia'
                ldapsearch (-L/LL/LLL) -x -b 'ou=managers,dc=example,dc=com' '(cn=Maria Garcia)' uid
                ```
        - ldapadd
        
            - add ldap entry
            - ex.
                ```
                # add manager ou
                vim myou.ldif

                ##+++>
                dn: ou=managers,dc=example,dc=com
                ou: managers
                description : Managers in the company
                objectclass: organizationalunit
                ##+++<

                sudo ldapadd -x -D "cn=ldapadm,dc=example,dc=com" -W -f myou.ldif
                
                sudo slapcat
                
                # add user for manager ou
                vim myuser.ldif
                
                ##+++>
                dn: cn=Bob Smith,ou=managers,dc=example,dc=com
                objectclass: inetOrgperson
                cn: Bob Smith
                cn: Bob J Smith
                cn: bob smith
                sn: smith
                uid: bjsmith
                userpassword: Aa12345
                carlicense: abc123
                homephone: 111-222-3344
                mail: b.smith@example.com
                mail: bsmith@example.com
                mail: bob.smith@exmple.com
                description: Big Boss
                ou: IT Department
                ##+++<
                
                sudo ldapadd -x -D "cn=ldapadm,dc=example,dc=com" -W -f myuser.ldif
                
                sudo slapcat
                
                # add more user for manager ou
                vim moreusers.ldif
                
                ##+++>
                dn: cn=James Smith,ou=managers,dc=example,dc=com
                objectclass: inetOrgPerson
                cn: James Smith
                cn: James J Smith
                sn: James
                uid: jsmith
                userpassword: Aa12345
                carlicense: A1B2C3
                homephone: 222-333-4455
                mail: j.smith@example.com
                mail: jsmith@example.com
                mail: james.smith@example.com
                ou: managers

                ### add anothr Entry to our OU
                dn: cn=Maria Garcia,ou=managers,dc=example,dc=com
                objectclass: inetOrgPerson
                cn: Maria Garcia
                sn: garcia
                uid: mgarcia
                userpassword: Aa12345
                carlicense: AABBCC
                homephone: 333-444-4466
                mail: m.garcia@example.com
                mail: mgarcia@example.com
                mail: maria.garcia@example.com
                ou: managers
                ##+++<
                
                sudo ldapadd -x -D "cn=ldapadm,dc=example,dc=com" -W -f moreusers.ldif
                sudo slapcat
                
                # add more ou
                vim moreou.ldif
                
                ##+++>
                ### Add Users OU
                dn: ou=users,dc=example,dc=com
                ou: users
                description : Ordinary users in the company
                objectclass: organizationalunit

                ### Add Devices OU

                dn: ou=sales,dc=example,dc=com
                ou: sales
                description: Sales group OU
                objectclass: organizationalunit
                ##+++<
                
                sudo ldapadd -x -D "cn=ldapadm,dc=example,dc=com" -W -f moreou.ldif
                sudo slapcat
                ```
        - ldapdelete
        
            - delete ldap entry
            - ex.
            
                `ldapdelete "cn= Maria Garcia,ou=managers,dc=example,dc=com" -x -D "cn=ldapadm,dc=example,dc=com" -W`
        - ldappasswd
        
            - change the password of an LDAP entry
            - ex.
            
                ```
                #change ldap administrator password
                ldapsswd
                
                # change Maria Garcia's password
                ldappasswd -x -D "cn=ldapadm,dc=example,dc=com" -s UserNewPassword -W "cn=Maria Garcia,ou=managers,dc=example,dc=com"
                ```
* PAM

    - configuratgion
    
        `/etc/pam.d`
    - control flag
        
        - requisite: Upon failure, the authentication process will be terminated immediately.
        - required: This will return failure after the remaining modules for this service and type have been invoked. (The success of the module is needed for the module-type facility to succeed. However, all remaining modules of the same type will be invoked)
        - sufficient: Upon success, the authentication process will be satisfied, unless a prior required module has failed the authentication.
        - optional: The success or failure of this module is only important if this is the only module associated with this service and this type.
    - module
    
        - directory
        
            `/lib/security` or `/lib64/security`
        - `pam_unix.so`: configures authentication via /etc/passwd and /etc/shadow
        
            - ex. remember last 3 user's password and dose not let user to set them again
            
                ```
                vim /etc/pam.d/system-auth
                
                ##+++>
                password    sufficient    pam_unix.so sha512 shadow nullok try_first_pass use_authtok remember=3
                ##+++<
                ```
        - `pam_cracklib.so`: provides strength-checking for passwords
        
            - ex. set minimum charachters wich are required for a password
            
                ```
                vim /etc/pam.d/system-auth
                
                ##+++>
                password    requisite     pam_pwquality.so try_first_pass local_users_only retry=3 minlen=10 authtok_type=
                ##+++<
                
                # note: pam_pwquality.s = pam_cracklib.so
                ```
        - `pam_limits.so`: sets limits on the system resources that can be obtained in a user-session
        
            - ex. avoid `pooruser` from loging more than once
            
                ```
                vim /etc/security/limits.conf
                
                ##+++>
                @pooruser    hard    maxlogins    1
                ##+++<
                ```
        - `pam_listfile.so`: allows or denies an action based on the presence of the item in a listfile
            
            - ex. vsftpd denying every user which his name/ her name is inside /etc/vsftpd/ftpusers

                ```
                vim /etc/pam.d/vsftfp

                ##+++>
                auth       required    pam_listfile.so item=user sense=deny file=/etc/vsftpd/ftpusers onerr=succeed
                ##+++<
                ```
        - `pam_sss.so`: System Security Services daemon (SSSD). Errors and results are logged through syslog.
    - sssd
    
        - Configure SSSD for LDAP authentication
        - install
        
            `yum install sssd`
        - ex.
            ```
            authconfig \
            --enablesssd \
            --enablesssdauth \
            --enablelocauthorize \
            --enableldap \
            --enableldapauth \
            --ldapserver=ldap://ldap.example.com:389 \
            --disableldaptls \
            --ldapbasedn=dc=example,dc=com \
            --enablerfc2307bis \
            --enablemkhomedir \
            --enablecachecreds \
            --update

            # check - method 1
            authconfig --test
            # check - method 2
            cat /etc/sssd/sssd.conf
            
            systemctl restart sssd
            
            # Update /etc/openldap.conf
            
            ##+++>
            SASL_NOCANON on
            URI ldaps://ldap.example.com:389
            BASE dc=example,dc=com
            TLS_REQUIRE never
            TLS_CACERTDIR /etc/pki/tls/cacerts
            TLS_CACERT /etc/pki/tls/certs/mybundle.pem
            ##+++<
            ```
    - nsswitch.conf
    
        - `/etc/pam.d/*` -> type (first column) = `auth` -> `/etc/nsswitch.conf`
    - [PAM - ArchWiki](https://wiki.archlinux.org/index.php/PAM)
* firewall

    * iptables

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
        - [iptables - ArchWiki](https://wiki.archlinux.org/index.php/iptables)
    * firewall-cmd

        - [Introduction to firewalld and firewall-cmd command on Linux](https://linuxconfig.org/introduction-to-firewalld-and-firewall-cmd-command-on-linux)
    * UFW

        - [UFW - Community Help Wiki - Official Ubuntu Documentation](https://help.ubuntu.com/community/UFW)
* VPN

    - server
    
        - OpenVPN
        
            - setup
        
                ```
                sudo yum install epel-release.noarch  -y
                yum repolist 
                yum search openvpn
                sudo yum install openvpn.x86_64 -y
                
                # open openvpn port
                sudo firewall-cmd --permanent --add-service openvpn
                sudo firewall-cmd --reload
                sudo firewall-cmd --list-all
                
                # generate shared key
                openvpn --genkey --secret openvpn.key
                
                # transfer shared-key to the client machine
                scp openvpn.key [CLIENT]:/home/[USER]
                
                # server: 10.10.10.1
                # client: 10.10.10.2
                vim server.conf
                
                ##+++>
                dev tun
                ifconfig 10.10.10.1 10.10.10.2
                secret openvpn.key
                ##+++<
                
                # start to listen openvpn client request...
                sudo openvpn --config server.conf
                ```
            - port
            
                - udp/1194
    - client
    
        - setup
        
            ```bash
            sudo apt install openvpn
            
            cd
            vim client.conf
            
            ##+++>
            remote [SERVER]
            dev tun
            ifconfig 10.10.10.2 10.10.10.1
            secret openvpn.key
            ##+++<
            
            # connectting to openvpn server
            sudo openvpn --config client.conf 
            ```
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
* grub

    - [GRUB 2 bootloader - Full tutorial](https://www.dedoimedo.com/computers/grub-2.html)
- syslinux

    - [Syslinux](https://wiki.archlinux.org/index.php/syslinux)
    - [How to create a multiboot USB drive using syslinux](https://opensourceict.com/linux/how-to-create-a-multiboot-usb-drive-using-syslinux)
    - [Tutorial Using Syslinux to make bootable media](https://tool.frogg.fr/Tutorial_Syslinux)
- ps

    - [Conquering the Command Line - ps](http://conqueringthecommandline.com/book/ps)
* top

    - [Cheatsheet on the `top` utility](https://dev.to/yanhan/cheatsheet-on-the-top-utility--82c)
* nice/renice

    - [How to Set Linux Process Priority Using nice and renice Commands](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/)
* lspci

    - [7 Linux lspci Command Examples to Get PCI Bus Hardware Device Info](https://www.thegeekstuff.com/2014/04/lspci-examples/)
* vmstat

    - [Linux Performance Monitoring with Vmstat and Iostat Commands](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)
* sar

    - [10 Useful Sar (Sysstat) Examples for UNIX / Linux Performance Monitoring](https://www.thegeekstuff.com/2011/03/sar-examples/)
* strace

    - [Linux Troubleshooting Cheatsheet: strace, htop, lsof, tcpdump, iftop & sysdig](https://sysdig.com/blog/linux-troubleshooting-cheatsheet/)
    - [Tracing Tools - strace, ltrace](https://doc.opensuse.org/documentation/leap/archive/42.3/tuning/html/book.sle.tuning/cha.tuning.tracing.html)
* sysctl

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
    - [Sysctl Command in Linux](https://linuxize.com/post/sysctl-command-in-linux/)
* udevadm

    - [udev](https://wiki.archlinux.org/index.php/udev)
* modprobe

    - [Kernel module](https://wiki.archlinux.org/index.php/Kernel_module)
    - [How to find Linux kernel driver associated to a device](https://wiki.st.com/stm32mpu/wiki/How_to_find_Linux_kernel_driver_associated_to_a_device#cite_note-3)
* dkms

    - [Dynamic Kernel Module Support](https://wiki.archlinux.org/index.php/Dynamic_Kernel_Module_Support)
* cdrecord

    - [CD writing using cdrecord](https://www.axllent.org/docs/cd-writing-using-cdrecord/)
* dd

    - [dd Cheat Sheet](https://www.jamescoyle.net/cheat-sheets/1012-dd-cheat-sheet)
* losetup

    - [How to create virtual block device (loop device/filesystem) in Linux](https://www.thegeekdiary.com/how-to-create-virtual-block-device-loop-device-filesystem-in-linux/)
* cryptsetup

    - [dm-crypt/Device encryption](https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption#Encryption_options_for_plain_mode)
    - [Encrypt disk with DM-Crypt Luks](https://linuxlasse.net/linux/howtos/Encrypt_disk_with_DM-Crypt_and_Luks)
* mdadm

    - [MDADM: Full usefull ‘Cheat Sheet’](https://upwork.link/arraysanddisks/mdadm-full-usefull-cheat-sheet/)
* hdparm

    - [hdparm](https://wiki.archlinux.org/index.php/hdparm)
* tgtadm/iscsiadm

    - [iSCSI devices](http://linux-training.be/sysadmin/ch12.html)
* scsi_id/multipath

    - [Configuring persistent storage Naming with UDEV on Linux](https://two-oes.medium.com/configuring-persistent-storage-naming-with-udev-on-linux-b81a6e7dc786)
* lvm

    - [LVM](https://wiki.archlinux.org/index.php/LVM)
* patch

    - [How to use diff and patch](https://www.pair.com/support/kb/paircloud-diff-and-patch/)
* tar

    - [CHEATSHEET: LINUX COMPRESS AND DECOMPRESS](https://cheatsheet.dennyzhang.com/cheatsheet-archive-a4)
* cpio
    
    - [Backing Up and Restoring Using the cpio Command](http://www.debianhelp.co.uk/cpiocommand.htm)
* rsync

    - [How to Backup Linux? 15 rsync Command Examples](https://www.thegeekstuff.com/2010/09/rsync-command-examples/)
* wall

    - [Linux wall Command Tutorial for Beginners (with Examples)](https://www.howtoforge.com/linux-wall-command/)
* update-alternatives

    - [How to Use update-alternatives Command on Ubuntu](https://linuxhint.com/update_alternatives_ubuntu/)
* ip
    
    - [Linux ip Command Networking Cheat Sheet](https://www.linuxtrainingacademy.com/linux-ip-command-networking-cheat-sheet/)
* nmcli

    - [27 nmcli command examples (cheatsheet), compare nm-settings with if-cfg file](https://www.golinuxcloud.com/nmcli-command-examples-cheatsheet-centos-rhel/)
* ss
    
    - [SS – Socket Statistics Commands Cheatsheet](https://neverendingsecurity.wordpress.com/2015/04/13/ss-socket-statistics-commands-cheatsheet/)
* iw/iwconfig/iwlist

    - [Network configuration/Wireless](https://wiki.archlinux.org/index.php/Network_configuration/Wireless)
* nmap

    - [Nmap Cheat Sheet](https://www.stationx.net/nmap-cheat-sheet/)
    - To see the SSL/TLS algorithms a server supports

        `nmap --script ssl-enum-ciphers -p 443 [TARGET|IP]`
    - `nmap -p xx,yy-zz A B n1.n2.n3.n4-n5`
* mtf

    - [How to use the Linux mtr (My Traceroute) command](https://vitux.com/how-to-use-the-linux-mtr-command/)
* nc

    - [NetcatCheatSheet](https://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf)
* fail2ban

    - setup
    
       ```bash
       sudo apt install fail2ban
       
       systemctl status fail2ban
       
       cd /etc/fail2ban
       
       # precedence: *.local > *.conf
       sudo cp fail2ban.conf fail2ban.local
       sudo vim fail2ban.local
       
       # A filter definition and a set of one or more actions to take when the filter is matched
       # ex. Ban Time and Retry Amount
       # ex. email alerts
       # ex. service/port ban rule
       sudo cp jail.conf jail.local
       sudo vim jail.local
       
       # check iptables
       sudo iptables -S
       
       # check status for ssh login fail
       sudo fail2ban-client status sshd
       ```
   - log
   
       - /var/log/fail2ban.log
* curl

    - [CURL CHEATSHEET](https://cheatsheet.dennyzhang.com/cheatsheet-curl-a4)
* xhost

    - | Server | Client |
      |--------|--------|
      | echo $DISPLAY to get [DISPLAY#] and [SCREEN#] |
      | xhost + [CLIENT_IP] |  |
      | telnet or ssh [CLIENT_IP] |  |
      |  | DISPLAY=[SERVER_IP]:[DISPLAY#.SCREEN#] [application, ex. gedit] |
      |  | exit |
      | xhost - [CLIENT_IP] |  |
      
      __NOTE__: $DISPLAY = [HOST_NAME:DISPLAY#.SCREEN#]
* gpg
    
    - | Encrypt | Decrpyt |
      |---------|---------|
      | x@X:-> gpg --gen-key |  |
      | x@X:-> gpg --list-keys |  |
      | x@X:-> gpg --export x > x.pub.key |  |
      | x@X:-> scp x.pub.key y@Y:/home/y/ |  |
      |  | y@Y:-> gpg --import x.pub.key |
      |  | y@Y:-> gpg --list-keys |
      |  | y@Y:-> echo "This is the message ..." > unencrypted-message
      |  | y@Y:-> gpg --output encrypted-message --recipient x --armor --encrypt unencrypted-message |
      |  | y@Y:-> scp encrypted-message x@X:/home/x/ |
      | x@X:-> gpg --decrypt encrypted-message |  |
      | x@X:-> gpg --output unencrypted-message --decrypt encrypted-message |  |
      
    - | Sign | Verify |
      |------|--------|
      | x@X:-> gpg --gen-key |  |
      | x@X:-> gpg --list-keys |  |
      | x@X:~> echo "This is the message to sign ..." > message |  |
      | x@X:~> gpg --output message.sig --sign message |  |
      | x@X:-> scp message.sig y@Y:/home/y |  |
      |  | y@Y:-> gpg --verify message.sig |
      |  | y@Y:-> gpg --output message --decrypt message.sig |
* openssl

    - [Cheat Sheet - OpenSSL](https://megamorf.gitlab.io/cheat-sheets/openssl/)
* iperf

    - [Iperf cheat sheet](https://www.jamescoyle.net/cheat-sheets/581-iperf-cheat-sheet)
* TCP Wrappers

    - [TCP Wrappers and xinetd](https://web.mit.edu/rhel-doc/5/RHEL-5-manual/Deployment_Guide-en-US/ch-tcpwrappers.html)
* ipsec

    - [CLI: Example for Using the Open-Source Software OpenSWan to Establish an IPSec VPN Tunnel to the](https://support.huawei.com/enterprise/en/doc/EDOC1000154805/d7d49f0a/cli-example-for-using-the-open-source-software-openswan-to-establish-an-ipsec-vpn-tunnel-to-the)
    - [strongSwan](https://wiki.archlinux.org/index.php/StrongSwan)
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

    - [Setting up a Raspberry Pi as a routed wireless access point](https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md)
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
    
        ```bash
        chsh -s /bin/zsh
        source ~/.zshrc
        ```
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
    - Build and Run
    
        ```bash
        sudo docker run --name yocto --rm -it \
        -v [/PATH/TO/WORKDIR]:/workdir \
        -v [/PATH/TO/DOWNLOADS]:/downloads \
        -v [/PATH/TO/SSTATE_CACHE]:/sstate_cache \
        --workdir=/workdir crops/poky
        
        # build
        . poky/oe-init-build-env
        bitbake core-image-minimal
        
        # Run QEMU
        runqemu qemuarm slirp nographic
        ```
        **Note:** quit QEMU: `ctrl-a x`
    - Run container
    
        ```bash
        sudo docker exec -u root -it yocto
        ```
* OpenBMC
    
    - [OpenBMC cheatsheet](https://github.com/openbmc/docs/blob/master/cheatsheet.md)
    - Build
    
        ```bash
        sudo docker run --name openbmc --rm -it \
        -v [/PATH/TO/WORKDIR]:/workdir \
        -v [/PATH/TO/DOWNLOADS]:/downloads \
        -v [/PATH/TO/SSTATE_CACHE]:/sstate_cache \
        --workdir=/workdir crops/poky
        
        # build romulus
        cd [/PATH/TO/OPENBMC]
        . setup romulus [/PATH/TO/BUILD]
        bitbake obmc-phosphor-image
        ```
    - Run QEMU
    
        ```bash
        sudo docker exec -u root -it openbmc bash
        
        apt install libpixman-1-dev
        
        # Run romulus
        ./qemu-system-arm -m 256 -M romulus-bmc -nographic \
        -drive file=[/PATH/TO/BUILD]/tmp/deploy/images/romulus/flash-romulus,format=raw,if=mtd \
        -net nic \
        -net user,hostfwd=:127.0.0.1:2222-:22,hostfwd=:127.0.0.1:2443-:443,hostname=qemu
        ```
        
        **Note:** user: `root`, password: `0penBmc`
* Intel-BMC/openbmc

    - Build
    
        ```bash
        sudo docker run --name intel-bmc --rm -it \
        -v [/PATH/TO/WORKDIR]:/workdir \
        -v [/PATH/TO/DOWNLOADS]:/downloads \
        -v [/PATH/TO/SSTATE_CACHE]:/sstate_cache \
        --workdir=/workdir crops/poky
        
        export TEMPLATECONF=[/PATH/TO/OPENBMC]/meta-openbmc-mods/meta-wolfpass/conf
        . [/PATH/TO/OPENBMC]/oe-init-build-env
        bitbake intel-platforms
        ```
    - Run QEMU
    
        ```bash
        sudo docker exec -u pokyuser -it openbmc bash
        
        runqemu intel-ast2500 slirp nographic
        ```

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
    |  | `echo "XX XX XX" \| xxd -r -p` |
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
    - [Function Index (The GNU C Library)](https://www.gnu.org/software/libc/manual/html_node/Function-Index.html)
    - [Linux System Call Table](https://thevivekpandey.github.io/posts/2017-09-25-linux-system-calls.html)
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
