<template>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <div class="container" align="center">
          <h1 class="title">Sign up</h1>

          <form @submit.prevent="submitForm">
            <div class="field">
              <div class="input-group flex-nowrap">
                <span class="input-group-text">🥰</span>
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

            <br />

            <div class="field">
              <div class="input-group flex-nowrap">
                <span class="input-group-text">🥰</span>
                <input
                  type="email"
                  class="form-control"
                  placeholder="Email"
                  aria-label="Email"
                  aria-describedby="addon-wrapping"
                  v-model="email"
                />
              </div>
            </div>

            <br />

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

            <br />

            <div class="field">
              <div class="input-group flex-nowrap">
                <span class="input-group-text">🥰</span>
                <input
                  type="password"
                  class="form-control"
                  placeholder="Password"
                  aria-label="Password"
                  aria-describedby="addon-wrapping"
                  v-model="password2"
                />
              </div>
            </div>

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <br />

            <div class="field">
              <div class="control">
                <button class="btn btn-outline-secondary">Sign up</button>
              </div>
            </div>

            <hr />

            Or 😇
            <router-link to="/login">click here</router-link>
            to log in!
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Signup",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      email: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match");
      }


      if (this.errors.length) {
        return;
      }

      const { success } = await this.$store.dispatch("signup", {
        username: this.username,
        password: this.password,
        email: this.email
      });

      if (success) {
        await this.$router.push("login");
      }
    },
  },
};
</script>

<style scoped></style>
