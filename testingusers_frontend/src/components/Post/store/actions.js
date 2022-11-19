import axios from "axios";

export default {
    async fetchMyExams(context) {
        const { status, data } = await axios.get('exams/exam/my_exams/')

        let result = { success: true, status, data }

        if (result.status === 200) {
            return { ...result }
        }
    },
    async fetchCategories(context) {
        const { status, data } = await axios.get('posts/categories_list/')

        let result = { success: true, status, data }

        if (result.status === 200) {
            return { ...result }
        }
    },
    async fetchPosts(context) {
        const { status, data } = await axios.get("posts/posts_list/");

        let result = { success: true, status, data };

        if (result.status === 200) {
            return { ...result };
        }
    },
    async fetchPostDetail(context, payload) {
        const { status, data } = await axios.get(`posts/posts_list/${payload.id}`);

        let result = { success: true, status, data };

        if (result.status === 200) {
            return { ...result };
        }
    },
};
