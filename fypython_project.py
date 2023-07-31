

import datetime
import pywhatkit

def get_lecture_message(timetable, current_day):
    if current_day in timetable:
        lecture = timetable[current_day]
        message = f"Attend lecture\n {lecture}"
        return message
    else:
        return None


# lecture timetable
timetable1 = {
    "Monday": "9:15-10:15 :- CMS \n 10:15-11:15 :- EC \n  ",
    "Tuesday": "9:15-11:15 :- F1 - MDC, F2 - IOT, F3 - PPS \n  ",
    "Wednesday": "9:15-10:15 :- MDC \n 10:15-11:15 :- TG \n  ",
    "Thursday": "9:15-10:15 - EC \n 10:15-11:15 :- ICDE \n ",
    "Friday": "9:15-11:15 :- FOREIGN LANGUAGE \n ",
}
timetable2 = {"Monday": "11:30-1:30 :- F1 - PPS, F2 - MDC, F3 - IOT \n  ",
    "Tuesday": " 11:30-1:30 :- F1 - IOT, F2 - PPS, F3 - MDC \n ",
    "Wednesday": " 11:30-12:30 :- MDC  \n 12:30-1:30 :-ICDE \n  ",
    "Thursday": " 11:30-1:30 :- F1 - PPS, F2 - EC, F3 - CMS \n ",
    "Friday": " 11:30-12:30 :- LAS \n 12:30-1:30 :- APTITUDE \n ",}

timetable3 = {"Monday": "2:15-4:15 :-F1 - CMS, F2 - PPS, F3 - EC \n",
    "Tuesday":"2:15-3:15 :- ICDE \n 3:15-4:15 :- SPORTS \n",
    "Wednesday":"2:15-4:15 :- F1 - EC, F2 - CMS, F3 - PPS \n",
    "Thursday":"2:15-3:15 :- LAS \n 3:15-4:15 :- CMS",
    "Friday": "2:15-3:15 :- LAS \n 3:15-4:15 :- MDC",
}



#current day of the week
current_day = datetime.datetime.now().strftime("%A")

# Check if it's Monday-Friday and send the corresponding lecture message
if current_day in timetable1:
    lecture1 = timetable1[current_day]

    message1 = f"Good morning!\n Today's lecture is \n {lecture1}.\n Don't forget to attend at 9 am."

    if current_day in timetable2:

        lecture2 = timetable2[current_day]

        message2 = f"Attend lecture\n {lecture2} "

        if current_day in timetable3:

           lecture3 = timetable3[current_day]

           message3 = f"Attend lecture\n {lecture3} "

    # Schedule the message to be sent at 7 am
    # We use here group ID to send msg to group
    pywhatkit.sendwhatmsg_to_group("whtasapp group address", message1, 19,11)
    pywhatkit.sendwhatmsg_to_group("whtasapp group address", message2, 19,12)
    pywhatkit.sendwhatmsg_to_group("whtasapp group address", message3, 19,13)

else:
    print("No lecture today.")
