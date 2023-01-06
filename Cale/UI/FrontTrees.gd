extends ParallaxLayer

export(float) var FRONTTREES_SPEED = 20

func _process(delta):
	motion_offset.x += FRONTTREES_SPEED * delta
