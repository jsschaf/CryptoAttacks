#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           P�j��Ѐ�d�
�jn)[���#nD?S<��+�Hi�����g(���Y��-����S qR-�X)^W���tvY~S��_�����>j�n=���PžZ�C�b`7�4gp��+����v��%K`"""
from hashlib import sha256
print sha256(blob).hexdigest()
