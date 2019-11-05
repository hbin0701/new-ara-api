from rest_framework import serializers


class MetaDataModelSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    deleted_at = serializers.ReadOnlyField()
