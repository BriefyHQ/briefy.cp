FROM briefy/plone:5.0.8
MAINTAINER Briefy <developers@briefy.co>

USER root

COPY ./docker.cfg /plone/instance/docker.cfg
COPY setup.* *.rst MANIFEST.in /plone/instance/src/briefy.cp/
COPY src /plone/instance/src/briefy.cp/src
RUN mkdir -p /home/plone/

RUN chown -R plone:plone /plone /home/plone

USER plone

RUN pip install -r requirements.txt
RUN bin/buildout -Nc docker.cfg
