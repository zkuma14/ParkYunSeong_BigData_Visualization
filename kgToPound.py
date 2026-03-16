kg = float(input("변환할 킬로그램(kg) 값을 입력하세요: "))

# 파운드(lb)로 변환 (1 kg = 2.20462 lb)
pounds = kg * 2.20462

# 결과 출력 (소수점 둘째 자리까지 반올림)
print(f"{kg}kg은 약 {round(pounds, 2)}lb(파운드)입니다.")