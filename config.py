#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
class Config:
    API_ID = int(os.environ.get("13780698", ''))
    API_HASH = os.environ.get("56536f4127ca90a7785d11d2c8e1f031", "")
    BOT_TOKEN = os.environ.get("5598089851:AAGAhMrGCqfM-C0BXQw6aDRb5-4yGEM2qlI", "")     
    LOG_CHANNEL = int(os.environ.get("-1001720413733", ''))
