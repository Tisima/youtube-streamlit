import streamlit as st
import time

st.title('Streamit 超入門')

st.write("プログレスバーの表示")
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右')

expander = st.expander('問い合わせ')
expander.write('問い合わせを書く')
# option = st.text_input('あなたの趣味を教えてください')
# st.slider('あなたの今の調子は？', 0, 100, 500, 50)

# 'コンディション：', text
# # if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='ka', use_column_width=True)
