# -*- coding: utf-8 -*-


from django import forms
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
    name=forms.CharField(label='お名前')
    email=forms.EmailField(label='メールアドレス')
    title=forms.CharField(label='件名')
    message=forms.CharField(label='メッセージ',widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args,**kwargs)
    
        self.fields['name'].widget.attrs['placeholder']='お名前を入力してください'
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['title'].widget.attrs['placeholder']='タイトルを入力してください'
        self.fields['title'].widget.attrs['class']='form-control'
        self.fields['message'].widget.attrs['placeholder']='メッセージを入力してください'
        self.fields['message'].widget.attrs['class']='form-control'
    def send_email(self):
        name=self.cleaned_data['name']
        email=self.cleaned_data['email']
        title=self.cleaned_data['title']
        message=self.cleaned_data['message']
        subject='お問い合わせ: {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\n タイトル: {2}\n メッセージ: \n{3}'.format(name,email,title,message)
        from_email = 'mori.kenichiro77@gmail.com'
        to_list=['mori.kenichiro77@gmail.com']
        message=EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,)
        message.send()                