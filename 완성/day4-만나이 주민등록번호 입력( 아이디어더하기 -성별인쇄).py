from datetime import datetime

num = input("주민번호(6): ")
chk = input("뒷자리(1): ")

# 첫 두글자 씩 읽어 와서 정수형으로 바꿉니다
year = int(num[:2])
month = int(num[2:4])
day = int(num[4:])

# 연도를 4자리로 만듭니다

if chk == '1'or chk == '2':
    year += 1900     ######## 계산식을 알맞게 수정하세요
else:
    year += 2000     ######## 계산식을 알맞게 수정하세요

age = datetime.today().year - year

# 만나이를 계산하기 위해서는 생일이 지났는지 판단을 해야 합니다
# 생일이 지나지 않았으면 -1 을 합니다

if month > datetime.today().month:
    age -= 1
elif month == datetime.today().month:
    if day > datetime.today().day:
        age -= 1
        
# 성별 구분합니다.       
if chk == '1'or chk == '3':
    gender = '남성'
else:
    gender = '여성'   
    
# 결과를 출력합니다
print("생년월일:", year, month, day)
print("오늘날짜:", datetime.today().year, datetime.today().month, datetime.today().day)
print("만  나이:", age, "살")
print("성    별:", gender)






