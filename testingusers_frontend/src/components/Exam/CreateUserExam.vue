<template>
  <Popup
    v-if="popupTriggers.buttonTrigger"
    :TogglePopup="() => TogglePopup('buttonTrigger')"
  >
    <h2>Information</h2>

    <p>Add your question and answer</p>
  </Popup>

  <div class="container">
    <h1>This is create user exam page</h1>
    {{ examTitle }}
    <form @submit.prevent="submitForm">
      <div class="field">
        <div class="input-group flex-nowrap">
          <span class="input-group-text">🥰</span>
          <input
            type="text"
            class="form-control"
            placeholder="Exam Title"
            aria-label="Count"
            aria-describedby="addon-wrapping"
            v-model="examTitle"
          />
        </div>
      </div>

      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>

      <hr />

      <div
        class="question_answer_fields"
        v-for="item in examQuestionAnswerList"
      >
        <div class="field-question">
          <div class="input-group flex-nowrap">
            <span class="input-group-text">🥰</span>
            <input
              type="text"
              class="form-control"
              placeholder="Question text"
              aria-label="Count"
              aria-describedby="addon-wrapping"
              v-model="item.question.question_text"
            />
          </div>
        </div>

        <div class="field-answer">
          <div class="input-group flex-nowrap">
            <span class="input-group-text">🥰</span>
            <input
              type="text"
              class="form-control"
              placeholder="Answer text"
              aria-label="Count"
              aria-describedby="addon-wrapping"
              v-model="item.answer.answer_text"
            />
          </div>
        </div>
      </div>

      <button type="button" class="btn btn-success" @click="addQuestionAnswer">
        +
      </button>

      <br />

      <div class="field">
        <div class="control">
          <button class="btn btn-outline-secondary">Create</button>
        </div>
      </div>
      <hr />
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import Popup from "../Popup.vue";

export default {
  name: "CreateUserExam",
  components: {
    Popup,
  },
  setup() {
    const popupTriggers = ref({
      buttonTrigger: false,
      timedTrigger: false,
    });

    const TogglePopup = (trigger) => {
      popupTriggers.value[trigger] = !popupTriggers.value[trigger];
    };

    return {
      Popup,
      popupTriggers,
      TogglePopup,
    };
  },
  data() {
    return {
      examTitle: "",
      examQuestionAnswerList: [],
      errors: [],
    };
  },
  methods: {
    async addQuestionAnswer() {
      this.examQuestionAnswerList.push({
        question: {
          question_text: "",
        },
        answer: {
          answer_text: "",
        },
      });
    },
    async submitForm() {
      const result = await this.$store.dispatch("createExam", {
        title: this.examTitle,
        body: this.examQuestionAnswerList
      })

      if (result.status === 200) {
        this.$router.push(`${result.data.author.username}/${result.data.id}`)
      }
    }
  },
};
</script>

<style scoped>
.btn {
  margin: 10px;
}

.field-question {
  display: inline-block;
  margin: 10px;
}

.field-answer {
  display: inline-block;
}
</style>