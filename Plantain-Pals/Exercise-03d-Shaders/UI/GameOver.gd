extends CanvasLayer


func _on_Restart_pressed():
	get_tree().change_scene("res://Game.tscn")

func _on_Exit_pressed():
	get_tree().quit()
