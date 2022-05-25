<template>
  <div>
    <el-container>
      <!-- 头部搜索栏 -->
      <el-header><head-search
          @getCollect="getCollectImages"
          @search="getSearchImages"
          :tagList="tags"
      /></el-header>
      <el-container>
        <!-- <el-scrollbar class="scollbar_box"> -->
        <el-aside width="300px">
          <!-- 侧边轮播图 -->
          <aside-carousel
            v-for="(images, index) in asideImageList"
            :key="index"
            :images="images"
          />
        </el-aside>
        <el-main class="main_box">
          <!-- 顶部轮播图 -->
          <carousel-item />
          <!-- 导航栏 -->
          <div class="line"></div>

          <el-menu
            :default-active="activeIndex2"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
            background-color="white"
            text-color="black"
            active-text-color="deepskyblue"
          >
            <el-menu-item index="1" @click="getAlImages">Home</el-menu-item>
            <el-submenu index="2">
              <template slot="title">Discover</template>
              <el-menu-item index="2-1">Beauty</el-menu-item>
              <el-menu-item index="2-2">Nature</el-menu-item>
              <el-menu-item index="2-3">Buildings</el-menu-item>
              <el-submenu index="2-4">
                <template slot="title">Videos</template>
                <el-menu-item index="2-4-1">People</el-menu-item>
                <el-menu-item index="2-4-2">History</el-menu-item>
                <el-menu-item index="2-4-3">Music</el-menu-item>
              </el-submenu>
            </el-submenu>
            <!-- <el-menu-item index="3" disabled>Leaderborder</el-menu-item> -->
            <el-menu-item index="3" @click="getCollectImages"
              >Collect</el-menu-item
            >
            <el-menu-item index="4"
              ><a href="https://www.pexels.com/" target="_blank"
                >Challenges</a
              ></el-menu-item
            >
          </el-menu>
          <el-divider></el-divider>
          <!-- 图片列表 -->

          <image-zone :imageList="imageList" :tags="tags" @search="getSearchImages"/>
        </el-main>
        <!-- </el-scrollbar> -->
      </el-container>
    </el-container>
  </div>
</template>

<script>
import HeadSearch from "@/components/HeadSearch.vue";
import ImageZone from "@/components/ImageZone.vue";
import CarouselItem from "@/components/CarouselItem.vue";
import AsideCarousel from "@/components/AsideCarousel.vue";

import axios from "axios";

export default {
  name: "Home",
  components: {
    HeadSearch,
    ImageZone,
    CarouselItem,
    AsideCarousel,
  },
  created() {
    this.getData();
    this.getTags();
  },
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
      imageList: [],
      tags: [],
      asideImageList: [
        {
          category: "People",
          images: [
            {
              id: 1,
              url: require("@/assets/people/pexels-edu-carvalho-2050994.jpg"),
            },
            {
              id: 2,
              url: require("@/assets/people/pexels-eli-burdette-762527.jpg"),
            },
            {
              id: 3,
              url: require("@/assets/people/pexels-luizclas-1848565.jpg"),
            },
            {
              id: 4,
              url: require("@/assets/people/pexels-tuấn-kiệt-jr-1308885.jpg"),
            },
            {
              id: 5,
              url: require("@/assets/people/pexels-nripen-kumar-roy-725458.jpg"),
            },
            {
              id: 6,
              url: require("@/assets/people/pexels-pixabay-157757.jpg"),
            },
          ],
        },
        {
          category: "Nature",
          images: [
            {
              id: 1,
              url: require("@/assets/nature/pexels-cliford-mervil-2469122.jpg"),
            },
            {
              id: 2,
              url: require("@/assets/nature/pexels-luis-dalvan-1770809.jpg"),
            },
            {
              id: 3,
              url: require("@/assets/nature/pexels-s-migaj-1402850.jpg"),
            },
          ],
        },
        {
          category: "Animals",
          images: [
            {
              id: 1,
              url: require("@/assets/animals/pexels-anna-shvets-4588065.jpg"),
            },
            {
              id: 2,
              url: require("@/assets/animals/pexels-jimmy-chan-1321524.jpg"),
            },
            {
              id: 3,
              url: require("@/assets/animals/pexels-pixabay-162318.jpg"),
            },
          ],
        },
        {
          category: "Apparels",
          images: [
            {
              id: 1,
              url: require("@/assets/apparels/pexels-anna-shvets-5325599.jpg"),
            },
            {
              id: 2,
              url: require("@/assets/apparels/pexels-maria-orlova-4906283.jpg"),
            },
            {
              id: 3,
              url: require("@/assets/apparels/pexels-masha-raymers-8196527.jpg"),
            },
          ],
        },
      ],
    };
  },
  methods: {
    getTags() {
      axios({
        url: "/api/tags",
        method: "get",
      })
        .then((res) => {
          // console.log(res.data)
          this.tags = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 搜索数据
    getSearchImages(keyword) {
      axios({
        url: "/api/search",
        method: "get",
        params: {
          keyword: keyword,
        },
      }).then((res) => {
        // console.log(res.data);
        this.imageList = res.data.data;
      });
    },
    
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    async getData() {
      axios
        .get("api/images")
        .then((response) => {
          // console.log(response.data);
          this.imageList = response.data.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    // 获取用户的收藏图片
    getCollectImages() {
      axios({
        url: "api/user/collect",
        method: "get",
        params: {
          userId: "5",
        },
      })
        .then((response) => {
          console.log(response.data);
          this.imageList = response.data.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    // 获取所有数据
    getAlImages() {
      this.getData();
    },
  },
};
</script>

<style scoped>
.el-menu-demo {
  margin-top: 2%;
  font-size: 20px;
  font-weight: bold;
}
.el-divider--vertical {
  height: 60em !important;
  width: 1.5px !important;
}
</style>