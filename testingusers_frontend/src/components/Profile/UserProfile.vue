<template>
  <div class="profile" v-if="user">
    <img :src="user.user_avatar" />
    <p>Username: {{ user.username }}</p>
    <p v-if="user.status">Status: {{ user.status }}</p>
    <p v-else>Status: nothing</p>
    <p>Email: {{ user.email }}</p>
    <p>All answers: {{ user.all_answers }}</p>
    <p>Right answers: {{ user.right_answers }}</p>
  </div>
</template>

<script>
export default {
  name: "UserProfile",
  props: {
    username: {
      required: true,
      default: null,
      type: String
    }
  },
  data() {
    return {
      user: null,
    }
  },
  async mounted() {
    await this.fetchUserProfile()
  },
  methods: {
    async fetchUserProfile() {
      const result = await this.$store.dispatch("fetchUserProfile", this.username);

      if (result.success === true) {
        this.user = result.data;
      }
    }
  }
}
</script>

<style scoped>
.profile img {
  border: 3px solid black;
  box-shadow: 0 0 7px #666;
  width: 20%;
  max-width: 20%;
}
</style>