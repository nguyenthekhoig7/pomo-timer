import streamlit as st
import datetime
import time


class TimerApp():
    def __init__(self):

        st.title('Pomo timer')
        st.markdown('<b>1. Timer</b>', unsafe_allow_html=True)
        cols = st.columns(5)
        with cols[1]:
            input_min = st.number_input(':one: Set minutes ', min_value=0)
        with cols[2]:
            input_sec = st.number_input(':two: Set seconds', min_value=0, max_value=59)
        self.time_input = datetime.time(0, input_min, input_sec)
        with cols[4]:
            self.start_timer_bttn = st.button('Start!')    

        st.markdown("""---""")
        st.markdown('<b>2. ALarm</b>', unsafe_allow_html=True)
        cols = st.columns(5)
        with cols[0]:
            input_alrm_hr = st.number_input(':one: Set hour', min_value=0, max_value=23)
        with cols[1]:
            input_alrm_min = st.number_input(':two: Set minute', min_value=0, max_value=59)
        with cols[4]:
            self.start_alarm_bttn = st.button('Set Alarm!')    
        self.alarm_input = datetime.time(input_alrm_hr, input_alrm_min, 00)
        st.markdown("""---""")
        st.markdown('<b>Status</b>', unsafe_allow_html=True)
        self.message_placeholder = st.empty()
        self.is_running = False


        if self.start_alarm_bttn:
            self.start_alarm(self.alarm_input)
        if self.start_timer_bttn:
            self.count_down(self.time_input)

    def start_alarm(self, time_to_alarm: time):
        timenow = datetime.datetime.now().time().replace(second=00) #.strftime("%H:%M:%S")
        if timenow > time_to_alarm:
            self.message_placeholder.write('Comeback tomorrow. Or try another time that is coming up in the same day.')
            return
        self.message_placeholder.write(f"Alarm is set to {time_to_alarm}. Go do your work. I'll call you then.")

        cols = st.columns(3)
        with cols[1]:
            reset_bttn = st.button('Reset')
        while True:
            timenow = datetime.datetime.now().time().replace(second=00) #.strftime("%H:%M:%S")
            if timenow >=  time_to_alarm: # time has arrived
                break
            if reset_bttn:
                self.refresh_app()
            time.sleep(20)
        self.message_placeholder.write('<b style="font-size:26px; color:Green;">Alarm Ringingg!!!</b>',
    unsafe_allow_html=True)
        self._play_notif_sound()


    def count_down(self, time_to_count:time):
        if not self.start_timer_bttn or self.is_running:
            return
        self.is_running = True
        
        cols = st.columns(3)
        with cols[1]:
            reset_bttn = st.button('Reset')

        ss = (time_to_count.hour * 60 + time_to_count.minute) * 60 + time_to_count.second
        while ss > 0:
            self.message_placeholder.markdown(f":alarm_clock: Time left: {ss}s")
            time.sleep(1)
            ss -= 1
            if reset_bttn:
                self.refresh_app()
        self.message_placeholder.write('<b style="font-size:26px; color:Green;">Time\'s up!!!</b>',
    unsafe_allow_html=True)
        self._play_notif_sound()
        self.is_running = False

    def refresh_app(self):
        st.write('Cancelling')
        st.experimental_rerun()


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