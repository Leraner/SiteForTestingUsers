<template>
  <div class="container">
    <form @submit="submitForm">
<!--      <Popup-->
<!--        v-if="popupTriggers.buttonTrigger"-->
<!--        :TogglePopup="() => TogglePopup('buttonTrigger')"-->
<!--      >-->
<!--        <h2>Cropping Image</h2>-->
<!--        <ImageCropper :aspectRation="16 / 9" :imgSrc="post.cover"/>-->
<!--      </Popup>-->
      <div class="form-group">
        <div class="custom-file">
          <input type="file" accept="image/jpeg" class="custom-file-input" id="inputGroupFile01" @change="onFileSelected">
          <label class="btn btn-outline-secondary" for="inputGroupFile01">Choose image</label>
        </div>
      </div>
      <div class="form-group">
        <label for="exampleFormControlInput1">Post title</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Post Title">
      </div>
      <div class="form-group">
        <label for="exampleFormControlTextarea1">Post body</label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
      </div>
      <div class="form-group">
        <label for="categories">Post category</label>
        <select class="form-control" id="categories" v-model="post.category">
          <option disabled value="">Select category</option>
          <option v-for="category in categories" > {{ category.title }} </option>
        </select>
      </div>
      <div class="form-group">
        <label for="examsList">Post exam</label>
        <select class="form-control" id="examsList" v-model="post.exam">
          <option disabled value="">Select exam</option>
          <option v-for="exam in exams" > {{ exam.title }} </option>
        </select>
      </div>
    </form>
  </div>
</template>
<script>
// import Popup from '../Popup.vue';
// import ImageCropper from '../Profile/ImageCropper.vue';
// import { ref } from 'vue';
// Data:
// title
// cover
// body
// tags
// exam
// category 

export default {
  name: "PostCreate",
  components: {
    Popup,
    ImageCropper,
  },
  setup() {
    const popupTriggers = ref({
      buttonTrigger: false,
      timedTrigger: false,
    });

    const TogglePopup = (trigger) => {
      popupTriggers.value[trigger] = !popupTriggers.value[trigger];
    };

    return {
      Popup,
      popupTriggers,
      TogglePopup,
    };
  },
  data() {
    return {
     post: {
      title: "",
      cover: "",
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
    async onFileSelected(e) {
      let image = e.target.files[0]
    },
    async submitForm() {
      console.log(123);
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
