<template>
  <div class="carousel-container">
    <el-col>
      <el-row>
        <el-carousel height="500px" :interval="5000" arrow="always">
          <el-carousel-item v-for="item in images.images" :key="item.id">
            <img :src="item.url" class="image" />
          </el-carousel-item>
        </el-carousel>
      </el-row>
      <el-row>
        <el-tag
          effect="dark"
          class="tag-group__title"
          size="medium"
          :type="tagType[randomIndex]"
          >{{ images.category }}</el-tag
        >
      </el-row>
    </el-col>
  </div>
</template>

<script>
export default {
  name: "AsideCarousel",
  props: ["images"],
  computed: {
    randomIndex() {
      return Math.floor(Math.random() * this.tagType.length);
    },
  },
  data() {
    return {
      tagType: ["", "success", "info", "danger", "warning"],
      imageList: [
        {
          id: 1,
          url: require("../assets/imgs/bg1.jpeg"),
        },
        {
          id: 2,
          url: require("../assets/imgs/bg2.jpg"),
        },
        {
          id: 3,
          url: require("../assets/imgs/bg3.jpg"),
        },
        {
          id: 4,
          url: require("../assets/imgs/bg4.jpg"),
        },
      ],
    };
  },
};
</script>


<style scoped>
.carousel-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  /* overflow: hidden; */
  margin-top: 5%;
  margin-left: 2%;
}

.image {
  width: 300px;
  height: 100%;
}

.tag-group__title {
  /* float: left; */
  font-size: 25px;
  margin-top: 2%;
  justify-content: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>