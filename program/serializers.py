from rest_framework import serializers

from program.models import Program

class ProgramSerializer(serializers.ModelSerializer):

        class Meta:
            model = Program
            fields = ('id',
                        'title',
                        'event_type',
                        'description',
                        'entry_fee',
                        'website',
                        'event_date',
                        'place',
                        'artiste',
                        'phone',
                        'event_start',
                        'event_end',
                        'duration',
                        'location_address1',
                        'location_address2',
                        'location_city',
                        'location_state',
                        'location_country',
                        'location_pincode',
                        'location_mapcoords',
                        'location_parking',
                        'location_eataries',
                        'artiste_image')

