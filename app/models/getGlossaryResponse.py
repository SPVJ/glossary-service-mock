from fsCommonLib.commonModel.baseResponse import BaseResponse
from models.glossary import Glossary
from typing import List, Optional

class GetGlossaryResponse(BaseResponse):
    glossary: Optional[List[Glossary]]