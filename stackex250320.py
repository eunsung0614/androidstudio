'''
stk = [10,20,30]
print(f'기존값 : {stk}')
stk.append(40)
print(f"40 추가 후 결과 = {stk}")
#topNum = stk.pop()
topNum = stk.pop(-1)
topNum = stk.pop()
print("topNum=%d"   %topNum)
print("topNum   ", topNum)
print(f'40 삭제 후 결과={stk}')
'''

def push(item):
    global top
    stack.append(item)
    top += 1 #top = top + 1

def pop():
    global top
    if len(stack) != 0 :
        #num = stack.pop()
        #num = stack.pop(-1)
        #num = stack.pop(top)
        num = stack.pop(len(stack)  -   1)
        top - 1 #top = top - 1
        return num
    else:
        print("stack이 텅 비어서 pop 불가함")

stack= [] #리스트 방식의 텅 빈 스택을 선언
top = -1 

if __name__ == "__main__":
    while True:
        num =int( input("1:삽입, 2:삭제, 3:종료 중 선택="))
        if num == 1:
            val = int(input("삽입할 데이터="))
            push(val)
            print("stack=", stack)
        elif num == 2:
            pop_val = pop()
            if pop_val != None:
                print("stack의 top값=%d" % pop_val)
                print("stack=", stack)
        else:
            print("3:종료를 입력하였습니다.")
            break