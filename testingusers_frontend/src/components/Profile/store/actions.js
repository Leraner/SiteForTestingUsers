import axios from "axios"
import store from "@/store/index.js";

export default {
  async fetchUserProfile(context, payload) {
    
    const { status, data } = await axios.get(`users/${payload}`);

    let result = { success: true, status, data };

    if (status === 200) {
      return { ...result }
    }
  },
  async fetchProfile(context, payload) {
    const { status, data } = await axios.get('users/profile/')

    let result = {success: true, status, data}

    if (store.state.user.username === "") {
      store.commit("setUser", result.data);
    }

    if (status === 200) {
      return {...result}
    }
  },
  async updateUserAvatar(context, payload) {
    const { status, data } = await axios.post('users/update_user_avatar/', payload)

    let result = { success: true, status, data }

    if (status === 200) {
      return { ...result }
    }
  }
}