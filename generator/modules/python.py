# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source, version
from .tools import Tools


@dependency(Tools)
@version('3.7')
@source('apt')
class Python(Module):

    def __init__(self, manager, **args):
        super(self.__class__, self).__init__(manager, **args)
        if self.version not in ('2.7', '3.6', '3.7'):
            raise NotImplementedError('unsupported python version')

    def build(self):
        return (r'''
            DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
                software-properties-common \
                && \
            add-apt-repository ppa:deadsnakes/ppa && \
            apt-get update && \
            DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
                python3.7 \
                python3.7-dev \
                python3-distutils%s \
                && \
            wget -O ~/get-pip.py \
                https://bootstrap.pypa.io/get-pip.py && \
            python3.7 ~/get-pip.py && \
            ln -s /usr/bin/python3.7 /usr/local/bin/python3 && \
            ln -s /usr/bin/python3.7 /usr/local/bin/python && \
            $PIP_INSTALL \
                setuptools \
                && \
            ''' % (
                '' if self.composer.ubuntu_ver.startswith('18.') else '-extra'
            ) if self.version == '3.7' else
            r'''
            DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
                python-pip \
                python-dev \
                && \
            $PIP_INSTALL \
                setuptools \
                pip \
                && \
            '''
        ).rstrip() + r'''
            $PIP_INSTALL \
                numpy \
                scipy \
                pandas \
                cloudpickle \
                scikit-learn \
                matplotlib \
                Cython \
                && \
        '''
