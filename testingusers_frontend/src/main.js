import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from "axios";
import VueCropper from "vue-cropperjs";
import "cropperjs/dist/cropper.css";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "bootstrap";


axios.defaults.baseURL = "http://127.0.0.1:8000";
axios.interceptors.response.use(
  async (response) => {
    return response;
  },
  async (error) => {
    if (error.response && error.response.status === 401) {
      const { config: originalReq } = error.response;

      if (originalReq.url === "/users/api/token/refresh/") {
        store.commit("removeToken");
        router.go("/login");
      }

      await store.dispatch("getNewTokens");
      originalReq.headers["Authorization"] =
        axios.defaults.headers.common["Authorization"];
      return axios.request(originalReq);
    }
    return Promise.reject(error);
  }
);

const app = createApp(App);

app.use(store);
app.use(router, axios);
app.component(VueCropper);
app.mount("#app");
