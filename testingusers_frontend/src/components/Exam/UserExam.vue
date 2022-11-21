w<template>
  <div><h1>Examination</h1></div>
  <div
      class="author"
      v-if="examAuthor"
  >
    {{ examAuthor.username }}
    {{ examAuthor.status }}
    {{ examAuthor.all_answers }}
    {{ examAuthor.right_answers }}
  </div>
  <Questions
      v-if="questionsList"
      :questions-list="questionsList"
      :questions-count="questionsCount"
      :not-first-try="notFirstTry"
      type-of-check="exam"
      @updateParent="onUpdateNotFirstTry"
  ></Questions>
</template>
<script>
import Questions from "../Exercise/Questions.vue";

export default {
  name: "UserExam",
  components: {
    Questions,
  },
  props: {
    username: {
      required: true,
      type: String,
    },
    exam_id: {
      required: true,
      type: Number,
    },
  },
  data() {
    return {
      notFirstTry: true,
      questionsCount: 0,
      questionsList: null,
      examAuthor: null,
    };
  },
  async mounted() {
    await this.fetchUserExam();
  },
  methods: {
    async onUpdateNotFirstTry(data) {
      this.notFirstTry = data.notFirstTry;
    },
    async fetchUserExam() {
      const result = await this.$store.dispatch("fetchExam", {
        username: this.username,
        exam_id: this.exam_id,
      });

      if (result.status === 200) {
        this.examAuthor = result.data.author;
        this.questionsList = result.data.questions;
        this.questionsCount = this.questionsList.length;
        for (let i = 0; i < this.questionsCount; i++) {
          this.questionsList[i].answer_text = "";
        }
      }
    },
  },
};
</script>