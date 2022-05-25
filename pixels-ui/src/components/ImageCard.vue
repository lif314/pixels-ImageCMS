<template>
  <div
    class="image_container"
    style="position: relative"
    @mouseover="showUserInfo"
    @mouseleave="closeUserInfo"
  >
    <!-- 添加鼠标点击或悬浮图片放大功能 -->
    <el-popover trigger="click">
      <img :src="imgInfo.url" slot="reference" class="image" />
      <img :src="imgInfo.url" class="imagePreview" />
    </el-popover>
    <!-- 预测分数 -->
    <div class="score" v-show="isShowInfo">
      <el-tag type="primary" effect="dark" :color="labelColor[1]">
        Score: {{ imgInfo.score }}
      </el-tag>
    </div>

    <!-- 分类信息 -->
    <div class="label-list" v-show="isShowInfo">
      <el-tag
        type="primary"
        v-for="(item, index) in image_tags"
        :key="index"
        effect="dark"
        :color="labelColor[index]"
      >
        {{ item }}
      </el-tag>
    </div>
    <div class="info" v-show="isShowInfo">
      <el-row :gutter="40" type="flex" justify="space-between" align="middle">
        <el-col :span="6">
          <!-- 用户肖像 -->
          <el-avatar
            style="margin-left: 3px"
            :size="35"
            fit="fill"
            src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
            @error="errorHandler"
          >
          </el-avatar>
        </el-col>
        <!-- 上传人信息 -->
        <el-col :span="8">
          <span class="name">{{ imgInfo.owner_name }}</span>
        </el-col>
        <el-col :span="3">
          <!--下载-->
          <em
            class="el-icon-download"
            style="font-size: 20px; color: white"
            @click="downs(imgInfo.url)"
          ></em>
        </el-col>
        <el-col :span="3">
          <!--查看大图-->
          <em
            class="el-icon-zoom-in"
            style="font-size: 20px; color: white"
            @click="seeBigImage"
          ></em>
        </el-col>
        <!--收藏图片-->
        <el-col :span="3">
          <div v-if="!isCollectedLoading">
            <em
              :class="isCollected ? 'el-icon-star-on' : 'el-icon-star-off'"
              style="font-size: 20px; color: white"
              @click="changeCollectImage(imgInfo.id)"
            ></em>
          </div>
          <div v-else>
            <em
              class="el-icon-loading"
              style="font-size: 20px; color: white"
            ></em>
          </div>
        </el-col>
      </el-row>
    </div>
    <el-dialog :visible.sync="dialogVisible">
      <img width="80%" height="80%" :src="imgInfo.url" alt="" />
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ImageCard",
  props: ["imgInfo"],
  computed: {
    image_tags() {
      // console.log(this.imgInfo.tags);
      let tags  = this.imgInfo.tags
      let tagArr = (tags || "").split(", ");
      if (tagArr.length > 3) {
        return tagArr.slice(1, 3);
      }
      return tagArr;
    },
  },
  data() {
    return {
      labelColor: [
        "#77C9D4",
        "#57BC90",
        "#015249",
        "#a3c6ea",
        "#70a8c4",
        "#559bcb",
      ],
      isShowInfo: false,
      isCollected: false,
      dialogVisible: false,
      isCollectedLoading: false,
    };
  },
  methods: {
    // 用户头像加载失败
    errorHandler() {
      return true;
    },
    // 显示图像的描述信息
    closeUserInfo() {
      this.isShowInfo = false;
    },
    showUserInfo() {
      this.isShowInfo = true;
    },
    // 收藏图片
    changeCollectImage(imageId) {
      this.isCollectedLoading = true;
      axios({
        method: "get",
        url: "/api/collect",
        params: {
          imageId: imageId,
          userId: "5", // TODO 注册登录时使用，目前假设用户都是5
          status: this.isCollected ? "0" : "1", // 1为收藏 0为取消收藏
        },
      })
        .then(() => {
          setTimeout(() => {
            this.isCollected = !this.isCollected;
            if (this.isCollected) {
              this.$message({
                message: "You collect it successfully!",
                type: "success",
              });
            } else {
              this.$message({
                message: "You remove it from collection successfully!",
                type: "success",
              });
            }
            this.isCollectedLoading = false;
          }, 600);
        })
        .catch(() => {
          this.isCollectedLoading = false;
        });
    },
    seeBigImage() {
      this.dialogVisible = true;
    },
    // 下载图片：需要在alioss配置跨域
    downs(url) {
      const a = document.createElement("a");
      a.href = url;
      // a.download = "pixels_share";
      a.click();
    },
  },
};
</script>

<style scoped>
.image_container {
  overflow: hidden;
  margin-left: 10%;
  margin-top: 2%;
}

/* 单张图片样式 */
.image {
  width: 400px;
  height: 440px;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: -1;
  margin: auto;
  border-radius: 10px 10px 0 0;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

.info {
  /* float: left; */
  display: flex;
  position: absolute;
  flex-direction: row;
  flex-wrap: nowrap;
  bottom: 2%;
  justify-content: space-between;
}

.name {
  font-size: 6px;
  color: white;
  float: left;
  /* font-weight: bold; */
}

.score {
  position: absolute;
  /* display: flex; */
  top: 1%;
  /* float: center; */
  left: 1%;
}

.button_box {
  text-align: right;
}
/* 标签列表 */
.label-list {
  position: absolute;
  top: 1%;
  right: 1%;
  left: 80%;
  /* float: right; */
  /* display: flex; */
  flex-direction: column;
  /*容器内成员的排列方式为从左到右*/
  flex-wrap: wrap;
  /*换行方式，放不下就换行*/
  justify-content: flex-end;
  /*项目在主轴上的对齐方式*/
  align-content: flex-end;
}

.el-tag {
  float: right;
  word-break: break-all;
  margin-top: 3px;
  margin-left: 3px;
  display: flex;
  text-align: center;
}
</style>