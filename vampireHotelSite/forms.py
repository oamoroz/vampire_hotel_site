from django import forms
from phonenumber_field.formfields import PhoneNumberField

class BookingForm(forms.Form):
	gender_choices = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('other', 'Другое')
    ]

	apartments_choices = [
    	('standard', 'Стандарт'),
    	('standard_premium', 'Стандарт премиум'),
    	('deluxe_comfort', 'Делюкс комфорт'),
    	('luxury_studio', 'Люкс студия'),
    	('luxury_premium', 'Люкс премиум'),
    	('luxury_romantic', 'Люкс романтик'),
    	('business_luxury', 'Бизнес люкс'),
    	('apartments', 'Апартаменты'),
    ]


	first_name = forms.CharField(max_length=100, label = "Имя")
	last_name = forms.CharField(max_length=100, label = "Фамилия")
	age = forms.IntegerField(min_value=14, max_value=120, label = "Возраст")
	gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender_choices, label = "Гендер")
	phone = PhoneNumberField(label = "Телефон")
	passport_series = forms.CharField(min_length=4, max_length=4, widget=forms.PasswordInput, label = "Серия паспорта")
	passport_number = forms.CharField(min_length=6, max_length=6, widget=forms.PasswordInput, label = "Номер паспорта")
	arrival_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}), label = "Дата прибытия")
	departure_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}), label = "Дата отъезда")
	apartments_type = forms.ChoiceField(choices = apartments_choices, label = "Тип номера")
	guests_number = forms.IntegerField(min_value=1, max_value=5, label = "Количество гостей")


class ReviewForm(forms.Form):
	name = forms.CharField(max_length=20, label="Имя")
	email = forms.EmailField()
	review = forms.CharField(min_length=10, max_length=1500, widget=forms.Textarea(), label="Ваш отзыв")
	rating = forms.IntegerField(min_value=1, max_value=10, label="Оцените нас от 1 до 10")