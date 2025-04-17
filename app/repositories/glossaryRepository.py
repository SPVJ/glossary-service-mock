from models.glossaryEntity import GlossaryEntity
from models.glossary import Glossary
from sqlalchemy.orm import Session

class GlossaryRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def queryById(self, id: int):
        
        tempData = self.db.query(GlossaryEntity).filter(GlossaryEntity.id == id).first()
        return tempData

    def insertTempData(self, tempDataEntity : GlossaryEntity):
            self.db.add(tempDataEntity)
            self.db.commit()
            self.db.refresh(tempDataEntity)
    
    def deleteTempData(self, id: int):
         
        tempData = self.db.query(GlossaryEntity).filter(GlossaryEntity.id == id).first()
        self.db.delete(tempData)
        self.db.commit()