from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'can_be_contacted', 'can_data_be_shared', 'password']
       
        '''
        extra_kwargs is a dictionary that allows you to specify additional options for individual serializer fields.
        the field password will be included when creating or updating an object but will not be included when retrieving an object
        '''
        extra_kwargs = {'password': {'write_only': True}}
    
    # Validate age
    def validate_age(self, value):
        if value < 16:
            raise serializers.ValidationError("Users under 16 years old cannot create an account.")
        return value
    
    # Validate data
    def validate(self, data):
        age = data.get('age')
        can_be_contacted = data.get('can_be_contacted', False)
        can_data_be_shared = data.get('can_data_be_shared', False)

        if age >= 16:
            if can_be_contacted not in [True, False]:
                raise serializers.ValidationError("Consent to be contacted must be a boolean value.")
            if can_data_be_shared not in [True, False]:
                raise serializers.ValidationError("Consent to share data must be a boolean value.")
        return data

    # Create and save user
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            age=validated_data['age'],
            can_be_contacted=validated_data['can_be_contacted'],
            can_data_be_shared=validated_data['can_data_be_shared'],
        )
        
        ''' set_password is a method to ensure that the password is properly hashed before saving the user object'''
        user.set_password(validated_data['password'])
        user.save()
        return user

    # Update user
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.age = validated_data.get('age', instance.age)
        instance.can_be_contacted = validated_data.get('can_be_contacted', instance.can_be_contacted)
        instance.can_data_be_shared = validated_data.get('can_data_be_shared', instance.can_data_be_shared)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance