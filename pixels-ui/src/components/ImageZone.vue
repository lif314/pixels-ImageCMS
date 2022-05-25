<template>
  <div class="image-zone">
    <!--tag列表-->
    <div class="label-list">
      <div v-for="(item, index) in tags" :key="index">
        <el-tag :type="labelColor[index % labelColor.length]" :hit="true">
          <el-checkbox v-model="item.status" @change="tagChange(item)" />
          {{ item.label }}({{ item.size }})
        </el-tag>
      </div>
    </div>

    <el-pagination
      class="pagination"
      background
      layout="prev, pager, next"
      :total="1000"
    >
    </el-pagination>

    <div class="image-container">
      <!-- 卡片 -->
      <div v-for="(item, index) in imageList" :key="index" class="image">
        <!-- 图片组件 -->
        <image-card :imgInfo="item" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ImageCard from "./ImageCard.vue";
export default {
  name: "ImageZone",
  components: {
    ImageCard,
  },
  props: ["imageList", "tags"],
  data() {
    return {
      my_tags: [
        {
          status: false,
          label: "cat",
          size: 1121,
        },
        {
          status: false,
          label: "people",
          size: 10,
        },
        {
          status: true,
          label: "tree",
          size: 134,
        },
        {
          status: false,
          label: "dog",
          size: 1121,
        },
        {
          status: false,
          label: "food",
          size: 122,
        },
      ],
      labelColor: ["", "success", "info", "warning", "danger"],
      images: [
        {
          id: 1,
          ower: "Linfei Li",
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          tags: ["people", "cat", "dog"],
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
        {
          id: 1,
          ower: "Linfei Li",
          tags: ["people", "cat", "dog"],
          avatar:
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
          url: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        },
      ],
    };
  },
  // created(){
  //     this.getTags()
  // },
  methods: {
    tagChange(item) {
      // TODO 多选机制：MYSQL查询吃力，可以hi用ES进行搜索
      // 使用tag进行查询
      // console.log(item);
      // 目前仅支持单一查询
      this.tags.forEach(element => {
        if (element.label !== item.label){
          element.status = false
        }
      });
      if (item.status) {
        this.$emit("search", item.label);
      }
    },
  },
};
</script>

<style scoped>
/*配置快速回到顶栏 */
.image-zone {
  margin-top: 2%;
  /* display: flex; */
  flex-direction: row;
  /*容器内成员的排列方式为从左到右*/
  flex-wrap: wrap;
  /*换行方式，放不下就换行*/
  justify-content: flex-start;
  /*项目在主轴上的对齐方式*/
  align-content: flex-start;
}

/* 图片总布局，样式 */

.image-container {
  margin-top: 3%;
  margin-left: 3%;
  margin-right: 3%;
  display: flex;
  flex-direction: row;
  /*容器内成员的排列方式为从左到右*/
  flex-wrap: wrap;
  /*换行方式，放不下就换行*/
  justify-content: flex-start;
  /*项目在主轴上的对齐方式*/
  align-content: flex-start;
}

.label-list {
  display: flex;
  flex-direction: row;
  /*容器内成员的排列方式为从左到右*/
  flex-wrap: wrap;
  /*换行方式，放不下就换行*/
  justify-content: flex-start;
  /*项目在主轴上的对齐方式*/
  align-content: flex-start;
}

.el-tag {
  float: left;
  white-space: pre-line;
  word-break: break-all;
  margin-top: 5px;
  margin-left: 5px;
}
.pagination {
  float: center;
  margin-top: 2%;
}

/* 图片之间 */
.image {
  margin-right: 30px;
  /* vertical-align: middle; */
  /* margin-bottom: 30px; */
  /* max-width: 100%; */
  /* max-height: 100%; */
  /* border: 1px solid red; */
}
</style>