from django import forms

class AddItemForm(forms.Form):
	lists = []
	tuples = []
	for name in lists:
		tuples.append((name, name))
	item_title = forms.CharField(required = True)
	item_list = forms.ChoiceField(choices=tuples, required = True)
