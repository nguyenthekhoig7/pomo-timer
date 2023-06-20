import streamlit as st 
import datetime
import time

def count_down(time_amount, message_placeholder):
    ss = (time_amount.hour * 60 + time_amount.minute) * 60 + time_amount.second
    # stop_bttn = st.button('Stop')
    # reset_bttn = st.button('Reset')
    while ss > 0:
        message_placeholder.write(f"Time left: {ss}s")
        time.sleep(1)
        ss -= 1

        # if stop_bttn:
        #     message_placeholder.write(f"Time left: {ss}s")
        #     break
        # if reset_bttn:
        #     stop_count_down()
        #     break

# def stop_count_down():
#     st.write("Input time then click 'Start!'")

st.title('Pomodoro timer')
time_input = st.time_input('Set a timer for', datetime.time(0, 1))
start_bttn = st.button('Start!')
message_placeholder = st.empty()
if start_bttn:
    count_down(time_input, message_placeholder)

