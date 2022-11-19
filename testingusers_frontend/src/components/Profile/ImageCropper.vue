<template>
  <div>
    <input
      ref="input"
      type="file"
      name="image"
      accept="image/*"
      @change="setImage"
    />

    <div class="content">
      <section class="cropper-area">
        <div class="img-cropper">
          <vue-cropper
            v-if="newImage"
            class="cropper-images"
            ref="cropper"
            :aspect-ratio="16 / 9"
            :src="newImage"
            preview=".preview"
          />
          <p v-else>Please, upload image</p>
        </div>
        <div class="actions">
          <a
            href="#"
            class="btn btn-outline-secondary"
            role="button"
            @click.prevent="cropImage"
          >
            Crop
          </a>
          <a
            href="#"
            class="btn btn-outline-secondary"
            role="button"
            @click.prevent="reset"
          >
            Reset
          </a>
          <a
            href="#"
            class="btn btn-outline-secondary"
            role="button"
            @click.prevent="showFileChooser"
          >
            Upload Image
          </a>
          <a
            href="#"
            class="btn btn-outline-success"
            role="button"
            @click.prevent="updateUserAvatar"
          >
            Done!
          </a>
        </div>
      </section>
      <section class="preview-area">
        <p>Preview</p>
        <div class="preview" />
        <p>Cropped Image</p>
        <div class="cropped-image">
          <img v-if="cropImg" :src="cropImg" alt="Cropped Image" />
          <div v-else class="crop-placeholder" />
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import VueCropper from "vue-cropperjs";
import "cropperjs/dist/cropper.css";

// TODO: replace image cropper like component with props
// :aspect-ratio="16 / 9" for posts 1116 / 272

export default {
  components: {
    VueCropper,
  },
  props: {
    imgSrc: {
      required: true,
      type: String,
      default: null,
    },
    aspectRation: {
      type: Number,
    }
  },
  data() {
    return {
      newImage: this.imgSrc,
      cropImg: "",
      data: null,
    };
  },
  methods: {
    async cropImage() {
      this.cropImg = this.$refs.cropper.getCroppedCanvas().toDataURL();
    },
    async updateUserAvatar() {
      this.data = await this.getData();

      const payload = {
        image: this.newImage,
        coords: JSON.parse(this.data),
      };

      const result = await this.$store.dispatch("updateUserAvatar", payload);

      if (result.success) {
        this.$router.go('/profile');
      }
    },
    async getData() {
      return JSON.stringify(this.$refs.cropper.getData(), null, 4);
    },
    async reset() {
      this.$refs.cropper.reset();
    },
    async setImage(e) {
      const file = e.target.files[0];
      if (file.type.indexOf("image/") === -1) {
        alert("Please select an image file");
        return;
      }
      if (typeof FileReader === "function") {
        const reader = new FileReader();
        reader.onload = (event) => {
          this.newImage = event.target.result;
          this.$refs.cropper.replace(event.target.result);
        };
        reader.readAsDataURL(file);
      } else {
        alert("Sorry, FileReader API not supported");
      }
    },
    async showFileChooser() {
      this.$refs.input.click();
    },
  },
};
</script>

<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  width: 500px;
  margin: 0 auto;
}
input[type="file"] {
  display: none;
}
.content {
  display: flex;
  justify-content: space-between;
}
.cropper-area {
  width: 500px;
}
.actions {
  margin-top: 1rem;
}
.actions a {
  display: inline-block;
  padding: 5px 15px;
  margin-right: 1rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.preview-area {
  width: 307px;
}
.preview-area p {
  font-size: 1.25rem;
  margin: 0;
  margin-bottom: 1rem;
}
.preview-area p:last-of-type {
  margin-top: 1rem;
}
.preview {
  width: 100%;
  height: calc(372px * (9 / 16));
  overflow: hidden;
}
.crop-placeholder {
  width: 100%;
  height: px;
  background: #ccc;
}
.cropped-image img {
  max-width: 100%;
}
.cropper-images {
  width: 300px;
  height: 300px;
  margin: auto;
}
</style>
