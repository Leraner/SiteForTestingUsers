<template>
  <div class="home">
    <Popup
      v-if="popupTriggers.buttonTrigger"
      :TogglePopup="() => TogglePopup('buttonTrigger')"
    >
      <h2>Information</h2>

      <small>
        If this isn't your first try, this results doesn't apply to your profile
        statistic
      </small>

      <p>This is your right answers: {{ rightAnswers }}</p>
      <p>This is your wrong answers: {{ wrongAnswers }}</p>
      <p>This is all answers: {{ wrongAnswers + rightAnswers }}</p>
    </Popup>
  </div>
  <div v-if="questionsList">
    <div class="container">
      <form @submit.prevent="submitForm">
        <div v-for="question in questionsList">
          {{ question.question_text }}
          <div class="input-group flex-nowrap">
            <span class="input-group-text" v-if="question.correct === true">
              🥰
            </span>
            <span class="input-group-text" v-if="question.correct === false">
              😡
            </span>
            <input
              type="text"
              class="form-control"
              placeholder="Answer"
              aria-label="Answer"
              aria-describedby="addon-wrapping"
              v-model="question.answer_text"
            />
          </div>
        </div>
        <div class="control">
          <button
            class="btn btn-outline-secondary"
            @click="() => TogglePopup('buttonTrigger')"
          >
            Check questions
          </button>
        </div>
      </form>
    </div>
  </div>
  <br />
</template>

<script>
import { ref } from "vue";
import Popup from "../Popup.vue";

export default {
  name: "Questions",
  components: {
    Popup,
  },
  props: {
    questionsList: {
      required: true,
      type: Object,
    },
    questionsCount: {
      required: true,
      type: Number,
    },
    notFirstTry: {
      required: true,
      type: Boolean,
    },
    typeOfCheck: {
      required: false,
      type: String,
      default: "questions",
    },
  },
  emits: ["updateParent"],
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
      rightAnswers: 0,
      wrongAnswers: 0,
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.rightAnswers = this.wrongAnswers = 0;

      const result = await this.$store.dispatch("CheckQuestions", {
        questions: {
          notFirstTry: this.notFirstTry,
          questionsList: this.questionsList
        },
        type: this.typeOfCheck,
      });

      for (let i = 0; i < this.questionsCount; i++) {
        if (result.data.result[i].correct === true) {
          this.rightAnswers++;
        } else {
          this.wrongAnswers++;
        }

        this.questionsList[i]["correct"] = result.data.result[i].correct;
      }

      if (!this.notFirstTry) {
        this.$emit("updateParent", { notFirstTry: true });
      }
    },
  },
};
</script>

<style scoped>
.control {
  margin: 1rem;
}
</style>