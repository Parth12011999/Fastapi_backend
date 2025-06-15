from fastapi.responses import JSONResponse

class ResponseService:
    @staticmethod
    def success(data=None, message="Success"):
        return JSONResponse(content={
            "success": True,
            "data": data,
            "message": message
        })

    @staticmethod
    def error(data=None, message="Error"):
        return JSONResponse(content={
            "success": False,
            "data": data,
            "message": message
        })
