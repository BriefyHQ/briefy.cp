FROM briefy/plone:5.0.8
MAINTAINER Briefy <developers@briefy.co>

USER root
RUN mkdir -p /home/plone/ && chown -R plone:plone /home/plone 

USER plone
RUN ./bin/pip install -U setuptools zc.buildout==2.9.5

COPY ./docker.cfg /plone/instance/docker.cfg
COPY setup.* *.rst MANIFEST.in /plone/instance/src/briefy.cp/
COPY src /plone/instance/src/briefy.cp/src

USER root
RUN chown -R plone:plone /plone/instance/docker.cfg /plone/instance/src/briefy.cp

USER plone
RUN ./bin/buildout -Nc docker.cfg
