extends ParallaxLayer

export(float) var BACKTREES_SPEED = -15

func _process(delta):
	motion_offset.x += BACKTREES_SPEED * delta
