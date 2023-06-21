import streamlit as st
import datetime
import time


class TimerApp():
    def __init__(self):

        st.title('Pomo timer')
        cols = st.columns(2)
        with cols[0]:
            input_min = st.number_input(':one: Set minutes ', min_value=0)
        with cols[1]:
            input_sec = st.number_input(':two: Set seconds', min_value=0, max_value=59)
        self.time_input = datetime.time(0, input_min, input_sec)
        cols = st.columns(3)
        with cols[1]:
            self.start_bttn = st.button('Start!')    
        st.text("")
        st.text("")
        self.message_placeholder = st.empty()
        self.is_running = False

        if self.start_bttn:
            self.count_down(self.time_input)


    def count_down(self, time_to_count:time):
        if not self.start_bttn or self.is_running:
            return
        self.is_running = True
        print('inside countdown, self.running: ', self.is_running)
        
        cols = st.columns(3)
        with cols[1]:
            reset_bttn = st.button('Reset')
        ss = (time_to_count.hour * 60 + time_to_count.minute) * 60 + time_to_count.second
        while ss > 0:
            self.message_placeholder.markdown(f":alarm_clock: Time left: {ss}s")
            time.sleep(1)
            ss -= 1
            if reset_bttn:
                st.write('Cancelling')
                st.experimental_rerun()
        self.message_placeholder.write('<b style="font-size:26px; color:Green;">Time\'s up!!!</b>',
    unsafe_allow_html=True)
        self._play_notif_sound()
        self.is_running = False

    def _play_notif_sound(self, sound_path = "https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3"): 
        html_string = f"""
                    <audio controls autoplay>
                    <source src="{sound_path}" type="audio/mp3" type="audio/mp3">
                    </audio>
                    """

        sound = st.empty()
        sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
        time.sleep(1.5)  # wait for 2 seconds to finish the playing of the audio
        sound.empty()  # optionally delete the element afterwards

app = TimerApp()
