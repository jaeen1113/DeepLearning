import survo
import time

def __main():
    ser = survo.init_serial()
    print("ser : ", ser)
    while(1):
        survo.send_signal(ser, "1")
        time.sleep(5)
__main();
