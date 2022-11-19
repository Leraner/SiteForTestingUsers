<template>
  
  <div v-if="post" class="post">
    <h1>Hello world!</h1>
    {{ post.cover }}
    <br />
    {{ post.title }}
    <br />
    {{ post.created_date }}
    <br />
    {{ post.category }}
    <br />
    {{ post.author }}
    <br />
    {{ post.body }}
    <br />
    {{ post.exam }}
    <br />
    {{ post.tags }}
    <br />
  </div>
</template>

<script>

// Collapse (bootstrap) for exam

export default {
  name: "PostDetail",
  props: {
    id: {
      required: true,
      type: String,
    },
  },
  data() {
    return {
      post: null,
    };
  },
  async mounted() {
    await this.fetchPostDetail();
  },
  methods: {
    async fetchPostDetail() {
      const result = await this.$store.dispatch("fetchPostDetail", {
        id: this.id,
      });

      if (result.success) {
        this.post = result.data;
        console.log(this.post);
      }
    },
  },
};
</script>

<style scoped></style>
