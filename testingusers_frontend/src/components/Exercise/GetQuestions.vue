<template>
  <Questions
      v-if="questionsList"
      :questions-list="questionsList"
      :questions-count="questionsCount"
      :not-first-try="notFirstTry"
      @updateParent="onUpdateNotFirstTry"
  />
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <div class="container" align="center">
          <form @submit.prevent="submitForm">
            <div class="field">
              <div class="input-group flex-nowrap">
                <span class="input-group-text">🥰</span>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Count"
                  aria-label="Count"
                  aria-describedby="addon-wrapping"
                  v-model="questionsCount"
                />
              </div>
            </div>

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <br />

            <div class="field">
              <div class="control">
                <button class="btn btn-outline-secondary">Get questions</button>
              </div>
            </div>

            <hr />
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useVuelidate } from "@vuelidate/core";
import { required, integer } from "@vuelidate/validators";
import Popup from "../Popup.vue";
import Questions from "./Questions";

export default {
  name: "GetQuestions",
  components: {
    Popup,
    Questions,
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
      v$: useVuelidate(),
      questionsCount: null,
      questionsList: null,
      notFirstTry: false,
      errors: [],
    };
  },
  validations: {
    questionsCount: { required, integer },
  },
  methods: {
    async onUpdateNotFirstTry(data) {
      this.notFirstTry = data.notFirstTry
    },
    async submitForm() {
      this.rightAnswers = this.wrongAnswers = 0;
      this.notFirstTry = false;

      this.errors = [];

      if (this.v$.questionsCount.$invalid) {
        return this.errors.push("You need input count of questions");
      }

      const result = await this.$store.dispatch("fetchQuestions", {
        questions_count: this.questionsCount,
      });

      if (result.success) {
        this.questionsList = [...result.data.data];

        for (let i = 0; i < this.questionsCount; i++) {
          this.questionsList[i].answer_text = "";
        }
      }
    },
  },

  // testusername
  // testpassword123
};
</script>

<style scoped>
</style>


