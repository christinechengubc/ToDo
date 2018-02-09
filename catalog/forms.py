from django import forms

class AddItemForm(forms.Form):
	def __init__(self, lists, list_name, *args, **kwargs):
		super(AddItemForm, self).__init__(*args, **kwargs)
		tuples = []
		for name in lists:
			tuples.append((name, name))
			print(name)
		self.fields['item_title'] = forms.CharField(label = "Item Title")
		self.fields['item_list'] = forms.ChoiceField(choices=tuples, label = "Item List", initial = (list_name, list_name))
