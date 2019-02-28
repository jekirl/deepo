# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source
from .python import Python


@dependency(Python)
@source('pip')
class Pytorch(Module):

    def build(self):
        cuver = 'cpu' if self.composer.cuda_ver is None else 'cu%d' % (
            float(self.composer.cuda_ver) * 10)
        return r'''
            $PIP_INSTALL \
                future \
                numpy \
                protobuf \
                enum34 \
                pyyaml \
                typing \
            	torchvision_nightly \
                && \
            $PIP_INSTALL \
                torch_nightly -f \
                https://download.pytorch.org/whl/%s/torch-1.0.1.post2-cp37-cp37m-linux_x86_64.whl \
                && \
        ''' % cuver
