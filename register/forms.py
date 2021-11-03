from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm,
    PasswordResetForm, SetPasswordForm
)
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailChangeForm(forms.ModelForm):
    """メールアドレス変更フォーム"""

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
           # field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
           


class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email


class UserUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = User
        fields = ('last_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


# ModelFormを継承してクラスを作成する
class  ThemeUpdateForm(forms.ModelForm):
    """テーマ更新フォーム"""

    class Meta:
        # Userモデルを使用する
        model = User
        
        # 表示するフィールド
        fields = ['theme']
        labels = {
            'theme': 'テーマ',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    # Theme = forms.fields.ChoiceField(
    #     choices=(
    #         ('white', 'ホワイト'),
    #         ('dark', 'ダーク')
    #     ),
    #     required=True,
    #     widget=forms.widgets.Select
    # )



class MyPasswordChangeForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MyPasswordResetForm(PasswordResetForm):
    """パスワード忘れたときのフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MySetPasswordForm(SetPasswordForm):
    """パスワード再設定用フォーム(パスワード忘れて再設定)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
