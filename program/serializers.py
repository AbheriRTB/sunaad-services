from rest_framework import serializers

from program.models import Program

class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ('title', 'description', 'event_date', 'place', 'phone',
		  				'location_eataries', 'event_start', 'event_end', 'duration',
                  'location_address', 'location_mapcoords', 'location_parking')
