extends Control

var map := {}
const savepath := "user://savedata.json"

func _ready() -> void:
	var save := FileAccess.open(savepath, FileAccess.READ)
	if save:
		var res = JSON.parse_string(save.get_as_text())
		if res:
			if res is Dictionary:
				map = res

func _on_text_edit_text_changed() -> void:
	var regex = RegEx.new()

	var compile := ""
	
	for i in map.keys().size()-1:
		var key : String = map.keys()[i]
		compile += key
		compile += "|"
	compile += map.keys()[-1]
	
	
	regex.compile(compile)
	var results := regex.search_all($TextEdit.text)

	if results:
		var highlighted_text = $TextEdit.text
		for result in results:
			highlighted_text = highlighted_text.replace(result.get_string(), map[result.get_string()])

		$TextEdit2.text = highlighted_text
	else:
		$TextEdit2.text = $TextEdit.text


func _on_button_pressed() -> void:
	$open.popup()


func _on_open_file_selected(path: String) -> void:
	var fa := FileAccess.open(path, FileAccess.READ)
	var result = JSON.parse_string(fa.get_as_text())
	if result:
		if result is Dictionary:
			map = result
			
			var save := FileAccess.open(savepath, FileAccess.WRITE)
			save.store_string(JSON.stringify(map))
			_on_text_edit_text_changed()
		else:
			$AcceptDialog.dialog_text = "import failed, result is not dictionary"
			$AcceptDialog.popup()
	else:
		$AcceptDialog.dialog_text = "import failed, file empty"
		$AcceptDialog.popup()


func _on_button_2_pressed() -> void:
	print(JSON.stringify(map))
	$TextEdit2.text = JSON.stringify(map, "\t")
