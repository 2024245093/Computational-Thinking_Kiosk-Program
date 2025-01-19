# 최종 수정: 6월 4일
dict_menus={"1-1":"아메리카노", "1-2":"라떼", "1-3":"바닐라 라떼", "1-4":"플랫화이트", "1-5":"에스프레소",
"2-1":"딸기스무디", "2-2":"바나나스무디", "2-3":"딸기바나나스무디", "2-4":"블루베리스무디", "3-1":"청포도에이드",
"3-2":"레몬에이드", "3-3":"자몽에이드", "3-4":"블루레몬에이드", "3-5":"망고에이드", "4-1":"아메리카노",
"4-2":"딸기스무디", "4-3":"망고에이드"}
dict_price={"1-1":2000, "1-2":2500, "1-3":3000, "1-4":2500, "1-5":1500, "2-1":4000, "2-2":4000,
"2-3":4300, "2-4":4000, "3-1":3000, "3-2":3000, "3-3":3000, "3-4":3200, "3-5":3000, "4-1":2000,
"4-2":4000, "4-3":3000}
dict_custom={"1-1":"덜 달게", "1-2":"기본", "1-3":"달게", "2-1":"얼음 추가 O", "2-2":"얼음 추가 X",
"3-1":"샷 추가 O", "3-2":"샷 추가 X", "4-1":"ICE", "4-2":"HOT"}
def customize_menu(a, b):
    stringify_menu = f"{a}-{b}"    #딕셔너리에 사용할 목적
    custom_list = [dict_menus[stringify_menu]]    #반환할 메뉴 리스트
    counter_sweeter = 0           #달게 횟수
    while True:
        print(f"======{dict_menus[stringify_menu]}======")
        print("""1. 당도 선택(기본)
2. 얼음 추가(기본)
3. 샷 추가(없음)
4. ICE/HOT(ICE)
5. 커스텀 완료
====================""")
        choose_custom = int(input("원하는 커스텀 메뉴를 골라주세요: "))
        if choose_custom == 5:
            break
        elif choose_custom == 1:
            print(f"""=====당도 선택=====
1. 덜 달게
2. 기본
3. 달게(+ 200원)
====================""")
        elif choose_custom == 2:
            print(f"""=====얼음 추가=====
1. 얼음 추가 O
2. 얼음 추가 X
====================""")
        elif choose_custom == 3:
            print(f"""=====샷 추가=====
1. 샷 추가 O
2. 샷 추가 X
====================""")
        elif choose_custom == 4:
            print(f"""=====ICE/HOT=====
1. ICE
2. HOT
====================""")
        choose_specific_custom = int(input("원하는 커스텀 방식을 골라주세요: "))
        stringify_custom = f"{choose_custom}-{choose_specific_custom}"
        if choose_custom == 1 and choose_specific_custom==3:     #달게 선택될시
            counter_sweeter += 1
        custom_list.append(dict_custom[stringify_custom])        #메뉴와 커스텀 append
    custom_list.append(dict_price[stringify_menu]+200*counter_sweeter)    #가격 append
    return custom_list
def choose_category():
    while True:
        print("""
====================
1번 커피
2번 스무디
3번 에이드  
4번 인기메뉴
====================
""")
        category = int(input("카테고리 선택\n"))
        if category == 1:
            print(f"""========커피========
0. 다시 카테고리 선택
1. 아메리카노 / {dict_price["1-1"]}원
2. 라떼 / {dict_price["1-2"]}원
3. 바닐라 라떼 / {dict_price["1-3"]}원
4. 플랫화이트 / {dict_price["1-4"]}원
5. 에스프레소 / {dict_price["1-5"]}원
====================""")
        elif category == 2:
            print(f"""=======스무디=======
0. 다시 카테고리 선택
1. 딸기스무디 / {dict_price["2-1"]}원
2. 바나나스무디 / {dict_price["2-2"]}원
3. 딸기바나나스무디 / {dict_price["2-3"]}원
4. 블루베리스무디 / {dict_price["2-4"]}원
====================""")
        elif category == 3:
            print(f"""=======에이드=======
0. 다시 카테고리 선택
1. 청포도에이드 / {dict_price["3-1"]}원
2. 레몬에이드 / {dict_price["3-2"]}원
3. 자몽에이드 / {dict_price["3-3"]}원
4. 블루레몬에이드 / {dict_price["3-4"]}원
5. 망고에이드 / {dict_price["3-5"]}원
====================""")
        elif category == 4:
            print(f"""=======인기메뉴=======
0. 다시 카테고리 선택
1. 아메리카노 / {dict_price["4-1"]}원
2. 딸기스무디 / {dict_price["4-2"]}원
3. 망고에이드 / {dict_price["4-3"]}원
====================""")
        menu = int(input())
        if menu != 0:
            final_menu = customize_menu(category, menu)
            return final_menu
is_takeout = input("""
====================
1. 포장
2. 매장
====================\n""")
menus = []
total_price = 0
def main():
    global total_price
    while True:
        chosen_menu = choose_category()
        total_price += chosen_menu[-1]
        chosen_menu[-1] = str(chosen_menu[-1])
        menus.append(chosen_menu)
        print("현재 메뉴")
        print("====================")
        for i in menus:
            print(" / ".join(i)+"원")
        print("====================")
        is_more = input("추가 메뉴 선택이 필요하신가요? [Y/N]: ")
        if is_more == "N" or is_more=="n":
            break
main()
while True:
    if len(menus) == 0:
        main()
    print("최종 메뉴")
    print("====================")
    for i, elem in enumerate(menus, start=1):
        print(i, " / ".join(elem)+"원")
    print("====================")
    print(f"총 가격 {total_price}원 입니다.")
    print("""취소하실 메뉴가 있나요?
1. O
2. X""")
    is_cancel = int(input())
    if is_cancel == 1:
        cancel_menu = int(input("취소할 메뉴를 선택하세요: "))
        total_price -= int(menus[cancel_menu-1][-1])
        menus.pop(cancel_menu-1)
    elif is_cancel == 2:
        break
print("최종 메뉴")
print("====================")
for i, elem in enumerate(menus, start=1):
    print(i, " / ".join(elem)+"원")
print("====================")
print(f"총 가격 {total_price}원 입니다.")
print("""====================
1. 카드
2. 현금
====================""")
payment_method = int(input("결제 수단을 선택해주세요: "))
print(f"{total_price}원 결제가 완료되었습니다.")
print("""영수증 출력 여부를 선택해주세요
1. O
2. X""")
is_receipt = int(input())
print("주문이 완료되었습니다.")
print("주문 번호는 1번입니다.")