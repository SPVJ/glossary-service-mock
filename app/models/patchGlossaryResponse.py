from fsCommonLib.commonModel.baseResponse import BaseResponse
from models.glossary import Glossary

class PatchGlossaryResponse(BaseResponse):
    glossary: Glossary