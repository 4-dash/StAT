# Generated by Django 5.2 on 2025-04-23 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("atTracker", "0002_alter_student_attendance_count"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="attendance_count",
            new_name="attendence_count",
        ),
    ]
