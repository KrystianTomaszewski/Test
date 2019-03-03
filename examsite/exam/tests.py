from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class QuestionViewTests(TestCase):

    def test_no_choice(self):
        response = self.client.get(reverse('exam:choice_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No choice are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

class SheetViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('exam:question_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No question are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
