#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import logging.config
from os import path

CON_LOG = './config/log.conf'
log_file_path = path.abspath(path.join(path.abspath('.'), CON_LOG))
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()
