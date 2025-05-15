from DBconnectLibrary.kimDBmanager import kimDBmanager

class snackDAO:
    def snackInfoGet(self):
        con, cur = None, None  # 초기화
        try:
            con, cur = kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            sql = "SELECT * FROM snack"

            cur.execute(sql)
            snacks = []
            for s_name, s_price in cur:
                s = {
                    "s_name": s_name,
                    "s_price": s_price
                }
                snacks.append(s)
            return snacks
        except Exception as e:
            print("조회 실패:", e)
            return {"result": "조회 실패"}
        finally:
            if con and cur:
                kimDBmanager.closeConCur(con, cur)

    def snackInfoReg(self, s_name,s_price):
        con, cur = None, None  # 초기화
        try:
            con, cur = kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            sql = "INSERT INTO snack (s_name, s_price) VALUES (:1, :2)"
            cur.execute(sql, (s_name, s_price))


            con.commit()
        except Exception as e:
            print("등록 실패:", e)
            return {"result": "등록 실패"}
        finally:
            if con and cur:
                kimDBmanager.closeConCur(con, cur)

    # snack정보 삭제하기 
    def snackInfoDel(self, s_name,s_price):
        con, cur = None, None  # 초기화
        try:
            con, cur = kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            sql = "DELETE FROM snack WHERE s_name = :1 AND s_price = :2"
            cur.execute(sql, (s_name, s_price))


            con.commit()
        except Exception as e:
            print("삭제 실패:", e)
            return {"result": "삭제 실패"}
        finally:
            if con and cur:
                kimDBmanager.closeConCur(con, cur)

    #snack정보 수정하기 
    def snackInfoUpd (self, s_name,s_price):
        con, cur = None, None  # 초기화
        try:
            con, cur = kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            sql = "UPDATE snack SET s_price = :1 WHERE s_name = :2"
            cur.execute(sql, (s_price, s_name))

            con.commit()
        except Exception as e:
            print("수정 실패:", e)
            return {"result": "수정 실패"}
        finally:
            if con and cur:
                kimDBmanager.closeConCur(con, cur)