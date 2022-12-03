<template>
  <div class="container">


    <div class="post">
      <router-link :to="{
        name: 'PostDetail',
        params: { id: post.id }
      }">
        <div class="card bg-dark text-white">
          <div class="post-cover">
            <img class="card-img" :src="post.cover" alt="Card image">
          </div>
          <div class="card-img-overlay">
            <h5 class="card-title">{{ post.title }}</h5>
            <p class="card-text">{{ post.created_date }}</p>
            <router-link
                class="card-text"
                :to="{
              name: 'UserProfile',
              params: { username: post.author.username  }
            }"
            >
              {{ post.author.username }}
            </router-link>
            <div v-if="post.tags" class="post_tags" v-for="tag in post.tags">
              {{ tag }}
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>
<script>
export default {
  name: "PostItem",
  props: {
    post: {
      required: true
    }
  }
}
</script>
<style scoped>
.card-text {
  color: white;
  text-decoration: none;
}

.card {
  overflow: hidden;
}

.container {
  margin-bottom: 2rem;
}

.post-cover {
  background: #000;
}

.post-cover img {
  opacity: 0.6;
}
</style>