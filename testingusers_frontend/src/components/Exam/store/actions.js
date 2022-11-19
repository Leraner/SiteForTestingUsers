import axios from "axios"

export default {
    async fetchExam(context, payload) {
        const { status, data } = await axios.get(`exams/exam/${payload.username}/?id=${payload.exam_id}`)
        
        let result = { success: true, status, data }

        if (result.success) {
            return { ...result }
        }
    },
    async createExam(context, payload) {
        const { status, data } = await axios.post('exams/exam/', payload)

        let result = { success: true, status, data }

        if (result.status === 200) {
            return { ...result }
        }
    },
}