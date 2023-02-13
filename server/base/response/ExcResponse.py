#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 0:49
# @Author  : cap669
# @File    : ExcResponse.py
# @Software: PyCharm
from server.base.response.ApiResponse import ApiResponse


class BadrequestException(ApiResponse):
    status_code = 400
    result = None
    msg = '错误的请求'
    code = 10031


class LimiterResException(ApiResponse):
    status_code = 429
    result = None
    msg = '访问的速度过快'
    code = 429


class ParameterException(ApiResponse):
    status_code = 400
    result = {}
    msg = '参数校验错误,请检查提交的参数信息'
    code = 10031


class UnauthorizedException(ApiResponse):
    status_code = 401
    result = {}
    msg = '未经许可授权'
    code = 10032


class ForbiddenException(ApiResponse):
    status_code = 403
    result = {}
    msg = '失败！当前访问没有权限，或操作的数据没权限!'
    code = 10033


class NotfoundException(ApiResponse):
    status_code = 404
    result = {}
    msg = '访问地址不存在'
    code = 10034


class MethodnotallowedException(ApiResponse):
    status_code = 405
    result = {}
    msg = '不允许使用此方法提交访问'
    code = 10034


class OtherException(ApiResponse):
    status_code = 800
    result = {}
    msg = '未知的其他HTTPEOOER异常'
    code = 10034


class InternalErrorException(ApiResponse):
    status_code = 500
    result = {}
    msg = '系统崩溃了！'
    code = 500


class InvalidTokenException(ApiResponse):
    status_code = 401
    msg = '很久没操作，令牌失效'
    code = 401


class ExpiredTokenException(ApiResponse):
    status_code = 422
    msg = '很久没操作，令牌过期'
    code = 10050


class FileTooLargeException(ApiResponse):
    status_code = 413
    msg = '文件体积过大'
    code = 413


class FileTooManyException(ApiResponse):
    status_code = 413
    result = None
    msg = '文件数量过多'
    code = 10120


class FileExtensionException(ApiResponse):
    status_code = 401
    result = None
    msg = '文件扩展名不符合规范'
    code = 10121


class Success(ApiResponse):
    status_code = 200
    result = None
    code = 200


class Fail(ApiResponse):
    status_code = 200
    msg = '自定义成功返回'
    result = None
    code = 200
