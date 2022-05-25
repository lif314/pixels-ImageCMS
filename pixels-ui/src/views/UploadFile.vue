<template>
  <div class="upload_container">
    <head-search />
    <div class="content">
      <h3>Upload Photos & Videos</h3>
      <ul>
        <li>
          <span>
            Your uploads will be distributed for free under the Pexels license.
            Learn more
          </span>
        </li>
        <li>
          <span>
            To increase the chance of being featured, please ensure that your
            submissions meet our guidelines.
          </span>
        </li>
        <li>
          <span>
            We'll review your submission. If it gets selected, you will receive
            an email notification and your content will be featured in our
            search.
          </span>
        </li>
      </ul>
    </div>

    <div class="upload">
      <el-button style="margin-bottom: 10px" type="primary" @click="handleClick"
        >Upload Image</el-button
      >
      <el-upload
        v-model="fileList"
        ref="uploadref"
        action="upload"
        :auto-upload="false"
        list-type="picture-card"
        :file-list="fileList"
        :on-change="handleChange"
        :on-preview="handlePictureCardPreview"
        :on-remove="handleRemove"
        :limit="1"
        :on-success="uploadSuccess"
        :multiple="false"
      >
        <i class="el-icon-plus"></i>
      </el-upload>
      <el-dialog v-model="dialogVisible">
        <img :src="dialogImageUrl" alt="" />
      </el-dialog>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { reqUploadImage } from "@/api/api";
import HeadSearch from "../components/HeadSearch.vue";

export default {
  components: { HeadSearch },
  name: "UploadFile",
  data() {
    return {
      dialogImageUrl: "",
      dialogVisible: false,
      fileParam: "",
      fileList: [],
    };
  },
  methods: {
    handleRemove() {
      this.fileList.splice(0, 1);
      // console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
      // console.log(file, fileList);
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleChange(file) {
      this.fileParam = new FormData(); //创建form对象
      this.fileParam.append("file", file["raw"]);
      this.fileParam.append("fileName", file["name"]);
    },
    async handleClick() {
      if (this.fileParam === "") {
        this.$message({
          message: "Please select a picture!",
          type: "error",
        });
        return;
      }
      await reqUploadImage({ data: this.fileParam });
      this.fileList = [];
      this.fileParam = "";
      // axios.post("http://127.0.0.1:5000/upload", this.fileParam)
      //   .then((response) => {
      //     console.log(response);
      //     this.fileList = [];
      //   })
      //   .catch((e) => {
      //     console.log(e);
      //   });
    },
  },
};
</script>

<style scoped>
/* body {
  margin: 0;
} */
.upload_container {
  position: relative;
  /* width: 100%; */
  /* height: 100%; */
  /* display: flex; */
}

.content {
  margin-top: 10;
}

.content ul {
  text-align: left;
  width: 600px;
  height: auto;
  margin-left: 30%;
}

.content h3 {
  text-align: center;
}

.upload {
  margin-top: 5%;
  height: auto;
  width: 400px;
  margin-left: 35%;
  padding: auto;
  margin-bottom: 0%;
}
</style>