<template>
  <div class="post-list" v-if="postList">
    <div v-for="post in postList">
      <PostItem 
        :post="post"
      />
    </div>
  </div>
</template>

<script>
import PostItem from '../Post/PostItem.vue';

export default {
  name: "Posts",
  components: {
    PostItem,
  },
  data() {
    return {
      postList: [],
    }
  },
  async mounted() {
    await this.fetchPosts()
  },
  methods: {
    async fetchPosts() {
      const result = await this.$store.dispatch('fetchPosts')

      if (result.success) {
        this.postList = result.data;
      }
    }
  }
}
</script>

<style scoped>
</style>