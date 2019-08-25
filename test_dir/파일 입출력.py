# 파일 입출력
# p.13 파일 열기 존재 x
f = open("test.py", "r")
print("file open")
f.close()

f = open("tttt.py", "r")
print("file open")
f.close()


# p.14 파일 열기 존재 x 쓰기
f = open("test.py", "w")
print("file open")
f.close()


# p.15 파일 읽기 read()
# 파일 객체를 생성합니다.
f = open("test.py", "r")
# 파일 전체를 읽습니다.
line = f.read()
# 파일의 내용을 출력합니다.
print(line)
# 파일 객체를 닫습니다.
f.close()


# p.16 파일 읽기 readline()
f = open("test.py", "r")
line1 = f.readline()
line2 = f.readline()
print(line1.strip(), end="end")   # 개행문자
print(line2, end="end")           # 제거 확인위해
f.close()


# p.17 파일 읽기 readlines()
f = open("test.py", "r")
lines = f.readlines()
print(lines)
f.close()


# p.18 파일 읽기 seek(0)
f = open("test.py", "r")
line1 = f.readline()
line2 = f.readline()
f.seek(0)
line3 = f.readline()

print(line1)
print(line2)
print(line3)

f.close()



# p.19 파일 쓰기 기본
# 파일 객체를 생성합니다.
f = open("writeTest.txt", "w")
name = "Yoon"
num = "2010100"
score = 95

# write() 함수를 이용해 파일 내용을 작성합니다.
f.write(name + "\n")
f.write(num + "\n")
f.write(str(score) + "\n")

# 파일 객체를 닫습니다.
f.close()


# p.20 추가모드
f = open("writeTest.txt", "a")
name = "Lee"
num = "2010200"
score = 90
f.write(name + "\n")
f.write(num + "\n")
f.write(str(score) + "\n")
f.close()



# p.22 피클링
import pickle

my_list = ["Yoon", "2010100", 95]
f = open("testpickle.dat", "wb")   # 이진모드 필수
pickle.dump(my_list, f)
f.close()


# p.23 언피클링
import pickle

f = open("testpickle.dat", "rb")   # 이진모드 필수
my_list = pickle.load(f)
print(my_list)
f.close()