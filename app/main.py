import uvicorn
from fastapi import FastAPI, Request
from routers.glossaryRouter import GlossaryRouter
from services.glossaryService import GlossaryService
from repositories.glossaryRepository import GlossaryRepository
from fsCommonLib.databases.database import engine, get_db, Base
from fsCommonLib.handlers.exceptionHandler import addExceptionHandler
from fsCommonLib.logs.logMiddleware import addLoggingMiddleware


Base.metadata.create_all(bind=engine)


glossaryRepository = GlossaryRepository(db= next(get_db()))
glossaryService = GlossaryService(glossaryRepository=glossaryRepository)
glossaryAuth = GlossaryRouter(glossaryService=glossaryService)

app = addExceptionHandler(FastAPI())
app = addLoggingMiddleware(app=app)
app.include_router(glossaryAuth.router)


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8080)