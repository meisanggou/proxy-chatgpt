from centos

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* && \
    yum install -y python39 && \
    pip3 install openai gevent gunicorn flask-helper flask-login eventlet

ENV CODEPATH /opt/proxy-chatgpt
ENV PYTHONPATH $CODEPATH
WORKDIR $CODEPATH
ENV LISTENPORT 2405

CMD ["bash", "-c", "gunicorn -b 0.0.0.0:$LISTENPORT -w 4 -k gevent --chdir /opt/proxy-chatgpt/proxy_chatgpt/web web:app"]
