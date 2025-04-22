from django.test import TestCase
from .models import Student

class StudentTestCase(TestCase) :
    def test_object_creation(self) :
        # Simple object creation
        st = Student.objects.create(
            firstname="test",
            surname="stest",
            attendance_count=2
        )

        self.assertEqual(st.firstname, "test")
        self.assertEqual(st.surname, "stest")
        self.assertEqual(st.attendance_count, 2)

    def test_min_attendence(self) :
        # Attendance count must be at least 0
        with self.assertRaises(Exception) :
            st = Student.objects.create(
                firstname="test",
                surname="stest",
                attendance_count=-5
            )
            st.full_clean()

