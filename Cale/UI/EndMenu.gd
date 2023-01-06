extends Control


func _ready():
	pass


func _on_PlayAgain_pressed():
	get_tree().change_scene("res://Levels/Level1.tscn")


func _on_MainMenu_pressed():
	get_tree().change_scene("res://UI/MainMenu.tscn")


func _on_Quit_pressed():
	get_tree().quit()
