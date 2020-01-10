from rest_framework import serializers

from accounts.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
	    model = Account
	    fields = ['email', 'username','first_name','last_name','password1', 'password2']
	    extra_kwargs = {
	    		'password': {'write_only': True},
	    }	


    def	save(self): 
	    account = Account(
		    		email=self.validated_data['email'],
			    	username=self.validated_data['username'],
                    first_name = self.validated_data['first_name'],
                    last_name = self.validated_data['last_name']
			    )
	    password = self.validated_data['password1']
	    password2 = self.validated_data['password2']
	    if password != password2:
	    	raise serializers.ValidationError({'password': 'Passwords must match.'})
	    account.set_password(password)
	    account.save()
	    return account


class AccountPropertiesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['pk', 'email', 'username', ]




class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)