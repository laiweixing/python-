#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import logging.config
from os import path

CON_LOG = 'logging.conf'
log_file_path = path.join(path.dirname(path.abspath(__file__)), CON_LOG)
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()
