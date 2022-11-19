<template>
  <div class="post">
    <div class="container">
      <div class="card bg-dark text-white">
        <img class="card-img" :src="post.cover" alt="Card image">
        <div class="card-img-overlay">
          <h5 class="card-title">{{ post.title }}</h5>
          <p class="card-text">{{ post.body }}</p>
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
    </div>
    <hr/>
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
<style>
.card-text {
  color: white;
  text-decoration: none;
}
.card-img {
  width: 1116px;
  height: 272px;
  opacity: 0.6;
}
</style>