import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

# Contact detection is disabled for base by default, because of many false positives
# If you want to enable it, use these lines of code below.
# robot.base.left_wheel.enable_guarded_mode()
# robot.base.right_wheel.enable_guarded_mode()

# Stops arm at 30% and lift at 50% max current detected (e.g. collides with a person)
robot.arm.move_to(0.5, contact_thresh_pos=30, contact_thresh_neg=-30)
robot.lift.move_to(0.9, contact_thresh_pos=50, contact_thresh_neg=-50)
# Stop the base if it collides into a wall
# robot.base.translate_by(0.5, contact_thresh=5)

robot.push_command()
robot.arm.wait_until_at_setpoint(timeout=5.0)
robot.lift.wait_until_at_setpoint(timeout=5.0)
# robot.base.wait_until_at_setpoint(timeout=1.0)

robot.stop()
