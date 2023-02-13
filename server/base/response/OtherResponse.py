from server.base.response.ApiResponse import ApiResponse


class ExcResponse(ApiResponse):
    status_code = 405


class ValidaResponse(ApiResponse):
    status_code = 404
