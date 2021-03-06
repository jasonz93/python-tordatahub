#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

class DatahubException(Exception):
    """
    There was an base exception class that occurred while handling your request to tordatahub server.
    """
    def __init__(self, status_code, request_id, error_code, error_msg):
        super(DatahubException, self).__init__(error_msg)
        self.status_code = status_code
        self.request_id = request_id
        self.error_code = error_code
        self.error_msg = error_msg

    def __str__(self):
        return "status_code:%d, request_id:%s, error_code:%s, error_msg:%s"\
                %(self.status_code, self.request_id, self.error_code, self.error_msg) 

# A long list of server defined exceptions
class ObjectAlreadyExistException(DatahubException):
    """
    The exception is raised while Datahub Object that you are creating is alreay exist.
    """
    def __init__(self, status_code, request_id, error_code, error_msg):
        super(ObjectAlreadyExistException, self).__init__(status_code, request_id, error_code, error_msg)

class NoSuchObjectException(DatahubException):
    """
    The exception is raised while Datahub Object that you are handling is not exist.
    """
    def __init__(self, status_code, request_id, error_code, error_msg):
        super(NoSuchObjectException, self).__init__(status_code, request_id, error_code, error_msg)

class InvalidParameterException(DatahubException):
    """
    The exception is raised while that your handling request parameter is invalid.
    """
    def __init__(self, status_code, request_id, error_code, error_msg):
        super(InvalidParameterException, self).__init__(status_code, request_id, error_code, error_msg)

class InvalidShardOperationException(DatahubException):
    """
    The opertaion of shard is not support yet.
    """
    def __init__(self, status_code, request_id, error_code, error_msg):
        super(InvalidShardOperationException, self).__init__(status_code, request_id, error_code, error_msg)

class MalformedRecordException(DatahubException):
    """
    The record is malformed.
    """
    def __init__(self, status_code, request_id, error_code, error_msg):
        super(MalformedRecordException, self).__init__(status_code, request_id, error_code, error_msg)

class LimitExceededException(DatahubException):
    """
    Too many request.
    """
    def __init__(self, status_code, request_id, error_code, error_msg):
        super(LimitExceededException, self).__init__(status_code, request_id, error_code, error_msg)

class ServerInternalError(DatahubException):
    """
    The Datahub server occured error.
    """
    def __init__(self, status_code, request_id, error_code, error_msg):
        super(ServerInternalError, self).__init__(status_code, request_id, error_code, error_msg)

