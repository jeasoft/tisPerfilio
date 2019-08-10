from rest_framework import serializers
from core.models import User, Experience, Education, Certification

class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = ("company_name","job_title","job_description",
            "year_starts","month_starts","year_ends", "month_ends")
        
class EducationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Education
        fields = ("institution","title","description",
            "year_starts","month_starts","year_ends", "month_ends")

class CertificationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Certification
        fields = ("certification_name","certification_institution",
            "year","month")

class UserSerializer(serializers.ModelSerializer):
    user_experiences = ExperienceSerializer(
        many=True,
        read_only=True
    )
    user_education = EducationSerializer(
        many=True,
        read_only=True
    )    
    user_certifications = CertificationSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = User
        fields = ("username","first_name","last_name","user_experiences",
            "user_certifications","user_education")
            