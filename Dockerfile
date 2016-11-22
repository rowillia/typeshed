FROM lyft/python:ac1269aa2cd19318cc1eb456b7b7ca5b2fdbb561
RUN curl -s -L -o /tmp/docker.tgz https://get.docker.com/builds/Linux/x86_64/docker-1.12.3.tgz && \
    tar -xvzf /tmp/docker.tgz -C /tmp && \
    mv /tmp/docker/* /usr/bin/ && \
    rm -rf /tmp/*
RUN apt-get update -y && \
    apt-get install -y --force-yes software-properties-common python-software-properties && \
    add-apt-repository ppa:webupd8team/java && \
    apt-get install -y --force-yes python3 python3-dev python3-pip
RUN pip3 install pip==8.1.1
COPY requirements.txt /code/containers/typeshed/requirements.txt
RUN /code/containers/python/pip-installer -3 /code/containers/typeshed/requirements.txt
COPY . /code/typeshed/
