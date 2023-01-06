extends ParallaxLayer

export(float) var BACK_SPEED = -15

func _process(delta):
	motion_offset.x += BACK_SPEED * delta
