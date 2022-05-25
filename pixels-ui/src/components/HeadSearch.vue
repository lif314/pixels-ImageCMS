<template>
  <div class="search-container">
    <el-row type="flex" justify="center" align="middle">
      <el-col :span="2">
        <!-- logo -->
        <img src="../assets/logo.png" @click="goHome" class="logo" />
      </el-col>
      <el-col :span="18">
        <el-autocomplete
          class="search"
          popper-class="my-autocomplete"
          v-model="keyword"
          :fetch-suggestions="querySearch"
          placeholder="Search for free photos"
          @select="handleSelect"
        >
          <i
            class="el-icon-search el-input__icon"
            slot="suffix"
            @click="handleIconClick"
          >
          </i>
          <template slot-scope="{ item }">
            <div class="name">{{ item['label'] }}</div>
          </template>
        </el-autocomplete>
      </el-col>
      <el-col :span="2">
        <el-button size="mini" type="primary" @click="getCollect"
          >Collect<i class="el-icon-s-opportunity el-icon--right"></i
        ></el-button>
      </el-col>
      <el-col :span="2">
        <el-button size="mini" type="primary" @click="goLogin"
          >Sign in<i class="el-icon-s-custom el-icon--right"></i
        ></el-button>
      </el-col>
      <el-col :span="2">
        <el-avatar
          style="margin-top: 5px"
          src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        ></el-avatar>
      </el-col>
      <el-col :span="2">
        <el-button size="mini" type="primary" @click="goUpload"
          >Upload<i class="el-icon-upload el-icon--right"></i
        ></el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "HeadSearch",
  //allInfos是父组件传来的值，如果allInfos不是父组件传来的就不用这样写
  props: ["tagList"],
  data() {
    return {
      keyword: "",
    };
  },
  methods: {
    goLogin() {
      this.$router.push("/login");
    },
    goHome() {
      this.$router.push("/home");
    },
    getCollect() {
      this.$emit("getCollect");
    },
    goUpload() {
      this.$router.push("/upload");
    },
    querySearch(queryString, cb) {
      var results = queryString
        ? this.tagList.filter(this.createFilter(queryString))
        : this.tagList;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter(queryString) {
      return (tag) => {
        console.log(tag)
        return (
          tag.label.toLowerCase().indexOf(queryString.toLowerCase()) ===
          0
        );
      };
    },
    handleSelect(item) {
      this.keyword = item.label
      // console.log(item);
    },
    // 进行查询
    handleIconClick(ev) {
      if(this.keyword!=null){
          this.$emit('search', this.keyword)
      }
      console.log(ev);
    },
  },
};
</script>

<style scoped>
.search-container {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  /* background-color: cornflowerblue; */
  background-color: royalblue;
}

.logo {
  margin-top: 5px;
  height: 45px;
  width: auto;
}

.search {
  width: 50%;
}
</style>