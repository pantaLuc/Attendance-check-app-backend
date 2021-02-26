from rest_framework import serializers 
from .models import Surveillant, Salle, Filiere, Niveau, Ue, Exam, Present
from rest_framework.serializers import SerializerMethodField

class SurveillantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveillant
        fields = "__all__"


class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = "__all__"


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = "__all__"


class FiliereRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return FiliereSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class NiveauSerializer(serializers.ModelSerializer):
    filiere = FiliereRelatedField(queryset=Filiere.objects.all(), many=False)
    class Meta:
        model = Niveau
        fields = [
                    'level',
                    'nbr_student',
                    'filiere'
                 ]


class NiveauRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return NiveauSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UeSerializer(serializers.ModelSerializer):
    level = NiveauRelatedField(queryset=Niveau.objects.all(), many=False)
    class Meta:
        model = Ue 
        fields = [
                    'code',
                    'intitule',
                    'duration',
                    'level'
                 ]


class UeRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return UeSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class SalleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return SalleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class ExamSerializer(serializers.ModelSerializer):
    ue = UeRelatedField(queryset=Ue.objects.all(), many=False)
    salle = SalleRelatedField(queryset=Salle.objects.all(), many=False)
    surv = SerializerMethodField()

    class Meta:
        model = Exam
        fields = [
                    'day',
                    'begin',
                    'end',
                    'ue',
                    'salle',
                    'surv'
                 ]

    def get_surv(self, obj):
        all_presents = obj.present.all()
        all_surv = []
        for item in all_presents:
            present = {
                "id" : item.surveillant.pk,
                "nom" : item.surveillant.first_name +" "+ item.surveillant.last_name
            }
            all_surv.append(present)
        return all_surv

    def create(self, validated_data):
        exam = Exam(
            day = validated_data['day'],
            begin = validated_data['begin'],
            end = validated_data['end'],
            ue = validated_data['ue'],
            salle = validated_data['salle']
        )
        exam.save()

        for id in validated_data['surv']:
            present = Present(
                examen = exam,
                surveillant = id,
            )
            present.save()

class SurveillantRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return SurveillantSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class ExamRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return ExamSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class PresentSerializer(serializers.ModelSerializer):
    examen = ExamRelatedField(queryset=Exam.objects.all(), many=False)
    #surveillant = SurveillantRelatedField(queryset=Surveillant.objects.all(), many=False)
    class Meta:
        model = Present
        fields = [
                    'examen',
                    #'surveillant',
                    'is_present'
                 ]
    