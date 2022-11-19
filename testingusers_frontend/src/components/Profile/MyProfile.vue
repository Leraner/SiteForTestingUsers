<template>
  <Popup
    v-if="popupTriggers.buttonTrigger"
    :TogglePopup="() => TogglePopup('buttonTrigger')"
  >
    <h2>Cropping Image</h2>
    <ImageCropper :aspectRation="16 / 9" :imgSrc="user.user_avatar"/>
  </Popup>
  <div class="profile" v-if="user">
    <img :src="user.user_avatar" @click="() => TogglePopup('buttonTrigger')" />
    <p>Username: {{ user.username }}</p>
    <p v-if="user.status">Status: {{ user.status }}</p>
    <p v-else>Status: nothing</p>
    <p>Email: {{ user.email }}</p>
    <p>All answers: {{ user.all_answers }}</p>
    <p>Right answers: {{ user.right_answers }}</p>
    <p>User exams {{ user.exam_count }}</p>
    <router-link class="btn btn-outline-secondary" to="/exam/create"
      >Create Exam</router-link
    >
  </div>
</template>

<script>
import { ref } from "vue";
import ImageCropper from "./ImageCropper.vue";
import Popup from "../Popup.vue";

export default {
  name: "GetProfile",
  components: {
    ImageCropper,
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
      user: null,
    };
  },
  async mounted() {
    await this.getProfile();
  },
  methods: {
    async getProfile() {
      if (this.$store.state.user.user_avatar) {
        this.user = this.$store.state.user
        return;
      }

      const result = await this.$store.dispatch("fetchProfile");

      if (result.status === 200) {
        this.user = result.data;
      }
    },
  },
};
</script>

<style scoped>
.profile img {
  cursor: pointer;
  border: 3px solid black;
  box-shadow: 0 0 7px #666;
  width: 50%;
}
</style>