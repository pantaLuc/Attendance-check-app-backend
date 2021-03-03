from rest_framework import serializers 
from .models import Surveillant, Salle, Filiere, Niveau, Ue, Plage, Semestre, Exam, Controler
from users.models import User
from users.serializers import UsersSerializer
from rest_framework.serializers import SerializerMethodField

class SurveillantSerializer(serializers.ModelSerializer):
    exam = SerializerMethodField()
    class Meta:
        model = Surveillant
        # fields = "__all__"
        fields = [
            "id",
            "first_name",
            "last_name",
            "genre",
            "exam"
        ]
    def get_exam(self, obj):
        presents = obj.surv_control.all()
        result = {
                    "present":[],
                    "absent":[]
                }

        for present in presents :
            item = {
                'niveau' : {
                            'id' : present.examen.ue.level.id,
                            'niveau' : present.examen.ue.level.level,
                            'filiere': present.examen.ue.level.filiere.name,
                        },
                'salle' : {
                            'id' : present.salle.id,
                            'code': present.salle.code,
                            'localisation': present.salle.localisation
                        },
                'Ue' : {
                        "id": present.examen.id,
                        "code": present.examen.ue.code,
                        "intitule": present.examen.ue.intitule,
                    },
                'Horaire' : {
                    'id' : present.examen.plage.id,
                    "date": present.examen.day,
                    'begin' : present.examen.plage.begin,
                    'end' : present.examen.plage.end
                }
            }
            
            if present.is_present:
                result["present"].append(item)
            else:
                result["absent"].append(item)
        return result

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


class SurveillantRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return SurveillantSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)



class PlageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plage
        fields = [
                    'begin',
                    'end'
                 ]


class PlageRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return PlageSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = [
                    'num_semestre',
                    'year'
                 ]


class SemestreRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return SemestreSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)



class ExamSerializer(serializers.ModelSerializer):
    ue = UeRelatedField(queryset=Ue.objects.all(), many=False)
    plage = PlageRelatedField(queryset=Plage.objects.all(), many=False)
    semestre = SemestreRelatedField(queryset=Semestre.objects.all(), many=False)

    class Meta:
        model = Exam
        fields = [
                    'day',
                    'plage',
                    'ue',
                    'name',
                    'semestre'
                 ]


class ExamRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return ExamSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UserRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return UsersSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)

    
class ControlerSerializer(serializers.ModelSerializer):
    surveillant = SurveillantRelatedField(queryset=Surveillant.objects.all(), many=False)
    examen = ExamRelatedField(queryset=Exam.objects.all(), many=False)
    user = UserRelatedField(queryset=User.objects.all(), many=False)
    salle = SalleRelatedField(queryset=Salle.objects.all(), many=False)

    class Meta:
        model = Controler
        fields = [
                    'user',
                    'surveillant',
                    'examen',
                    'salle',
                    'is_present'
                 ]

