import time

def getMsgDrive (y, magnitude):

    y = y * 255
    y=int(y)
    y=round(y)
    if (y>=25):
        direction="01"
        if (magnitude>0.95): y=255
    elif(y<=-25):
        direction="00"
        y=y*-1
        if (magnitude > 0.95): y = 255
    else:
        direction = "00"
        drive_msg = {
            "sbrick_id": "88:6B:0F:80:29:D1",  # "string. SBrick ID. <sbrick MAC>",
            "channel": "02",  # " string. hex string. the LEGO power function port you
            # want to drive. <00|01|02|03>",
            "direction": direction,  # "string. clockwise or counterclockwise. <00|01>",
            "power": "00",  # "string. hex string. FF means 100% speed. <00~FF>",
            "exec_time": 0.1,  # "number. seconds. 5566 means forever."
            "timestamp": time.time()
        }
        return (drive_msg)


    drive_msg = {
    "sbrick_id": "88:6B:0F:80:29:D1",  # "string. SBrick ID. <sbrick MAC>",
    "channel": "02",  # " string. hex string. the LEGO power function port you
    # want to drive. <00|01|02|03>",
    "direction": direction,  # "string. clockwise or counterclockwise. <00|01>",
    "power": "{0:x}".format(y),  # "string. hex string. FF means 100% speed. <00~FF>",
    "exec_time": 0.1,  # "number. seconds. 5566 means forever."
    "timestamp": time.time()
    }

    return (drive_msg)

def getMsgSteer (x):

    x = x * 255
    x=int(x)
    x=round(x)
    if (x>=25): direction="00"
    elif (x<=-25):
        direction="01"
        x=x*-1
    else:
        direction = "00"
        steer_msg = {
            "sbrick_id": "88:6B:0F:80:29:D1",  # "string. SBrick ID. <sbrick MAC>",
            "channel": "00",  # " string. hex string. the LEGO power function port you
            # want to drive. <00|01|02|03>",
            "direction": direction,  # "string. clockwise or counterclockwise. <00|01>",
            "power": "00",  # "string. hex string. FF means 100% speed. <00~FF>",
            "exec_time": 0.1,  # "number. seconds. 5566 means forever."
            "timestamp": time.time()
        }
        return (steer_msg)


    steer_msg = {
    "sbrick_id": "88:6B:0F:80:29:D1",  # "string. SBrick ID. <sbrick MAC>",
    "channel": "00",  # " string. hex string. the LEGO power function port you
    # want to drive. <00|01|02|03>",
    "direction": direction,  # "string. clockwise or counterclockwise. <00|01>",
    "power": "{0:x}".format(x),  # "string. hex string. FF means 100% speed. <00~FF>",
    "exec_time": 0.1,  # "number. seconds. 5566 means forever."
    "timestamp": time.time()
    }
    return (steer_msg)

def getMsgUp():
    Up_msg = {
    "sbrick_id": "88:6B:0F:80:29:D1",  # "string. SBrick ID. <sbrick MAC>",
    "channel": "03",  # " string. hex string. the LEGO power function port you
    # want to drive. <00|01|02|03>",
    "direction": "01",  # "string. clockwise or counterclockwise. <00|01>",
    "power": "ff",  # "string. hex string. FF means 100% speed. <00~FF>",
    "exec_time": 8,  # "number. seconds. 5566 means forever."
    "timestamp": time.time()
    }
    return (Up_msg)

def getMsgDown():
    Down_msg = {
    "sbrick_id": "88:6B:0F:80:29:D1",  # "string. SBrick ID. <sbrick MAC>",
    "channel": "03",  # " string. hex string. the LEGO power function port you
    # want to drive. <00|01|02|03>",
    "direction": "00",  # "string. clockwise or counterclockwise. <00|01>",
    "power": "ff",  # "string. hex string. FF means 100% speed. <00~FF>",
    "exec_time": 7,  # "number. seconds. 5566 means forever."
    "timestamp": time.time()
    }
    return (Down_msg)

