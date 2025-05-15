from fastapi import FastAPI
from fastapi.responses import JSONResponse

from snack.snackDAO import snackDAO
app=FastAPI()
sDAO=snackDAO()
@app.get("/te.st")
def test():
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse({"A":"A"},headers=h)

@app.get("/snack.get")
def snackGet():
    print("조회")
    result=sDAO.snackInfoGet()
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/snack.reg")
def snackReg(
    s_name:str,
    s_price:int

):
    print("등록")
    print(s_name,s_price)
    result=sDAO.snackInfoReg(s_name,s_price)
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/snack.upd")
def snackReg(
    s_name:str,
    s_price:int

):
    print("수정")
    print(s_name,s_price)
    result=sDAO.snackInfoUpd(s_name,s_price)
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/snack.del")
def snackReg(
    s_name:str,
    s_price:int

):
    print("삭제")
    print(s_name,s_price)
    result=sDAO.snackInfoDel(s_name,s_price)
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)