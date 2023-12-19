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

def main():
    st.title('감지영독서논술 학생 여러분 안녕하세요!')

    num1 = st.number_input("당신의 키를 입력하세요.", key="height_input_1")
    num2 = st.number_input("당신의 몸무게를 입력하세요.", key="weight_input_1")

    if st.button('BMI 계산하기'):
        result = bmical(num1, num2)
        st.write(result)



if __name__ == "__main__":
    main()
