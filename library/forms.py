from django import forms
from .models import Library, Catalog, Category, Ebook, Author, Member, Borrowed, Supplier, Purchase, Employee, Designation, Department
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.utils.translation import ugettext as _

COUNTRIES = (
    ('AD', _('Andorra')),
    ('AE', _('United Arab Emirates')),
    ('AF', _('Afghanistan')),
    ('AG', _('Antigua & Barbuda')),
    ('AI', _('Anguilla')),
    ('AL', _('Albania')),
    ('AM', _('Armenia')),
    ('AN', _('Netherlands Antilles')),
    ('AO', _('Angola')),
    ('AQ', _('Antarctica')),
    ('AR', _('Argentina')),
    ('AS', _('American Samoa')),
    ('AT', _('Austria')),
    ('AU', _('Australia')),
    ('AW', _('Aruba')),
    ('AZ', _('Azerbaijan')),
    ('BA', _('Bosnia and Herzegovina')),
    ('BB', _('Barbados')),
    ('BD', _('Bangladesh')),
    ('BE', _('Belgium')),
    ('BF', _('Burkina Faso')),
    ('BG', _('Bulgaria')),
    ('BH', _('Bahrain')),
    ('BI', _('Burundi')),
    ('BJ', _('Benin')),
    ('BM', _('Bermuda')),
    ('BN', _('Brunei Darussalam')),
    ('BO', _('Bolivia')),
    ('BR', _('Brazil')),
    ('BS', _('Bahama')),
    ('BT', _('Bhutan')),
    ('BV', _('Bouvet Island')),
    ('BW', _('Botswana')),
    ('BY', _('Belarus')),
    ('BZ', _('Belize')),
    ('CA', _('Canada')),
    ('CC', _('Cocos (Keeling) Islands')),
    ('CF', _('Central African Republic')),
    ('CG', _('Congo')),
    ('CH', _('Switzerland')),
    ('CI', _('Ivory Coast')),
    ('CK', _('Cook Iislands')),
    ('CL', _('Chile')),
    ('CM', _('Cameroon')),
    ('CN', _('China')),
    ('CO', _('Colombia')),
    ('CR', _('Costa Rica')),
    ('CU', _('Cuba')),
    ('CV', _('Cape Verde')),
    ('CX', _('Christmas Island')),
    ('CY', _('Cyprus')),
    ('CZ', _('Czech Republic')),
    ('DE', _('Germany')),
    ('DJ', _('Djibouti')),
    ('DK', _('Denmark')),
    ('DM', _('Dominica')),
    ('DO', _('Dominican Republic')),
    ('DZ', _('Algeria')),
    ('EC', _('Ecuador')),
    ('EE', _('Estonia')),
    ('EG', _('Egypt')),
    ('EH', _('Western Sahara')),
    ('ER', _('Eritrea')),
    ('ES', _('Spain')),
    ('ET', _('Ethiopia')),
    ('FI', _('Finland')),
    ('FJ', _('Fiji')),
    ('FK', _('Falkland Islands (Malvinas)')),
    ('FM', _('Micronesia')),
    ('FO', _('Faroe Islands')),
    ('FR', _('France')),
    ('FX', _('France, Metropolitan')),
    ('GA', _('Gabon')),
    ('GB', _('United Kingdom (Great Britain)')),
    ('GD', _('Grenada')),
    ('GE', _('Georgia')),
    ('GF', _('French Guiana')),
    ('GH', _('Ghana')),
    ('GI', _('Gibraltar')),
    ('GL', _('Greenland')),
    ('GM', _('Gambia')),
    ('GN', _('Guinea')),
    ('GP', _('Guadeloupe')),
    ('GQ', _('Equatorial Guinea')),
    ('GR', _('Greece')),
    ('GS', _('South Georgia and the South Sandwich Islands')),
    ('GT', _('Guatemala')),
    ('GU', _('Guam')),
    ('GW', _('Guinea-Bissau')),
    ('GY', _('Guyana')),
    ('HK', _('Hong Kong')),
    ('HM', _('Heard & McDonald Islands')),
    ('HN', _('Honduras')),
    ('HR', _('Croatia')),
    ('HT', _('Haiti')),
    ('HU', _('Hungary')),
    ('ID', _('Indonesia')),
    ('IE', _('Ireland')),
    ('IL', _('Israel')),
    ('IN', _('India')),
    ('IO', _('British Indian Ocean Territory')),
    ('IQ', _('Iraq')),
    ('IR', _('Islamic Republic of Iran')),
    ('IS', _('Iceland')),
    ('IT', _('Italy')),
    ('JM', _('Jamaica')),
    ('JO', _('Jordan')),
    ('JP', _('Japan')),
    ('KE', _('Kenya')),
    ('KG', _('Kyrgyzstan')),
    ('KH', _('Cambodia')),
    ('KI', _('Kiribati')),
    ('KM', _('Comoros')),
    ('KN', _('St. Kitts and Nevis')),
    ('KP', _('Korea, Democratic People\'s Republic of')),
    ('KR', _('Korea, Republic of')),
    ('KW', _('Kuwait')),
    ('KY', _('Cayman Islands')),
    ('KZ', _('Kazakhstan')),
    ('LA', _('Lao People\'s Democratic Republic')),
    ('LB', _('Lebanon')),
    ('LC', _('Saint Lucia')),
    ('LI', _('Liechtenstein')),
    ('LK', _('Sri Lanka')),
    ('LR', _('Liberia')),
    ('LS', _('Lesotho')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('LV', _('Latvia')),
    ('LY', _('Libyan Arab Jamahiriya')),
    ('MA', _('Morocco')),
    ('MC', _('Monaco')),
    ('MD', _('Moldova, Republic of')),
    ('MG', _('Madagascar')),
    ('MH', _('Marshall Islands')),
    ('ML', _('Mali')),
    ('MN', _('Mongolia')),
    ('MM', _('Myanmar')),
    ('MO', _('Macau')),
    ('MP', _('Northern Mariana Islands')),
    ('MQ', _('Martinique')),
    ('MR', _('Mauritania')),
    ('MS', _('Monserrat')),
    ('MT', _('Malta')),
    ('MU', _('Mauritius')),
    ('MV', _('Maldives')),
    ('MW', _('Malawi')),
    ('MX', _('Mexico')),
    ('MY', _('Malaysia')),
    ('MZ', _('Mozambique')),
    ('NA', _('Namibia')),
    ('NC', _('New Caledonia')),
    ('NE', _('Niger')),
    ('NF', _('Norfolk Island')),
    ('NG', _('Nigeria')),
    ('NI', _('Nicaragua')),
    ('NL', _('Netherlands')),
    ('NO', _('Norway')),
    ('NP', _('Nepal')),
    ('NR', _('Nauru')),
    ('NU', _('Niue')),
    ('NZ', _('New Zealand')),
    ('OM', _('Oman')),
    ('PA', _('Panama')),
    ('PE', _('Peru')),
    ('PF', _('French Polynesia')),
    ('PG', _('Papua New Guinea')),
    ('PH', _('Philippines')),
    ('PK', _('Pakistan')),
    ('PL', _('Poland')),
    ('PM', _('St. Pierre & Miquelon')),
    ('PN', _('Pitcairn')),
    ('PR', _('Puerto Rico')),
    ('PT', _('Portugal')),
    ('PW', _('Palau')),
    ('PY', _('Paraguay')),
    ('QA', _('Qatar')),
    ('RE', _('Reunion')),
    ('RO', _('Romania')),
    ('RU', _('Russian Federation')),
    ('RW', _('Rwanda')),
    ('SA', _('Saudi Arabia')),
    ('SB', _('Solomon Islands')),
    ('SC', _('Seychelles')),
    ('SD', _('Sudan')),
    ('SE', _('Sweden')),
    ('SG', _('Singapore')),
    ('SH', _('St. Helena')),
    ('SI', _('Slovenia')),
    ('SJ', _('Svalbard & Jan Mayen Islands')),
    ('SK', _('Slovakia')),
    ('SL', _('Sierra Leone')),
    ('SM', _('San Marino')),
    ('SN', _('Senegal')),
    ('SO', _('Somalia')),
    ('SR', _('Suriname')),
    ('ST', _('Sao Tome & Principe')),
    ('SV', _('El Salvador')),
    ('SY', _('Syrian Arab Republic')),
    ('SZ', _('Swaziland')),
    ('TC', _('Turks & Caicos Islands')),
    ('TD', _('Chad')),
    ('TF', _('French Southern Territories')),
    ('TG', _('Togo')),
    ('TH', _('Thailand')),
    ('TJ', _('Tajikistan')),
    ('TK', _('Tokelau')),
    ('TM', _('Turkmenistan')),
    ('TN', _('Tunisia')),
    ('TO', _('Tonga')),
    ('TP', _('East Timor')),
    ('TR', _('Turkey')),
    ('TT', _('Trinidad & Tobago')),
    ('TV', _('Tuvalu')),
    ('TW', _('Taiwan, Province of China')),
    ('TZ', _('Tanzania, United Republic of')),
    ('UA', _('Ukraine')),
    ('UG', _('Uganda')),
    ('UM', _('United States Minor Outlying Islands')),
    ('US', _('United States of America')),
    ('UY', _('Uruguay')),
    ('UZ', _('Uzbekistan')),
    ('VA', _('Vatican City State (Holy See)')),
    ('VC', _('St. Vincent & the Grenadines')),
    ('VE', _('Venezuela')),
    ('VG', _('British Virgin Islands')),
    ('VI', _('United States Virgin Islands')),
    ('VN', _('Viet Nam')),
    ('VU', _('Vanuatu')),
    ('WF', _('Wallis & Futuna Islands')),
    ('WS', _('Samoa')),
    ('YE', _('Yemen')),
    ('YT', _('Mayotte')),
    ('YU', _('Yugoslavia')),
    ('ZA', _('South Africa')),
    ('ZM', _('Zambia')),
    ('ZR', _('Zaire')),
    ('ZW', _('Zimbabwe')),
    ('ZZ', _('Unknown or unspecified country')),
)

LIBRARY_TYPES = (

('Entertainment','Entertainment'),
('Legal','Legal'),
('Politics/Government','Politics/Government'),
('Business','Business'),
('Sports','Sports'),
('Education','Education'),
('Tech','Tech'),
('Art','Art'),
('History','History'),
('Litterature','Litterature'),
('Medical','Medical'),
('Religion','Religion'),
)

STATUS = (('Active','Active'),('Inactive','Inactive'))

CHECKING = (('Not Returned','Not Returned'),('Returned','Returned'))

TYPE    =   (('Academic','Academic'),('Administative','Administative'))


class AddLibraryForm(forms.ModelForm):

    library_name         =   forms.CharField(max_length=300,widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Library complete name'
    }))

    library_type         =   forms.ChoiceField(choices=LIBRARY_TYPES,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))

    library_email        =   forms.EmailField(max_length=300,widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Email',
    'type':'Email'
    }))

    library_country = forms.ChoiceField(choices=COUNTRIES,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))

    library_phone         =   forms.CharField(max_length=300,widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Tel'
    }))



    class Meta:
        model   =  Library
        fields  =  ['library_name','library_type','library_email','library_country','library_phone',]


class AddCatalogForm(forms.ModelForm):

    class Meta:
        model   = Catalog
        exclude =('library',)

class UpdateCatalogForm(forms.ModelForm):

    class Meta:
        model   = Catalog
        exclude =('library',)

class AddEbookForm(forms.ModelForm):
    book_pdf    =   forms.FileField()

    class Meta:
        model   = Ebook
        exclude =('library',)


class UpdateEbookForm(forms.ModelForm):

    class Meta:
        model   = Ebook
        exclude =('library',)

class AddCategoryForm(forms.ModelForm):

    class Meta:
        model   = Category
        exclude =('library',)

class UpdateCategoryForm(forms.ModelForm):

    class Meta:
        model   = Category
        exclude =('library',)

class AddAuthorForm(forms.ModelForm):

    country     =       forms.ChoiceField(choices=COUNTRIES,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))

    class Meta:
        model   = Author
        exclude =('library',)

class UpdateAuthorForm(forms.ModelForm):

    country     =       forms.ChoiceField(choices=COUNTRIES,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))

    class Meta:
        model   = Author
        exclude =('library',)

class AddMemberForm(forms.ModelForm):

    status  =   forms.ChoiceField(choices=STATUS,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))
    class Meta:
        model   = Member
        exclude =('library',)

class UpdateMemberForm(forms.ModelForm):

    status  =   forms.ChoiceField(choices=STATUS,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))

    class Meta:
        model   = Member
        exclude =('library',)

class AddBorrowForm(forms.ModelForm):

    due_return = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    'type':'date'
    }))
    class Meta:
        model   = Borrowed
        fields =('member_no','catalog','due_return')

class CheckoutForm(forms.ModelForm):

    status  =   forms.ChoiceField(choices=CHECKING,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))

    class Meta:
        model   = Member
        fields =('status',)


class AddSupplierForm(forms.ModelForm):

    country     =       forms.ChoiceField(choices=COUNTRIES,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))


    class Meta:
        model = Supplier
        exclude = ('library',)

class AddPurchaseForm(forms.ModelForm):

    purchase_date = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    'type':'date'
    }))

    class Meta:
        model   =   Purchase
        exclude =   ('library',)

class UpdateSupplierForm(forms.ModelForm):

    class Meta:
        model   = Supplier
        exclude =('library',)

class UpdatePurchaseForm(forms.ModelForm):

    class Meta:
        model   = Purchase
        exclude =('library',)


class AddEmployeeForm(forms.ModelForm):

    status  =   forms.ChoiceField(choices=STATUS,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))

    class Meta:
        model   =   Employee
        exclude =   ('library',)

class UpdateEmployee(forms.ModelForm):

    class Meta:
        model   =   Employee
        exclude =   ('library',)

class AddDesignationForm(forms.ModelForm):

    status  =   forms.ChoiceField(choices=STATUS,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))


    class Meta:
        model   =   Designation
        exclude =   ('library',)

class UpdateDesignation(forms.ModelForm):

    class Meta:
        model   =   Designation
        exclude =   ('library',)

class AddDepartmentForm(forms.ModelForm):

    type  =   forms.ChoiceField(choices=TYPE,widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder':'Type',
    }))


    class Meta:
        model   =   Department
        exclude =   ('library',)

class UpdateDepartment(forms.ModelForm):

    class Meta:
        model   =   Department
        exclude =   ('library',)

class AddMediaForm(forms.ModelForm):

    class Meta:
        model   =   Department
        exclude =   ('library',)

class UpdateMedia(forms.ModelForm):

    class Meta:
        model   =   Department
        exclude =   ('library',)
