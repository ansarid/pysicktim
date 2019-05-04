import time
import rcpy
import rcpy.motor as motor
import pytim5xx as lidar

class stepinfo:
    state = 0
    enabled = 0

def step(direction):

    if direction > 0:
        stepinfo.state += 1

    elif direction < 0:
        stepinfo.state -= 1

    if stepinfo.state > 3:
        stepinfo.state = 0

    elif stepinfo.state < 0:
        stepinfo.state = 3

    if stepinfo.state == 0:
        motor.set(M1,1)
        motor.set(M2,1)

    elif stepinfo.state == 1:
        motor.set(M1,-1)
        motor.set(M2,1)

    elif stepinfo.state == 2:
        motor.set(M1,-1)
        motor.set(M2,-1)

    elif stepinfo.state == 3:
        motor.set(M1,1)
        motor.set(M2,-1)

    else:
        motor.set(M1,1)
        motor.set(M2,1)

M1 = 3
M2 = 4

position = 0
direction = 1

rcpy.set_state(rcpy.RUNNING)

try:

    while rcpy.get_state() != rcpy.EXITING:

        if rcpy.get_state() == rcpy.RUNNING:

            while position < 4300:

                direction = 1;

                step(direction)

                # print(position)

                position = position + direction

                if position % 10 == 0:
                    lidar.scan()
                    data = lidar.scan.distances
                    print(data,"! ", end ="")

                time.sleep(0.01)

            exit()

        elif rcpy.get_state() == rcpy.PAUSED:

                pass

except KeyboardInterrupt: # condition added to catch a "Ctrl-C" event and exit cleanly

	rcpy.set_state(rcpy.EXITING)

	pass

finally:

	rcpy.set_state(rcpy.EXITING)
