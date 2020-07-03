import time

input("엔터를 누르고 20초를 셉니다")
start = time.time()
input("20초에 엔터")
end = time.time()
print("시간 : ", end-start)
print("차이 : ", abs(20-(end-start)))