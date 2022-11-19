from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from .exceptions import UserNotFoundException, DataNotFoundException
from .models import Answer

CustomUser = get_user_model()


class Examination:
    @staticmethod
    def _get_user(user_id: int) -> CustomUser:
        if user_id is None:
            raise DataNotFoundException()

        return CustomUser.objects.filter(pk=user_id).first()

    @staticmethod
    def _update_user_answers(user: CustomUser, right_answers_count: int, checked_answers: int) -> None:
        """This function update user statistic"""
        if not user:
            raise UserNotFoundException()

        user.right_answers = user.right_answers + right_answers_count
        user.all_answers = user.all_answers + checked_answers
        user.save()

    @staticmethod
    def _convert_text(text: str) -> str:
        """
        This function convert answer
        Example: AnsWer 1 => answer1
        """
        return text.lower().strip().replace(' ', '')

    def _get_right_answer(self, answer_id: int):
        """This function get right answer from database and return it"""
        right_answer = None
        try:
            right_answer = Answer.objects.get(question=answer_id)
        except ObjectDoesNotExist:
            self._get_right_answer(answer_id)

        return right_answer

    def _check_answer(self, answer: dict) -> dict:
        """This function check that right answer from database equal answer that we got from user"""
        right_answer = self._get_right_answer(answer["id"])
        right_converted_answer = self._convert_text(right_answer.answer_text)
        converted_answer = self._convert_text(answer["answer_text"])

        checked_answer = {
            "question_id": answer["id"],
            "answer": answer["answer_text"],
            "correct": False
        }

        if converted_answer == right_converted_answer:
            checked_answer.update({'correct': True, 'right_answer': 1})
            return checked_answer

        return checked_answer

    def _reconciliation_of_answers(self, data: list, user_id: int, not_first_try: bool) -> list:
        """This is main function that collects all function in main logic and check not_first_try"""
        checked_answers = []
        right_answers_count = 0
        all_answers = 0

        if data is None:
            raise DataNotFoundException()

        for answer in data:
            checked_answer = self._check_answer(answer)

            # If it is first user try, we will calculate wrong and right answers
            # If true => this isn't user first try
            # If false => this is user first try
            if not_first_try is False:
                if checked_answer.get('right_answer') is not None:
                    right_answers_count += checked_answer.pop('right_answer')

                all_answers += 1

            checked_answers.append(checked_answer)
        
        if not_first_try is False:
            self._update_user_answers(self._get_user(user_id), right_answers_count, all_answers)

        return checked_answers
