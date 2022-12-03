<template>
  <div class="page-log-in">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <div class="container" align="center">
          <h1 class="title">Log in</h1>
          <form @submit.prevent="submitForm">
            <div class="field">
              <div class="input-group flex-nowrap">
                <span class="input-group-text" id="addon-wrapping">🥰</span>
                <input
                    type="text"
                    class="form-control"
                    placeholder="Username"
                    aria-label="Username"
                    aria-describedby="addon-wrapping"
                    v-model="username"
                />
              </div>
            </div>

            <br/>

            <div class="field">
              <div class="input-group flex-nowrap">
                <span class="input-group-text">🥰</span>
                <input
                    type="password"
                    class="form-control"
                    placeholder="Password"
                    aria-label="Password"
                    aria-describedby="addon-wrapping"
                    v-model="password"
                />
              </div>
            </div>

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <br/>

            <div class="field">
              <div class="control">
                <button class="btn btn-outline-secondary">Log in</button>
              </div>
            </div>

            <hr/>

            Or
            <router-link to="/signup">click here</router-link>
            to sign up!
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }

      if (this.errors.length) {
        return;
      }
      const result = await this.$store.dispatch("login", {
        username: this.username,
        password: this.password,
      });

      if (result.success && result.status === 200) {
        if (result.data) {
          this.$store.commit("setUser", result.data);
        }
        await this.$router.push("/");
      }
    },
  },
};
</script>


<style scoped>

</style>