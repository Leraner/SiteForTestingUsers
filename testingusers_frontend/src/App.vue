<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <div class="inner" v-if="this.$store.state.isAuthenticated">
      <router-link to="/tasks">Tasks</router-link>
      |
      <router-link to="/profile">Profile</router-link>
      |
      <router-link to="/post/create">Create Post</router-link>
      |
      <a @click="logout">Logout</a>
    </div>
    <router-link to="/login" v-if="!this.$store.state.isAuthenticated"
      >Login</router-link
    >
    |
    <router-link to="/signup" v-if="!this.$store.state.isAuthenticated"
      >SignUp</router-link
    >
  </div>
  <router-view />
</template>
<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "App",
  computed: mapGetters(["AuthState"]),
  methods: {
    async logout() {
      await this.$store.dispatch("logout");
    },
  },
  async beforeCreate() {
    this.$store.commit("initializeSite");

    const token = this.$store.state.accessToken;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else if (this.$store.state.refreshToken && !token) {
      await this.$store.dispatch("getNewTokens");
      axios.defaults.headers.common["Authorization"] =
        this.$store.state.accessToken;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>

<style>
.logout-button {
  border: None;
}

.inner {
  display: inline-block;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  cursor: pointer;
  text-decoration: underline;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
