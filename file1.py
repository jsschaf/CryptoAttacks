#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           P�j��Ѐ�d�
�jn)[��j#nD?S<��+�Hi�����g(���ٺ�-����S�qR-�X)^W���tvY~S��_���~�>j�n=���PžZ�C�b`7��gp��+����v�%K`"""
from hashlib import sha256
print sha256(blob).hexdigest()
