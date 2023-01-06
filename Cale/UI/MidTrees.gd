extends ParallaxLayer

export(float) var MIDTREES_SPEED = -15

func _process(delta):
	motion_offset.x += MIDTREES_SPEED * delta
