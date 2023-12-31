# # Array 배열 왜 써 ? (관련된)여러 변수들을 묶어서 관리하려고.
# w1 = 'SJ'
# w2 = 'SH'
# w3 = 'BH'
# w3 = 'TH'

# wait = ['SJ', 'SH', 'BH', 'TH']
# # w1 == wait[0]


# # 메서드 (배열에 추가) append
# mem = [100]
# # mem.append(90)
# mem = [100, 90]
# # mem.append(60)
# mem = [100, 90, 60]
# # mem.append(100)
# mem = [100, 90, 60, 160]


# ATM
def withdrow():
    global account_balance
    amount = int(input("출금할 잔액을 입력해 주세요:"))
    if account_balance < amount:
        print("잔액부족")
    else:
        account_balance -= amount
        history.append(account_balance)


def deposit():
    global account_balance
    amount = int(input("입금할 잔액을 입력해 주세요:"))
    account_balance += amount
    history.append(account_balance)


def show_history():
    print("=======history========")
    for i, step in enumerate(history):
        print(f"{i+1}  :   {step}")
    # print(*history)
    print("=====================")


# -------------main---------------


global account_balance
account_balance = 100000

# history = [account_balance]
history = []
history.append(account_balance)

flag = True
while flag:
    print('''=======manual========
1: withdrow
2: deposit
3: history
4 :exit''')

    command = int(input("Enter your command: "))
    if command == 4:
        flag = False
        # break
    elif command == 1:
        # 출금
        print(f"출금전 잔액 : {account_balance}")
        withdrow()
        print(f"출금후 잔액 : {account_balance}")
    elif command == 2:
        # 입금
        print(f"입금전 잔액 : {account_balance}")
        deposit()
        print(f"입금후 잔액 : {account_balance}")
    elif command == 3:
        # 조회
        show_history()
    else:
        print("Not vaild command")
