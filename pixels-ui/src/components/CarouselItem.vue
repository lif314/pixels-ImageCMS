<template>
<div class="carousel-container">
  <el-carousel height="500px" :interval="5000"  arrow="always">
    <el-carousel-item v-for="item in imageList" :key="item.id">
      <img :src="item.url" class="image"/>
    </el-carousel-item>
  </el-carousel>
</div>
</template>

<script>
export default {
  name: "CarouselItem",
  data() {
    return {
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
          url:require("../assets/imgs/bg3.jpg"),
        },
        {
          id: 4,
          url:require("../assets/imgs/bg4.jpg"),
        },
      ],
    };
  },
};
</script>


<style scoped>
.ccarousel-container{
  display: flex;
}

.image{
  width: 100%;
  height: 500px;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

</style>