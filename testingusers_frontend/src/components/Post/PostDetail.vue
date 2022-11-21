<template>
  <div class="container" v-if="post">
    <div class="card">
      <h1 class="card-title">{{ post.title }}</h1>
      <div class="post-author">
        <router-link
          class="post-author-username"
          v-if="!isMyProfile"
          :to="{
            name: 'UserProfile',
            params: { username: post.author.username }
          }"
        >
          {{ post.author.username }}
        </router-link>
        <router-link
          class="post-author-username"
          v-else
          :to="{
            name: 'MyProfile',
          }"
        >
          {{ post.author.username }}
        </router-link>
      </div>
      <img class="card-img" :src="post.cover" alt="Card image">

      <div class="card-body">
        {{ post.body }}
      </div>
    </div>

    <div v-if="post.exam" class="post-exam">
      <UserExam :username="post.exam.author.username" :exam_id="post.exam.id"/>
    </div>

    <div class="tags" v-if="post.tags.length > 0">
      Tags:
      <div class="tag" v-for="tag in tags">
        {{ tag }}
      </div>
    </div>
    <br>
    {{ post.created_date }}
    <br>
    Category: {{ post.category.title }}
  </div>
</template>

<script>
import UserExam from '../Exam/UserExam.vue';
// Collapse (bootstrap) for exam

export default {
  name: "PostDetail",
  components: {
    UserExam,
  },
  props: {
    id: {
      required: true,
      type: String,
    },
  },
  data() {
    return {
      post: null,
      isMyProfile: null,
    };
  },
  async mounted() {
    await this.fetchPostDetail();
    await this.checkMyProfile();
  },
  methods: {
    async checkMyProfile() {
      if (!this.$store.state.isAuthenticated) {
        return this.isMyProfile = false;
      }

      if (this.$store.state.user.user_avatar) {
        this.user = this.$store.state.user
        return;
      }

      const result = await this.$store.dispatch("fetchProfile");

      if (result.status === 200) {
        if (this.post.author.username === result.data.username) {
          return this.isMyProfile = true;
        }
        return this.isMyProfile = false;
      }
    },
    async fetchPostDetail() {
      const result = await this.$store.dispatch("fetchPostDetail", {
        id: this.id,
      });

      if (result.success) {
        this.post = result.data;
      }
    },
  },
};
</script>

<style scoped>
.post-author {
  position: absolute;
  padding: 10px;
  right: 1;
}

.post-author-username {
  color: black;
  text-decoration: none;
}

.post-exam {
  margin-top: 5rem;
}
</style>
