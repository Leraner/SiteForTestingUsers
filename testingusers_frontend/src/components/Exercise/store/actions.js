import axios from "axios";

export default {
  async fetchQuestions(context, payload) {
    const { status, data } = await axios.post('questions/question_list/', payload)

    let result = { success: true, status, data }

    if (status === 200) {
      return { ...result }
    }
  },
  async CheckQuestions(context, payload) {
    let formBody = {}
    if (payload.type === "questions") {
      const { status, data } = await axios.post(
        'answers/checked_list_of_answers/', payload.questions)
      formBody = { status, data }
    }

    if (payload.type === "exam") {
      const { status, data } = await axios.post(
        'exams/exam_answers/checked_list_of_exam_answers/', payload.questions)
      formBody = { status, data }
    }

    let result = { success: true, ...formBody }

    if (result.status === 200) {
      return { ...result }
    }
  }
}
