# misc

A playground to note something.

## Tool
- ipmitool

    - How to make in Ubuntu

    ```
    apt-get install automake libtool
    ./bootstrap
    ./configure
    make
    ```

- Beyond Compare

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