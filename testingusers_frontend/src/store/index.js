import {createStore} from 'vuex';
import axios from "axios";
import router from "../router";
import questions from "../components/Exercise/store/index";
import profile from "../components/Profile/store/index";
import exam from "../components/Exam/store/index";
import post from "../components/Post/store/index";

export default createStore({
  state: {
    isAuthenticated: false,
    refreshToken: "",
    accessToken: "",
    user: {
      username: "",
      user_avatar: "",
      id: null,
      email: "",
      all_answers: null,
      right_answers: null,
    }
  },
  mutations: {
    initializeSite(state) {
      if (
       localStorage.getItem("accessToken") ||
       localStorage.getItem("refreshToken")
      ) {
        state.accessToken = localStorage.getItem("accessToken");
        state.refreshToken = localStorage.getItem("refreshToken");
        state.isAuthenticated = true;
      } else {
        state.accessToken = "";
        state.refreshToken = "";
        state.isAuthenticated = false;
      }
    },
    setToken(state, data) {
      if (data.refresh || data.access) {
        axios.defaults.headers.common["Authorization"] = "Bearer " + data.access
        state.accessToken = data.access;
        state.refreshToken = data.refresh;
        state.isAuthenticated = true;
      }
    },
    setUser(state, data) {
      state.user.username = data.username;
      state.user.user_avatar = data.user_avatar
      state.user.id = data.id;
      state.user.email = data.email;
      state.user.right_answers = data.right_answers;
      state.user.all_answers = data.all_answers;
      state.isAuthenticated = true
    },
    removeToken(state) {
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      state.accessToken = "";
      state.refreshToken = "";
      state.isAuthenticated = false;
    }
  },
  actions: {
    async signup(context, payload) {
      const {status, data} = await axios.post("auth/users/", payload);

      let result = {success: true, data, status};

      if (status === 201) {
        return {...result};
      }
    },
    async logout({commit, state}) {
      let data = {};
      if (state.refreshToken) {
        const {status} = await axios.post("users/logout/", {
          refresh: state.refreshToken,
        });
        data = { status }
      }

      if (data.status === 205) {
        commit("removeToken");
      }

      if (!state.isAuthenticated) {
        router.go("/");
      }
    },
    async login({commit, state}, payload) {
      const { status, data } = await axios.post("users/api/token/", payload);

      if (data.access && data.refresh) {
        localStorage.setItem("accessToken", data.access);
        localStorage.setItem("refreshToken", data.refresh);
        commit("setToken", data);
      }

      if (state.isAuthenticated) {
        return {success: true, status};
      }
    },
    async getNewTokens({commit}) {
      const refreshToken = localStorage.getItem("refreshToken");

      if (!refreshToken) {
        commit("removeToken");
        router.go("/login");
        return;
      }

      const formData = {
        refresh: refreshToken,
      };

      const { status, data } = await axios.post(
       "/users/api/token/refresh/",
       formData
      );

      if (status === 200) {
        localStorage.setItem("accessToken", data.access);
        const tokensData = {
          refresh: refreshToken,
          access: data.access,
        };
        commit("setToken", tokensData);
      }
    },

  },
  modules: {
    questions,
    profile,
    exam,
    post,
  }
})
