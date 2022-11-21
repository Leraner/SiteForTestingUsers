<template>
  <div class="container">
    <h2>Cropping Image</h2>
    <ImageCropper :aspectRation="1116 / 272" @updateParent="updatePostCover"/>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="exampleFormControlInput1">Post title</label>
        <input v-model="post.title" type="text" class="form-control" id="exampleFormControlInput1"
               placeholder="Post Title">
      </div>
      <div class="form-group">
        <label for="exampleFormControlTextarea1">Post body</label>
        <textarea v-model="post.body" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
      </div>
      <div class="form-group">
        <label for="categories">Post category</label>
        <select class="form-control" id="categories" v-model="post.category">
          <option disabled value="">Select category</option>
          <option v-for="category in categories" :value="category.slug"> {{ category.title }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="examsList">Post exam</label>
        <select class="form-control" id="examsList" v-model="post.exam">
          <option disabled value="">Select exam</option>
          <option v-for="exam in exams" :value="exam.id"> {{ exam.title }}</option>
        </select>
      </div>
      <button class="btn btn-outline-secondary">Create</button>
    </form>
  </div>
</template>
<script>
import ImageCropper from '../Profile/ImageCropper.vue';

// TODO: add validators

export default {
  name: "PostCreate",
  components: {
    ImageCropper,
  },
  data() {
    return {
      post: {
        title: "",
        cover: null,
        category: "",
        exam: "",
        body: "",
        tags: []
      },
      categories: null,
      exams: null,
    }
  },
  async mounted() {
    await this.fetchCategories()
    await this.fetchMyExams()
  },
  methods: {
    async updatePostCover(data) {
      this.post.cover = {
        image: data.newImage,
        coords: JSON.parse(data.coordinates)
      }
    },
    async submitForm() {
      console.log(this.post)
      const result = await this.$store.dispatch('createPost', this.post)

      if (result.success) {
        this.$router.push('/')
      }
    },
    async fetchMyExams() {
      const result = await this.$store.dispatch('fetchMyExams')

      if (result.success) {
        this.exams = result.data
      }
    },
    async fetchCategories() {
      const result = await this.$store.dispatch('fetchCategories')

      if (result.success) {
        this.categories = result.data;
      }
    }
  }
}
</script>
