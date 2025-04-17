from typing import Optional, List
from fsCommonLib.commonModel.baseResponse import BaseResponse
from models.glossary import Glossary

class PostGlossaryResponse(BaseResponse):
    glossary: Glossary
