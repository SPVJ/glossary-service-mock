import datetime

from models.deleteGlossaryResponse import DeleteGlossaryResponse
from models.postGlossaryRequest import PostGlossaryRequest
from models.getGlossaryResponse import GetGlossaryResponse
from models.postGlossaryResponse import PostGlossaryResponse
from models.glossary import Glossary
from models.patchGlossaryResponse import PatchGlossaryResponse
from repositories.glossaryRepository import GlossaryRepository
from fsCommonLib.logs.logger import logger
from fsCommonLib.handlers.genericException import GenericException
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from uuid import uuid4

#TODO Mocking Only
glossaries = [
    Glossary(id="id1", key="example", value="test value", createdAt=str(datetime.datetime.now()), updatedAt=str(datetime.datetime.now())),
    Glossary(id="id2", key="example", value="test value", createdAt=str(datetime.datetime.now()), updatedAt=str(datetime.datetime.now()))
]
counter = 2

class GlossaryService:
    def __init__(self, glossaryRepository: GlossaryRepository):
        self.glossaryRepository = glossaryRepository
    
    def getGlossary(self):

        #Mocking = no need
        # tempData = self.glossaryRepository.queryById(request.email)

        # if tempData == None :
        #     logger.error("GET /example query data not found")
        #     raise GenericException(status_code=500, err_code=9001, description="No Data Found")

        logger.info("Querying all glossaries")


        return GetGlossaryResponse(
            status="2000",
            code="Success",
            glossary=glossaries
        )
    
    def postGlossary(self, request: PostGlossaryRequest):

        #Mocking

        #  tempDataEntity = GlossaryEntity(id=request.id, value= request.value)
        #
        # logger.info("Inserting to temp_data table with entity : {}".format(tempDataEntity))

        # try:
        #     self.glossaryRepository.insertTempData(tempDataEntity)
        # except IntegrityError as e:
        #     assert isinstance(e.orig, UniqueViolation)
        #     raise GenericException(status_code=400, err_code=9002, description="Bad Request, Id {} already exist".format(tempDataEntity.id))
        global counter
        counter += 1
        newId = "id"+str(counter)
        logger.info("Adding new glossary with key {} and value {} with id {}".format(request.key, request.value, newId))
        global glossaries
        newGlossary = Glossary(id= newId, key=request.key, value=request.value, createdAt=str(datetime.datetime.now()), updatedAt=str(datetime.datetime.now()))
        glossaries.append(newGlossary)

        return PostGlossaryResponse(
            status="2000",
            code="Success",
            glossary=newGlossary
        )

    def patchGlossary(self,id : str, request: PostGlossaryRequest):
        # Mocking

        #  tempDataEntity = GlossaryEntity(id=request.id, value= request.value)
        #
        # logger.info("Inserting to temp_data table with entity : {}".format(tempDataEntity))

        # try:
        #     self.glossaryRepository.insertTempData(tempDataEntity)
        # except IntegrityError as e:
        #     assert isinstance(e.orig, UniqueViolation)
        #     raise GenericException(status_code=400, err_code=9002, description="Bad Request, Id {} already exist".format(tempDataEntity.id))

        logger.info("Updating a glossary with key {} and value {} with id {}".format(request.key, request.value, id))
        global glossaries
        updatedGlossary = None

        for index in range(len(glossaries)):
            if glossaries[index].id == id:
                glossaries[index].key = request.key
                glossaries[index].value = request.value
                glossaries[index].updatedAt = str(datetime.datetime.now())
                updatedGlossary = Glossary(id=id, key=request.key, value=request.value,
                                           createdAt=glossaries[index].createdAt,
                                           updatedAt=str(datetime.datetime.now()))


        return PatchGlossaryResponse(
            status="2000",
            code="Success",
            glossary=updatedGlossary
        )

    def deleteGlossary(self, id: str):
        # Mocking

        #  tempDataEntity = GlossaryEntity(id=request.id, value= request.value)
        #
        # logger.info("Inserting to temp_data table with entity : {}".format(tempDataEntity))

        # try:
        #     self.glossaryRepository.insertTempData(tempDataEntity)
        # except IntegrityError as e:
        #     assert isinstance(e.orig, UniqueViolation)
        #     raise GenericException(status_code=400, err_code=9002, description="Bad Request, Id {} already exist".format(tempDataEntity.id))

        logger.info("Deleting a glossary with id {}".format(id))
        global glossaries

        for index in range(len(glossaries)):
            if glossaries[index].id == id:
                glossaries.pop(index)

        return DeleteGlossaryResponse(
            status="2000",
            code="Success",
            message="Successfully deleted id {}".format(id)
        )
