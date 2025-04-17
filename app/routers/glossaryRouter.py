from models.patchGlossaryRequest import PatchGlossaryRequest
from fastapi import APIRouter, Body
from models.postGlossaryRequest import PostGlossaryRequest
from services.glossaryService import GlossaryService
from fsCommonLib.logs.logger import logger

class GlossaryRouter:
    def __init__(self, glossaryService: GlossaryService):
        self.glossaryService = glossaryService

        self.router = APIRouter(
            responses = {404: {"description": "Not found"}}
        )

        self.router.add_api_route(
            "/glossary",
            self.getGlossary,
            methods=["GET"]
        )

        self.router.add_api_route(
            "/glossary",
            self.postGlossary,
            methods=["POST"]
        )

        self.router.add_api_route(
            "/glossary/{id}",
            self.patchGlossary,
            methods=["PATCH"]
        )

        self.router.add_api_route(
            "/glossary/{id}",
            self.deleteGlossary,
            methods=["DELETE"]
        )

    def getGlossary(self):
        logger.info("GET /glossary controller handling")
        
        return self.glossaryService.getGlossary()
    
    def postGlossary(self, request: PostGlossaryRequest = Body(...)):
        logger.info("POST /glossary controller handling")

        return self.glossaryService.postGlossary(request)
    
    def patchGlossary(self, id: str = "0", request: PatchGlossaryRequest = Body(...)):
        logger.info("PATCH /glossary{} controller handling".format(id))

        return self.glossaryService.patchGlossary(id,request)

    def deleteGlossary(self, id: str = "0"):
        logger.info("DELETE /Glossary/{} controller handling".format(id))

        return self.glossaryService.deleteGlossary(id)
