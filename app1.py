import streamlit as st

def bmical(num1, num2):
    k = num1 / 100
    k = k ** 2
    d = num2 / k
    if d >= 25:
        f = '비만'
    elif d >= 23:
        f = '과체중'
    elif d >= 18.5:
        f = '정상'
    elif d < 18.5:
        f = '저체중'
    d = round(d, 1)
    result = "BMI 지수: " + str(d) + ", " + f + "입니다."
    return result

def calculate_average_bmi(bmi_list):
    if len(bmi_list) == 0:
        return 0
    total_bmi = sum(bmi_list)
    average_bmi = total_bmi / len(bmi_list)
    return average_bmi

def main():
    st.title('월봉고등학교 학생 여러분 안녕하세요!')
    bmi_list = []

    num1 = st.number_input("당신의 키를 입력하세요.", key="height_input_1")
    num2 = st.number_input("당신의 몸무게를 입력하세요.", key="weight_input_1")

    if st.button('BMI 계산하기'):
        result = bmical(num1, num2)
        bmi_list.append(num2 / (num1 / 100) ** 2)
        st.write(result)

    if st.button('초기화'):
        num1 = 0
        num2 = 0
        bmi_list = []

    if st.button('입력한 키와 몸무게 정리하기'):
        data = {'키': num1, '몸무게': num2}
        st.write("입력한 키와 몸무게:")
        st.write(data)

    if st.button('BMI 평균치 계산하기'):
        average_bmi = calculate_average_bmi(bmi_list)
        if average_bmi == 0:
            st.write("BMI 평균치를 계산할 데이터가 없습니다.")
        else:
            st.write("BMI 평균치:", round(average_bmi, 1))

if __name__ == "__main__":
    main()
