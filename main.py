import datetime,codecs,json,os
# from typing import Union
# import json
# from uuid import UUID

# from db import DBTypes
from fastapi import FastAPI, HTTPException



app = FastAPI()
#
# database = DBTypes.DB(host=env_data["settings"]["db"]["host"],
#                       port=env_data["settings"]["db"]["port"],
#                       name=env_data["settings"]["db"]["name"],
#                       user=env_data["settings"]["db"]["users"]["web"]["login"],
#                       password=env_data["settings"]["db"]["users"]["web"]["password"])
# database.connect()
#
# answer = {
#     "status": False,  # true - всё нормально, false - ошибка
#     "response": {
#
#     }
# }
#
# def verifyToUse(auth_token: str, secret_key: int = None, immortal: bool = False):
#     _ = database.getRowsTable("tokenizer", token=auth_token, key=secret_key, immortal=immortal)
#     result = bool(_)
#     if result and _[0][6] is not None: result = _[0][6] > datetime.datetime.now(_[0][6].tzinfo)
#     if not result: database.delete("tokenizer", id_token=_[0][0])
#     return result
#

@app.get("/test")
async def system(id_app: int, secret_key: str, login: str, password: str):
    return dict(success=True)


# if __name__ == "__main__":
#     try: main()
#     finally:
#         database.mydb.commit()
#         database.mydb.close()
